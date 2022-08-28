
from brownie import network, config, interface
from matplotlib.style import available
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth
from web3 import Web3

AMOUNT = Web3.toWei(0.1, "ether")



def main():
    account  = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork"]:
        get_weth()
        
    #ABI
    #ADDRESS
    lending_pool = get_lending_pool()
    #print(lending_pool)
    #now we need to deposit this erc20 token. first we will approve it
    #approve sending...
    
    approve_tx = approve_erc20(AMOUNT, lending_pool.address, erc20_address, account)
    
    print("Depositing...")
    tx = lending_pool.deposit(
        erc20_address, AMOUNT, account.address, 0, {"from": account}
    )
    tx.wait(1)
    print("Deposited!")
    
    """
    Now the depositing to AAVE is done... 
    Now we can take borrow... But how much borrow should we take...
    """
    
    borrowable_eth, total_debt = get_borrowable_data(lending_pool, account)
    
    """ Now we can finally borrow"""
    print("\n\nLets borrow some DAI...")
    
    #1. convert DAI in terms of ETH
    # we will use chainlink pricefeed
    #dai_eth_price_feed = config["networks"][network.show_active()]["dai_eth_price_feed"]
    dai_eth_price = get_asset_price(config["networks"][network.show_active()]["dai_eth_price_feed"])
    
    amount_dai_to_borrow = (1/dai_eth_price) * (borrowable_eth * 0.95)
    
    print(f"We are going to borrow {amount_dai_to_borrow} DAI...")
    dai_address
    borrow_tx = lending_pool.borrow()
    

def get_asset_price(price_feed_address):
    # we need an ABI and address to work with this as always...
    dai_eth_price_feed = interface.AggregatorV3Interface(price_feed_address)
    latest_price = dai_eth_price_feed.latestRoundData()[1]
    converted_latest_price = Web3.fromWei(latest_price, "ether")
    print(f"Dai/ETH price is {converted_latest_price}")
    return float(converted_latest_price)


def get_borrowable_data(lending_pool, account):
    (total_collateral_eth, total_debt_eth, available_borrow_eth, current_liquidation_threshold, ltv, health_factor ) = lending_pool.getUserAccountData(account.address)
    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_collateral_eth = Web3.fromWei(total_collateral_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")
    print(f"You have {total_collateral_eth} worth of ETH deposited..")
    print(f"You have {total_debt_eth} worth of ETH borrowed..")
    print(f"You have {available_borrow_eth} worth of ETH..")
    return (float(available_borrow_eth), float(total_debt_eth))

    
def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1)
    print("Approved!")
    return tx


def get_lending_pool():
    #this thing can change from time to time
    #ABI
    #Address
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(config["networks"][network.show_active()]["lending_pool_addresses_provider"])
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
     
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
    
    
    
    
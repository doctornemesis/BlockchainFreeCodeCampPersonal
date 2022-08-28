
from brownie import accounts, network, config


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
FORKED_LOCAL_ENVIRONMENTS = ["development", "ganache-local"]

def get_account(index = None, id = None):
    # account[0]
    # accounts.add("env")
    print(network.show_active)
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    
    return accounts.add(config["wallets"]["from_key"])
    
from scripts.helpful_scripts import get_account, get_contract
from brownie import Lottery, network, config

def deploy_lottery():
    #print(network.show_active())
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address, 
        get_contract("vrf_coordinator").address, 
        get_contract("link_token").address, 
        config["networks"][network.show_active()]["fee"], 
        config["networks"][network.show_active()]["keyhash"],
        {"from": account}, 
        publish_source = config["networks"][network.show_active()].get("verify", False))
    print("Deployed Lottery!!!")
    return lottery


def main():
    deploy_lottery()


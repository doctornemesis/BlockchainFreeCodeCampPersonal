from brownie import accounts, config, SimpleStorage, network

# import os

# def DeploySimpleStorage():
#     account = accounts[0]
#     # account = accounts.load("TestingAccountRinkebyFromMetaMask")
#     # print(account)
#     #account = accounts.add(os.getenv("PRIVATE_KEY"))
#     #account = accounts.add(config["wallets"]["from_key"])
#     print(account)
# this will print the public keys
# not private keys


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def DeploySimpleStorage():
    # account = accounts[0]
    account = get_account()
    print("Deploying Contract...")
    simple_storage_variable = SimpleStorage.deploy(
        {"from": account}
    )  # Here we are making a transaction
    print("Contract Deployed!")
    # basically a state change
    # print();
    # gvdgvd
    # fs
    print(simple_storage_variable)
    print("\n")

    print("Retrieving Value From Contract...")
    stored_value = simple_storage_variable.retrieve()
    # here retrieve is a view function... basically it wont change the state hence not a transaction...
    # so we wont send the <<<"from": account>>> in here
    print("Value Retrieved!")
    print(stored_value)

    print("Storing New Value to the Contract...")
    transaction = simple_storage_variable.store(15, {"from": account})
    transaction.wait(1)
    print("New Value 15 Stored!")
    print("Retrieving New Value From Contract...")
    stored_value = simple_storage_variable.retrieve()
    print("Value Retrieved!")
    print(stored_value)


def main():
    print("OHIO")
    DeploySimpleStorage()

from brownie import SimpleStorage, accounts

def test_deploy():
    #Arranging
    account = accounts[0]
    #Acting
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    #Asserting
    assert starting_value == expected


def test_updating_storage():
    #Arranging
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    #Acting
    expected = 15
    simple_storage.store(expected,{"from": account})
    updated_value = simple_storage.retrieve()
    #Asserting
    assert updated_value == expected
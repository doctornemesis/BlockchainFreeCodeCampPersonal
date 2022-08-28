Hello There...
SO now, we will be starting how to write Tests
Tests????

Tests are basically used to check if our contract is behaving as expected
well u can always get wrong output.. right???

#### First of all

create a test file
test_<name_of_the_file>.py
this is the exact syntax

start with the word test

# start with the word test

def test_deploy():
#Arranging
#Acting
#Asserting

Well this is going to be the step for testing....

def test_deploy():
#Arranging
account = accounts[0]
#Acting
simple_storage = SimpleStorage.deploy({"from": account})
starting_value = simple_storage.retrieve()
expected = 0
#Asserting
assert starting_value == expected

And this is the code...

Now how to test finally...

WELL USE BROWNIE TEST

# Terminal

        brownie test

Thats basically IT.......

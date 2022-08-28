okay so...
first we have to create a .sol file
this is the file that stores the contract

    it will be stored in the contracts folder not in build/contracts

    after creating that file, edit that file as per your contract requirements...

    Currently this file has a SimpleStorage from freecodecamp that stores a number...

    once this FILE is Created

    hit in the terminal.....
    ........

##### TERMINAL

                brownie compile

    #####################################

    Finally when compiled, your json file will be created.

    This json file will be stored in build/contracts...

    this will have your OPcode and ABI
    i dont know exactly what those 2 are as of now.....




    OKAY.....

    SO THE CODE IS COMPILED NOW.........

    WHAT NEXT......

    BLOCKCHAIN.......

    EXACTLY....

    NOW WE DEPLOY THIS TO BLOCKCHAIN......


    open the 'Scripts' folder and create your deploy.py file..
    you can name it whatever... but this will be a python file

    and this file will load our code to blockchain using brownie and whatever else we may use...





    So we are back to the 'deploy.py' file

    okay...

    So here we define the main() function

###### basically this...

    def main():
        //Whatever our functions are...


    We will have to take care of other functions in the main function...

    Finally after all the functions are written
    and called from the main function

    We will have to run this using Brownie from Terminal

    Dont directly RUN this... It will just use Python

    Instead...

###### TERMINAL

    brownie run scripts\deploy.py

###########################################

This will deploy the file using Brownie

This will default to ganache-cli

#### BASICALLY THIS PART

Launching 'ganache-cli.cmd --port 8545 --gasLimit 12000000 --accounts 10 --hardfork accounts 10 --hardfork istanbul --mnemonic brownie'...

##### EXPLAINATION

Okay, so this part means that Brownie
creates a new chain on Ganache-cli and deploys the code
Finally it shuts it down too...

##### ADDING ACCOUNT

##### There are 3 ways BRO....

# 1.

from brownie import accounts

def DeploySimpleStorage():
    account = accounts[0]
    print(account)

Okay... so here we are taking one of those
10 default accounts generated from Brownie
while it was deploying directly the Ganache-cli

# 2.

This way we can add an account directly to
command line

#### Terminal

    brownie accounts new <NameOfTheAccount>
    this will then ask you for PrivateKey..
    GO AHEAD
    basically..
    Add a '0X' like this 0XQWERTYUIOP......
    Then add a password...
    Hence we have security....

    you can remove this by...
    brownie accounts delete <NameOfTheAccount>

    you can see the list of accounts using
    brownie accounts list

    NOW IF WE WANT TO USE THIS ACCOUNT

    account = accounts.load("<NameOfTheAccount>")

    e.g.
    account = accounts.load("TestingAccountRinkebyFromMetaMask")

    now this will ask for password everytime
    we will try to run this...
    this is kinda best practice for account
    this wont store on github...

# 3.

    env variable method...
    dont prefer this method if you have real money in this....

    CREATE A .env file first
    and write whatever u need as the env variable

    in out case:
    export PRIVATE_KEY=0x2b5996c5bc......

# to use this method

        you will have to create a brownie-config.yaml file

        Then write in this file that you will create
        DOTENV as '.env'

        Then...
        account = accounts.add(os.getenv("PRIVATE_KEY"))

#### Then you can also modify the yaml file

well there are a couple of things u can add

wallets:
from_key: \${PRIVATE_KEY}
Basically this will help us remove OS dependencies
account = accounts.add(config["wallets"]["from_key"])
when u print this account, exactly same

# FINALLY WE ARE ACTUALLY DEPLOYING OUR FIRST CONTRACT

# AND MAKING USE OF STORE AND RETRIEVE FUNCTIONS THAT WE BUILT

You can directly check the code from here....
Its in deploy.py

    THATS IT....................

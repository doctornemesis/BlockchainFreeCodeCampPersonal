OKay...
So this file will explain everything in brief regarding our Lottery Application...

 Starting with 
1. brownie init
This will start our project and create the necessary files...

2. Create contracts\Lottery.sol 
Then we will code this file...

3. create brownie-config.yaml
Always remember spelling of dependencies, remappings (s is here) etc...

4. brownie compile
do this in terminal to check if your yaml file is ok

5. We are doing a test
6. Extra step...
I am configuring the network because we wont be using mainnet
but something which will look like mainnet
# brownie networks delete mainnet-fork
next we will add a new network using Alchemy
# visit alchemy
# create your own app in there
# generate your http key
in this case, we will be using... https://eth-mainnet.alchemyapi.io/v2/qRJHGM9zoxlBjMqvftGkojeoYRx29gYb
then we will add a new network
we use this code
# brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/qRJHGM9zoxlBjMqvftGkojeoYRx29gYb accounts=10 mnemonic=brownie port=8545
this will add a new network...

we will get this output:
Brownie v1.16.4 - Python development framework for Ethereum

SUCCESS: A new network 'mainnet-fork' has been added
  └─mainnet-fork
    ├─id: mainnet-fork
    ├─cmd: ganache-cli
    ├─cmd_settings: {'fork': 'https://eth-mainnet.alchemyapi.io/v2/qRJHGM9zoxlBjMqvftGkojeoYRx29gYb', 'accounts': 10, 'mnemonic': 'brownie', 'port': 8545}
    └─host: http://127.0.0.1

7.  Run tests
# brownie test --network mainnet-fork
adjust your pricing though... it failed for 19... hence changed to 15


8. ENUM
Now the next thing to do is timing the lottery
we dont want to end the lottery before it even starts
we will wait and iterate through the different phases of lottery

# Always remember to check spelling

9. OnlyOwner from OpenZeppelin
if we compile this right with all spellings correct, we get this...
        Compiling contracts...
        Solc version: 0.6.12
        Optimizer: Enabled  Runs: 200
        EVM Version: Istanbul
        Generating build data...
        - OpenZeppelin/openzeppelin-contracts@3.4.0/Ownable
        - OpenZeppelin/openzeppelin-contracts@3.4.0/Context
        - smartcontractkit/chainlink-brownie-contracts@1.1.1/AggregatorV3Interface      
        - Lottery

        Project has been compiled. Build artifacts saved at D:\Blockchain\FreeCodeCampPractice\lottery\build\contracts
This basically means that now, we can make any contract onlyOwner...

10. Then modify the contract in sol file to 'is Ownable'
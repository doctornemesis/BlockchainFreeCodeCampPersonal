okay...

welcome back...

This time we are working with AAVE

and guess what... we dont need to deploy any contract of our own...
everything is already there...

So, in this project we will be...
1. SWAP our ETH for WETH
1. Deposit some ETH(weth) into AAVE
2. Then we will borrow some asset with ETH collateral
    1. Maybe you can try to sell that borrowed asset
3. REPAY back everything...

This things works same in every other swapping contract 
like Uniswap, sushiswap, paraswap

now create script...
# aave_borrow.py

okay... so info...
generally on AAVE UI, AAVE is swapping our ETH to WETH(ERC20)

Basically, we have to convery 
#    ETH -> WETH




so... first...
#### get_weth.py

search for weth kovan contract etherscan
YOu will find a verified contract...
That deposits ETH and transfers WETH 

HEre we are using interfaces...
we created a file called IWETH.sol

created config....

### TESTING
we can do integration test on kovan
and maybe local test...
but AAVE has everything...

so, Unit test would be MainNet-fork
here instead of deploying mocks... 
we will mock the entire mainnet

### DEPOSIT ETH(WETH) into AAVE


Now, verification can be only done on the 
Rinkeby chain because the Price Feed contract is hardcoded
basically the address is written in the 
FundMe.sol file

   AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
     
Basically this line...

We will modify this line with appropriate option now

There are two ways.. 
Forking and Mocking....

#### FORKING
This is basically Forking a chain from the blockchain
and working on it for the project...


#### MOCKING
This is basically deploying a fake PriceFeed
on our local blockchain...




Okay... so if you try running this file now...
It will be deployed on a local Ganache-cli and then it will try
to verify the contract which will fail obviously...

 

#### DOING WITH MOCKS.....



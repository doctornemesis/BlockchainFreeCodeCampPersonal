Well...

Here we are going to learn how to verify

First go to Etherscan.io

and SignUp

Then go to MyProfile
then go to API Keys from the Left Menu

Then create your App
and get your API key...

For this project, the 
#### API KEY is

337GK9T74VW9G8MPICT4N39USGFS9H1HVQ

this thing ^^^^^^^




Then go to the .env file and create your etherscan token


then to verify, just add a ',' and write 
####     'publish_source=True' 
in the same line as {"from": account}

Example:::

fund_me = FundMe.deploy({"from": account}, publish_source=True)


That's basically it....


Now, verification can be only done on the 
Rinkeby chain because the Price Feed contract is hardcoded
basically the address is written in the 
FundMe.sol file

   AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
     
Basically this line...

We will modify this line with appropriate option in the next file...

There are two ways.. 
Forking and Mocking....


---
title: "Account & Portfolio Data"
description: "TWS API Documentation - Account & Portfolio Data"
source: "Interactive Brokers TWS API Documentation"
nav_id: "accounts"
scraped_at: "2025-08-01T00:35:10.751448"
word_count: 11238
paragraph_count: 481
subsection_count: 39
code_block_count: 42
format: "markdown"
---

# Account & Portfolio Data

## Account & Portfolio Data

The IBApi.EClient.reqAccountSummary method creates a subscription for the account data displayed in the TWS Account Summary window. It is commonly used with multiple-account structures. Introducing broker (IBroker) accounts with more than 50 subaccounts or configured for on-demand account lookup cannot use reqAccountSummary with group=”All”. A profile name can be accepted in place of group. See Unification of Groups and Profiles.
The TWS offers a comprehensive overview of your account and portfolio through its Account and Portfolio windows. This information can be obtained via the TWS API through three different kind of requests/operations.

The IBApi.EClient.reqAccountSummary method creates a subscription for the account data displayed in the TWS Account Summary window. It is commonly used with multiple-account structures. Introducing broker (IBroker) accounts with more than 50 subaccounts or configured for on-demand account lookup cannot use reqAccountSummary with group=”All”. A profile name can be accepted in place of group. See Unification of Groups and Profiles.
The TWS offers a comprehensive overview of your account and portfolio through its Account and Portfolio windows. This information can be obtained via the TWS API through three different kind of requests/operations.

### Account Summary

The initial invocation of reqAccountSummary will result in a list of all requested values being returned, and then every three minutes those values which have changed will be returned. The update frequency of 3 minutes is the same as the TWS Account Window and cannot be changed.

The initial invocation of reqAccountSummary will result in a list of all requested values being returned, and then every three minutes those values which have changed will be returned. The update frequency of 3 minutes is the same as the TWS Account Window and cannot be changed.

### Requesting Account Summary

Requests a specific account’s summary. This method will subscribe to the account summary as presented in the TWS’ Account Summary tab. Customers can specify the data received by using a specific tags value. See the Account Summary Tags section for available options.
Alternatively, many languages offer the import of AccountSummaryTags with a method to retrieve all tag values.

Requests a specific account’s summary. This method will subscribe to the account summary as presented in the TWS’ Account Summary tab. Customers can specify the data received by using a specific tags value. See the Account Summary Tags section for available options.
Alternatively, many languages offer the import of AccountSummaryTags with a method to retrieve all tag values.

#### EClient.reqAccountSummary(

reqId:int. The unique request identifier.
group:String. set to “All” to return account summary data for all accounts, or set to a specific Advisor Account Group name that has already been created in TWS Global Configuration.
tags:String. A comma separated list with thedesired tags
Important:onlytwoactive summary subscriptions are allowed at a time!
Code example:

#### EClient.reqAccountSummary(

reqId:int. The unique request identifier.
group:String. set to “All” to return account summary data for all accounts, or set to a specific Advisor Account Group name that has already been created in TWS Global Configuration.
tags:String. A comma separated list with thedesired tags
Important:onlytwoactive summary subscriptions are allowed at a time!

Code example:

Code example:

Code example:

#### EClient.reqAccountSummary(

Requests a specific account’s summary. This method will subscribe to the account summary as presented in the TWS’ Account Summary tab. Customers can specify the data received by using a specific tags value. See the Account Summary Tags section for available options.
Alternatively, many languages offer the import of AccountSummaryTags with a method to retrieve all tag values.

Requests a specific account’s summary. This method will subscribe to the account summary as presented in the TWS’ Account Summary tab. Customers can specify the data received by using a specific tags value. See the Account Summary Tags section for available options.
Alternatively, many languages offer the import of AccountSummaryTags with a method to retrieve all tag values.

Code example:

Code example:

Code example:

```python
self.reqAccountSummary(9001, "All", AccountSummaryTags.AllTags)
```

```python
from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import Contract
import time

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def accountSummary(self, reqId: int, account: str, tag: str, value: str,currency: str):
        print("AccountSummary. ReqId:", reqId, "Account:", account,"Tag: ", tag, "Value:", value, "Currency:", currency)
    
    def accountSummaryEnd(self, reqId: int):
        print("AccountSummaryEnd. ReqId:", reqId)
    
app = TradeApp()      
app.connect("127.0.0.1", 7496, clientId=1)

time.sleep(1)

app.reqAccountSummary(9001, "All", 'NetLiquidation')
app.run()
```

### Account Summary Tags

AccountTypeIdentifies the IB account structureNetLiquidationThe basis for determining the price of the assets in your account. Total cash value + stock value + options value + bond valueTotalCashValueTotal cash balance recognized at the time of trade + futures PNLSettledCashCash recognized at the time of settlement – purchases at the time of trade – commissions – taxes – feesAccruedCashTotal accrued cash value of stock, commodities and securitiesBuyingPowerBuying power serves as a measurement of the dollar value of securities that one may purchase in a securities account without depositing additional fundsEquityWithLoanValueForms the basis for determining whether a client has the necessary assets to either initiate or maintain security positions. Cash + stocks + bonds + mutual fundsPreviousEquityWithLoanValueMarginable Equity with Loan value as of 16:00 ET the previous dayGrossPositionValueThe sum of the absolute value of all stock and equity option positionsRegTEquityRegulation T equity for universal accountRegTMarginRegulation T margin for universal accountSMASpecial Memorandum Account: Line of credit created when the market value of securities in a Regulation T account increase in valueInitMarginReqInitial Margin requirement of whole portfolioMaintMarginReqMaintenance Margin requirement of whole portfolioAvailableFundsThis value tells what you have available for tradingExcessLiquidityThis value shows your margin cushion, before liquidationCushionExcess liquidity as a percentage of net liquidation valueFullInitMarginReqInitial Margin of whole portfolio with no discounts or intraday creditsFullMaintMarginReqMaintenance Margin of whole portfolio with no discounts or intraday creditsFullAvailableFundsAvailable funds of whole portfolio with no discounts or intraday creditsFullExcessLiquidityExcess liquidity of whole portfolio with no discounts or intraday creditsLookAheadNextChangeTime when look-ahead values take effectLookAheadInitMarginReqInitial Margin requirement of whole portfolio as of next period’s margin changeLookAheadMaintMarginReqMaintenance Margin requirement of whole portfolio as of next period’s margin changeLookAheadAvailableFundsThis value reflects your available funds at the next margin changeLookAheadExcessLiquidityThis value reflects your excess liquidity at the next margin changeHighestSeverityA measure of how close the account is to liquidationDayTradesRemainingThe Number of Open/Close trades a user could put on before Pattern Day Trading is detected. A value of “-1” means that the user can put on unlimited day trades.LeverageGrossPositionValue / NetLiquidation$LEDGERSingle flag to relay all cash balance tags*, only in base currency.$LEDGER:CURRENCYSingle flag to relay all cash balance tags*, only in the specified currency.$LEDGER:ALLSingle flag to relay all cash balance tags* in all currencies.

### Receiving Account Summary

#### EWrapper.accountSummary(

reqId:int. the request’s unique identifier.
account:String. the account id
tag:String. the account’s attribute being received.
value:String. the account’s attribute’s value.
currency:String. the currency on which the value is expressed.
Receives the account information. This method will receive the account information just as it appears in the TWS’ Account Summary Window.

#### EWrapper.accountSummary(

reqId:int. the request’s unique identifier.
account:String. the account id
tag:String. the account’s attribute being received.
value:String. the account’s attribute’s value.
currency:String. the currency on which the value is expressed.
Receives the account information. This method will receive the account information just as it appears in the TWS’ Account Summary Window.

#### EWrapper.accountSummaryEnd(

reqId:String. The request’s identifier.
Notifies when all the accounts’ information has ben received. Requires TWS 967+ to receive accountSummaryEnd in linked account structures.

#### EWrapper.accountSummaryEnd(

reqId:String. The request’s identifier.
Notifies when all the accounts’ information has ben received. Requires TWS 967+ to receive accountSummaryEnd in linked account structures.

#### EWrapper.accountSummary(

#### EWrapper.accountSummaryEnd(

reqId:String. The request’s identifier.
Notifies when all the accounts’ information has ben received. Requires TWS 967+ to receive accountSummaryEnd in linked account structures.

#### EWrapper.accountSummaryEnd(

reqId:String. The request’s identifier.
Notifies when all the accounts’ information has ben received. Requires TWS 967+ to receive accountSummaryEnd in linked account structures.

#### EWrapper.accountSummaryEnd(

#### EWrapper.accountSummary(

reqId:int. the request’s unique identifier.
account:String. the account id
tag:String. the account’s attribute being received.
value:String. the account’s attribute’s value.
currency:String. the currency on which the value is expressed.
Receives the account information. This method will receive the account information just as it appears in the TWS’ Account Summary Window.

#### EWrapper.accountSummary(

reqId:int. the request’s unique identifier.
account:String. the account id
tag:String. the account’s attribute being received.
value:String. the account’s attribute’s value.
currency:String. the currency on which the value is expressed.
Receives the account information. This method will receive the account information just as it appears in the TWS’ Account Summary Window.

```python
def accountSummary(self, reqId: int, account: str, tag: str, value: str,currency: str):
  print("AccountSummary. ReqId:", reqId, "Account:", account,"Tag: ", tag, "Value:", value, "Currency:", currency)
```

```python
def accountSummaryEnd(self, reqId: int):
    print("AccountSummaryEnd. ReqId:", reqId)
```

### Cancel Account Summary

Once the subscription to account summary is no longer needed, it can be cancelled via the IBApi::EClient::cancelAccountSummary method:

Once the subscription to account summary is no longer needed, it can be cancelled via the IBApi::EClient::cancelAccountSummary method:

#### EClient.cancelAccountSummary(

reqId:int. The identifier of the previously performed account request
PythonC++

#### EClient.cancelAccountSummary(

reqId:int. The identifier of the previously performed account request

PythonC++

PythonC++

PythonC++

#### EClient.cancelAccountSummary(

Once the subscription to account summary is no longer needed, it can be cancelled via the IBApi::EClient::cancelAccountSummary method:

Once the subscription to account summary is no longer needed, it can be cancelled via the IBApi::EClient::cancelAccountSummary method:

PythonC++

PythonC++

PythonC++

```python
self.cancelAccountSummary(9001)
```

### Account Updates

The IBApi.EClient.reqAccountUpdates function creates a subscription to the TWS through which account and portfolio information is delivered. This information is the exact same as the one displayed within the TWS’ Account Window. Just as with the TWS’ Account Window, unless there is a position change this information is updated at a fixed interval of three minutes.

The IBApi.EClient.reqAccountUpdates function creates a subscription to the TWS through which account and portfolio information is delivered. This information is the exact same as the one displayed within the TWS’ Account Window. Just as with the TWS’ Account Window, unless there is a position change this information is updated at a fixed interval of three minutes.

Unrealized and Realized P&L is sent to the API function IBApi.EWrapper.updateAccountValue function after a subscription request is made with IBApi.EClient.reqAccountUpdates. This information corresponds to the data in the TWS Account Window, and has a different source of information, a different update frequency, and different reset schedule than PnL data in the TWS Portfolio Window and associated API functions (below). In particular, the unrealized P&L information shown in the TWS Account Window which is sent toEWrapper.updatePortfoliowill update either (1) when a trade for that particular instrument occurs or (2) every 3 minutes. The realized P&L data in the TWS Account Window is reset to 0 once per day.
It is important to keep in mind that the P&L data shown in the Account Window and Portfolio Window will sometimes differ because there is a different source of information and a different reset schedule.
SeeProfit & Lossfor alternative PnL data

Unrealized and Realized P&L is sent to the API function IBApi.EWrapper.updateAccountValue function after a subscription request is made with IBApi.EClient.reqAccountUpdates. This information corresponds to the data in the TWS Account Window, and has a different source of information, a different update frequency, and different reset schedule than PnL data in the TWS Portfolio Window and associated API functions (below). In particular, the unrealized P&L information shown in the TWS Account Window which is sent toEWrapper.updatePortfoliowill update either (1) when a trade for that particular instrument occurs or (2) every 3 minutes. The realized P&L data in the TWS Account Window is reset to 0 once per day.
It is important to keep in mind that the P&L data shown in the Account Window and Portfolio Window will sometimes differ because there is a different source of information and a different reset schedule.
SeeProfit & Lossfor alternative PnL data

### Requesting Account Updates

Subscribes to a specific account’s information and portfolio. Through this method, a single account’s subscription can be started/stopped. As a result from the subscription, the account’s information, portfolio and last update time will be received at EWrapper.updateAccountValue, EWrapper.updatePortfolio, EWrapper.updateAccountTime respectively. All account values and positions will be returned initially, and then there will only be updates when there is a change in a position, or to an account value every 3 minutes if it has changed. Only one account can be subscribed at a time. A second subscription request for another account when the previous one is still active will cause the first one to be canceled in favor of the second one.

Subscribes to a specific account’s information and portfolio. Through this method, a single account’s subscription can be started/stopped. As a result from the subscription, the account’s information, portfolio and last update time will be received at EWrapper.updateAccountValue, EWrapper.updatePortfolio, EWrapper.updateAccountTime respectively. All account values and positions will be returned initially, and then there will only be updates when there is a change in a position, or to an account value every 3 minutes if it has changed. Only one account can be subscribed at a time. A second subscription request for another account when the previous one is still active will cause the first one to be canceled in favor of the second one.

#### EClient.reqAccountUpdates(

subscribe:bool. Set to true to start the subscription and to false to stop it.
acctCode:String. The account id (i.e. U123456) for which the information is requested.
Code example:

#### EClient.reqAccountUpdates(

subscribe:bool. Set to true to start the subscription and to false to stop it.
acctCode:String. The account id (i.e. U123456) for which the information is requested.

Code example:

Code example:

Code example:

#### EClient.reqAccountUpdates(

Subscribes to a specific account’s information and portfolio. Through this method, a single account’s subscription can be started/stopped. As a result from the subscription, the account’s information, portfolio and last update time will be received at EWrapper.updateAccountValue, EWrapper.updatePortfolio, EWrapper.updateAccountTime respectively. All account values and positions will be returned initially, and then there will only be updates when there is a change in a position, or to an account value every 3 minutes if it has changed. Only one account can be subscribed at a time. A second subscription request for another account when the previous one is still active will cause the first one to be canceled in favor of the second one.

Subscribes to a specific account’s information and portfolio. Through this method, a single account’s subscription can be started/stopped. As a result from the subscription, the account’s information, portfolio and last update time will be received at EWrapper.updateAccountValue, EWrapper.updatePortfolio, EWrapper.updateAccountTime respectively. All account values and positions will be returned initially, and then there will only be updates when there is a change in a position, or to an account value every 3 minutes if it has changed. Only one account can be subscribed at a time. A second subscription request for another account when the previous one is still active will cause the first one to be canceled in favor of the second one.

Code example:

Code example:

Code example:

```python
self.reqAccountUpdates(True, self.account)
```

```python
from ibapi.client import *
from ibapi.wrapper import *
from ibapi.contract import Contract
import time

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def updateAccountValue(self, key: str, val: str, currency: str,accountName: str):
        print("UpdateAccountValue. Key:", key, "Value:", val, "Currency:", currency, "AccountName:", accountName)
    
    def updatePortfolio(self, contract: Contract, position: Decimal,marketPrice: float, marketValue: float, averageCost: float, unrealizedPNL: float, realizedPNL: float, accountName: str):
        print("UpdatePortfolio.", "Symbol:", contract.symbol, "SecType:", contract.secType, "Exchange:",contract.exchange, "Position:", decimalMaxString(position), "MarketPrice:", floatMaxString(marketPrice),"MarketValue:", floatMaxString(marketValue), "AverageCost:", floatMaxString(averageCost), "UnrealizedPNL:", floatMaxString(unrealizedPNL), "RealizedPNL:", floatMaxString(realizedPNL), "AccountName:", accountName)

    def updateAccountTime(self, timeStamp: str):
        print("UpdateAccountTime. Time:", timeStamp)

    def accountDownloadEnd(self, accountName: str):
        print("AccountDownloadEnd. Account:", accountName)
    
app = TradeApp()      
app.connect("127.0.0.1", 7496, clientId=1)

time.sleep(1)

app.reqAccountUpdates(True, 'U123456')
app.run()
```

### Receiving Account Updates

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.updateAccountValue(

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.updatePortfolio(

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.updateAccountTime(

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.accountDownloadEnd(

account:String. The account identifier.
Notifies when all the account’s information has finished.

#### EWrapper.accountDownloadEnd(

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

Resulting account and portfolio information will be delivered via the IBApi.EWrapper.updateAccountValue, IBApi.EWrapper.updatePortfolio, IBApi.EWrapper.updateAccountTime and IBApi.EWrapper.accountDownloadEnd

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updateAccountValue(

key:String. The value being updated.
value:String. up-to-date value
currency:String. The currency on which the value is expressed.
accountName:String. The account identifier.)
Receives the subscribed account’s information. Only one account can be subscribed at a time. After the initial callback to updateAccountValue, callbacks only occur for values which have changed. This occurs at the time of a position change, or every 3 minutes at most. This frequency cannot be adjusted.
Note:An important key passed back in EWrapper.updateAccountValue after a call to EClient.reqAccountUpdates is a boolean value ‘accountReady’. If an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.updatePortfolio(

contract:Contract. The Contract for which a position is held.
position:Decimal. The number of positions held.
marketPrice:Double. The instrument’s unitary price
marketValue:Double. Total market value of the instrument.
averageCost:Double. Average cost of the overall position.
unrealizedPNL:Double. Daily unrealized profit and loss on the position.
realizedPNL:Double. Daily realized profit and loss on the position.
accountName:String. Account ID for the update.
Receives the subscribed account’s portfolio. This function will receive only the portfolio of the subscribed account. After the initial callback to updatePortfolio, callbacks only occur for positions which have changed.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

#### EWrapper.updateAccountTime(

timestamp:String. the last update system time.
Receives the last time on which the account was updated.

```python
def updateAccountValue(self, key: str, val: str, currency: str,accountName: str):
    print("UpdateAccountValue. Key:", key, "Value:", val, "Currency:", currency, "AccountName:", accountName)
```

```python
def updatePortfolio(self, contract: Contract, position: Decimal,marketPrice: float, marketValue: float, averageCost: float, unrealizedPNL: float, realizedPNL: float, accountName: str):
    print("UpdatePortfolio.", "Symbol:", contract.symbol, "SecType:", contract.secType, "Exchange:",contract.exchange, "Position:", decimalMaxString(position), "MarketPrice:", floatMaxString(marketPrice),"MarketValue:", floatMaxString(marketValue), "AverageCost:", floatMaxString(averageCost), "UnrealizedPNL:", floatMaxString(unrealizedPNL), "RealizedPNL:", floatMaxString(realizedPNL), "AccountName:", accountName)
```

```python
def updateAccountTime(self, timeStamp: str):
     print("UpdateAccountTime. Time:", timeStamp)
```

```python
def accountDownloadEnd(self, accountName: str):
    print("AccountDownloadEnd. Account:", accountName)
```

### Account Value Keys

When requestingreqAccountUpdatescustomers will receive values corresponding to various account key/value pairs. The table below documents potential responses and what they mean.
Account values delivered viaIBApi.EWrapper.updateAccountValuecan be classified in the following way:
Commodities: suffixed by a “-C”Securities: suffixed by a “-S”Totals: no suffix

When requestingreqAccountUpdatescustomers will receive values corresponding to various account key/value pairs. The table below documents potential responses and what they mean.
Account values delivered viaIBApi.EWrapper.updateAccountValuecan be classified in the following way:
Commodities: suffixed by a “-C”Securities: suffixed by a “-S”Totals: no suffix

KeyDescriptionAccountCodeThe account ID numberAccountOrGroup“All” to return account summary data for all accounts, or set to a specific Advisor Account Group name that has already been created in TWS Global ConfigurationAccountReadyIf an accountReady value of false is returned that means that the IB server is in the process of resetting at that moment, i.e. the account is ‘not ready’. When this occurs subsequent key values returned to EWrapper.updateAccountValue in the current update can be out of date or incorrect.AccountTypeIdentifies the IB account structureAccruedCashTotal accrued cash value of stock, commodities and securitiesAccruedCash-CReflects the current’s month accrued debit and credit interest to date, updated daily in commodity segmentAccruedCash-SReflects the current’s month accrued debit and credit interest to date, updated daily in security segmentAccruedDividendTotal portfolio value of dividends accruedAccruedDividend-CDividends accrued but not paid in commodity segmentAccruedDividend-SDividends accrued but not paid in security segmentAvailableFundsThis value tells what you have available for tradingAvailableFunds-CNet Liquidation Value – Initial MarginAvailableFunds-SEquity with Loan Value – Initial MarginBillableTotal portfolio value of treasury billsBillable-CValue of treasury bills in commodity segmentBillable-SValue of treasury bills in security segmentBuyingPowerCash Account: Minimum (Equity with Loan Value, Previous Day Equity with Loan Value)-Initial Margin, Standard Margin Account: Minimum (Equity with Loan Value, Previous Day Equity with Loan Value) – Initial Margin *4CashBalanceCash recognized at the time of trade + futures PNLCorporateBondValueValue of non-Government bonds such as corporate bonds and municipal bondsCurrencyOpen positions are grouped by currencyCushionExcess liquidity as a percentage of net liquidation valueDayTradesRemainingNumber of Open/Close trades one could do before Pattern Day Trading is detectedDayTradesRemainingT+1Number of Open/Close trades one could do tomorrow before Pattern Day Trading is detectedDayTradesRemainingT+2Number of Open/Close trades one could do two days from today before Pattern Day Trading is detectedDayTradesRemainingT+3Number of Open/Close trades one could do three days from today before Pattern Day Trading is detectedDayTradesRemainingT+4Number of Open/Close trades one could do four days from today before Pattern Day Trading is detectedEquityWithLoanValueForms the basis for determining whether a client has the necessary assets to either initiate or maintain security positionsEquityWithLoanValue-CCash account: Total cash value + commodities option value – futures maintenance margin requirement + minimum (0, futures PNL) Margin account: Total cash value + commodities option value – futures maintenance margin requirementEquityWithLoanValue-SCash account: Settled Cash Margin Account: Total cash value + stock value + bond value + (non-U.S. & Canada securities options value)ExcessLiquidityThis value shows your margin cushion, before liquidationExcessLiquidity-CEquity with Loan Value – Maintenance MarginExcessLiquidity-SNet Liquidation Value – Maintenance MarginExchangeRateThe exchange rate of the currency to your base currencyFullAvailableFundsAvailable funds of whole portfolio with no discounts or intraday creditsFullAvailableFunds-CNet Liquidation Value – Full Initial MarginFullAvailableFunds-SEquity with Loan Value – Full Initial MarginFullExcessLiquidityExcess liquidity of whole portfolio with no discounts or intraday creditsFullExcessLiquidity-CNet Liquidation Value – Full Maintenance MarginFullExcessLiquidity-SEquity with Loan Value – Full Maintenance MarginFullInitMarginReqInitial Margin of whole portfolio with no discounts or intraday creditsFullInitMarginReq-CInitial Margin of commodity segment’s portfolio with no discounts or intraday creditsFullInitMarginReq-SInitial Margin of security segment’s portfolio with no discounts or intraday creditsFullMaintMarginReqMaintenance Margin of whole portfolio with no discounts or intraday creditsFullMaintMarginReq-CMaintenance Margin of commodity segment’s portfolio with no discounts or intraday creditsFullMaintMarginReq-SMaintenance Margin of security segment’s portfolio with no discounts or intraday creditsFundValueValue of funds value (money market funds + mutual funds)FutureOptionValueReal-time market-to-market value of futures optionsFuturesPNLReal-time changes in futures value since last settlementFxCashBalanceCash balance in related IB-UKL accountGrossPositionValueGross Position Value in securities segmentGrossPositionValue-SLong Stock Value + Short Stock Value + Long Option Value + Short Option ValueIndianStockHaircutMargin rule for IB-IN accountsInitMarginReqInitial Margin requirement of whole portfolioInitMarginReq-CInitial Margin of the commodity segment in base currencyInitMarginReq-SInitial Margin of the security segment in base currencyIssuerOptionValueReal-time mark-to-market value of Issued OptionLeverage-SGrossPositionValue / NetLiquidation in security segmentLookAheadNextChangeTime when look-ahead values take effectLookAheadAvailableFundsThis value reflects your available funds at the next margin changeLookAheadAvailableFunds-CNet Liquidation Value – look ahead Initial MarginLookAheadAvailableFunds-SEquity with Loan Value – look ahead Initial MarginLookAheadExcessLiquidityThis value reflects your excess liquidity at the next margin changeLookAheadExcessLiquidity-CNet Liquidation Value – look ahead Maintenance MarginLookAheadExcessLiquidity-SEquity with Loan Value – look ahead Maintenance MarginLookAheadInitMarginReqInitial margin requirement of whole portfolio as of next period’s margin changeLookAheadInitMarginReq-CInitial margin requirement as of next period’s margin change in the base currency of the accountLookAheadInitMarginReq-SInitial margin requirement as of next period’s margin change in the base currency of the accountLookAheadMaintMarginReqMaintenance margin requirement of whole portfolio as of next period’s margin changeLookAheadMaintMarginReq-CMaintenance margin requirement as of next period’s margin change in the base currency of the accountLookAheadMaintMarginReq-SMaintenance margin requirement as of next period’s margin change in the base currency of the accountMaintMarginReqMaintenance Margin requirement of whole portfolioMaintMarginReq-CMaintenance Margin for the commodity segmentMaintMarginReq-SMaintenance Margin for the security segmentMoneyMarketFundValueMarket value of money market funds excluding mutual fundsMutualFundValueMarket value of mutual funds excluding money market fundsNetDividendThe sum of the Dividend Payable/Receivable Values for the securities and commodities segments of the accountNetLiquidationThe basis for determining the price of the assets in your accountNetLiquidation-CTotal cash value + futures PNL + commodities options valueNetLiquidation-STotal cash value + stock value + securities options value + bond valueNetLiquidationByCurrencyNet liquidation for individual currenciesOptionMarketValueReal-time mark-to-market value of optionsPASharesValuePersonal Account shares value of whole portfolioPASharesValue-CPersonal Account shares value in commodity segmentPASharesValue-SPersonal Account shares value in security segmentPostExpirationExcessTotal projected “at expiration” excess liquidityPostExpirationExcess-CProvides a projected “at expiration” excess liquidity based on the soon-to expire contracts in your portfolio in commodity segmentPostExpirationExcess-SProvides a projected “at expiration” excess liquidity based on the soon-to expire contracts in your portfolio in security segmentPostExpirationMarginTotal projected “at expiration” marginPostExpirationMargin-CProvides a projected “at expiration” margin value based on the soon-to expire contracts in your portfolio in commodity segmentPostExpirationMargin-SProvides a projected “at expiration” margin value based on the soon-to expire contracts in your portfolio in security segmentPreviousDayEquityWithLoanValueMarginable Equity with Loan value as of 16:00 ET the previous day in securities segmentPreviousDayEquityWithLoanValue-SIMarginable Equity with Loan value as of 16:00 ET the previous dayRealCurrencyOpen positions are grouped by currencyRealizedPnLShows your profit on closed positions, which is the difference between your entry execution cost and exit execution costs, or (execution price + commissions to open the positions) – (execution price + commissions to close the position)RegTEquityRegulation T equity for universal accountRegTEquity-SRegulation T equity for security segmentRegTMarginRegulation T margin for universal accountRegTMargin-SRegulation T margin for security segmentSMALine of credit created when the market value of securities in a Regulation T account increase in valueSMA-SRegulation T Special Memorandum Account balance for security segmentSegmentTitleAccount segment nameStockMarketValueReal-time mark-to-market value of stockTBondValueValue of treasury bondsTBillValueValue of treasury billsTotalCashBalanceTotal Cash Balance including Future PNLTotalCashValueTotal cash value of stock, commodities and securitiesTotalCashValue-CCashBalance in commodity segmentTotalCashValue-SCashBalance in security segmentTradingType-SAccount TypeUnrealizedPnLThe difference between the current market value of your open positions and the average cost, or Value – Average CostWarrantValueValue of warrantsWhatIfPMEnabledTo check projected margin requirements under Portfolio Margin model

### Cancel Account Updates

Once the subscription to account updates is no longer needed, it can be cancelled by invoking the IBApi.EClient.reqAccountUpdates method while specifying the susbcription flag to be False.
Important:only one account at a time can be subscribed at a time. Attempting a second subscription without previously cancelling an active one will not yield any error message although it will override the already subscribed account with the new one. With Financial Advisory (FA) account structures there is an alternative way of specifying the account code such that information is returned for ‘All’ sub accounts- this is done by appending the letter ‘A’ to the end of the account number, i.e. reqAccountUpdates(true, “F123456A”)

Once the subscription to account updates is no longer needed, it can be cancelled by invoking the IBApi.EClient.reqAccountUpdates method while specifying the susbcription flag to be False.
Important:only one account at a time can be subscribed at a time. Attempting a second subscription without previously cancelling an active one will not yield any error message although it will override the already subscribed account with the new one. With Financial Advisory (FA) account structures there is an alternative way of specifying the account code such that information is returned for ‘All’ sub accounts- this is done by appending the letter ‘A’ to the end of the account number, i.e. reqAccountUpdates(true, “F123456A”)

#### EClient.reqAccountUpdates(

subscribe:bool. Set to true to start the subscription and to false to stop it.
acctCode:String. The account id (i.e. U123456) for which the information is requested.

#### EClient.reqAccountUpdates(

subscribe:bool. Set to true to start the subscription and to false to stop it.
acctCode:String. The account id (i.e. U123456) for which the information is requested.

#### EClient.reqAccountUpdates(

Once the subscription to account updates is no longer needed, it can be cancelled by invoking the IBApi.EClient.reqAccountUpdates method while specifying the susbcription flag to be False.
Important:only one account at a time can be subscribed at a time. Attempting a second subscription without previously cancelling an active one will not yield any error message although it will override the already subscribed account with the new one. With Financial Advisory (FA) account structures there is an alternative way of specifying the account code such that information is returned for ‘All’ sub accounts- this is done by appending the letter ‘A’ to the end of the account number, i.e. reqAccountUpdates(true, “F123456A”)

Once the subscription to account updates is no longer needed, it can be cancelled by invoking the IBApi.EClient.reqAccountUpdates method while specifying the susbcription flag to be False.
Important:only one account at a time can be subscribed at a time. Attempting a second subscription without previously cancelling an active one will not yield any error message although it will override the already subscribed account with the new one. With Financial Advisory (FA) account structures there is an alternative way of specifying the account code such that information is returned for ‘All’ sub accounts- this is done by appending the letter ‘A’ to the end of the account number, i.e. reqAccountUpdates(true, “F123456A”)

```python
self.reqAccountUpdates(False, self.account)
```

### Account Update by Model

Account Update by Model

### Requesting Account Update by Model

The IBApi.EClient.reqAccountUpdatesMulti can be used in any account structure to create simultaneous account value subscriptions from one or multiple accounts and/or models. As with IBApi.EClient.reqAccountUpdates the data returned will match that displayed within the TWS Account Window.

The IBApi.EClient.reqAccountUpdatesMulti can be used in any account structure to create simultaneous account value subscriptions from one or multiple accounts and/or models. As with IBApi.EClient.reqAccountUpdates the data returned will match that displayed within the TWS Account Window.

#### EClient.reqAccountUpdatesMulti(

reqId:int. Identifier to label the request
account:String. Account values can be requested for a particular account
modelCode:String. Values can also be requested for a model
ledgerAndNLV:bool. returns light-weight request; only currency positions as opposed to account values and currency positions
Requests account updates for account and/or model.
IBApi.EClient.reqAccountUpdatesMulti cannot be used with Account=”All” in IBroker accounts with more than 50 subaccounts.
A profile name can be accepted in place of group in the account parameter forFinancial Advisors
Code example:

#### EClient.reqAccountUpdatesMulti(

reqId:int. Identifier to label the request
account:String. Account values can be requested for a particular account
modelCode:String. Values can also be requested for a model
ledgerAndNLV:bool. returns light-weight request; only currency positions as opposed to account values and currency positions
Requests account updates for account and/or model.
IBApi.EClient.reqAccountUpdatesMulti cannot be used with Account=”All” in IBroker accounts with more than 50 subaccounts.
A profile name can be accepted in place of group in the account parameter forFinancial Advisors

Code example:

Code example:

Code example:

#### EClient.reqAccountUpdatesMulti(

The IBApi.EClient.reqAccountUpdatesMulti can be used in any account structure to create simultaneous account value subscriptions from one or multiple accounts and/or models. As with IBApi.EClient.reqAccountUpdates the data returned will match that displayed within the TWS Account Window.

The IBApi.EClient.reqAccountUpdatesMulti can be used in any account structure to create simultaneous account value subscriptions from one or multiple accounts and/or models. As with IBApi.EClient.reqAccountUpdates the data returned will match that displayed within the TWS Account Window.

Code example:

Code example:

Code example:

```python
self.reqAccountUpdatesMulti(reqId, self.account, "", True)
```

```python
from ibapi.client import *
from ibapi.wrapper import *
import time

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def accountUpdateMulti(self, reqId: int, account: str, modelCode: str, key: str, value: str, currency: str):
        print("AccountUpdateMulti. RequestId:", reqId, "Account:", account, "ModelCode:", modelCode, "Key:", key, "Value:", value, "Currency:", currency)

    def accountUpdateMultiEnd(self, reqId: int):
        print("AccountUpdateMultiEnd. RequestId:", reqId)
    
app = TradeApp()      
app.connect("127.0.0.1", 7496, clientId=1)

time.sleep(1)

app.reqAccountUpdatesMulti(103, 'U123456', "", True)

app.run()
```

### Receiving Account Updates by Model

The resulting account and portfolio information will be delivered via the IBApi.EWrapper.accountUpdateMulti and IBApi.EWrapper.accountUpdateMultiEnd

The resulting account and portfolio information will be delivered via the IBApi.EWrapper.accountUpdateMulti and IBApi.EWrapper.accountUpdateMultiEnd

#### EWrapper.accountUpdateMulti(

requestId:int. The id of request.
account:String. The account with updates.
modelCode:String. The model code with updates.
key:String. The name of parameter.
value:String. The value of parameter.
currency:String. The currency of parameter.)
Provides the account updates.

#### EWrapper.accountUpdateMulti(

requestId:int. The id of request.
account:String. The account with updates.
modelCode:String. The model code with updates.
key:String. The name of parameter.
value:String. The value of parameter.
currency:String. The currency of parameter.)
Provides the account updates.

#### EWrapper.accountUpdateMultiEnd(

requestId:int. The id of request
Indicates all the account updates have been transmitted.

#### EWrapper.accountUpdateMultiEnd(

requestId:int. The id of request
Indicates all the account updates have been transmitted.

#### EWrapper.accountUpdateMulti(

The resulting account and portfolio information will be delivered via the IBApi.EWrapper.accountUpdateMulti and IBApi.EWrapper.accountUpdateMultiEnd

The resulting account and portfolio information will be delivered via the IBApi.EWrapper.accountUpdateMulti and IBApi.EWrapper.accountUpdateMultiEnd

#### EWrapper.accountUpdateMultiEnd(

requestId:int. The id of request
Indicates all the account updates have been transmitted.

#### EWrapper.accountUpdateMultiEnd(

requestId:int. The id of request
Indicates all the account updates have been transmitted.

#### EWrapper.accountUpdateMultiEnd(

The resulting account and portfolio information will be delivered via the IBApi.EWrapper.accountUpdateMulti and IBApi.EWrapper.accountUpdateMultiEnd

The resulting account and portfolio information will be delivered via the IBApi.EWrapper.accountUpdateMulti and IBApi.EWrapper.accountUpdateMultiEnd

#### EWrapper.accountUpdateMulti(

requestId:int. The id of request.
account:String. The account with updates.
modelCode:String. The model code with updates.
key:String. The name of parameter.
value:String. The value of parameter.
currency:String. The currency of parameter.)
Provides the account updates.

#### EWrapper.accountUpdateMulti(

requestId:int. The id of request.
account:String. The account with updates.
modelCode:String. The model code with updates.
key:String. The name of parameter.
value:String. The value of parameter.
currency:String. The currency of parameter.)
Provides the account updates.

```python
def accountUpdateMulti(self, reqId: int, account: str, modelCode: str, key: str, value: str, currency: str):
  print("AccountUpdateMulti. RequestId:", reqId, "Account:", account, "ModelCode:", modelCode, "Key:", key, "Value:", value, "Currency:", currency)
```

```python
def accountUpdateMultiEnd(self, reqId: int):
    print("AccountUpdateMultiEnd. RequestId:", reqId)
```

### Cancel Account Updates by Model

#### EClient.reqAccountUpdatesMulti (

reqId:int. Identifier to label the request
account:String. Account values can be requested for a particular account
modelCode:String. Values can also be requested for a model
ledgerAndNLV:bool. Specify false to cancel your subscription.

#### EClient.reqAccountUpdatesMulti (

reqId:int. Identifier to label the request
account:String. Account values can be requested for a particular account
modelCode:String. Values can also be requested for a model
ledgerAndNLV:bool. Specify false to cancel your subscription.

#### EClient.reqAccountUpdatesMulti (

```python
self.reqAccountUpdatesMulti(reqId, self.account, "", False)
```

### Family Codes

It is possible to determine from the API whether an account exists under an account family, and find the family code using the function reqFamilyCodes.
For instance, if individual account U112233 is under a financial advisor with account number F445566, if the function reqFamilyCodes is invoked for the user of account U112233, the family code “F445566A” will be returned, indicating that it belongs within that account family.

It is possible to determine from the API whether an account exists under an account family, and find the family code using the function reqFamilyCodes.
For instance, if individual account U112233 is under a financial advisor with account number F445566, if the function reqFamilyCodes is invoked for the user of account U112233, the family code “F445566A” will be returned, indicating that it belongs within that account family.

### Request Family Codes

#### EClient.reqFamilyCodes()

Requests family codes for an account, for instance if it is a FA, IBroker, or associated account.

#### EClient.reqFamilyCodes()

Requests family codes for an account, for instance if it is a FA, IBroker, or associated account.

#### EClient.reqFamilyCodes()

```python
self.reqFamilyCodes()
```

### Receive Family Codes

#### EWrapper.familyCodes(

familyCodes:FamilyCodes[]. Unique family codes array of accountIds.
Returns array of family codes.

#### EWrapper.familyCodes(

familyCodes:FamilyCodes[]. Unique family codes array of accountIds.
Returns array of family codes.

#### EWrapper.familyCodes(

```python
def familyCodes(self, familyCodes: ListOfFamilyCode):
    print("Family Codes:", familyCode)
```

```python
@Override
public void familyCodes(FamilyCode[] familyCodes) {
    System.out.print(EWrapperMsgGenerator.familyCodes(familyCodes));
}
```

### Managed Accounts

A single user name can handle more than one account. As mentioned in theConnectivitysection, the TWS will automatically send a list of managed accounts once the connection is established. The list can also be fetched via the IBApi.EClient.reqManagedAccts method.

A single user name can handle more than one account. As mentioned in theConnectivitysection, the TWS will automatically send a list of managed accounts once the connection is established. The list can also be fetched via the IBApi.EClient.reqManagedAccts method.

### Request Managed Accounts

#### EClient.reqManagedAccts()

Requests the accounts to which the logged user has access to.

#### EClient.reqManagedAccts()

Requests the accounts to which the logged user has access to.

#### EClient.reqManagedAccts()

```python
self.reqManagedAccts()
```

### Receive Managed Accounts

#### EWrapper.managedAccounts (

accountsList:String. A comma-separated string with the managed account ids.
Returns a string of all available accounts for the logged in user. Occurs automatically on initial API client connection.

#### EWrapper.managedAccounts (

accountsList:String. A comma-separated string with the managed account ids.
Returns a string of all available accounts for the logged in user. Occurs automatically on initial API client connection.

#### EWrapper.managedAccounts (

```python
def managedAccounts(self, accountsList: str):
    print("Account list:", accountsList)
```

### Positions

A limitation of the functionIBApi.EClient.reqAccountUpdatesis that it can only be used with a single account at a time. To create a subscription for position updates from multiple accounts, the functionIBApi.EClient.reqPositionsis available.
Note:The reqPositions function is not available in Introducing Broker or Financial Advisor master accounts that have very large numbers of subaccounts (> 50) to optimize the performance of TWS/IB Gateway. Instead the function reqPositionsMulti can be used to subscribe to updates from individual subaccounts. Also not available with IBroker accounts configured for on-demand account lookup.
After initially invoking reqPositions, information about all positions in all associated accounts will be returned, followed by theIBApi::EWrapper::positionEndcallback. Thereafter, when a position has changed an update will be returned to theIBApi::EWrapper::positionfunction. To cancel a reqPositions subscription, invokeIBApi::EClient::cancelPositions.

A limitation of the functionIBApi.EClient.reqAccountUpdatesis that it can only be used with a single account at a time. To create a subscription for position updates from multiple accounts, the functionIBApi.EClient.reqPositionsis available.
Note:The reqPositions function is not available in Introducing Broker or Financial Advisor master accounts that have very large numbers of subaccounts (> 50) to optimize the performance of TWS/IB Gateway. Instead the function reqPositionsMulti can be used to subscribe to updates from individual subaccounts. Also not available with IBroker accounts configured for on-demand account lookup.
After initially invoking reqPositions, information about all positions in all associated accounts will be returned, followed by theIBApi::EWrapper::positionEndcallback. Thereafter, when a position has changed an update will be returned to theIBApi::EWrapper::positionfunction. To cancel a reqPositions subscription, invokeIBApi::EClient::cancelPositions.

### Request Positions

#### EClient.reqPositions()

Subscribes to position updates for all accessible accounts. All positions sent initially, and then only updates as positions change.
Code example:

#### EClient.reqPositions()

Subscribes to position updates for all accessible accounts. All positions sent initially, and then only updates as positions change.

Code example:

Code example:

Code example:

#### EClient.reqPositions()

Code example:

Code example:

Code example:

```python
self.reqPositions()
```

```python
from ibapi.client import *
from ibapi.wrapper import *
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def position(self, account: str, contract: Contract, position: Decimal, avgCost: float):
        print("Position.", "Account:", account, "Contract:", contract, "Position:", position, "Avg cost:", avgCost)
        
    def positionEnd(self):
       print("PositionEnd")
       
def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7496, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

app.reqPositions()
time.sleep(1)
```

### Receive Positions

#### EWrapper.position(

account:String. The account holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held. avgCost the average cost of the position.
avgCost:double. The total average cost of all trades for the currently held position.)
Provides the portfolio’s open positions. After the initial callback (only) of all positions, the IBApi.EWrapper.positionEnd function will be triggered.
For futures, the exchange field will not be populated in the position callback as some futures trade on multiple exchanges

#### EWrapper.position(

account:String. The account holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held. avgCost the average cost of the position.
avgCost:double. The total average cost of all trades for the currently held position.)
Provides the portfolio’s open positions. After the initial callback (only) of all positions, the IBApi.EWrapper.positionEnd function will be triggered.
For futures, the exchange field will not be populated in the position callback as some futures trade on multiple exchanges

#### Ewrapper.positionEnd()

Indicates all the positions have been transmitted. Only returned after the initial callback of EWrapper.position.

#### Ewrapper.positionEnd()

Indicates all the positions have been transmitted. Only returned after the initial callback of EWrapper.position.

#### EWrapper.position(

#### Ewrapper.positionEnd()

Indicates all the positions have been transmitted. Only returned after the initial callback of EWrapper.position.

#### Ewrapper.positionEnd()

Indicates all the positions have been transmitted. Only returned after the initial callback of EWrapper.position.

#### Ewrapper.positionEnd()

#### EWrapper.position(

account:String. The account holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held. avgCost the average cost of the position.
avgCost:double. The total average cost of all trades for the currently held position.)
Provides the portfolio’s open positions. After the initial callback (only) of all positions, the IBApi.EWrapper.positionEnd function will be triggered.
For futures, the exchange field will not be populated in the position callback as some futures trade on multiple exchanges

#### EWrapper.position(

account:String. The account holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held. avgCost the average cost of the position.
avgCost:double. The total average cost of all trades for the currently held position.)
Provides the portfolio’s open positions. After the initial callback (only) of all positions, the IBApi.EWrapper.positionEnd function will be triggered.
For futures, the exchange field will not be populated in the position callback as some futures trade on multiple exchanges

```python
def position(self, account: str, contract: Contract, position: Decimal, avgCost: float):
  print("Position.", "Account:", account, "Contract:", contract, "Position:", position, "Avg cost:", avgCost)
```

```python
def positionEnd(self):
  print("PositionEnd")
```

### Cancel Positions Request

#### EClient.cancelPositions()

Cancels a previous position subscription request made with EClient.reqPositions().

#### EClient.cancelPositions()

Cancels a previous position subscription request made with EClient.reqPositions().

#### EClient.cancelPositions()

```python
self.cancelPositions()
```

### Positions By Model

The function IBApi.EClient.reqPositionsMulti can be used with any account structure to subscribe to positions updates for multiple accounts and/or models. The account and model parameters are optional if there are not multiple accounts or models available. It is more efficient to use this function for a specific subset of accounts than using IBApi.EClient.reqPositions. A profile name can be accepted in place of group in the account parameter.

The function IBApi.EClient.reqPositionsMulti can be used with any account structure to subscribe to positions updates for multiple accounts and/or models. The account and model parameters are optional if there are not multiple accounts or models available. It is more efficient to use this function for a specific subset of accounts than using IBApi.EClient.reqPositions. A profile name can be accepted in place of group in the account parameter.

### Request Positions By Model

#### EClient.reqPositionsMulti(

requestId:int. Request’s identifier.
account:String. If an account Id is provided, only the account’s positions belonging to the specified model will be delivered.
modelCode:String. The code of the model’s positions we are interested in.)
Requests position subscription for account and/or model Initially all positions are returned, and then updates are returned for any position changes in real time.
Code example:

#### EClient.reqPositionsMulti(

requestId:int. Request’s identifier.
account:String. If an account Id is provided, only the account’s positions belonging to the specified model will be delivered.
modelCode:String. The code of the model’s positions we are interested in.)
Requests position subscription for account and/or model Initially all positions are returned, and then updates are returned for any position changes in real time.

Code example:

Code example:

Code example:

#### EClient.reqPositionsMulti(

Code example:

Code example:

Code example:

```python
self.reqPositionsMulti(requestid, "U1234567", "")
```

```python
from ibapi.client import *
from ibapi.wrapper import *
import threading
import time

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
            
    def positionMulti(self, reqId: int, account: str, modelCode: str, contract: Contract, pos: Decimal, avgCost: float):
       print("PositionMulti. RequestId:", reqId, "Account:", account, "ModelCode:", modelCode, "Contract:", contract, ",Position:", pos, "AvgCost:", avgCost)         
        
    def positionMultiEnd(self, reqId: int):
        print("")
        print("PositionMultiEnd. RequestId:", reqId)       

def websocket_con():
    app.run()
    
app = TradingApp()      
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1) 

app.reqPositionsMulti(2, "DU1234567", "")  #To specify a U-account number
time.sleep(1)

app.reqPositionsMulti(3, "Group1", "")     #To specify a Financial Advisor Group / Profile 
time.sleep(1)
```

### Receive Positions By Model

#### EWrapper.positionMulti(

requestId:int. The id of request
account:String. The account holding the position.
modelCode:String. The model code holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held.
avgCost:double. The average cost of the position.)
Provides the portfolio’s open positions.

#### EWrapper.positionMulti(

requestId:int. The id of request
account:String. The account holding the position.
modelCode:String. The model code holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held.
avgCost:double. The average cost of the position.)
Provides the portfolio’s open positions.

#### EWrapper.positionMultiEnd(

requestId:int. The id of request)
Indicates all the positions have been transmitted.

#### EWrapper.positionMultiEnd(

requestId:int. The id of request)
Indicates all the positions have been transmitted.

#### EWrapper.positionMulti(

#### EWrapper.positionMultiEnd(

requestId:int. The id of request)
Indicates all the positions have been transmitted.

#### EWrapper.positionMultiEnd(

requestId:int. The id of request)
Indicates all the positions have been transmitted.

#### EWrapper.positionMultiEnd(

#### EWrapper.positionMulti(

requestId:int. The id of request
account:String. The account holding the position.
modelCode:String. The model code holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held.
avgCost:double. The average cost of the position.)
Provides the portfolio’s open positions.

#### EWrapper.positionMulti(

requestId:int. The id of request
account:String. The account holding the position.
modelCode:String. The model code holding the position.
contract:Contract. The position’s Contract
pos:decimal. The number of positions held.
avgCost:double. The average cost of the position.)
Provides the portfolio’s open positions.

```python
def positionMulti(self, reqId: int, account: str, modelCode: str, contract: Contract, pos: Decimal, avgCost: float):
  print("PositionMulti. RequestId:", reqId, "Account:", account, "ModelCode:", modelCode, "Contract:", contract, ",Position:", pos, "AvgCost:", avgCost)
```

```python
def positionMultiEnd(self, reqId: int):
	print("PositionMultiEnd. RequestId:", reqId)
```

### Cancel Positions By Model

#### EClient.cancelPositionsMulti (

requestId:int. The identifier of the request to be canceled.
Cancels positions request for account and/or model.

#### EClient.cancelPositionsMulti (

requestId:int. The identifier of the request to be canceled.
Cancels positions request for account and/or model.

#### EClient.cancelPositionsMulti (

```python
self.cancelPositionsMulti(requestid)
```

### Profit & Loss (PnL)

Requests can be made to receive real time updates about the daily P&L and unrealized P&L for an account, or for individual positions. Financial Advisors can also request P&L figures for ‘All’ subaccounts, or for a portfolio model. This is further extended to include realized P&L information at the account or individual position level.
The P&L API functions demonstrated below return the data which is displayed in the TWS Portfolio Window in current versions of TWS. As such, the P&L values are calculated based on the reset schedule specified in TWS Global Configuration (by default an instrument-specific reset schedule) and this setting affects values sent to the associated API functions as well. Also in TWS, P&L data from virtual forex positions will be included in the account P&L if and only if the Virtual Fx section of the Account Window is expanded.
SeeAccount Updatesfor alternative PnL data.

Requests can be made to receive real time updates about the daily P&L and unrealized P&L for an account, or for individual positions. Financial Advisors can also request P&L figures for ‘All’ subaccounts, or for a portfolio model. This is further extended to include realized P&L information at the account or individual position level.
The P&L API functions demonstrated below return the data which is displayed in the TWS Portfolio Window in current versions of TWS. As such, the P&L values are calculated based on the reset schedule specified in TWS Global Configuration (by default an instrument-specific reset schedule) and this setting affects values sent to the associated API functions as well. Also in TWS, P&L data from virtual forex positions will be included in the account P&L if and only if the Virtual Fx section of the Account Window is expanded.
SeeAccount Updatesfor alternative PnL data.

### Request P&L for individual positions

Subscribe using the IBApi::EClient::reqPnLSingle function Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’. Currently updates are returned to IBApi.EWrapper.pnlSingle approximately once per second*.
If a P&L subscription request is made for an invalid conId or contract not in the account, there will not be a response.As elsewhere in the API, a max double value will indicate an ‘unset’ value. This corresponds to an empty cell in TWS.Introducing broker accounts without a large number of subaccounts (<50) can receive aggregate data by specifying the account as “All”.*Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’
*subject to change in the future.

Subscribe using the IBApi::EClient::reqPnLSingle function Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’. Currently updates are returned to IBApi.EWrapper.pnlSingle approximately once per second*.
If a P&L subscription request is made for an invalid conId or contract not in the account, there will not be a response.As elsewhere in the API, a max double value will indicate an ‘unset’ value. This corresponds to an empty cell in TWS.Introducing broker accounts without a large number of subaccounts (<50) can receive aggregate data by specifying the account as “All”.*Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’
*subject to change in the future.

#### EClient.reqPnLSingle (

reqId:int. Request identifier for to track the data.
account:String. Account in which position exists
modelCode:String. Model in which position exists
conId:int. Contract ID (conId) of contract to receive daily PnL updates for. Note: does not return message if invalid conId is entered
Requests real time updates for daily PnL of individual positions.
Code example:

#### EClient.reqPnLSingle (

reqId:int. Request identifier for to track the data.
account:String. Account in which position exists
modelCode:String. Model in which position exists
conId:int. Contract ID (conId) of contract to receive daily PnL updates for. Note: does not return message if invalid conId is entered
Requests real time updates for daily PnL of individual positions.

Code example:

Code example:

Code example:

#### EClient.reqPnLSingle (

Subscribe using the IBApi::EClient::reqPnLSingle function Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’. Currently updates are returned to IBApi.EWrapper.pnlSingle approximately once per second*.
If a P&L subscription request is made for an invalid conId or contract not in the account, there will not be a response.As elsewhere in the API, a max double value will indicate an ‘unset’ value. This corresponds to an empty cell in TWS.Introducing broker accounts without a large number of subaccounts (<50) can receive aggregate data by specifying the account as “All”.*Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’
*subject to change in the future.

Subscribe using the IBApi::EClient::reqPnLSingle function Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’. Currently updates are returned to IBApi.EWrapper.pnlSingle approximately once per second*.
If a P&L subscription request is made for an invalid conId or contract not in the account, there will not be a response.As elsewhere in the API, a max double value will indicate an ‘unset’ value. This corresponds to an empty cell in TWS.Introducing broker accounts without a large number of subaccounts (<50) can receive aggregate data by specifying the account as “All”.*Cannot be used with IBroker accounts configured for on-demand lookup with account = ‘All’
*subject to change in the future.

Code example:

Code example:

Code example:

```python
self.reqPnLSingle(requestId, "U1234567", "", 265598)
```

```python
from ibapi.client import *
from ibapi.wrapper import *
import time

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def pnlSingle(self, reqId: int, pos: Decimal, dailyPnL: float, unrealizedPnL: float, realizedPnL: float, value: float):
        print("Daily PnL Single. ReqId:", reqId, "Position:", pos, "DailyPnL:", dailyPnL, "UnrealizedPnL:", unrealizedPnL, "RealizedPnL:", realizedPnL, "Value:", value)
    
app = TradeApp()      
app.connect("127.0.0.1", 7496, clientId=1)

time.sleep(1)
app.reqPnLSingle(101, "U123456", "", 8314) #IBM conId: 8314

app.run()
```

### Receive P&L for individual positions

#### EWrapper.pnlSingle (

reqId:int. Request identifier used for tracking.
pos:decimal. Current size of the position
dailyPnL:double. DailyPnL for the position
unrealizedPnL:double. Total unrealized PnL for the position (since inception) updating in real time
realizedPnL:double. Total realized PnL for the position (since inception) updating in real time
value:double. Current market value of the position.)
Receives real time updates for single position daily PnL values

#### EWrapper.pnlSingle (

reqId:int. Request identifier used for tracking.
pos:decimal. Current size of the position
dailyPnL:double. DailyPnL for the position
unrealizedPnL:double. Total unrealized PnL for the position (since inception) updating in real time
realizedPnL:double. Total realized PnL for the position (since inception) updating in real time
value:double. Current market value of the position.)
Receives real time updates for single position daily PnL values

#### EWrapper.pnlSingle (

```python
def pnlSingle(self, reqId: int, pos: Decimal, dailyPnL: float, unrealizedPnL: float, realizedPnL: float, value: float):
  print("Daily PnL Single. ReqId:", reqId, "Position:", pos, "DailyPnL:", dailyPnL, "UnrealizedPnL:", unrealizedPnL, "RealizedPnL:", realizedPnL, "Value:", value)
```

### Cancel P&L request for individual positions

#### EClient.cancelPnLSingle (

reqId:int. Request identifier to cancel the P&L subscription for.)
Cancels real time subscription for a positions daily PnL information.

#### EClient.cancelPnLSingle (

reqId:int. Request identifier to cancel the P&L subscription for.)
Cancels real time subscription for a positions daily PnL information.

#### EClient.cancelPnLSingle (

```python
self.cancelPnLSingle(requestId);
```

### Request P&L for accounts

Subscribe using the IBApi::EClient::reqPnL function. Updates are sent to IBApi.EWrapper.pnl.
Introducing broker accounts with less than 50 subaccounts can receive aggregate PnL for all subaccounts by specifying ‘All’ as the account code.With requests for advisor accounts with many subaccounts and/or positions can take several seconds for aggregated P&L to be computed and returned.For account P&L data the TWS setting “Prepare portfolio PnL data when downloading positions” must be checked.

Subscribe using the IBApi::EClient::reqPnL function. Updates are sent to IBApi.EWrapper.pnl.
Introducing broker accounts with less than 50 subaccounts can receive aggregate PnL for all subaccounts by specifying ‘All’ as the account code.With requests for advisor accounts with many subaccounts and/or positions can take several seconds for aggregated P&L to be computed and returned.For account P&L data the TWS setting “Prepare portfolio PnL data when downloading positions” must be checked.

#### EClient.reqPnL (

reqId:int. Request ID to track the data.
account:String. Account for which to receive PnL updates
modelCode:String. Specify to request PnL updates for a specific model.)
Creates subscription for real time daily PnL and unrealized PnL updates.
Code example:

#### EClient.reqPnL (

reqId:int. Request ID to track the data.
account:String. Account for which to receive PnL updates
modelCode:String. Specify to request PnL updates for a specific model.)
Creates subscription for real time daily PnL and unrealized PnL updates.

Code example:

Code example:

Code example:

#### EClient.reqPnL (

Subscribe using the IBApi::EClient::reqPnL function. Updates are sent to IBApi.EWrapper.pnl.
Introducing broker accounts with less than 50 subaccounts can receive aggregate PnL for all subaccounts by specifying ‘All’ as the account code.With requests for advisor accounts with many subaccounts and/or positions can take several seconds for aggregated P&L to be computed and returned.For account P&L data the TWS setting “Prepare portfolio PnL data when downloading positions” must be checked.

Subscribe using the IBApi::EClient::reqPnL function. Updates are sent to IBApi.EWrapper.pnl.
Introducing broker accounts with less than 50 subaccounts can receive aggregate PnL for all subaccounts by specifying ‘All’ as the account code.With requests for advisor accounts with many subaccounts and/or positions can take several seconds for aggregated P&L to be computed and returned.For account P&L data the TWS setting “Prepare portfolio PnL data when downloading positions” must be checked.

Code example:

Code example:

Code example:

```python
self.reqPnL(reqId, "U1234567", "")
```

```python
from ibapi.client import *
from ibapi.wrapper import *
import time

class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
        print("Daily PnL. ReqId:", reqId, "DailyPnL:", dailyPnL, "UnrealizedPnL:", unrealizedPnL, "RealizedPnL:", realizedPnL)
    
app = TradeApp()      
app.connect("127.0.0.1", 7496, clientId=1)

time.sleep(1)
app.reqPnL(102, "U123456", "")

app.run()
```

### Receive P&L for accounts

#### EWrapper.pnl (

reqId:int. Request identifier for tracking data.
dailyPnL:double. DailyPnL updates for the account in real time
unrealizedPnL:double. Total Unrealized PnL updates for the account in real time
realizedPnL:double. Total Realized PnL updates for the account in real time

#### EWrapper.pnl (

reqId:int. Request identifier for tracking data.
dailyPnL:double. DailyPnL updates for the account in real time
unrealizedPnL:double. Total Unrealized PnL updates for the account in real time
realizedPnL:double. Total Realized PnL updates for the account in real time

#### EWrapper.pnl (

```python
def pnl(self, reqId: int, dailyPnL: float, unrealizedPnL: float, realizedPnL: float):
  print("Daily PnL. ReqId:", reqId, "DailyPnL:", dailyPnL, "UnrealizedPnL:", unrealizedPnL, "RealizedPnL:", realizedPnL)
```

### Cancel P&L subscription requests for accounts

#### EClient.cancelPnL (

reqId:int. Request identifier for tracking data.)
Cancels subscription for real time updated daily PnL params reqId

#### EClient.cancelPnL (

reqId:int. Request identifier for tracking data.)
Cancels subscription for real time updated daily PnL params reqId

#### EClient.cancelPnL (

```python
self.cancelPnL(reqId)
```

### White Branding User Info

This function will returnWhite Branding IDassociated with the user.
Please note, that nothing will be returned if requesting username is not associated with any White Branding entity.

This function will returnWhite Branding IDassociated with the user.
Please note, that nothing will be returned if requesting username is not associated with any White Branding entity.

### Requesting White Branding Info

#### EClient.reqUserInfo(

reqId:int. Request ID

#### EClient.reqUserInfo(

reqId:int. Request ID

#### EClient.reqUserInfo(

```python
self.reqUserInfo(reqId)
```

### Receiving White Branding Info

#### EWrapper.userInfo (

reqId:int. Identifier for the given request.
whiteBrandingId:String. Identifier for the white branded entity.)

#### EWrapper.userInfo (

reqId:int. Identifier for the given request.
whiteBrandingId:String. Identifier for the white branded entity.)

#### EWrapper.userInfo (

```python
def userInfo(self, reqId: int, whiteBrandingId: str):
	print("UserInfo.", "ReqId:", reqId, "WhiteBrandingId:", whiteBrandingId)
```
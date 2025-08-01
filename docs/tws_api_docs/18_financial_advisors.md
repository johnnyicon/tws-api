---
title: "Financial Advisors"
description: "TWS API Documentation - Financial Advisors"
source: "Interactive Brokers TWS API Documentation"
nav_id: "financial-advisors"
order: 18
prev_section: "Error Handling"
next_section: "Market Data: Delayed"
prev_file: "17_error_handling.md"
next_file: "19_market_data_delayed.md"
scraped_at: "2025-08-01T09:13:29.313948"
word_count: 4382
paragraph_count: 144
subsection_count: 57
code_block_count: 5
format: "markdown"
---

# Financial Advisors

## Financial Advisors

Financial Advisors are able to manage their allocation groups from the TWS API.
Note:Modifications made through the API will effect orders placed through TWS, the TWS API, Client Portal, and the Client Portal API.

Financial Advisors are able to manage their allocation groups from the TWS API.
Note:Modifications made through the API will effect orders placed through TWS, the TWS API, Client Portal, and the Client Portal API.

### Request FA Groups and Profiles

#### EClient.requestFA (

faDataType:int. The configuration to change. Set to 1 or 3 as defined in the table below.)
Requests the FA configuration as set in TWS for the given FA Group or Profile.

#### EClient.requestFA (

faDataType:int. The configuration to change. Set to 1 or 3 as defined in the table below.)
Requests the FA configuration as set in TWS for the given FA Group or Profile.

#### requestFA FA Data Types


| Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 3 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

#### requestFA FA Data Types


| Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 3 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

#### EClient.requestFA (

#### requestFA FA Data Types


| Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 3 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

#### requestFA FA Data Types


| Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 3 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

#### requestFA FA Data Types

#### EClient.requestFA (

faDataType:int. The configuration to change. Set to 1 or 3 as defined in the table below.)
Requests the FA configuration as set in TWS for the given FA Group or Profile.

#### EClient.requestFA (

faDataType:int. The configuration to change. Set to 1 or 3 as defined in the table below.)
Requests the FA configuration as set in TWS for the given FA Group or Profile.

```python
self.requestFA(1)
```

### Receiving FA Groups and Profiles

#### EWrapper.receiveFA (

faDataType:int. Receive the faDataType value specified in the requestFA. SeeFA Data Types
faXmlData:String. The xml-formatted configuration.)
Receives the Financial Advisor’s configuration available in the TWS.

#### EWrapper.receiveFA (

faDataType:int. Receive the faDataType value specified in the requestFA. SeeFA Data Types
faXmlData:String. The xml-formatted configuration.)
Receives the Financial Advisor’s configuration available in the TWS.

#### EWrapper.receiveFA (

```python
def receiveFA(self, faData: FaDataType, cxml: str):
	print("Receiving FA: ", faData)
	open('log/fa.xml', 'w').write(cxml)
```

### Replace FA Allocations

#### EClient.replaceFA (

reqId:int. Request identifier used to track data.
faDataType:int. The configuration structure to change. Set to 1 or 3 as defined above.
xml:String. XML configuration for allocation profiles or group. SeeAllocation Method XML Formatfor more details.)

#### EClient.replaceFA (

reqId:int. Request identifier used to track data.
faDataType:int. The configuration structure to change. Set to 1 or 3 as defined above.
xml:String. XML configuration for allocation profiles or group. SeeAllocation Method XML Formatfor more details.)

#### replaceFA FA Data Types


| replaceFA Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 2 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

In order to confirm that your FA changes were saved, you may wait for theEWrapper.replaceFAEndcallback, which provides the corresponding reqId. In addition, after saving changes, it is advised to verify the new FA setup viaEClient.requestFA. If it is called before changes are fully saved, you may receive an error, such aserror 10230. SeeMessage Codes.
EClient.replaceFAonly accepts faDataType 1 now. Otherwise, it may triggererror 585.

#### replaceFA FA Data Types


| replaceFA Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 2 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

In order to confirm that your FA changes were saved, you may wait for theEWrapper.replaceFAEndcallback, which provides the corresponding reqId. In addition, after saving changes, it is advised to verify the new FA setup viaEClient.requestFA. If it is called before changes are fully saved, you may receive an error, such aserror 10230. SeeMessage Codes.
EClient.replaceFAonly accepts faDataType 1 now. Otherwise, it may triggererror 585.

#### EWrapper.replaceFAEnd (

reqId:int. Request identifier used to track data.
text:String. the message text.
Marks the ending of the replaceFA reception.

#### EWrapper.replaceFAEnd (

reqId:int. Request identifier used to track data.
text:String. the message text.
Marks the ending of the replaceFA reception.

#### EClient.replaceFA (

#### replaceFA FA Data Types


| replaceFA Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 2 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

In order to confirm that your FA changes were saved, you may wait for theEWrapper.replaceFAEndcallback, which provides the corresponding reqId. In addition, after saving changes, it is advised to verify the new FA setup viaEClient.requestFA. If it is called before changes are fully saved, you may receive an error, such aserror 10230. SeeMessage Codes.
EClient.replaceFAonly accepts faDataType 1 now. Otherwise, it may triggererror 585.

#### replaceFA FA Data Types


| replaceFA Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 2 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

In order to confirm that your FA changes were saved, you may wait for theEWrapper.replaceFAEndcallback, which provides the corresponding reqId. In addition, after saving changes, it is advised to verify the new FA setup viaEClient.requestFA. If it is called before changes are fully saved, you may receive an error, such aserror 10230. SeeMessage Codes.
EClient.replaceFAonly accepts faDataType 1 now. Otherwise, it may triggererror 585.

#### EWrapper.replaceFAEnd (

reqId:int. Request identifier used to track data.
text:String. the message text.
Marks the ending of the replaceFA reception.

#### EWrapper.replaceFAEnd (

reqId:int. Request identifier used to track data.
text:String. the message text.
Marks the ending of the replaceFA reception.

#### replaceFA FA Data Types

#### EClient.replaceFA (

reqId:int. Request identifier used to track data.
faDataType:int. The configuration structure to change. Set to 1 or 3 as defined above.
xml:String. XML configuration for allocation profiles or group. SeeAllocation Method XML Formatfor more details.)

#### EClient.replaceFA (

reqId:int. Request identifier used to track data.
faDataType:int. The configuration structure to change. Set to 1 or 3 as defined above.
xml:String. XML configuration for allocation profiles or group. SeeAllocation Method XML Formatfor more details.)

#### EWrapper.replaceFAEnd (

reqId:int. Request identifier used to track data.
text:String. the message text.
Marks the ending of the replaceFA reception.

#### EWrapper.replaceFAEnd (

reqId:int. Request identifier used to track data.
text:String. the message text.
Marks the ending of the replaceFA reception.

#### EWrapper.replaceFAEnd (

#### EClient.replaceFA (

reqId:int. Request identifier used to track data.
faDataType:int. The configuration structure to change. Set to 1 or 3 as defined above.
xml:String. XML configuration for allocation profiles or group. SeeAllocation Method XML Formatfor more details.)

#### EClient.replaceFA (

reqId:int. Request identifier used to track data.
faDataType:int. The configuration structure to change. Set to 1 or 3 as defined above.
xml:String. XML configuration for allocation profiles or group. SeeAllocation Method XML Formatfor more details.)

#### replaceFA FA Data Types


| replaceFA Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 2 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

In order to confirm that your FA changes were saved, you may wait for theEWrapper.replaceFAEndcallback, which provides the corresponding reqId. In addition, after saving changes, it is advised to verify the new FA setup viaEClient.requestFA. If it is called before changes are fully saved, you may receive an error, such aserror 10230. SeeMessage Codes.
EClient.replaceFAonly accepts faDataType 1 now. Otherwise, it may triggererror 585.

#### replaceFA FA Data Types


| replaceFA Type Code | Type Name | Description |
| --- | --- | --- |
| 1 | Groups | offer traders a way to create a group of accounts and apply a single allocation method to all accounts in the group. |
| 2 | Account Aliases | let you easily identify the accounts by meaningful names rather than account numbers. |

In order to confirm that your FA changes were saved, you may wait for theEWrapper.replaceFAEndcallback, which provides the corresponding reqId. In addition, after saving changes, it is advised to verify the new FA setup viaEClient.requestFA. If it is called before changes are fully saved, you may receive an error, such aserror 10230. SeeMessage Codes.
EClient.replaceFAonly accepts faDataType 1 now. Otherwise, it may triggererror 585.

```python
self.replaceFa(reqId, 1, xml)
```

```python
def replaceFAEnd(self, reqId: int, text: str):
    super().replaceFAEnd(reqId, text)
    print("ReplaceFAEnd.", "ReqId:", reqId, "Text:", text)
```

### Allocation Methods and Groups

A number of methods for account allocations are available with Financial Advisor and IBroker account structures to specify how trades should be distributed across multiple accounts.
Allocation Groups can be created or modified in the Trader Workstation directly as described inTWS: Allocations and Transfers.
Alternatively, allocation groups can be created or modified through theEClient.replaceFA()method in the API.
Interactive Brokers supports two forms of allocation methods. Allocation methods that have calculations completed by Interactive Brokers, and a set of allocation methods calculated by the user and then specified.

A number of methods for account allocations are available with Financial Advisor and IBroker account structures to specify how trades should be distributed across multiple accounts.
Allocation Groups can be created or modified in the Trader Workstation directly as described inTWS: Allocations and Transfers.
Alternatively, allocation groups can be created or modified through theEClient.replaceFA()method in the API.
Interactive Brokers supports two forms of allocation methods. Allocation methods that have calculations completed by Interactive Brokers, and a set of allocation methods calculated by the user and then specified.

#### IB-computed allocation methods

Available EquityEqual QuantityNet Liquidation Value

#### User-specified allocation methods

Cash QuantityPercentagesRatiosShares

#### IB-computed allocation methods

Available EquityEqual QuantityNet Liquidation Value

#### User-specified allocation methods

Cash QuantityPercentagesRatiosShares

#### IB-computed allocation methods

A number of methods for account allocations are available with Financial Advisor and IBroker account structures to specify how trades should be distributed across multiple accounts.
Allocation Groups can be created or modified in the Trader Workstation directly as described inTWS: Allocations and Transfers.
Alternatively, allocation groups can be created or modified through theEClient.replaceFA()method in the API.
Interactive Brokers supports two forms of allocation methods. Allocation methods that have calculations completed by Interactive Brokers, and a set of allocation methods calculated by the user and then specified.

A number of methods for account allocations are available with Financial Advisor and IBroker account structures to specify how trades should be distributed across multiple accounts.
Allocation Groups can be created or modified in the Trader Workstation directly as described inTWS: Allocations and Transfers.
Alternatively, allocation groups can be created or modified through theEClient.replaceFA()method in the API.
Interactive Brokers supports two forms of allocation methods. Allocation methods that have calculations completed by Interactive Brokers, and a set of allocation methods calculated by the user and then specified.

#### User-specified allocation methods

Cash QuantityPercentagesRatiosShares

#### User-specified allocation methods

A number of methods for account allocations are available with Financial Advisor and IBroker account structures to specify how trades should be distributed across multiple accounts.
Allocation Groups can be created or modified in the Trader Workstation directly as described inTWS: Allocations and Transfers.
Alternatively, allocation groups can be created or modified through theEClient.replaceFA()method in the API.
Interactive Brokers supports two forms of allocation methods. Allocation methods that have calculations completed by Interactive Brokers, and a set of allocation methods calculated by the user and then specified.

A number of methods for account allocations are available with Financial Advisor and IBroker account structures to specify how trades should be distributed across multiple accounts.
Allocation Groups can be created or modified in the Trader Workstation directly as described inTWS: Allocations and Transfers.
Alternatively, allocation groups can be created or modified through theEClient.replaceFA()method in the API.
Interactive Brokers supports two forms of allocation methods. Allocation methods that have calculations completed by Interactive Brokers, and a set of allocation methods calculated by the user and then specified.

#### IB-computed allocation methods

Available EquityEqual QuantityNet Liquidation Value

### Allocation Method XML Format

Allocation methods for financial advisor’s allocation groups are created using an XML format. The content below signifies the supported allocation groups and how to format them in their respective XML.

Allocation methods for financial advisor’s allocation groups are created using an XML format. The content below signifies the supported allocation groups and how to format them in their respective XML.

### Available Equity

Requires you to specify an order size. This method distributes shares based on the amount of available equity in each account. The system calculates ratios based on the Available Equity in each account and allocates shares based on these ratios.
Example:You transmit an order for 700 shares of stock XYZ. The account group includes three accounts, A, B and C with available equity in the amounts of $25,000, $50,000 and $100,000 respectively. The system calculates a ratio of 1:2:4 and allocates 100 shares to Client A, 200 shares to Client B, and 400 shares to Client C.

Requires you to specify an order size. This method distributes shares based on the amount of available equity in each account. The system calculates ratios based on the Available Equity in each account and allocates shares based on these ratios.
Example:You transmit an order for 700 shares of stock XYZ. The account group includes three accounts, A, B and C with available equity in the amounts of $25,000, $50,000 and $100,000 respectively. The system calculates a ratio of 1:2:4 and allocates 100 shares to Client A, 200 shares to Client B, and 400 shares to Client C.

### Contracts Or Shares

This method allocates the absolute number of shares you enter to each account listed. If you use this method, the order size is calculated by adding together the number of shares allocated to each account in the profile.
Example:
Assume an order for 300 shares of stock ABC is transmitted.
In the example code shown in the right side, you can see that:
Account A is set to receive 100.0 shares while Account B is set to receive 200.0 shares. Account A should receive 100 shares and Account B should receive 200 shares.

This method allocates the absolute number of shares you enter to each account listed. If you use this method, the order size is calculated by adding together the number of shares allocated to each account in the profile.
Example:
Assume an order for 300 shares of stock ABC is transmitted.
In the example code shown in the right side, you can see that:
Account A is set to receive 100.0 shares while Account B is set to receive 200.0 shares. Account A should receive 100 shares and Account B should receive 200 shares.

### Equal Quantity

Requires you to specify an order size. This method distributes shares equally between all accounts in the group.
Example:You transmit an order for 400 shares of stock ABC. If your Account Group includes four accounts, each account receives 100 shares. If your Account Group includes six accounts, each account receives 66 shares, and then 1 share is allocated to each account until all are distributed.

Requires you to specify an order size. This method distributes shares equally between all accounts in the group.
Example:You transmit an order for 400 shares of stock ABC. If your Account Group includes four accounts, each account receives 100 shares. If your Account Group includes six accounts, each account receives 66 shares, and then 1 share is allocated to each account until all are distributed.

### MonetaryAmount

The Monetary Amount method calculates the number of units to be allocated based on the monetary value assigned to each account.

The Monetary Amount method calculates the number of units to be allocated based on the monetary value assigned to each account.

### Net Liquidation Value

Requires you to specify an order size. This method distributes shares based on the net liquidation value of each account. The system calculates ratios based on the Net Liquidation value in each account and allocates shares based on these ratios.
Example:You transmit an order for 700 shares of stock XYZ. The account group includes three accounts, A, B and C with Net Liquidation values of $25,000, $50,000 and $100,000 respectively. The system calculates a ratio of 1:2:4 and allocates 100 shares to Client A, 200 shares to Client B, and 400 shares to Client C.

Requires you to specify an order size. This method distributes shares based on the net liquidation value of each account. The system calculates ratios based on the Net Liquidation value in each account and allocates shares based on these ratios.
Example:You transmit an order for 700 shares of stock XYZ. The account group includes three accounts, A, B and C with Net Liquidation values of $25,000, $50,000 and $100,000 respectively. The system calculates a ratio of 1:2:4 and allocates 100 shares to Client A, 200 shares to Client B, and 400 shares to Client C.

### Percentages

This method will split the total number of shares in the order between listed accounts based on the percentages you indicate.
Example:
Assume an order for 300 shares of stock ABC is transmitted.
In the example code shown in the right side, you can see that:
Account A is set to have 60.0 percentage while Account B is set to have 40.0 percentage. Account A should receive 180 shares and Account B should receive 120 shares.
While making modifications to allocations for profiles, the method uses an enumerated value. The number shown below demonstrates precisely what profile corresponds to which value.

| BUY ORDER | Positive Percent | Negative Percent |
| --- | --- | --- |
| Long Position | Increases position | No effect |
| Short Position | No effect | Decreases position |


| SELL ORDER | Positive Percent | Negative Percent |
| --- | --- | --- |
| Long Position | No effect | Decreases position |
| Short Position | Increases position | No effect |

Note:Do not specify an order size. Since the quantity is calculated by the system, the order size is displayed in the Quantity field after the order is acknowledged. This method increases or decreases an already existing position. Positive percents will increase a position, negative percents will decrease a position. For exmaple, to fully close out a position, you just need to specify percentage to be -100.

This method will split the total number of shares in the order between listed accounts based on the percentages you indicate.
Example:
Assume an order for 300 shares of stock ABC is transmitted.
In the example code shown in the right side, you can see that:
Account A is set to have 60.0 percentage while Account B is set to have 40.0 percentage. Account A should receive 180 shares and Account B should receive 120 shares.
While making modifications to allocations for profiles, the method uses an enumerated value. The number shown below demonstrates precisely what profile corresponds to which value.

| BUY ORDER | Positive Percent | Negative Percent |
| --- | --- | --- |
| Long Position | Increases position | No effect |
| Short Position | No effect | Decreases position |


| SELL ORDER | Positive Percent | Negative Percent |
| --- | --- | --- |
| Long Position | No effect | Decreases position |
| Short Position | Increases position | No effect |

Note:Do not specify an order size. Since the quantity is calculated by the system, the order size is displayed in the Quantity field after the order is acknowledged. This method increases or decreases an already existing position. Positive percents will increase a position, negative percents will decrease a position. For exmaple, to fully close out a position, you just need to specify percentage to be -100.

### Ratios

This method calculates the allocation of shares based on the ratios you enter.
Example:
Assume an order for 300 shares of stock ABC is transmitted.
In the example code shown in the right side, you can see that:
A ratio of 1.0 and 2.0 is set to Account A and Account B. Account A should receive 100 shares and Account B should receive 200 shares.

This method calculates the allocation of shares based on the ratios you enter.
Example:
Assume an order for 300 shares of stock ABC is transmitted.
In the example code shown in the right side, you can see that:
A ratio of 1.0 and 2.0 is set to Account A and Account B. Account A should receive 100 shares and Account B should receive 200 shares.

### Model Portfolios and the API

Advisors can use Model Portfolios to easily invest some or all of a client’s assets into one or multiple custom-created portfolios, rather than tediously managing individual investments in single instruments.
More about Model Portfolios
The TWS API can access model portfolios in accounts where this functionality is available and a specific model has previously been setup in TWS. API functionality allows the client application to request model position update subscriptions, request model account update subscriptions, or place orders to a specific model.
Model Portfolio functionalitynotavailable in the TWS API:
Portfolio Model CreationPortfolio Model RebalancingPortfolio Model Position or Cash Transfer

Advisors can use Model Portfolios to easily invest some or all of a client’s assets into one or multiple custom-created portfolios, rather than tediously managing individual investments in single instruments.
More about Model Portfolios
The TWS API can access model portfolios in accounts where this functionality is available and a specific model has previously been setup in TWS. API functionality allows the client application to request model position update subscriptions, request model account update subscriptions, or place orders to a specific model.
Model Portfolio functionalitynotavailable in the TWS API:
Portfolio Model CreationPortfolio Model RebalancingPortfolio Model Position or Cash Transfer

To request position updates from a specific model, the functionIBApi::EClient::reqPositionsMultican be used:Position Update Subscription by Model
To request model account updates, there is the functionIBApi::EClient::reqAccountUpdatesMulti, see:Account Value Update Subscriptions by Model

To request position updates from a specific model, the functionIBApi::EClient::reqPositionsMultican be used:Position Update Subscription by Model
To request model account updates, there is the functionIBApi::EClient::reqAccountUpdatesMulti, see:Account Value Update Subscriptions by Model

To place an order to a model, the IBApi.Order.ModelCode field must be set accordingly, for example:

To place an order to a model, the IBApi.Order.ModelCode field must be set accordingly, for example:

```python
modelOrder = Order()
modelOrder.account = "DF12345"
modelOrder.modelCode = "Technology" # model for tech stocks first created in TWS
self.placeOrder(self.nextOrderId(), contract, modelOrder)
```

### Unification of Groups and Profiles

With TWS/IBGW build 983+, the API settings will have a new flag/checkbox,“Use Account Groups with Allocation Methods”(enabled by default for new users). If not enabled, groups and profiles would behave the same as before. If it is checked, group and profile functionality will be merged.
With TWS/IBGW Build 10.20+, this setting is now enabled by default, and moving forward into new versions, the two systems can be deemed as interchangeable for modifying allocation groups, placing orders, requesting account or portfolio summaries, or requesting multiple positions.

With TWS/IBGW build 983+, the API settings will have a new flag/checkbox,“Use Account Groups with Allocation Methods”(enabled by default for new users). If not enabled, groups and profiles would behave the same as before. If it is checked, group and profile functionality will be merged.
With TWS/IBGW Build 10.20+, this setting is now enabled by default, and moving forward into new versions, the two systems can be deemed as interchangeable for modifying allocation groups, placing orders, requesting account or portfolio summaries, or requesting multiple positions.

### Order Placement

For advisors to place orders to theirallocation groupsusers would simply declare their allocation group name in the order object. This would be done with the Order’s faGroup field. The example to the right references a standard market order placed to our allocation group, MyTestProfile.

For advisors to place orders to theirallocation groupsusers would simply declare their allocation group name in the order object. This would be done with the Order’s faGroup field. The example to the right references a standard market order placed to our allocation group, MyTestProfile.
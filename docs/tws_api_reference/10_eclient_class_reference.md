---
title: "EClient Class Reference"
description: "TWS API Reference - EClient Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "eclient-ref"
order: 10
prev_section: "DeltaNeutralContract Class Reference"
next_section: "EClientSocket Class Reference"
prev_file: "09_deltaneutralcontract_class_reference.md"
next_file: "11_eclientsocket_class_reference.md"
scraped_at: "2025-08-01T09:13:02.320356"
word_count: 5801
paragraph_count: 23
subsection_count: 4
code_block_count: 0
format: "markdown"
---

# EClient Class Reference

## EClient Class Reference

TWS/Gateway client class This client class contains all the available methods to communicate with IB. Up to thirty-two clients can be connected to a single instance of the TWS/Gateway simultaneously. From herein, the TWS/Gateway will be referred to as the Host.

TWS/Gateway client class This client class contains all the available methods to communicate with IB. Up to thirty-two clients can be connected to a single instance of the TWS/Gateway simultaneously. From herein, the TWS/Gateway will be referred to as the Host.

NameTypeDescriptionAllowRedirectboolServerTimestringoptionalCapabilitiesstringAsyncEConnectbool

| Name | Type | Description |
| --- | --- | --- |
| AllowRedirect | bool |  |
| ServerTime | string |  |
| optionalCapabilities | string |  |
| AsyncEConnect | bool |  |

| Name | Type | Description |
| --- | --- | --- |
| AllowRedirect | bool |  |
| ServerTime | string |  |
| optionalCapabilities | string |  |
| AsyncEConnect | bool |  |

### Public Member Functions

NameTypeDescriptionSetConnectOptions (string connectOptions)voidIgnore. Used for IB’s internal purposes.DisableUseV100Plus ()voidAllows to switch between different current (V100+) and previous connection mechanisms.IsConnected ()boolIndicates whether the API-TWS connection has been closed. Note: This function is not automatically invoked and must be by the API client. More…startApi ()voidInitiates the message exchange between the client application and the TWS/IB Gateway.Close ()voidTerminates the connection and notifies the EWrapper implementing class. More…eDisconnect (bool resetState=true)virtual voidCloses the socket connection and terminates its thread.reqCompletedOrders (bool apiOnly)voidRequests completed orders.None. More…NonecancelTickByTickData (int requestId)voidCancels tick-by-tick data.None. More…NonereqTickByTickData (int requestIdvoidContract contractNone. More…NonecancelHistoricalData (int reqId)voidCancels a historical data request. More…calculateImpliedVolatility (int reqIdvoidContract contractNoneRequest the calculation of the implied volatility based on hypothetical option and its underlying prices.NoneNoneThe calculation will be return in EWrapper’s tickOptionComputation callback.NoneNone. More…NonecalculateOptionPrice (int reqIdvoidContract contractNoneThe calculation will be return in EWrapper’s tickOptionComputation callback.NoneNone. More…NonecancelAccountSummary (int reqId)voidCancels the account’s summary request. After requesting an account’s summarycancelCalculateImpliedVolatility (int reqId)voidCancels an option’s implied volatility calculation request. More…cancelCalculateOptionPrice (int reqId)voidCancels an option’s price calculation request. More…cancelFundamentalData (int reqId)voidCancels Fundamental data request. More…cancelMktData (int tickerId)voidCancels a RT Market Data request. More…cancelMktDepth (int tickerIdvoidbool isSmartDepth)cancelNewsBulletin ()voidCancels IB’s news bulletin subscription. More…cancelOrder (int orderIdvoidstring manualOrderCancelTime)NoneNote: API clients cannot cancel individual orders placed by other clients. Only reqGlobalCancel is available.NoneNone. More…NonecancelPositions ()voidCancels a previous position subscription request made with reqPositions. More…cancelRealTimeBars (int tickerId)voidCancels Real Time Bars’ subscription. More…cancelScannerSubscription (int tickerId)voidCancels Scanner Subscription. More…exerciseOptions (int tickerIdvoidContract contractNoneNote: this function is affected by a TWS setting which specifies if an exercise request must be finalized. More…NoneplaceOrder (int idvoidContract contractreplaceFA (int reqIdvoidint faDataTyperequestFA (int faDataType)voidRequests the FA configuration A Financial Advisor can define three different configurations: More…reqAccountSummary (int reqIdvoidstring groupNoneThis method will subscribe to the account summary as presented in the TWS’ Account Summary tab. The data is returned at EWrapper::accountSummaryNoneNonehttps://www.interactivebrokers.com/en/software/tws/accountwindowtop.htm. More…NonereqAccountUpdates (bool subscribevoidstring acctCode)reqAllOpenOrders ()voidRequests all current open orders in associated accounts at the current moment. The existing orders will be received via the openOrder and orderStatus events. Open orders are returned once; this function does not initiate a subscription. More…reqAutoOpenOrders (bool autoBind)voidRequests status updates about future orders placed from TWS. Can only be used with client ID 0. More…reqContractDetails (int reqIdvoidContract contract)NoneThis method will provide all the contracts matching the contract provided. It can also be used to retrieve complete options and futures chains. This information will be returned at EWrapper:contractDetails. Though it is now (in API version > 9.72.12) advised to use reqSecDefOptParams for that purpose.NoneNone. More…NonereqCurrentTime ()voidRequests TWS’s current time. More…reqExecutions (int reqIdvoidExecutionFilter filter)reqFundamentalData (int reqIdvoidContract contractreqGlobalCancel ()voidCancels all active orders.NoneThis method will cancel ALL open orders including those placed directly from TWS. More…NonereqHistoricalData (int tickerIdvoidContract contractreqIds (int numIds)voidRequests the next valid order ID at the current moment. More…reqManagedAccts ()voidRequests the accounts to which the logged user has access to. More…reqMktData (int tickerIdvoidContract contractreqMarketDataType (int marketDataType)voidSwitches data type returned from reqMktData request to “frozen”NoneThe API can receive frozen market data from Trader Workstation. Frozen market data is the last data recorded in our system.Nonethe API receives real-time market data. Invoking this function with argument 2 requests a switch to frozen data immediately or after the close.During normal trading hoursNonethe market data type will automatically switch back to real time if available. More…When the market reopensNonereqMarketDepth (int tickerIdvoidContract contractcommissionsThis request must be direct-routed to an exchange and not smart-routed. The number of simultaneous market depth requests allowed in an account is calculated based on a formula that looks at an accounts equityand quote booster packs. More…reqNewsBulletins (bool allMessages)voidSubscribes to IB’s News Bulletins. More…reqOpenOrders ()voidRequests all open orders places by this specific API client (identified by the API client id). For client ID 0reqPositions ()voidSubscribes to position updates for all accessible accounts. All positions sent initiallyreqRealTimeBars (int tickerIdvoidContract contractonly 5 seconds bars are provided. This request is subject to the same pacing as any historical data request: no more than 60 API queries in more than 600 seconds.CurrentlyNoneNoneReal time bars subscriptions are also included in the calculation of the number of Level 1 market data subscriptions allowed in an account. More…NonereqScannerParameters ()voidRequests an XML list of scanner parameters valid in TWS.NoneNot all parameters are valid from API scanner. More…NonereqScannerSubscription (int reqIdvoidScannerSubscription subscriptionreqScannerSubscription (int reqIdvoidScannerSubscription subscriptionsetServerLogLevel (int logLevel)voidChanges the TWS/GW log level. The default is 2 = ERRORNone5 = DETAIL is required for capturing all API messages and troubleshooting API programsNoneNoneValid values are:NoneNone1 = SYSTEMNoneNone2 = ERRORNoneNone3 = WARNINGNoneNone4 = INFORMATIONNoneNone5 = DETAILNoneNone.NoneverifyRequest (string apiNamevoidstring apiVersion)verifyMessage (string apiData)voidFor IB’s internal purpose. Allows to provide means of verification between the TWS and third party programs.verifyAndAuthRequest (string apiNamevoidstring apiVersionverifyAndAuthMessage (string apiDatavoidstring xyzResponse)queryDisplayGroups (int requestId)voidRequests all available Display Groups in TWS. More…subscribeToGroupEvents (int requestIdvoidint groupId)updateDisplayGroup (int requestIdvoidstring contractInfo)unsubscribeFromGroupEvents (int requestId)voidCancels a TWS Window Group subscription.reqPositionsMulti (int requestIdvoidstring accountcancelPositionsMulti (int requestId)voidCancels positions request for account and/or model. More…reqAccountUpdatesMulti (int requestIdvoidstring accountcancelAccountUpdatesMulti (int requestId)voidCancels account updates request for account and/or model. More…reqSecDefOptParams (int reqIdvoidstring underlyingSymbolreqSoftDollarTiers (int reqId)voidRequests pre-defined Soft Dollar Tiers. This is only supported for registered professional advisors and hedge and mutual funds who have configured Soft Dollar Tiers in Account Management. Refer to: https://www.interactivebrokers.com/en/software/am/am/manageaccount/requestsoftdollars.htm?Highlight=soft%20dollar%20tier. More…reqFamilyCodes ()voidRequests family codes for an accountreqMatchingSymbols (int reqIdvoidstring pattern)reqMktDepthExchanges ()voidRequests venues for which market data is returned to updateMktDepthL2 (those with market makers) More…reqSmartComponents (int reqIdvoidstring bboExchange)reqNewsProviders ()voidRequests news providers which the user has subscribed to. More…reqNewsArticle (int requestIdvoidstring providerCodereqHistoricalNews (int requestIdvoidint conIdreqHeadTimestamp (int tickerIdvoidContract contractcancelHeadTimestamp (int tickerId)voidCancels a pending reqHeadTimeStamp requestNone. More…NonereqHistogramData (int tickerIdvoidContract contractNone. More…NonecancelHistogramData (int tickerId)voidCancels an active data histogram request. More…reqMarketRule (int marketRuleId)voidRequests details about a given market ruleNoneThe market rule for an instrument on a particular exchange provides details about how the minimum price increment changes with priceNoneNoneA list of market rule ids can be obtained by invoking reqContractDetails on a particular contract. The returned market rule ID list will provide the market rule ID for the instrument in the correspond valid exchange list in contractDetails.NoneNone. More…NonereqPnL (int reqIdvoidstring accountcancelPnL (int reqId)voidcancels subscription for real time updated daily PnL params reqIdreqPnLSingle (int reqIdvoidstring accountcancelPnLSingle (int reqId)voidCancels real time subscription for a positions daily PnL information. More…reqHistoricalTicks (int reqIdvoidContract contractreqWshMetaData (int reqId)voidRequests metadata from the WSH calendar. More…cancelWshMetaData (int reqId)voidCancels pending request for WSH metadata. More…reqWshEventData (int reqIdvoidWshEventData wshEventData)cancelWshEventData (int reqId)voidCancels pending WSH event data request. More…reqUserInfo (int reqId)voidRequests user info. More…IsDataAvailable ()boolNoneReadInt ()intNoneReadAtLeastNBytes (int msgSize)byte[]NoneReadByteArray (int msgSize)byte[]None

| Name | Type | Description |
| --- | --- | --- |
| SetConnectOptions (string connectOptions) | void | Ignore. Used for IB’s internal purposes. |
| DisableUseV100Plus () | void | Allows to switch between different current (V100+) and previous connection mechanisms. |
| IsConnected () | bool | Indicates whether the API-TWS connection has been closed. Note: This function is not automatically invoked and must be by the API client. More… |
| startApi () | void | Initiates the message exchange between the client application and the TWS/IB Gateway. |
| Close () | void | Terminates the connection and notifies the EWrapper implementing class. More… |
| eDisconnect (bool resetState=true) | virtual void | Closes the socket connection and terminates its thread. |
| reqCompletedOrders (bool apiOnly) | void | Requests completed orders. |
| None | . More… | None |
| cancelTickByTickData (int requestId) | void | Cancels tick-by-tick data. |
| None | . More… | None |
| reqTickByTickData (int requestId | void | Contract contract |
| None | . More… | None |
| cancelHistoricalData (int reqId) | void | Cancels a historical data request. More… |
| calculateImpliedVolatility (int reqId | void | Contract contract |
| None | Request the calculation of the implied volatility based on hypothetical option and its underlying prices. | None |
| None | The calculation will be return in EWrapper’s tickOptionComputation callback. | None |
| None | . More… | None |
| calculateOptionPrice (int reqId | void | Contract contract |
| None | The calculation will be return in EWrapper’s tickOptionComputation callback. | None |
| None | . More… | None |
| cancelAccountSummary (int reqId) | void | Cancels the account’s summary request. After requesting an account’s summary |
| cancelCalculateImpliedVolatility (int reqId) | void | Cancels an option’s implied volatility calculation request. More… |
| cancelCalculateOptionPrice (int reqId) | void | Cancels an option’s price calculation request. More… |
| cancelFundamentalData (int reqId) | void | Cancels Fundamental data request. More… |
| cancelMktData (int tickerId) | void | Cancels a RT Market Data request. More… |
| cancelMktDepth (int tickerId | void | bool isSmartDepth) |
| cancelNewsBulletin () | void | Cancels IB’s news bulletin subscription. More… |
| cancelOrder (int orderId | void | string manualOrderCancelTime) |
| None | Note: API clients cannot cancel individual orders placed by other clients. Only reqGlobalCancel is available. | None |
| None | . More… | None |
| cancelPositions () | void | Cancels a previous position subscription request made with reqPositions. More… |
| cancelRealTimeBars (int tickerId) | void | Cancels Real Time Bars’ subscription. More… |
| cancelScannerSubscription (int tickerId) | void | Cancels Scanner Subscription. More… |
| exerciseOptions (int tickerId | void | Contract contract |
| None | Note: this function is affected by a TWS setting which specifies if an exercise request must be finalized. More… | None |
| placeOrder (int id | void | Contract contract |
| replaceFA (int reqId | void | int faDataType |
| requestFA (int faDataType) | void | Requests the FA configuration A Financial Advisor can define three different configurations: More… |
| reqAccountSummary (int reqId | void | string group |
| None | This method will subscribe to the account summary as presented in the TWS’ Account Summary tab. The data is returned at EWrapper::accountSummary | None |
| None | https://www.interactivebrokers.com/en/software/tws/accountwindowtop.htm. More… | None |
| reqAccountUpdates (bool subscribe | void | string acctCode) |
| reqAllOpenOrders () | void | Requests all current open orders in associated accounts at the current moment. The existing orders will be received via the openOrder and orderStatus events. Open orders are returned once; this function does not initiate a subscription. More… |
| reqAutoOpenOrders (bool autoBind) | void | Requests status updates about future orders placed from TWS. Can only be used with client ID 0. More… |
| reqContractDetails (int reqId | void | Contract contract) |
| None | This method will provide all the contracts matching the contract provided. It can also be used to retrieve complete options and futures chains. This information will be returned at EWrapper:contractDetails. Though it is now (in API version > 9.72.12) advised to use reqSecDefOptParams for that purpose. | None |
| None | . More… | None |
| reqCurrentTime () | void | Requests TWS’s current time. More… |
| reqExecutions (int reqId | void | ExecutionFilter filter) |
| reqFundamentalData (int reqId | void | Contract contract |
| reqGlobalCancel () | void | Cancels all active orders. |
| None | This method will cancel ALL open orders including those placed directly from TWS. More… | None |
| reqHistoricalData (int tickerId | void | Contract contract |
| reqIds (int numIds) | void | Requests the next valid order ID at the current moment. More… |
| reqManagedAccts () | void | Requests the accounts to which the logged user has access to. More… |
| reqMktData (int tickerId | void | Contract contract |
| reqMarketDataType (int marketDataType) | void | Switches data type returned from reqMktData request to “frozen” |
| None | The API can receive frozen market data from Trader Workstation. Frozen market data is the last data recorded in our system. | None |
| the API receives real-time market data. Invoking this function with argument 2 requests a switch to frozen data immediately or after the close. | During normal trading hours | None |
| the market data type will automatically switch back to real time if available. More… | When the market reopens | None |
| reqMarketDepth (int tickerId | void | Contract contract |
| commissions | This request must be direct-routed to an exchange and not smart-routed. The number of simultaneous market depth requests allowed in an account is calculated based on a formula that looks at an accounts equity | and quote booster packs. More… |
| reqNewsBulletins (bool allMessages) | void | Subscribes to IB’s News Bulletins. More… |
| reqOpenOrders () | void | Requests all open orders places by this specific API client (identified by the API client id). For client ID 0 |
| reqPositions () | void | Subscribes to position updates for all accessible accounts. All positions sent initially |
| reqRealTimeBars (int tickerId | void | Contract contract |
| only 5 seconds bars are provided. This request is subject to the same pacing as any historical data request: no more than 60 API queries in more than 600 seconds. | Currently | None |
| None | Real time bars subscriptions are also included in the calculation of the number of Level 1 market data subscriptions allowed in an account. More… | None |
| reqScannerParameters () | void | Requests an XML list of scanner parameters valid in TWS. |
| None | Not all parameters are valid from API scanner. More… | None |
| reqScannerSubscription (int reqId | void | ScannerSubscription subscription |
| reqScannerSubscription (int reqId | void | ScannerSubscription subscription |
| setServerLogLevel (int logLevel) | void | Changes the TWS/GW log level. The default is 2 = ERROR |
| None | 5 = DETAIL is required for capturing all API messages and troubleshooting API programs | None |
| None | Valid values are: | None |
| None | 1 = SYSTEM | None |
| None | 2 = ERROR | None |
| None | 3 = WARNING | None |
| None | 4 = INFORMATION | None |
| None | 5 = DETAIL | None |
| None | . | None |
| verifyRequest (string apiName | void | string apiVersion) |
| verifyMessage (string apiData) | void | For IB’s internal purpose. Allows to provide means of verification between the TWS and third party programs. |
| verifyAndAuthRequest (string apiName | void | string apiVersion |
| verifyAndAuthMessage (string apiData | void | string xyzResponse) |
| queryDisplayGroups (int requestId) | void | Requests all available Display Groups in TWS. More… |
| subscribeToGroupEvents (int requestId | void | int groupId) |
| updateDisplayGroup (int requestId | void | string contractInfo) |
| unsubscribeFromGroupEvents (int requestId) | void | Cancels a TWS Window Group subscription. |
| reqPositionsMulti (int requestId | void | string account |
| cancelPositionsMulti (int requestId) | void | Cancels positions request for account and/or model. More… |
| reqAccountUpdatesMulti (int requestId | void | string account |
| cancelAccountUpdatesMulti (int requestId) | void | Cancels account updates request for account and/or model. More… |
| reqSecDefOptParams (int reqId | void | string underlyingSymbol |
| reqSoftDollarTiers (int reqId) | void | Requests pre-defined Soft Dollar Tiers. This is only supported for registered professional advisors and hedge and mutual funds who have configured Soft Dollar Tiers in Account Management. Refer to: https://www.interactivebrokers.com/en/software/am/am/manageaccount/requestsoftdollars.htm?Highlight=soft%20dollar%20tier. More… |
| reqFamilyCodes () | void | Requests family codes for an account |
| reqMatchingSymbols (int reqId | void | string pattern) |
| reqMktDepthExchanges () | void | Requests venues for which market data is returned to updateMktDepthL2 (those with market makers) More… |
| reqSmartComponents (int reqId | void | string bboExchange) |
| reqNewsProviders () | void | Requests news providers which the user has subscribed to. More… |
| reqNewsArticle (int requestId | void | string providerCode |
| reqHistoricalNews (int requestId | void | int conId |
| reqHeadTimestamp (int tickerId | void | Contract contract |
| cancelHeadTimestamp (int tickerId) | void | Cancels a pending reqHeadTimeStamp request |
| None | . More… | None |
| reqHistogramData (int tickerId | void | Contract contract |
| None | . More… | None |
| cancelHistogramData (int tickerId) | void | Cancels an active data histogram request. More… |
| reqMarketRule (int marketRuleId) | void | Requests details about a given market rule |
| None | The market rule for an instrument on a particular exchange provides details about how the minimum price increment changes with price | None |
| None | A list of market rule ids can be obtained by invoking reqContractDetails on a particular contract. The returned market rule ID list will provide the market rule ID for the instrument in the correspond valid exchange list in contractDetails. | None |
| None | . More… | None |
| reqPnL (int reqId | void | string account |
| cancelPnL (int reqId) | void | cancels subscription for real time updated daily PnL params reqId |
| reqPnLSingle (int reqId | void | string account |
| cancelPnLSingle (int reqId) | void | Cancels real time subscription for a positions daily PnL information. More… |
| reqHistoricalTicks (int reqId | void | Contract contract |
| reqWshMetaData (int reqId) | void | Requests metadata from the WSH calendar. More… |
| cancelWshMetaData (int reqId) | void | Cancels pending request for WSH metadata. More… |
| reqWshEventData (int reqId | void | WshEventData wshEventData) |
| cancelWshEventData (int reqId) | void | Cancels pending WSH event data request. More… |
| reqUserInfo (int reqId) | void | Requests user info. More… |
| IsDataAvailable () | bool | None |
| ReadInt () | int | None |
| ReadAtLeastNBytes (int msgSize) | byte[] | None |
| ReadByteArray (int msgSize) | byte[] | None |

| Name | Type | Description |
| --- | --- | --- |
| SetConnectOptions (string connectOptions) | void | Ignore. Used for IB’s internal purposes. |
| DisableUseV100Plus () | void | Allows to switch between different current (V100+) and previous connection mechanisms. |
| IsConnected () | bool | Indicates whether the API-TWS connection has been closed. Note: This function is not automatically invoked and must be by the API client. More… |
| startApi () | void | Initiates the message exchange between the client application and the TWS/IB Gateway. |
| Close () | void | Terminates the connection and notifies the EWrapper implementing class. More… |
| eDisconnect (bool resetState=true) | virtual void | Closes the socket connection and terminates its thread. |
| reqCompletedOrders (bool apiOnly) | void | Requests completed orders. |
| None | . More… | None |
| cancelTickByTickData (int requestId) | void | Cancels tick-by-tick data. |
| None | . More… | None |
| reqTickByTickData (int requestId | void | Contract contract |
| None | . More… | None |
| cancelHistoricalData (int reqId) | void | Cancels a historical data request. More… |
| calculateImpliedVolatility (int reqId | void | Contract contract |
| None | Request the calculation of the implied volatility based on hypothetical option and its underlying prices. | None |
| None | The calculation will be return in EWrapper’s tickOptionComputation callback. | None |
| None | . More… | None |
| calculateOptionPrice (int reqId | void | Contract contract |
| None | The calculation will be return in EWrapper’s tickOptionComputation callback. | None |
| None | . More… | None |
| cancelAccountSummary (int reqId) | void | Cancels the account’s summary request. After requesting an account’s summary |
| cancelCalculateImpliedVolatility (int reqId) | void | Cancels an option’s implied volatility calculation request. More… |
| cancelCalculateOptionPrice (int reqId) | void | Cancels an option’s price calculation request. More… |
| cancelFundamentalData (int reqId) | void | Cancels Fundamental data request. More… |
| cancelMktData (int tickerId) | void | Cancels a RT Market Data request. More… |
| cancelMktDepth (int tickerId | void | bool isSmartDepth) |
| cancelNewsBulletin () | void | Cancels IB’s news bulletin subscription. More… |
| cancelOrder (int orderId | void | string manualOrderCancelTime) |
| None | Note: API clients cannot cancel individual orders placed by other clients. Only reqGlobalCancel is available. | None |
| None | . More… | None |
| cancelPositions () | void | Cancels a previous position subscription request made with reqPositions. More… |
| cancelRealTimeBars (int tickerId) | void | Cancels Real Time Bars’ subscription. More… |
| cancelScannerSubscription (int tickerId) | void | Cancels Scanner Subscription. More… |
| exerciseOptions (int tickerId | void | Contract contract |
| None | Note: this function is affected by a TWS setting which specifies if an exercise request must be finalized. More… | None |
| placeOrder (int id | void | Contract contract |
| replaceFA (int reqId | void | int faDataType |
| requestFA (int faDataType) | void | Requests the FA configuration A Financial Advisor can define three different configurations: More… |
| reqAccountSummary (int reqId | void | string group |
| None | This method will subscribe to the account summary as presented in the TWS’ Account Summary tab. The data is returned at EWrapper::accountSummary | None |
| None | https://www.interactivebrokers.com/en/software/tws/accountwindowtop.htm. More… | None |
| reqAccountUpdates (bool subscribe | void | string acctCode) |
| reqAllOpenOrders () | void | Requests all current open orders in associated accounts at the current moment. The existing orders will be received via the openOrder and orderStatus events. Open orders are returned once; this function does not initiate a subscription. More… |
| reqAutoOpenOrders (bool autoBind) | void | Requests status updates about future orders placed from TWS. Can only be used with client ID 0. More… |
| reqContractDetails (int reqId | void | Contract contract) |
| None | This method will provide all the contracts matching the contract provided. It can also be used to retrieve complete options and futures chains. This information will be returned at EWrapper:contractDetails. Though it is now (in API version > 9.72.12) advised to use reqSecDefOptParams for that purpose. | None |
| None | . More… | None |
| reqCurrentTime () | void | Requests TWS’s current time. More… |
| reqExecutions (int reqId | void | ExecutionFilter filter) |
| reqFundamentalData (int reqId | void | Contract contract |
| reqGlobalCancel () | void | Cancels all active orders. |
| None | This method will cancel ALL open orders including those placed directly from TWS. More… | None |
| reqHistoricalData (int tickerId | void | Contract contract |
| reqIds (int numIds) | void | Requests the next valid order ID at the current moment. More… |
| reqManagedAccts () | void | Requests the accounts to which the logged user has access to. More… |
| reqMktData (int tickerId | void | Contract contract |
| reqMarketDataType (int marketDataType) | void | Switches data type returned from reqMktData request to “frozen” |
| None | The API can receive frozen market data from Trader Workstation. Frozen market data is the last data recorded in our system. | None |
| the API receives real-time market data. Invoking this function with argument 2 requests a switch to frozen data immediately or after the close. | During normal trading hours | None |
| the market data type will automatically switch back to real time if available. More… | When the market reopens | None |
| reqMarketDepth (int tickerId | void | Contract contract |
| commissions | This request must be direct-routed to an exchange and not smart-routed. The number of simultaneous market depth requests allowed in an account is calculated based on a formula that looks at an accounts equity | and quote booster packs. More… |
| reqNewsBulletins (bool allMessages) | void | Subscribes to IB’s News Bulletins. More… |
| reqOpenOrders () | void | Requests all open orders places by this specific API client (identified by the API client id). For client ID 0 |
| reqPositions () | void | Subscribes to position updates for all accessible accounts. All positions sent initially |
| reqRealTimeBars (int tickerId | void | Contract contract |
| only 5 seconds bars are provided. This request is subject to the same pacing as any historical data request: no more than 60 API queries in more than 600 seconds. | Currently | None |
| None | Real time bars subscriptions are also included in the calculation of the number of Level 1 market data subscriptions allowed in an account. More… | None |
| reqScannerParameters () | void | Requests an XML list of scanner parameters valid in TWS. |
| None | Not all parameters are valid from API scanner. More… | None |
| reqScannerSubscription (int reqId | void | ScannerSubscription subscription |
| reqScannerSubscription (int reqId | void | ScannerSubscription subscription |
| setServerLogLevel (int logLevel) | void | Changes the TWS/GW log level. The default is 2 = ERROR |
| None | 5 = DETAIL is required for capturing all API messages and troubleshooting API programs | None |
| None | Valid values are: | None |
| None | 1 = SYSTEM | None |
| None | 2 = ERROR | None |
| None | 3 = WARNING | None |
| None | 4 = INFORMATION | None |
| None | 5 = DETAIL | None |
| None | . | None |
| verifyRequest (string apiName | void | string apiVersion) |
| verifyMessage (string apiData) | void | For IB’s internal purpose. Allows to provide means of verification between the TWS and third party programs. |
| verifyAndAuthRequest (string apiName | void | string apiVersion |
| verifyAndAuthMessage (string apiData | void | string xyzResponse) |
| queryDisplayGroups (int requestId) | void | Requests all available Display Groups in TWS. More… |
| subscribeToGroupEvents (int requestId | void | int groupId) |
| updateDisplayGroup (int requestId | void | string contractInfo) |
| unsubscribeFromGroupEvents (int requestId) | void | Cancels a TWS Window Group subscription. |
| reqPositionsMulti (int requestId | void | string account |
| cancelPositionsMulti (int requestId) | void | Cancels positions request for account and/or model. More… |
| reqAccountUpdatesMulti (int requestId | void | string account |
| cancelAccountUpdatesMulti (int requestId) | void | Cancels account updates request for account and/or model. More… |
| reqSecDefOptParams (int reqId | void | string underlyingSymbol |
| reqSoftDollarTiers (int reqId) | void | Requests pre-defined Soft Dollar Tiers. This is only supported for registered professional advisors and hedge and mutual funds who have configured Soft Dollar Tiers in Account Management. Refer to: https://www.interactivebrokers.com/en/software/am/am/manageaccount/requestsoftdollars.htm?Highlight=soft%20dollar%20tier. More… |
| reqFamilyCodes () | void | Requests family codes for an account |
| reqMatchingSymbols (int reqId | void | string pattern) |
| reqMktDepthExchanges () | void | Requests venues for which market data is returned to updateMktDepthL2 (those with market makers) More… |
| reqSmartComponents (int reqId | void | string bboExchange) |
| reqNewsProviders () | void | Requests news providers which the user has subscribed to. More… |
| reqNewsArticle (int requestId | void | string providerCode |
| reqHistoricalNews (int requestId | void | int conId |
| reqHeadTimestamp (int tickerId | void | Contract contract |
| cancelHeadTimestamp (int tickerId) | void | Cancels a pending reqHeadTimeStamp request |
| None | . More… | None |
| reqHistogramData (int tickerId | void | Contract contract |
| None | . More… | None |
| cancelHistogramData (int tickerId) | void | Cancels an active data histogram request. More… |
| reqMarketRule (int marketRuleId) | void | Requests details about a given market rule |
| None | The market rule for an instrument on a particular exchange provides details about how the minimum price increment changes with price | None |
| None | A list of market rule ids can be obtained by invoking reqContractDetails on a particular contract. The returned market rule ID list will provide the market rule ID for the instrument in the correspond valid exchange list in contractDetails. | None |
| None | . More… | None |
| reqPnL (int reqId | void | string account |
| cancelPnL (int reqId) | void | cancels subscription for real time updated daily PnL params reqId |
| reqPnLSingle (int reqId | void | string account |
| cancelPnLSingle (int reqId) | void | Cancels real time subscription for a positions daily PnL information. More… |
| reqHistoricalTicks (int reqId | void | Contract contract |
| reqWshMetaData (int reqId) | void | Requests metadata from the WSH calendar. More… |
| cancelWshMetaData (int reqId) | void | Cancels pending request for WSH metadata. More… |
| reqWshEventData (int reqId | void | WshEventData wshEventData) |
| cancelWshEventData (int reqId) | void | Cancels pending WSH event data request. More… |
| reqUserInfo (int reqId) | void | Requests user info. More… |
| IsDataAvailable () | bool | None |
| ReadInt () | int | None |
| ReadAtLeastNBytes (int msgSize) | byte[] | None |
| ReadByteArray (int msgSize) | byte[] | None |

### Public Attributes

NameTypeDescriptionServerVersion => serverVersionintreturns the Host’s version. Some of the API functionality might not be available in older Hosts and therefore it is essential to keep the TWS/Gateway as up to date as possible.

| Name | Type | Description |
| --- | --- | --- |
| ServerVersion => serverVersion | int | returns the Host’s version. Some of the API functionality might not be available in older Hosts and therefore it is essential to keep the TWS/Gateway as up to date as possible. |

| Name | Type | Description |
| --- | --- | --- |
| ServerVersion => serverVersion | int | returns the Host’s version. Some of the API functionality might not be available in older Hosts and therefore it is essential to keep the TWS/Gateway as up to date as possible. |

### Protected Member Functions

NameTypeDescriptionprepareBuffer (BinaryWriter paramsList)abstract uintNonesendConnectRequest ()voidNoneCheckServerVersion (int requiredVersion)boolNoneCheckServerVersion (int requestIdboolint requiredVersion)CheckServerVersion (int requiredVersionboolstring updatetail)CheckServerVersion (int tickerIdboolint requiredVersionCloseAndSend (BinaryWriter paramsListvoiduint lengthPosCloseAndSend (int reqIdvoidBinaryWriter paramsListCloseAndSend (BinaryWriter requestabstract voiduint lengthPos)CheckConnection ()boolNoneReportError (int reqIdvoidCodeMsgPair errorReportUpdateTWS (int reqIdvoidstring tail)ReportUpdateTWS (string tail)voidNoneReportError (int reqIdvoidint codeSendCancelRequest (OutgoingMessages msgTypevoidint versionSendCancelRequest (OutgoingMessages msgTypevoidint versionVerifyOrderContract (Contract contractboolint id)VerifyOrder (Order orderboolint id

| Name | Type | Description |
| --- | --- | --- |
| prepareBuffer (BinaryWriter paramsList) | abstract uint | None |
| sendConnectRequest () | void | None |
| CheckServerVersion (int requiredVersion) | bool | None |
| CheckServerVersion (int requestId | bool | int requiredVersion) |
| CheckServerVersion (int requiredVersion | bool | string updatetail) |
| CheckServerVersion (int tickerId | bool | int requiredVersion |
| CloseAndSend (BinaryWriter paramsList | void | uint lengthPos |
| CloseAndSend (int reqId | void | BinaryWriter paramsList |
| CloseAndSend (BinaryWriter request | abstract void | uint lengthPos) |
| CheckConnection () | bool | None |
| ReportError (int reqId | void | CodeMsgPair error |
| ReportUpdateTWS (int reqId | void | string tail) |
| ReportUpdateTWS (string tail) | void | None |
| ReportError (int reqId | void | int code |
| SendCancelRequest (OutgoingMessages msgType | void | int version |
| SendCancelRequest (OutgoingMessages msgType | void | int version |
| VerifyOrderContract (Contract contract | bool | int id) |
| VerifyOrder (Order order | bool | int id |

| Name | Type | Description |
| --- | --- | --- |
| prepareBuffer (BinaryWriter paramsList) | abstract uint | None |
| sendConnectRequest () | void | None |
| CheckServerVersion (int requiredVersion) | bool | None |
| CheckServerVersion (int requestId | bool | int requiredVersion) |
| CheckServerVersion (int requiredVersion | bool | string updatetail) |
| CheckServerVersion (int tickerId | bool | int requiredVersion |
| CloseAndSend (BinaryWriter paramsList | void | uint lengthPos |
| CloseAndSend (int reqId | void | BinaryWriter paramsList |
| CloseAndSend (BinaryWriter request | abstract void | uint lengthPos) |
| CheckConnection () | bool | None |
| ReportError (int reqId | void | CodeMsgPair error |
| ReportUpdateTWS (int reqId | void | string tail) |
| ReportUpdateTWS (string tail) | void | None |
| ReportError (int reqId | void | int code |
| SendCancelRequest (OutgoingMessages msgType | void | int version |
| SendCancelRequest (OutgoingMessages msgType | void | int version |
| VerifyOrderContract (Contract contract | bool | int id) |
| VerifyOrder (Order order | bool | int id |

### Protected Attributes

NameTypeDescriptionserverVersionintNonesocketTransportETransportNonewrapperEWrapperNoneisConnectedvolatile boolNoneclientIdintNoneextraAuthboolNoneuseV100Plus = trueboolNoneallowRedirectboolNonetcpStreamStreamNone

| Name | Type | Description |
| --- | --- | --- |
| serverVersion | int | None |
| socketTransport | ETransport | None |
| wrapper | EWrapper | None |
| isConnected | volatile bool | None |
| clientId | int | None |
| extraAuth | bool | None |
| useV100Plus = true | bool | None |
| allowRedirect | bool | None |
| tcpStream | Stream | None |

| Name | Type | Description |
| --- | --- | --- |
| serverVersion | int | None |
| socketTransport | ETransport | None |
| wrapper | EWrapper | None |
| isConnected | volatile bool | None |
| clientId | int | None |
| extraAuth | bool | None |
| useV100Plus = true | bool | None |
| allowRedirect | bool | None |
| tcpStream | Stream | None |
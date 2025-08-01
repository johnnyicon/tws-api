---
title: "Error Handling"
description: "TWS API Documentation - Error Handling"
source: "Interactive Brokers TWS API Documentation"
nav_id: "error-handling"
scraped_at: "2025-08-01T00:35:11.264628"
word_count: 1762
paragraph_count: 29
subsection_count: 8
code_block_count: 1
format: "markdown"
---

# Error Handling

## Error Handling

When a client application sends a message to TWS which requires a response which has an expected response (i.e. placing an order, requesting market data, subscribing to account updates, etc.), TWS will almost either always 1) respond with the relevant data or 2) send an error message toEWrapper.error().
Exceptions when no response can occur: Also, if a request is made prior to full establishment of connection (denoted by a returned 2104 or 2106 error code“Data Server is Ok”), there may not be a response from the request.
Error messages sent by the TWS are handled by theEWrapper.error()method. TheEWrapper.error()event contains the originating request Id (or the orderId in case the error was raised when placing an order), a numeric error code and a brief description. It is important to keep in mind that this function is used fortrueerror messages as well as notifications that do not mean anything is wrong.
API Error Messages when TWS is not set to the English Language
Currently on the Windows platform, error messages are sent using Latin1 encoding. If TWS is launched in a non-Western language, it is recommended to enable the setting at Global Configuration -> API -> Settings to “Show API error messages in English”.

When a client application sends a message to TWS which requires a response which has an expected response (i.e. placing an order, requesting market data, subscribing to account updates, etc.), TWS will almost either always 1) respond with the relevant data or 2) send an error message toEWrapper.error().
Exceptions when no response can occur: Also, if a request is made prior to full establishment of connection (denoted by a returned 2104 or 2106 error code“Data Server is Ok”), there may not be a response from the request.
Error messages sent by the TWS are handled by theEWrapper.error()method. TheEWrapper.error()event contains the originating request Id (or the orderId in case the error was raised when placing an order), a numeric error code and a brief description. It is important to keep in mind that this function is used fortrueerror messages as well as notifications that do not mean anything is wrong.
API Error Messages when TWS is not set to the English Language
Currently on the Windows platform, error messages are sent using Latin1 encoding. If TWS is launched in a non-Western language, it is recommended to enable the setting at Global Configuration -> API -> Settings to “Show API error messages in English”.

### Understanding Message Codes

The TWS uses theEWrapper.errormethod not only to deliver errors but also warnings or informative messages. This is done mostly for simplicity’s sake. Below is a table with all the messages which can be sent by the TWS/IB Gateway. All messages delivered by the TWS are usually accompanied by a brief but meaningful description pointing in the direction of the problem.
Remember that the TWS API simply connects to a running TWS/IB Gateway which most of times will be running on your local network if not in the same host as the client application. It is your responsibility to provide reliable connectivity between the TWS and your client application.

The TWS uses theEWrapper.errormethod not only to deliver errors but also warnings or informative messages. This is done mostly for simplicity’s sake. Below is a table with all the messages which can be sent by the TWS/IB Gateway. All messages delivered by the TWS are usually accompanied by a brief but meaningful description pointing in the direction of the problem.
Remember that the TWS API simply connects to a running TWS/IB Gateway which most of times will be running on your local network if not in the same host as the client application. It is your responsibility to provide reliable connectivity between the TWS and your client application.

### System Message Codes

The messages in the table below are not a consequence of any action performed by the client application. They are notifications about the connectivity status between the TWS and our servers. Your client application must pay special attention to them and handle the situation accordingly. You are very likely to lose connectivity to our servers at least once a day due to our daily server maintenance downtime as clearly detailed in our Current System Status page. Note that after the system reset, the TWS/IB Gateway will automatically reconnect to our servers and you can resume your operations normally.
During a reset period, there may be an interruption in the ability to log in or manage orders. Existing orders (native types) will operate normally although execution reports and simulated orders will be delayed until the reset is complete. It is not recommended to operate during the scheduled reset times.

The messages in the table below are not a consequence of any action performed by the client application. They are notifications about the connectivity status between the TWS and our servers. Your client application must pay special attention to them and handle the situation accordingly. You are very likely to lose connectivity to our servers at least once a day due to our daily server maintenance downtime as clearly detailed in our Current System Status page. Note that after the system reset, the TWS/IB Gateway will automatically reconnect to our servers and you can resume your operations normally.
During a reset period, there may be an interruption in the ability to log in or manage orders. Existing orders (native types) will operate normally although execution reports and simulated orders will be delayed until the reset is complete. It is not recommended to operate during the scheduled reset times.

CodeTWS messageAdditional notes1100Connectivity between IB and the TWS has been lost.Your TWS/IB Gateway has been disconnected from IB servers. This can occur because of an internet connectivity issue, a nightly reset of the IB servers, or a competing session.1101Connectivity between IB and TWS has been restored- data lost.*The TWS/IB Gateway has successfully reconnected to IB’s servers. Your market data requests have been lost and need to be re-submitted.1102Connectivity between IB and TWS has been restored- data maintained.The TWS/IB Gateway has successfully reconnected to IB’s servers. Your market data requests have been recovered and there is no need for you to re-submit them.1300TWS socket port has been reset and this connection is being dropped. Please reconnect on the new port – <port_num>The port number in the TWS/IBG settings has been changed during an active API connection.

### Error Codes

Error codes in different ranges have different indications.

Error codes in different ranges have different indications.

### Receiving Error Messages

#### EWrapper.error(

reqId:int. The request identifier corresponding to the most recent reqId that maintained the error stream.This does not pertain to the orderId from placeOrder, but whatever the most recent requestId is.
errorTime:int. The Unix timestamp of when the error took place.Note: This is only implemented for TWS API 10.33+
errorCode:int. The code identifying the error.
errorMsg:String. The error’s description.
advancedOrderRejectJson:String. Advanced order reject description in json format.)

#### EWrapper.error(

reqId:int. The request identifier corresponding to the most recent reqId that maintained the error stream.This does not pertain to the orderId from placeOrder, but whatever the most recent requestId is.
errorTime:int. The Unix timestamp of when the error took place.Note: This is only implemented for TWS API 10.33+
errorCode:int. The code identifying the error.
errorMsg:String. The error’s description.
advancedOrderRejectJson:String. Advanced order reject description in json format.)

#### EWrapper.error(

```python
def error(self, reqId: TickerId, errorTime: int, errorCode: int, errorString: str, advancedOrderRejectJson = ""):
  print("Error. Id:", reqId, errorTime, "Code:", errorCode, "Msg:", errorString, "AdvancedOrderRejectJson:", advancedOrderRejectJson)
```

### Common Error Resolution

The content below references some of the most common errors received by clients at Interactive Brokers, and offers direct resolutions for the matters in most instances. If further information is required, please feel to contactCustomer Servicefor additional insight.

The content below references some of the most common errors received by clients at Interactive Brokers, and offers direct resolutions for the matters in most instances. If further information is required, please feel to contactCustomer Servicefor additional insight.

### Market data farm connection is OK

Error code 2104, 2106, and 2158 all generally state that farm connection is OK. What this means is that the API has successfully connected to Trader Workstation or the IB Gateway, and that connection is able to reach Interactive Brokers servers. There is no issue with the connection, and it is a sign you connected successfully.
While using IB Gateway, users may encounter the error, “A historical data farm connection has become inactive but should be available upon demand.” This means that while no historical data requests are being sent, the connection is halted. Once a historical data request is sent over the API connection, the market data farm will reconnect and supply market data.

Error code 2104, 2106, and 2158 all generally state that farm connection is OK. What this means is that the API has successfully connected to Trader Workstation or the IB Gateway, and that connection is able to reach Interactive Brokers servers. There is no issue with the connection, and it is a sign you connected successfully.
While using IB Gateway, users may encounter the error, “A historical data farm connection has become inactive but should be available upon demand.” This means that while no historical data requests are being sent, the connection is halted. Once a historical data request is sent over the API connection, the market data farm will reconnect and supply market data.

### Requested market data requires additional subscription for API. See link in 'Market Data Connections' dialog for more details.Delayed market data is available.

Error 10089 notes that clients are requesting market data when they do not maintain a valid market data subscription. To resolve this issue, users must add a market data subscription tothe specific user they are requesting market data with. Alternatively, users mustrequest delayed market dataprior to requesting market data.
Market data availability is different inTWS versus the API. As a result, market data you can receive in Trader Workstation may not be available in the API.
Interactive Brokers lists many of our most popular market data subscriptionshere.

Error 10089 notes that clients are requesting market data when they do not maintain a valid market data subscription. To resolve this issue, users must add a market data subscription tothe specific user they are requesting market data with. Alternatively, users mustrequest delayed market dataprior to requesting market data.
Market data availability is different inTWS versus the API. As a result, market data you can receive in Trader Workstation may not be available in the API.
Interactive Brokers lists many of our most popular market data subscriptionshere.
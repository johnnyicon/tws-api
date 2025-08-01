---
title: "Market Data: Delayed"
description: "TWS API Documentation - Market Data: Delayed"
source: "Interactive Brokers TWS API Documentation"
nav_id: "delayed-market-data"
order: 19
prev_section: "Financial Advisors"
next_section: "Market Data: Historical"
prev_file: "18_financial_advisors.md"
next_file: "20_market_data_historical.md"
scraped_at: "2025-08-01T09:13:29.314060"
word_count: 1309
paragraph_count: 25
subsection_count: 9
code_block_count: 2
format: "markdown"
---

# Market Data: Delayed

## Market Data: Delayed

Delayed market data canonlybe used withEClient.reqMktDataandEClient.reqHistoricalData. This does not function for tick data.
The API can request Live, Frozen, Delayed and Delayed Frozen market data from Trader Workstation by switching market data type via theEClient.reqMarketDataTypebefore making a market data request. A successful switch to a different (non-live) market data type for a particular market data request will be indicated by a callback toEWrapper.marketDataTypewith the ticker ID of the market data request which is returning a different type of data.
AEClient.reqMarketDataTypecallback of1will occur automatically after invoking reqMktData if the user has live data permissions for the instrument.

Delayed market data canonlybe used withEClient.reqMktDataandEClient.reqHistoricalData. This does not function for tick data.
The API can request Live, Frozen, Delayed and Delayed Frozen market data from Trader Workstation by switching market data type via theEClient.reqMarketDataTypebefore making a market data request. A successful switch to a different (non-live) market data type for a particular market data request will be indicated by a callback toEWrapper.marketDataTypewith the ticker ID of the market data request which is returning a different type of data.
AEClient.reqMarketDataTypecallback of1will occur automatically after invoking reqMktData if the user has live data permissions for the instrument.

| Market Data Type | ID | Description |
| --- | --- | --- |
| Live | 1 | Live market data is streaming data relayed back in real time. Market data subscriptions are required to receive live market data. |
| Frozen | 2 | Frozen market data is the last data recorded at market close. In TWS, Frozen data is displayed in gray numbers. When you set the market data type to Frozen, you are asking TWS to send the last available quote when there is not one currently available. For instance, if a market is currently closed and real time data is requested, -1 values will commonly be returned for the bid and ask prices to indicate there is no current bid/ask data available. TWS will often show a ‘frozen’ bid/ask which represents the last value recorded by the system. To receive the last know bid/ask price before the market close, switch to market data type 2 from the API before requesting market data. API frozen data requires TWS/IBG v.962 or higher and the same market data subscriptions necessary for real time streaming data. |
| Delayed | 3 | Free, delayed data is 15 – 20 minutes delayed. In TWS, delayed data is displayed in brown background. When you set market data type to delayed, you are telling TWS to automatically switch to delayed market data if the user does not have the necessary real time data subscription. If live data is available a request for delayed data would be ignored by TWS. Delayed market data is returned with delayed Tick Types (Tick ID 66~76). |
| Delayed Frozen | 4 | Requests delayed “frozen” data for a user without market data subscriptions. |

Free, delayed data is 15 – 20 minutes delayed. In TWS, delayed data is displayed in brown background. When you set market data type to delayed, you are telling TWS to automatically switch to delayed market data if the user does not have the necessary real time data subscription. If live data is available a request for delayed data would be ignored by TWS. Delayed market data is returned with delayedTick Types(Tick ID 66~76).

| Market Data Type | ID | Description |
| --- | --- | --- |
| Live | 1 | Live market data is streaming data relayed back in real time. Market data subscriptions are required to receive live market data. |
| Frozen | 2 | Frozen market data is the last data recorded at market close. In TWS, Frozen data is displayed in gray numbers. When you set the market data type to Frozen, you are asking TWS to send the last available quote when there is not one currently available. For instance, if a market is currently closed and real time data is requested, -1 values will commonly be returned for the bid and ask prices to indicate there is no current bid/ask data available. TWS will often show a ‘frozen’ bid/ask which represents the last value recorded by the system. To receive the last know bid/ask price before the market close, switch to market data type 2 from the API before requesting market data. API frozen data requires TWS/IBG v.962 or higher and the same market data subscriptions necessary for real time streaming data. |
| Delayed | 3 | Free, delayed data is 15 – 20 minutes delayed. In TWS, delayed data is displayed in brown background. When you set market data type to delayed, you are telling TWS to automatically switch to delayed market data if the user does not have the necessary real time data subscription. If live data is available a request for delayed data would be ignored by TWS. Delayed market data is returned with delayed Tick Types (Tick ID 66~76). |
| Delayed Frozen | 4 | Requests delayed “frozen” data for a user without market data subscriptions. |

Free, delayed data is 15 – 20 minutes delayed. In TWS, delayed data is displayed in brown background. When you set market data type to delayed, you are telling TWS to automatically switch to delayed market data if the user does not have the necessary real time data subscription. If live data is available a request for delayed data would be ignored by TWS. Delayed market data is returned with delayedTick Types(Tick ID 66~76).

### Market Data Type Behavior

1) If user sends reqMarketDataType(1) – TWS will start sending only regular (1) market data.
2) If user sends reqMarketDataType(2) – frozen, TWS will start sending regular (1) as default and frozen (2) market data. TWS sends marketDataType callback (1 or 2) indicating what market data will be sent after this callback. It can be regular or frozen.
3) If user sends reqMarketDataType(3) – delayed, TWS will start sending regular (1) as default and delayed (3) market data.
4) If user sends reqMarketDataType(4) – delayed-frozen, TWS will start sending regular (1) as default, delayed (3) and delayed-frozen (4) market data.
Interactive Brokers data will always try to provide the most up to date market data possible, but will permit additional delayed or frozen data if available upon request.

1) If user sends reqMarketDataType(1) – TWS will start sending only regular (1) market data.
2) If user sends reqMarketDataType(2) – frozen, TWS will start sending regular (1) as default and frozen (2) market data. TWS sends marketDataType callback (1 or 2) indicating what market data will be sent after this callback. It can be regular or frozen.
3) If user sends reqMarketDataType(3) – delayed, TWS will start sending regular (1) as default and delayed (3) market data.
4) If user sends reqMarketDataType(4) – delayed-frozen, TWS will start sending regular (1) as default, delayed (3) and delayed-frozen (4) market data.
Interactive Brokers data will always try to provide the most up to date market data possible, but will permit additional delayed or frozen data if available upon request.

### Request Market Data Type

#### EClient.reqMarketDataType (

marketDataType:int. Type of market data to retrieve.)
Switches data type returned from reqMktData request to Live (1), Frozen (2), Delayed (3), or Frozen-Delayed (4).

#### EClient.reqMarketDataType (

marketDataType:int. Type of market data to retrieve.)
Switches data type returned from reqMktData request to Live (1), Frozen (2), Delayed (3), or Frozen-Delayed (4).

#### EClient.reqMarketDataType (

```python
self.reqMarketDataType(3)
```

### Receive Market Data Type

#### EWrapper.marketDataType (

reqId:int. Request identifier used to track data.
marketDataType:int. Type of market data to retrieve.)

#### EWrapper.marketDataType (

reqId:int. Request identifier used to track data.
marketDataType:int. Type of market data to retrieve.)

#### EWrapper.marketDataType (

```python
def marketDataType(self, reqId: TickerId, marketDataType: int):
	print("MarketDataType. ReqId:", reqId, "Type:", marketDataType)
```
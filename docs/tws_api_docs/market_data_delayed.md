---
title: "Market Data: Delayed"
description: "TWS API Documentation - Market Data: Delayed"
source: "Interactive Brokers TWS API Documentation"
nav_id: "delayed-market-data"
scraped_at: "2025-08-01T00:35:11.493121"
word_count: 725
paragraph_count: 22
subsection_count: 4
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

Free, delayed data is 15 – 20 minutes delayed. In TWS, delayed data is displayed in brown background. When you set market data type to delayed, you are telling TWS to automatically switch to delayed market data if the user does not have the necessary real time data subscription. If live data is available a request for delayed data would be ignored by TWS. Delayed market data is returned with delayedTick Types(Tick ID 66~76).

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
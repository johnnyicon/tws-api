---
title: "Market Data: Historical"
description: "TWS API Documentation - Market Data: Historical"
source: "Interactive Brokers TWS API Documentation"
nav_id: "hist-md"
scraped_at: "2025-08-01T00:35:11.649592"
word_count: 9967
paragraph_count: 347
subsection_count: 47
code_block_count: 15
format: "markdown"
---

# Market Data: Historical

## Market Data: Historical

Historical Market data is available for Interactive Brokers market data subscribers in a range of methods and structures. This includes requests for historical bars, identical to the Trader Workstation, historical Time & Sales, as well as Histogram data.

Historical Market data is available for Interactive Brokers market data subscribers in a range of methods and structures. This includes requests for historical bars, identical to the Trader Workstation, historical Time & Sales, as well as Histogram data.

### Historical Data Limitations

Historical market data has it’s own set of market data limitations unique to other requests such as real time market data. This section will cover all limitations that effect historical market data in the Trader Workstation API.

Historical market data has it’s own set of market data limitations unique to other requests such as real time market data. This section will cover all limitations that effect historical market data in the Trader Workstation API.

### Historical Data Filtering

Historical data at IB is filtered for trade types which occur away from the NBBO such as combo legs, block trades, and derivative trades. For that reason the daily volume from the (unfiltered) real time data functionality will generally be larger than the (filtered) historical volume reported by historical data functionality. Also, differences are expected in other fields such as the VWAP between the real time and historical data feeds.
As historical data at IB gets adjusted, compressed and filtered by default, there may be historical data differences if you request historical data at different time points.

Historical data at IB is filtered for trade types which occur away from the NBBO such as combo legs, block trades, and derivative trades. For that reason the daily volume from the (unfiltered) real time data functionality will generally be larger than the (filtered) historical volume reported by historical data functionality. Also, differences are expected in other fields such as the VWAP between the real time and historical data feeds.
As historical data at IB gets adjusted, compressed and filtered by default, there may be historical data differences if you request historical data at different time points.

### Historical Volume Scaling

Volume data returned for historical bars can be modified to return in shares or lots.
Open the Global Configuration windowNavigate to “API” and then “Settings” on the left paneScroll down to the “Send market data in lots for US Stocks for dual-mode API clients”
If the setting is checked, historical volume data will return as aRound Lot.
If the setting is unchecked, historical volume data will return in Shares.

Volume data returned for historical bars can be modified to return in shares or lots.
Open the Global Configuration windowNavigate to “API” and then “Settings” on the left paneScroll down to the “Send market data in lots for US Stocks for dual-mode API clients”
If the setting is checked, historical volume data will return as aRound Lot.
If the setting is unchecked, historical volume data will return in Shares.

### Pacing Violations for Small Bars (30 secs or less)

Although Interactive Brokers offers our clients high quality market data, IB is not a specialised market data provider and as such it is forced to put in place restrictions to limit traffic which is not directly associated to trading. A Pacing Violation occurs whenever one or more of the following restrictions is not observed:
Important: these limitations apply to all our clients and it is not possible to overcome them. If your trading strategy’s market data requirements are not met by our market data services please consider contacting a specialized provider.
Making identical historical data requests within 15 seconds.Making six or more historical data requests for the same Contract, Exchange and Tick Type within two seconds.Making more than 60 requests within any ten minute period.Note that when BID_ASK historical data is requested, each request is counted twice. In a nutshell, the information above can simply be put as “do not request too much data too quick”.
Making identical historical data requests within 15 seconds.Making six or more historical data requests for the same Contract, Exchange and Tick Type within two seconds.Making more than 60 requests within any ten minute period.Note that when BID_ASK historical data is requested, each request is counted twice. In a nutshell, the information above can simply be put as “do not request too much data too quick”.

Although Interactive Brokers offers our clients high quality market data, IB is not a specialised market data provider and as such it is forced to put in place restrictions to limit traffic which is not directly associated to trading. A Pacing Violation occurs whenever one or more of the following restrictions is not observed:
Important: these limitations apply to all our clients and it is not possible to overcome them. If your trading strategy’s market data requirements are not met by our market data services please consider contacting a specialized provider.

Making identical historical data requests within 15 seconds.Making six or more historical data requests for the same Contract, Exchange and Tick Type within two seconds.Making more than 60 requests within any ten minute period.Note that when BID_ASK historical data is requested, each request is counted twice. In a nutshell, the information above can simply be put as “do not request too much data too quick”.

### Unavailable Historical Data

The other historical data limitations listed are general limitations for all trading platforms:
Bars whose size is 30 seconds or less older than six monthsExpired futures data older than two years counting from the future’s expiration date.Expired options, FOPs, warrants and structured products.End of Day (EOD) data for options, FOPs, warrants and structured products.Data for expired future spreadsData for securities which are no longer trading.Native historical data for combos. Historical data is not stored in the IB database separately for combos.; combo historical data in TWS or the API is the sum of data from the legs.Historical data for securities which move to a new exchange will often not be available prior to the time of the move. For example, SOXX stock moved to NASDAQ exchange on 15 Oct 2010, so no SOXX data before 15 Oct 2010 can be retrieved despite SOXX was listed in 2001. This limitation also applied to contract which specifiesSMARTas the exchange.Studies and indicators such as Weighted Moving Averages or Bollinger Bands are not available from the API.

The other historical data limitations listed are general limitations for all trading platforms:
Bars whose size is 30 seconds or less older than six monthsExpired futures data older than two years counting from the future’s expiration date.Expired options, FOPs, warrants and structured products.End of Day (EOD) data for options, FOPs, warrants and structured products.Data for expired future spreadsData for securities which are no longer trading.Native historical data for combos. Historical data is not stored in the IB database separately for combos.; combo historical data in TWS or the API is the sum of data from the legs.Historical data for securities which move to a new exchange will often not be available prior to the time of the move. For example, SOXX stock moved to NASDAQ exchange on 15 Oct 2010, so no SOXX data before 15 Oct 2010 can be retrieved despite SOXX was listed in 2001. This limitation also applied to contract which specifiesSMARTas the exchange.Studies and indicators such as Weighted Moving Averages or Bollinger Bands are not available from the API.

### Finding the Earliest Available Data Point

For many functions, such as EClient.reqHistoricalData, you will need to request market data for a contract. Given that you may not know how long a symbol has been available, you can use EClient.reqHeadTimestamp to find the first available point of data for a given whatToShow value.
ReqHeadTimeStamp counts as an ongoing historical data request, similar to using EClient.reqHistoricalData’s keepUpToDate=True flag. As a result, users should always:
Cancel timestamp requests usingEClient.cancelHeadTimeStamp.All EClient.reqHeadTimestamp requests follow the30 second bar limitations, regardless of which bar size value has been requested.

For many functions, such as EClient.reqHistoricalData, you will need to request market data for a contract. Given that you may not know how long a symbol has been available, you can use EClient.reqHeadTimestamp to find the first available point of data for a given whatToShow value.
ReqHeadTimeStamp counts as an ongoing historical data request, similar to using EClient.reqHistoricalData’s keepUpToDate=True flag. As a result, users should always:
Cancel timestamp requests usingEClient.cancelHeadTimeStamp.All EClient.reqHeadTimestamp requests follow the30 second bar limitations, regardless of which bar size value has been requested.

### Requesting the Earliest Data Point

#### EClient.reqHeadTimestamp (

tickerId:int., A unique identifier which will serve to identify the incoming data.
contract:Contract.The IBApi.Contract you are interested in.
whatToShow:String. The type of data to retrieve. See Historical Data Types
useRTH:int. Whether (1) or not (0) to retrieve data generated only within Regular Trading Hours (RTH)
formatDate:int. Using 1 will return UTC time in YYYYMMDD-hh:mm:ss format. Using 2 will return epoch time.)
Returns the timestamp of earliest available historical data for a contract and data type.

#### EClient.reqHeadTimestamp (

tickerId:int., A unique identifier which will serve to identify the incoming data.
contract:Contract.The IBApi.Contract you are interested in.
whatToShow:String. The type of data to retrieve. See Historical Data Types
useRTH:int. Whether (1) or not (0) to retrieve data generated only within Regular Trading Hours (RTH)
formatDate:int. Using 1 will return UTC time in YYYYMMDD-hh:mm:ss format. Using 2 will return epoch time.)
Returns the timestamp of earliest available historical data for a contract and data type.

#### EClient.reqHeadTimestamp (

```python
self.reqHeadTimeStamp(1, ContractSamples.USStockAtSmart(), "TRADES", 1, 1)
```

### Receiving the Earliest Data Point

#### EWrapper.headTimestamp (

requestId:int. Request identifier used to track data.
headTimestamp:String. Value identifying earliest data date)
The data requested will be returned to EWrapper.headTimeStamp.

#### EWrapper.headTimestamp (

requestId:int. Request identifier used to track data.
headTimestamp:String. Value identifying earliest data date)
The data requested will be returned to EWrapper.headTimeStamp.

#### EWrapper.headTimestamp (

```python
def headTimestamp(self, reqId, headTimestamp):
        print(reqId, headTimestamp)
```

### Cancelling Timestamp Requests

#### EWrapper.cancelHistogramData (

tickerId:int. Request identifier used to track data.)
A reqHeadTimeStamp request can be cancelled with EClient.cancelHeadTimestamp

#### EWrapper.cancelHistogramData (

tickerId:int. Request identifier used to track data.)
A reqHeadTimeStamp request can be cancelled with EClient.cancelHeadTimestamp

#### EWrapper.cancelHistogramData (

```python
self.cancelHeadTimeStamp(reqId)
```

### Historical Bars

Historical Bar data returns a candlestick value based on the requested duration and bar size. This will always return an open, high, low, and close values. Based on which whatToShow value is used, you may also receive volume data. See thewhatToShow sectionfor more details.

Historical Bar data returns a candlestick value based on the requested duration and bar size. This will always return an open, high, low, and close values. Based on which whatToShow value is used, you may also receive volume data. See thewhatToShow sectionfor more details.

### Requesting Historical Bars

#### EClient.reqHistoricalData(

reqId:int, A unique identifier which will serve to identify the incoming data.
contract:Contract, The IBApi.Contract object you are working with.
endDateTime:String, The request’s end date and time. This should be formatted as “YYYYMMDD HH:mm:ss TMZ” or an empty string indicates current present moment).Please be aware that endDateTime must be left as an empty string when requesting continuous futures contracts.
durationStr:String, The amount of time (or Valid Duration String units) to go back from the request’s given end date and time.
barSizeSetting:String, The data’s granularity or Valid Bar Sizes
whatToShow:String, The type of data to retrieve. See Historical Data Types
useRTH:bool, Whether (1) or not (0) to retrieve data generated only within Regular Trading Hours (RTH)
formatDate:bool, The format in which the incoming bars’ date should be presented. Note that for day bars, only yyyyMMdd format is available.
keepUpToDate:bool, Whether a subscription is made to return updates of unfinished real time bars as they are available (True), or all data is returned on a one-time basis (False). IfTrue, and endDateTime cannot be specified.Supported whatToShow values: Trades, Midpoint, Bid, Ask.
chartOptions:TagValueList, This is a field used exclusively for internal use.

#### EClient.reqHistoricalData(

reqId:int, A unique identifier which will serve to identify the incoming data.
contract:Contract, The IBApi.Contract object you are working with.
endDateTime:String, The request’s end date and time. This should be formatted as “YYYYMMDD HH:mm:ss TMZ” or an empty string indicates current present moment).Please be aware that endDateTime must be left as an empty string when requesting continuous futures contracts.
durationStr:String, The amount of time (or Valid Duration String units) to go back from the request’s given end date and time.
barSizeSetting:String, The data’s granularity or Valid Bar Sizes
whatToShow:String, The type of data to retrieve. See Historical Data Types
useRTH:bool, Whether (1) or not (0) to retrieve data generated only within Regular Trading Hours (RTH)
formatDate:bool, The format in which the incoming bars’ date should be presented. Note that for day bars, only yyyyMMdd format is available.
keepUpToDate:bool, Whether a subscription is made to return updates of unfinished real time bars as they are available (True), or all data is returned on a one-time basis (False). IfTrue, and endDateTime cannot be specified.Supported whatToShow values: Trades, Midpoint, Bid, Ask.
chartOptions:TagValueList, This is a field used exclusively for internal use.

#### EClient.reqHistoricalData(

```python
self.reqHistoricalData(4102, contract, queryTime, "1 M", "1 day", "MIDPOINT", 1, 1, False, [])
```

### Duration

The Interactive Brokers Historical Market Data maintains a duration parameter which specifies the overall length of time that data can be collected. The duration specified will derive the bars of data that can then be collected.

#### Valid Duration String Units:

The Interactive Brokers Historical Market Data maintains a duration parameter which specifies the overall length of time that data can be collected. The duration specified will derive the bars of data that can then be collected.

#### Valid Duration String Units:

#### Valid Duration String Units:

The Interactive Brokers Historical Market Data maintains a duration parameter which specifies the overall length of time that data can be collected. The duration specified will derive the bars of data that can then be collected.

### Historical Bar Sizes

Bar sizes dictate the data returned by historical bar requests. The bar size will dictate the scale over which the OHLC/V is returned to the API.

#### Valid Bar Sizes:

Bar sizes dictate the data returned by historical bar requests. The bar size will dictate the scale over which the OHLC/V is returned to the API.

#### Valid Bar Sizes:

#### Valid Bar Sizes:

Bar sizes dictate the data returned by historical bar requests. The bar size will dictate the scale over which the OHLC/V is returned to the API.

### Step Sizes

The functionality of market data requests are predicated on preset step sizes. As such, not all bar sizes will work with all duration values. The table listed here will discuss the smallest to largest bar size value for each duration string.
Duration UnitBar units allowedBar size Interval (Min/Max)Ssecs | mins1 secs -> 1minsDsecs | mins | hrs5 secs -> 1 hoursWsec | mins | hrs10 secs -> 4 hrsMsec | mins | hrs30 secs -> 8 hrsYmins | hrs   | d1 mins-> 1 day

The functionality of market data requests are predicated on preset step sizes. As such, not all bar sizes will work with all duration values. The table listed here will discuss the smallest to largest bar size value for each duration string.

### Max Duration Per Bar Size

The table below displays the maximum duration values allowed for a given bar.
As an example, the maximum duration for Seconds values supported for 5 seconds bars are 86400 S. This means that if I want to retrieve more than 1 day’s worth of 5 second bars, I will then need to request data in increments of D (days).

The table below displays the maximum duration values allowed for a given bar.
As an example, the maximum duration for Seconds values supported for 5 seconds bars are 86400 S. This means that if I want to retrieve more than 1 day’s worth of 5 second bars, I will then need to request data in increments of D (days).

Bar SizeMax Second DurationMax Day DurationMax Week DurationMax Month DurationMax Year Duration1 secs2000 S{Not Supported}{Not Supported}{Not Supported}{Not Supported}5 secs86400 S365 D52 W12 M68 Y10 secs86400 S365 D52 W12 M68 Y15 secs86400 S365 D52 W12 M68 Y30 secs86400 S365 D52 W12 M68 Y1 min86400 S365 D52 W12 M68 Y2 mins86400 S365 D52 W12 M68 Y3 mins86400 S365 D52 W12 M68 Y5 mins86400 S365 D52 W12 M68 Y10 mins86400 S365 D52 W12 M68 Y15 mins86400 S365 D52 W12 M68 Y20 mins86400 S365 D52 W12 M68 Y30 mins86400 S365 D52 W12 M68 Y1 hour86400 S365 D52 W12 M68 Y2 hours86400 S365 D52 W12 M68 Y3 hours86400 S365 D52 W12 M68 Y4 hours86400 S365 D52 W12 M68 Y8 hours86400 S365 D52 W12 M68 Y1 day86400 S365 D52 W12 M68 Y1M86400 S365 D52 W12 M68 Y1W86400 S365 D52 W12 M68 Y

### Format Date Received

Interactive Brokers will return historical market data based on the format set from the request. The formatDate parameter can be provided an integer value to indicate how data should be returned.
Note:Day bars will only return dates in the yyyyMMdd format. Time data is not available.
ValueDescriptionExample1String Time Zone Date“20231019 16:11:48 America/New_York”2Epoch Date16977463083Day & Time Date“1019 16:11:48 America/New_York”

Interactive Brokers will return historical market data based on the format set from the request. The formatDate parameter can be provided an integer value to indicate how data should be returned.
Note:Day bars will only return dates in the yyyyMMdd format. Time data is not available.

### Keep Up To Date

When using keepUpToDate=True for historical data requests, you will see several bars returned with the same timestamp. This is because data is updated approximately every 1-2 seconds. These updates compound until the end of the specified bar size.
In our example to the below, 15 second bars are requested, and we can see the 30 second bar built out incrementally until 20231204 13:30:30 is completed. At which point, we move on to the 45th second bars. This same logic extends into minute, hourly, or daily bars.
keepUpToDate is only available for whatToShow: Trades, Midpoint, Bid, Ask

When using keepUpToDate=True for historical data requests, you will see several bars returned with the same timestamp. This is because data is updated approximately every 1-2 seconds. These updates compound until the end of the specified bar size.
In our example to the below, 15 second bars are requested, and we can see the 30 second bar built out incrementally until 20231204 13:30:30 is completed. At which point, we move on to the 45th second bars. This same logic extends into minute, hourly, or daily bars.

keepUpToDate is only available for whatToShow: Trades, Midpoint, Bid, Ask

### Receiving Historical Bars

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalData (

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### Default Return Format

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalSchedule (

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalDataUpdate (

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalDataEnd (

reqId:int. Request identifier used to track data.
start:String. Returns the starting time of the first historical data bar.
end:String. Returns the end time of the last historical data bar.)
Marks the ending of the historical bars reception.

#### EWrapper.historicalDataEnd (

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### EWrapper.historicalData (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
The historical data will be delivered via the EWrapper.historicalData method in the form of candlesticks. The time zone of returned bars is the time zone chosen in TWS on the login screen.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### Default Return Format

The text on the right is the default formatting for returning data.
The datetime value here wasmodified to return UTC datetimeformatting.
Note:The datetime value indicates thebeginningof the request range rather than the end. The last bar on the right would then indicate data that took place between 20241111-16:53:15 to 20241111-16:53:20.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalSchedule (

reqId:int. Request identifier used to track data.
startDateTime:String. Returns the start date and time of the historical schedule range.
endDateTime:String. Returns the end date and time of the historical schedule range.
timeZone:String. Returns the time zone referenced by the schedule.
sessions:HistoricalSession[]. Returns the full block of historical schedule data for the duration.)
In the case of whatToShow=”schedule”, you will need to also define the EWrapper.historicalSchedule value. This is a unique method that will only be called in the case of the unique whatToShow value to display calendar information.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

#### EWrapper.historicalDataUpdate (

reqId:int. Request identifier used to track data.
bar:Bar. The OHLC historical data Bar. The time zone of the bar is the time zone chosen on the TWS login screen. Smallest bar size is 1 second.)
Receives bars in real time if keepUpToDate is set as True in reqHistoricalData. Similar to realTimeBars function, except returned data is a composite of historical data and real time data that is equivalent to TWS chart functionality to keep charts up to date. Returned bars are successfully updated using real time data.

```python
def historicalData(self, reqId:int, bar: BarData):
	print("HistoricalData. ReqId:", reqId, "BarData.", bar)
```

```python
def historicalSchedule(self, reqId: int, startDateTime: str, endDateTime: str, timeZone: str, sessions: ListOfHistoricalSessions):
	print("HistoricalSchedule. ReqId:", reqId, "Start:", startDateTime, "End:", endDateTime, "TimeZone:", timeZone)
	for session in sessions:
		print("\tSession. Start:", session.startDateTime, "End:", session.endDateTime, "Ref Date:", session.refDate)
```

```python
def historicalDataUpdate(self, reqId: int, bar: BarData):
	print("HistoricalDataUpdate. ReqId:", reqId, "BarData.", bar)
```

```python
def historicalDataEnd(self, reqId: int, start: str, end: str):
	print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
```

### Historical Bar whatToShow

The historical bar types listed below can be used as the whatToShow value for historical bars. These values are used to request different data such as Trades, Midpoint, Bid_Ask data and more. Some bar types support more products than others. Please note theSupported Productssection for each bar type below.

The historical bar types listed below can be used as the whatToShow value for historical bars. These values are used to request different data such as Trades, Midpoint, Bid_Ask data and more. Some bar types support more products than others. Please note theSupported Productssection for each bar type below.

### AGGTRADES

Bar Values:
Supported Products:Cryptocurrency

Bar Values:
Supported Products:Cryptocurrency

### ASK

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures,  Metals, Options, SSFs, Stocks, Structured Products, Warrants

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures,  Metals, Options, SSFs, Stocks, Structured Products, Warrants

### BID

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures,  Metals, Options, SSFs, Stocks, Structured Products, Warrants

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures,  Metals, Options, SSFs, Stocks, Structured Products, Warrants

### BID_ASK

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures, Metals, Options, SSFs, Stocks, Structured Products, Warrants

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures, Metals, Options, SSFs, Stocks, Structured Products, Warrants

### FEE_RATE

Bar Values:
Supported Products:Stocks, ETFs,

Bar Values:
Supported Products:Stocks, ETFs,

### HISTORICAL_VOLATILITY

Bar Values:
Supported Products:ETFs, Indices, Stocks

Bar Values:
Supported Products:ETFs, Indices, Stocks

### MIDPOINT

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures,  Metals, Options, SSFs, Stocks, Structured Products, Warrants

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, FOPs, Forex, Funds, Futures,  Metals, Options, SSFs, Stocks, Structured Products, Warrants

### OPTION_IMPLIED_VOLATILITY

Bar Values:
Supported Products:ETFs, Indices, Stocks

Bar Values:
Supported Products:ETFs, Indices, Stocks

### SCHEDULE

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, Forex, Funds, Futures, Indices, Metals,  SSFs, Stocks, Structured Products, Warrants
NOTE:SCHEDULE data returns only on 1 day bars but returns historical trading schedule only with no information about OHLCV.

Bar Values:
Supported Products:Bonds, CFDs, Commodities, Cryptocurrencies, ETFs, Forex, Funds, Futures, Indices, Metals,  SSFs, Stocks, Structured Products, Warrants
NOTE:SCHEDULE data returns only on 1 day bars but returns historical trading schedule only with no information about OHLCV.

### TRADES

Bar Values:
Supported Products:Bonds, ETFs, FOPs, Futures, Indices, Metals, Options, SSFs, Stocks, Structured Products, Warrants
NOTES:TRADES data is adjusted for splits, but not dividends.

Bar Values:
Supported Products:Bonds, ETFs, FOPs, Futures, Indices, Metals, Options, SSFs, Stocks, Structured Products, Warrants
NOTES:TRADES data is adjusted for splits, but not dividends.

### YIELD_ASK

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

### YIELD_BID

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

### YIELD_BID_ASK

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

### YIELD_LAST

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

Bar Values:
Supported Products:Indices
Note:Yield historical data only available for corporate bonds.

### Histogram Data

Instead of returned data points as a function of time as with the function IBApi::EClient::reqHistoricalData, histograms return data as a function of price level with function IBApi::EClient::reqHistogramData

Instead of returned data points as a function of time as with the function IBApi::EClient::reqHistoricalData, histograms return data as a function of price level with function IBApi::EClient::reqHistogramData

### Requesting Histogram Data

#### EClient.reqHistogramData (

requestId:int, id of the request
contract:Contract, Contract object that is subject of query.
useRth:bool, Data from regular trading hours (1), or all available hours (0).
period:String, string value of requested date range. This will be tied to the same bar size strings as thehistorical bar sizes)
Returns data histogram of specified contract.

#### EClient.reqHistogramData (

requestId:int, id of the request
contract:Contract, Contract object that is subject of query.
useRth:bool, Data from regular trading hours (1), or all available hours (0).
period:String, string value of requested date range. This will be tied to the same bar size strings as thehistorical bar sizes)
Returns data histogram of specified contract.

#### EClient.reqHistogramData (

```python
self.reqHistogramData(4004, contract, false, "3 days")
```

### Receiving Histogram Data

#### EWrapper.histogramData (

requestId:int. Request identifier used to track data.
data:HistogramEntry[]. Returned Tuple of histogram data, number of trades at specified price level.)
Returns relevant histogram data.

#### EWrapper.histogramData (

requestId:int. Request identifier used to track data.
data:HistogramEntry[]. Returned Tuple of histogram data, number of trades at specified price level.)
Returns relevant histogram data.

#### EWrapper.histogramData (

```python
def histogramData(self, reqId:int, items:HistogramDataList):
	print("HistogramData. reqid, items)
```

### Cancelling Histogram Data

#### EClient.cancelHistogramData (

tickerId:int. Request identifier used to track data.)
An active histogram request which has not returned data can be cancelled with EClient.cancelHistogramData

#### EClient.cancelHistogramData (

tickerId:int. Request identifier used to track data.)
An active histogram request which has not returned data can be cancelled with EClient.cancelHistogramData

#### EClient.cancelHistogramData (

```python
self.reqHistogramData(4004)
```

### Historical Time & Sales

The highest granularity of historical data from IB’s database can be retrieved using the API functionEClient.reqHistoricalTicksfor historical time and sales values. Historical Time & Sales will return the same data as what is available in Trader Workstation under the Time and Sales window. This is a series of ticks indicating each trade based on the requested values.
Historical Tick-By-Tick data is not available for combos.Data will not be returned from multiple trading sessions in a single request; Multiple requests must be used.To complete a full second, more ticks may be returned than requested.Time & Sales data requires a Level 1, Top Of Book market data subscription. This would be the same subscription asEClient.reqMktData()orEClient.reqHistoricalData().

The highest granularity of historical data from IB’s database can be retrieved using the API functionEClient.reqHistoricalTicksfor historical time and sales values. Historical Time & Sales will return the same data as what is available in Trader Workstation under the Time and Sales window. This is a series of ticks indicating each trade based on the requested values.
Historical Tick-By-Tick data is not available for combos.Data will not be returned from multiple trading sessions in a single request; Multiple requests must be used.To complete a full second, more ticks may be returned than requested.Time & Sales data requires a Level 1, Top Of Book market data subscription. This would be the same subscription asEClient.reqMktData()orEClient.reqHistoricalData().

### Requesting Time and Sales data

#### EClient.reqHistoricalTicks (

requestId:int, id of the request
contract:Contract, Contract object that is subject of query.
startDateTime:String, i.e. “20170701 12:01:00”. Uses TWS timezone specified at login.
endDateTime:String, i.e. “20170701 13:01:00”. In TWS timezone. Exactly one of startDateTime or endDateTime must be defined.
numberOfTicks:int, Number of distinct data points. Max is 1000 per request.
whatToShow:String, (Bid_Ask, Midpoint, or Trades) Type of data requested.
useRth:bool, Data from regular trading hours (1), or all available hours (0).
ignoreSize:bool, Omit updates that reflect only changes in size, and not price. Applicable to Bid_Ask data requests.Note:Options and Future Options will only display a value of 1, unless to indicate a removed bid/ask, which will instead return a price and size value of 0.
miscOptions:list,Should be defined asnull; reserved for internal use.)
Requests historical Time & Sales data for an instrument.

#### EClient.reqHistoricalTicks (

requestId:int, id of the request
contract:Contract, Contract object that is subject of query.
startDateTime:String, i.e. “20170701 12:01:00”. Uses TWS timezone specified at login.
endDateTime:String, i.e. “20170701 13:01:00”. In TWS timezone. Exactly one of startDateTime or endDateTime must be defined.
numberOfTicks:int, Number of distinct data points. Max is 1000 per request.
whatToShow:String, (Bid_Ask, Midpoint, or Trades) Type of data requested.
useRth:bool, Data from regular trading hours (1), or all available hours (0).
ignoreSize:bool, Omit updates that reflect only changes in size, and not price. Applicable to Bid_Ask data requests.Note:Options and Future Options will only display a value of 1, unless to indicate a removed bid/ask, which will instead return a price and size value of 0.
miscOptions:list,Should be defined asnull; reserved for internal use.)
Requests historical Time & Sales data for an instrument.

#### EClient.reqHistoricalTicks (

```python
self.reqHistoricalTicks(18001, contract, "20170712 21:39:33 US/Eastern", "", 10, "TRADES", 1, True, [])
```

### Receiving Time and Sales data

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

#### EWrapper.historicalTicks (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=MIDPOINT

#### EWrapper.historicalTicks (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=MIDPOINT

#### EWrapper.historicalTicksBidAsk (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=BidAsk

#### EWrapper.historicalTicksBidAsk (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=BidAsk

#### EWrapper.historicalTicksLast (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=Last & AllLast

#### EWrapper.historicalTicksLast (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=Last & AllLast

#### EWrapper.historicalTicks (

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

#### EWrapper.historicalTicksBidAsk (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=BidAsk

#### EWrapper.historicalTicksBidAsk (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=BidAsk

#### EWrapper.historicalTicksLast (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=Last & AllLast

#### EWrapper.historicalTicksLast (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=Last & AllLast

#### EWrapper.historicalTicksBidAsk (

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

#### EWrapper.historicalTicks (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=MIDPOINT

#### EWrapper.historicalTicks (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=MIDPOINT

#### EWrapper.historicalTicksLast (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=Last & AllLast

#### EWrapper.historicalTicksLast (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=Last & AllLast

#### EWrapper.historicalTicksLast (

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

Data is returned to unique functions based on what is requested in the whatToShow field.
IBApi.EWrapper.historicalTicks for whatToShow=MIDPOINTIBApi.EWrapper.historicalTicksBidAsk for whatToShow=BID_ASKIBApi.EWrapper.historicalTicksLast for for whatToShow=TRADES

#### EWrapper.historicalTicks (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=MIDPOINT

#### EWrapper.historicalTicks (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=MIDPOINT

#### EWrapper.historicalTicksBidAsk (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=BidAsk

#### EWrapper.historicalTicksBidAsk (

reqId:int, id of the request
ticks:ListOfHistoricalTick, object containing a list of tick values for the requested timeframe.
done:bool, return whether or not this is the end of the historical ticks requested.)
For whatToShow=BidAsk

```python
def historicalTicks(self, reqId: int, ticks: ListOfHistoricalTickLast, done: bool):
	for tick in ticks:
		print("historicalTicks. ReqId:", reqId, tick)
```

```python
def historicalTicksBidAsk(self, reqId: int, ticks: ListOfHistoricalTickLast, done: bool):
	for tick in ticks:
		print("historicalTicksBidAsk. ReqId:", reqId, tick)
```

```python
def historicalTicksLast(self, reqId: int, ticks: ListOfHistoricalTickLast, done: bool):
	for tick in ticks:
		print("HistoricalTickLast. ReqId:", reqId, tick)
```

### Historical Halted and Unhalted ticks

The tick attribute pastLimit is also returned with streaming Tick-By-Tick responses. Check Halted and Unhalted ticks section.
If tick has zero price, zero size and pastLimit flag is set – this is “Halted” tick.If tick has zero price, zero size and followed immediately after “Halted” tick – this is “Unhalted” tick.

The tick attribute pastLimit is also returned with streaming Tick-By-Tick responses. Check Halted and Unhalted ticks section.
If tick has zero price, zero size and pastLimit flag is set – this is “Halted” tick.If tick has zero price, zero size and followed immediately after “Halted” tick – this is “Unhalted” tick.

### Historical Date Formatting

When creating dates in the TWS API, Interactive Brokers typically supports three methods:
Operator Time ZoneExchange Time ZoneCoordinated Universal Time (UTC)

When creating dates in the TWS API, Interactive Brokers typically supports three methods:
Operator Time ZoneExchange Time ZoneCoordinated Universal Time (UTC)

### Operator Time Zone

Operator Time Zone is the local time set by the user in Trader Workstation. The Operator Time Zone typically maintains a unique formatting structure separate from Exchange Time Zones; however, they can match.

Operator Time Zone is the local time set by the user in Trader Workstation. The Operator Time Zone typically maintains a unique formatting structure separate from Exchange Time Zones; however, they can match.

A user can confirm their Operator Time Zone by launching Trader Workstation then, before logging in, click “More Options >”.

A user can confirm their Operator Time Zone by launching Trader Workstation then, before logging in, click “More Options >”.

Users can then confirm their active Operator Time Zone by referencing the “Time Zone” field.
For US residents, this will typically appear as “America/New_York”, “America/Chicago”, or “America/Los_Angeles”. It is essential to note the Time Zone value, as this will be the value supplied when making requests with the Operator Time Zone.

Users can then confirm their active Operator Time Zone by referencing the “Time Zone” field.
For US residents, this will typically appear as “America/New_York”, “America/Chicago”, or “America/Los_Angeles”. It is essential to note the Time Zone value, as this will be the value supplied when making requests with the Operator Time Zone.

After logging in to Trader Workstation or IB Gateway, you would be able to submit time stamps in the format of “YYYYMMDD HH:mm:ss Operator/Time_Zone”.
Given our prior example, a historical data endDateTime value would appear as”20250101 23:59:59 America/Chicago”. This would mean the latest value I want is just before midnight in Chicago on January 1st, 2025. Even if I am trading contracts in New York or overseas, all historical data requests would be relative to my own time zone.

After logging in to Trader Workstation or IB Gateway, you would be able to submit time stamps in the format of “YYYYMMDD HH:mm:ss Operator/Time_Zone”.
Given our prior example, a historical data endDateTime value would appear as”20250101 23:59:59 America/Chicago”. This would mean the latest value I want is just before midnight in Chicago on January 1st, 2025. Even if I am trading contracts in New York or overseas, all historical data requests would be relative to my own time zone.

### Exchange Time Zone

The exchange Time Zone is the value the exchange itself uses to calculate time. This value is typically unique to the Operator Time Zone, but these values can overlap.

The exchange Time Zone is the value the exchange itself uses to calculate time. This value is typically unique to the Operator Time Zone, but these values can overlap.

As an example, the New York Stock Exchange operates on “US/Eastern”. However, the CME operates on “US/Central”. This values can be programmatically requested using the EClient.reqContractDetails method, and then received from EWrapper.contractDetails in contractDetails.Time ZoneId.
Note that this will be interpreted differently from “America/Chicago”.

As an example, the New York Stock Exchange operates on “US/Eastern”. However, the CME operates on “US/Central”. This values can be programmatically requested using the EClient.reqContractDetails method, and then received from EWrapper.contractDetails in contractDetails.Time ZoneId.
Note that this will be interpreted differently from “America/Chicago”.

### Coordinated Universal Time (UTC)

UTC is a time standard centered around Greenwich Mean Time (GMT). UTC historical data can be formatted as “YYYYMMDD-hh:mm:ss”. Please keep in mind this is based on UTC+0, and as a reference, US/Eastern time is approximately UTC-4 or UTC-5 depending on U.S. Daylight savings.
Please note GMT is unaffected by Daylight savings, and so 09:00:00 will be the same time of day year round regardless of the exchange’s or your local daylight savings observation.

UTC is a time standard centered around Greenwich Mean Time (GMT). UTC historical data can be formatted as “YYYYMMDD-hh:mm:ss”. Please keep in mind this is based on UTC+0, and as a reference, US/Eastern time is approximately UTC-4 or UTC-5 depending on U.S. Daylight savings.
Please note GMT is unaffected by Daylight savings, and so 09:00:00 will be the same time of day year round regardless of the exchange’s or your local daylight savings observation.

### Modifying Returned Date

You may also log in to the Trader Workstation and modify this in the Global Configuration under API and then Settings. Here, you will find a modifiable setting labeled “Send instrument-specific attributes for dual-mode API client in” Here you can select one of the following:
operator timezone: refers to the local timezone you have set in the Trader Workstation or IB Gatewayinstrument timezone: refers to the timezone of the requested exchange. If “SMART” is used, this will use the instrument’s primary exchange.UTC format: refers to a standardized return using UTC as the timezone. This will be returned in the format YYYYMMDD-hh:mm:ss

You may also log in to the Trader Workstation and modify this in the Global Configuration under API and then Settings. Here, you will find a modifiable setting labeled “Send instrument-specific attributes for dual-mode API client in” Here you can select one of the following:
operator timezone: refers to the local timezone you have set in the Trader Workstation or IB Gatewayinstrument timezone: refers to the timezone of the requested exchange. If “SMART” is used, this will use the instrument’s primary exchange.UTC format: refers to a standardized return using UTC as the timezone. This will be returned in the format YYYYMMDD-hh:mm:ss
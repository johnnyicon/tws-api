---
title: "Wall Street Horizon"
description: "TWS API Documentation - Wall Street Horizon"
source: "Interactive Brokers TWS API Documentation"
nav_id: "wsh"
scraped_at: "2025-08-01T00:35:12.710235"
word_count: 1695
paragraph_count: 69
subsection_count: 11
code_block_count: 6
format: "markdown"
---

# Wall Street Horizon

## Wall Street Horizon

Calendar and Event data can be retrieved from the Wall Street Horizon Event Calendar and accessed via the TWS API through the functions IBApi.EClient.reqWshMetaData and IBApi.EClient.reqWshEventData.
It is necessary to have theWall Street Horizon Corporate Event Dataresearch subscription activated first inAccount Management.

Calendar and Event data can be retrieved from the Wall Street Horizon Event Calendar and accessed via the TWS API through the functions IBApi.EClient.reqWshMetaData and IBApi.EClient.reqWshEventData.
It is necessary to have theWall Street Horizon Corporate Event Dataresearch subscription activated first inAccount Management.

WSH provides IBKR with corporate event datasets, including earnings dates, dividend dates, options expiration dates, splits, spinoffs and a wide variety of investor-related conferences.
Data Classes and Fields PDF

WSH provides IBKR with corporate event datasets, including earnings dates, dividend dates, options expiration dates, splits, spinoffs and a wide variety of investor-related conferences.

### Meta Data

The function IBApi.EClient.reqWshMetaData is used to request available event types, or supported filter values, that may be used in the call forEClient.reqWshEventData()filter field.
Regardless of whether or not you are aware of the Meta Data filters, this request mustalwaysbe called once per session prior to theEClient.reqWshEventData()function.

The function IBApi.EClient.reqWshMetaData is used to request available event types, or supported filter values, that may be used in the call forEClient.reqWshEventData()filter field.
Regardless of whether or not you are aware of the Meta Data filters, this request mustalwaysbe called once per session prior to theEClient.reqWshEventData()function.

### Meta Data Filters

While this list contains an array of Meta Data filters that may be used, please be aware that new values may be made available or removed without notice.
In addition to the EClient.reqWshMetaData field being mandatory prior to theEClient.reqWshEventData()function, the JSON content will also return the appropriate column values that are returned along with the function.
Event Type NameEvent Type TagBoard of Directors Meetingwshe_bodBuybackwshe_bybkBuyBack Modificationwshe_bybkmodConference Callwshe_ccFDA Advisory Committee Meetingwshe_fda_adv_commFuture Quarterwshe_fqInvestors Conferencewshe_icIndex Changewshe_idxInterim Dateswshe_interim_datesInitial Public Offeringwshe_ipoMovie Releasewshe_moviesOption Expiration Datewshe_optionMerger and Acquistionwshe_merg_acqQuarter Endwshe_qeSecondary Offeringwshe_secondaryVideo Releasewshe_videosSplitswshe_splitsSpinoffwshe_spinoffsShareholder Meetingwshe_shFiling Due Datewshe_secWSHE Dividendwshe_divDividends Suspend/Resumewshe_divsrEarnings Datewshe_edEarnings Reportwshe_eps

While this list contains an array of Meta Data filters that may be used, please be aware that new values may be made available or removed without notice.
In addition to the EClient.reqWshMetaData field being mandatory prior to theEClient.reqWshEventData()function, the JSON content will also return the appropriate column values that are returned along with the function.

### Requesting Meta Data

#### EClient.reqWshMetaData (

requestId:int. Request identifier used to track data.)
Requests metadata from the WSH calendar.

#### EClient.reqWshMetaData (

requestId:int. Request identifier used to track data.)
Requests metadata from the WSH calendar.

#### EClient.reqWshMetaData (

```python
self.reqWshMetaData(1100)
```

### Receive Meta Data

#### EWrapper.wshEventData (

requestId:int. Request identifier used to track data.
dataJson:String. metadata in json format.)
Returns meta data from the WSH calendar

#### EWrapper.wshEventData (

requestId:int. Request identifier used to track data.
dataJson:String. metadata in json format.)
Returns meta data from the WSH calendar

Once the json content has been received, the specific event types used to filterEClient.reqWshEventData()are listed under “meta_data” -> “event_types”.
The “name” field will express what the filter will return, such as “Board of Directors Meeting”
The “tag” field will return the filter used in your JSON query. The related example would be “wshe_bod”.

Once the json content has been received, the specific event types used to filterEClient.reqWshEventData()are listed under “meta_data” -> “event_types”.
The “name” field will express what the filter will return, such as “Board of Directors Meeting”
The “tag” field will return the filter used in your JSON query. The related example would be “wshe_bod”.

#### EWrapper.wshEventData (

Once the json content has been received, the specific event types used to filterEClient.reqWshEventData()are listed under “meta_data” -> “event_types”.
The “name” field will express what the filter will return, such as “Board of Directors Meeting”
The “tag” field will return the filter used in your JSON query. The related example would be “wshe_bod”.

Once the json content has been received, the specific event types used to filterEClient.reqWshEventData()are listed under “meta_data” -> “event_types”.
The “name” field will express what the filter will return, such as “Board of Directors Meeting”
The “tag” field will return the filter used in your JSON query. The related example would be “wshe_bod”.

```python
def wshMetaData(self, reqId: int, dataJson: str):
	print("WshMetaData.", "ReqId:", reqId, "Data JSON:", dataJson)
```

### Cancel Meta Data

#### EClient.cancelWshMetaData (

requestId:int. Request identifier used to track data.)
Cancels pending request for WSH metadata.

#### EClient.cancelWshMetaData (

requestId:int. Request identifier used to track data.)
Cancels pending request for WSH metadata.

#### EClient.cancelWshMetaData (

```python
self.cancelWshMetaData(1100)
```

### Event Data

The function EClient.reqWshEventData is used to request various calendar events from Wall Street Horizon. The event data is then received via the callback EWrapper.wshEventData. Pending event data requests can be canceled with the function IBApi.EClient.cancelWshEventData.
Note:Prior to sending this message, the API client must make a request for metadata viaEClient.reqWshMetaData.
Also note that TWS will not support multiple concurrent requests. Previous request should succeed, fail, or be cancelled by client before next one. TWS will reject such requests with text “Duplicate WSH meta-data request” or “Duplicate WSH event request”.

The function EClient.reqWshEventData is used to request various calendar events from Wall Street Horizon. The event data is then received via the callback EWrapper.wshEventData. Pending event data requests can be canceled with the function IBApi.EClient.cancelWshEventData.
Note:Prior to sending this message, the API client must make a request for metadata viaEClient.reqWshMetaData.
Also note that TWS will not support multiple concurrent requests. Previous request should succeed, fail, or be cancelled by client before next one. TWS will reject such requests with text “Duplicate WSH meta-data request” or “Duplicate WSH event request”.

### WshEventData Object

When making a request to the Wall Street Horizons Event Calendar with the API, users must create a wshEventData Object. This object contains several fields, along with a filter field, which takes a json-formatted string. The filter values are returned from WSH Meta Data requests.
When creating the object, users are able to specify either the WshEventData.conId, WshEventData.startDate, and WshEventData.endDate, or they may choose to use the WshEventData.filter value. Attempting to use both will result in an error.
Only one Event Type tag may be passed per request. Multiple submitted filters will be ignored beyond the final request.

#### WshEventData()

conId:String. Specify the contract identifier for the event request.
startDate:String. Specify the start date of the event requests. Formatted as “YYYYMMDD”
endDate:String. Specify the end date of the event requests. Formatted as “YYYYMMDD”
fillCompetitors:bool. Automatically fill in competitor values of existing positions.
fillPortfolio:bool. Automatically fill in portfolio values.
fillWatchlist:bool. Automatically fill in watchlist values.
totalLimit:int. Maximum of 100.
filter:String. Json-formatted string containing all filter values. Some available values include:
watchlist: Array of string. Takes a single conid.country: String. Specify a country code, or “All”.EClient.reqWshMetaData()responses will include an Event Type tag which can be used to filter the Event Data’s response. The Json field is a boolean that can only take true to filter the given value

When making a request to the Wall Street Horizons Event Calendar with the API, users must create a wshEventData Object. This object contains several fields, along with a filter field, which takes a json-formatted string. The filter values are returned from WSH Meta Data requests.
When creating the object, users are able to specify either the WshEventData.conId, WshEventData.startDate, and WshEventData.endDate, or they may choose to use the WshEventData.filter value. Attempting to use both will result in an error.
Only one Event Type tag may be passed per request. Multiple submitted filters will be ignored beyond the final request.

#### WshEventData()

conId:String. Specify the contract identifier for the event request.
startDate:String. Specify the start date of the event requests. Formatted as “YYYYMMDD”
endDate:String. Specify the end date of the event requests. Formatted as “YYYYMMDD”
fillCompetitors:bool. Automatically fill in competitor values of existing positions.
fillPortfolio:bool. Automatically fill in portfolio values.
fillWatchlist:bool. Automatically fill in watchlist values.
totalLimit:int. Maximum of 100.
filter:String. Json-formatted string containing all filter values. Some available values include:
watchlist: Array of string. Takes a single conid.country: String. Specify a country code, or “All”.EClient.reqWshMetaData()responses will include an Event Type tag which can be used to filter the Event Data’s response. The Json field is a boolean that can only take true to filter the given value

#### WshEventData()

When making a request to the Wall Street Horizons Event Calendar with the API, users must create a wshEventData Object. This object contains several fields, along with a filter field, which takes a json-formatted string. The filter values are returned from WSH Meta Data requests.
When creating the object, users are able to specify either the WshEventData.conId, WshEventData.startDate, and WshEventData.endDate, or they may choose to use the WshEventData.filter value. Attempting to use both will result in an error.
Only one Event Type tag may be passed per request. Multiple submitted filters will be ignored beyond the final request.

### Request Event Data

#### EClient.reqWshEventData (

requestId:int. Request identifier used to track data.
wshEventData:WshEventData. Unique object used to track all parameters for the event data request. SeeWshEventData Objectfor more details.)
MIN_SERVER_VER_WSH_EVENT_DATA_FILTERS_DATE:*Only passed in the Python implementation. Server version of the API implementationmust be passed. This can be accomplished with the EClient.serverVersion() function call.
Requests event data from the WSH calendar.

#### EClient.reqWshEventData (

requestId:int. Request identifier used to track data.
wshEventData:WshEventData. Unique object used to track all parameters for the event data request. SeeWshEventData Objectfor more details.)
MIN_SERVER_VER_WSH_EVENT_DATA_FILTERS_DATE:*Only passed in the Python implementation. Server version of the API implementationmust be passed. This can be accomplished with the EClient.serverVersion() function call.
Requests event data from the WSH calendar.

#### EClient.reqWshEventData (

```python
self.reqWshEventData(1101, eventDataObj, serverVersion)
```

### Receive Event Data

#### EWrapper.wshEventData (

requestId:int. Request identifier used to track data.
dataJson:String. Event data json format.)
Returns calendar events from the WSH.

#### EWrapper.wshEventData (

requestId:int. Request identifier used to track data.
dataJson:String. Event data json format.)
Returns calendar events from the WSH.

#### EWrapper.wshEventData (

```python
def wshEventData(self, reqId: int, dataJson: str):
	print("WshEventData.", "ReqId:", reqId, "Data JSON:", dataJson)
```

### Cancel Event Data

#### EClient.cancelWshEventData (

requestId:int. Request identifier used to track data.
Cancels pending WSH event data request.

#### EClient.cancelWshEventData (

requestId:int. Request identifier used to track data.
Cancels pending WSH event data request.

#### EClient.cancelWshEventData (

```python
self.cancelWshEventData(1101, eventDataObj)
```
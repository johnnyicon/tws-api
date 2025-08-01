---
title: "WshEventData Class Reference"
description: "TWS API Reference - WshEventData Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "wsh-ref"
order: 36
prev_section: "VolumeCondition Class Reference"
next_section: null
prev_file: "35_volumecondition_class_reference.md"
next_file: null
scraped_at: "2025-08-01T09:13:02.322709"
word_count: 328
paragraph_count: 8
subsection_count: 0
code_block_count: 0
format: "markdown"
---

# WshEventData Class Reference

## WshEventData Class Reference

Class used to define the parameters for the EClient::reqWshEventData query to filter results.

| Name | Type | Description |
| --- | --- | --- |
| ConId | int | Contract identifier used to specify an unique contract |
| Filter | string | A JSON formatted string containing a minimum of string Country, and array watchlist tags. In addition, a unique filter may be specified as “true” in order to receive a specific filter. Filter values are returned from the wshMetaData function. |
| FillWatchlist | boolean | Defines |
| FillPortfolio | boolean |  |
| FillCompetitors | boolean |  |
| StartDate | string |  |
| EndDate | string | The end of your request formatting. Values should be represented like “YYYYMMDD”. |
| TotalLimit | int | Specify the maximum number of results that can be returned. A maximum of |

The beginning of your request formatting. Values should be represented like “YYYYMMDD”.

Class used to define the parameters for the EClient::reqWshEventData query to filter results.

| Name | Type | Description |
| --- | --- | --- |
| ConId | int | Contract identifier used to specify an unique contract |
| Filter | string | A JSON formatted string containing a minimum of string Country, and array watchlist tags. In addition, a unique filter may be specified as “true” in order to receive a specific filter. Filter values are returned from the wshMetaData function. |
| FillWatchlist | boolean | Defines |
| FillPortfolio | boolean |  |
| FillCompetitors | boolean |  |
| StartDate | string |  |
| EndDate | string | The end of your request formatting. Values should be represented like “YYYYMMDD”. |
| TotalLimit | int | Specify the maximum number of results that can be returned. A maximum of |

The beginning of your request formatting. Values should be represented like “YYYYMMDD”.
---
title: "TickAttrib Class Reference"
description: "TWS API Reference - TickAttrib Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "tickattrib-ref"
order: 33
prev_section: "TagValue Class Reference"
next_section: "TimeCondition Class Reference"
prev_file: "32_tagvalue_class_reference.md"
next_file: "34_timecondition_class_reference.md"
scraped_at: "2025-08-01T09:13:02.322558"
word_count: 477
paragraph_count: 11
subsection_count: 1
code_block_count: 0
format: "markdown"
---

# TickAttrib Class Reference

## TickAttrib Class Reference

Tick attributes that describes additional information for price ticks

Tick attributes that describes additional information for price ticks

NameTypeDescriptionCanAutoExecuteboolUsed with tickPrice callback from reqMktData. Specifies whether the price tick is available for automatic execution (1) or not (0).PastLimitboolUsed with tickPrice to indicate if the bid price is lower than the day’s lowest value or the ask price is higher than the highest ask.PreOpenboolIndicates whether the bid/ask price tick is from pre-open session.UnreportedboolUsed with tick-by-tick data to indicate if a trade is classified as ‘unreportable’ (odd lotsBidPastLowboolUsed with real time tick-by-tick. Indicates if bid is lower than day’s lowest low.AskPastHighboolUsed with real time tick-by-tick. Indicates if ask is higher than day’s highest ask.

| Name | Type | Description |
| --- | --- | --- |
| CanAutoExecute | bool | Used with tickPrice callback from reqMktData. Specifies whether the price tick is available for automatic execution (1) or not (0). |
| PastLimit | bool | Used with tickPrice to indicate if the bid price is lower than the day’s lowest value or the ask price is higher than the highest ask. |
| PreOpen | bool | Indicates whether the bid/ask price tick is from pre-open session. |
| Unreported | bool | Used with tick-by-tick data to indicate if a trade is classified as ‘unreportable’ (odd lots |
| BidPastLow | bool | Used with real time tick-by-tick. Indicates if bid is lower than day’s lowest low. |
| AskPastHigh | bool | Used with real time tick-by-tick. Indicates if ask is higher than day’s highest ask. |

| Name | Type | Description |
| --- | --- | --- |
| CanAutoExecute | bool | Used with tickPrice callback from reqMktData. Specifies whether the price tick is available for automatic execution (1) or not (0). |
| PastLimit | bool | Used with tickPrice to indicate if the bid price is lower than the day’s lowest value or the ask price is higher than the highest ask. |
| PreOpen | bool | Indicates whether the bid/ask price tick is from pre-open session. |
| Unreported | bool | Used with tick-by-tick data to indicate if a trade is classified as ‘unreportable’ (odd lots |
| BidPastLow | bool | Used with real time tick-by-tick. Indicates if bid is lower than day’s lowest low. |
| AskPastHigh | bool | Used with real time tick-by-tick. Indicates if ask is higher than day’s highest ask. |

### Public Member Functions

NameTypeDescriptionToString()override stringReturns string to display.

| Name | Type | Description |
| --- | --- | --- |
| ToString() | override string | Returns string to display. |

| Name | Type | Description |
| --- | --- | --- |
| ToString() | override string | Returns string to display. |
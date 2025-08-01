---
title: "HistoricalTickBidAsk Class Reference"
description: "TWS API Reference - HistoricalTickBidAsk Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "hist-tick-bidask"
order: 19
prev_section: "HistoricalTick Class Reference"
next_section: "HistoricalTickLast Class Reference"
prev_file: "18_historicaltick_class_reference.md"
next_file: "20_historicalticklast_class_reference.md"
scraped_at: "2025-08-01T09:13:02.321287"
word_count: 265
paragraph_count: 7
subsection_count: 0
code_block_count: 0
format: "markdown"
---

# HistoricalTickBidAsk Class Reference

## HistoricalTickBidAsk Class Reference

Used when requesting historical tick data with whatToShow = BID_ASK.

Used when requesting historical tick data with whatToShow = BID_ASK.

NameTypeDescriptionTimelongThe UNIX timestamp of the historical tick.TickAttribLastTickAttribLastTick attribs of historical last tick.PricedoubleThe last price of the historical tick.SizedecimalThe last size of the historical tick.ExchangestringThe source exchange of the historical tick.SpecialConditionsstringThe conditions of the historical tick. Refer toTrade Conditionspage for more details

| Name | Type | Description |
| --- | --- | --- |
| Time | long | The UNIX timestamp of the historical tick. |
| TickAttribLast | TickAttribLast | Tick attribs of historical last tick. |
| Price | double | The last price of the historical tick. |
| Size | decimal | The last size of the historical tick. |
| Exchange | string | The source exchange of the historical tick. |
| SpecialConditions | string | The conditions of the historical tick. Refer to Trade Conditions page for more details |

| Name | Type | Description |
| --- | --- | --- |
| Time | long | The UNIX timestamp of the historical tick. |
| TickAttribLast | TickAttribLast | Tick attribs of historical last tick. |
| Price | double | The last price of the historical tick. |
| Size | decimal | The last size of the historical tick. |
| Exchange | string | The source exchange of the historical tick. |
| SpecialConditions | string | The conditions of the historical tick. Refer to Trade Conditions page for more details |
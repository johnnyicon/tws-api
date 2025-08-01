---
title: "Bar Class Reference"
description: "TWS API Reference - Bar Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "bar-ref"
order: 3
prev_section: "AccountSummaryTags Class"
next_section: "ComboLeg Class Reference"
prev_file: "02_accountsummarytags_class.md"
next_file: "04_comboleg_class_reference.md"
scraped_at: "2025-08-01T09:13:02.318664"
word_count: 366
paragraph_count: 7
subsection_count: 0
code_block_count: 0
format: "markdown"
---

# Bar Class Reference

## Bar Class Reference

The historical data bar’s description.

The historical data bar’s description.

NameTypeDescriptionTimestringThe bar’s date and time (either as a yyyymmss hh:mm:ss formatted string or as system time according to the request). Time zone is the TWS time zone chosen on login.OpendoubleThe bar’s open price.HighdoubleThe bar’s high price.LowdoubleThe bar’s low price.ClosedoubleThe bar’s close price.VolumedecimalThe bar’s traded volume if available (only available for TRADES)CountintThe number of trades during the bar’s timespan (only available for TRADES)WAPdecimalThe bar’s Weighted Average Price (only available for TRADES)

| Name | Type | Description |
| --- | --- | --- |
| Time | string | The bar’s date and time (either as a yyyymmss hh:mm:ss formatted string or as system time according to the request). Time zone is the TWS time zone chosen on login. |
| Open | double | The bar’s open price. |
| High | double | The bar’s high price. |
| Low | double | The bar’s low price. |
| Close | double | The bar’s close price. |
| Volume | decimal | The bar’s traded volume if available (only available for TRADES) |
| Count | int | The number of trades during the bar’s timespan (only available for TRADES) |
| WAP | decimal | The bar’s Weighted Average Price (only available for TRADES) |

| Name | Type | Description |
| --- | --- | --- |
| Time | string | The bar’s date and time (either as a yyyymmss hh:mm:ss formatted string or as system time according to the request). Time zone is the TWS time zone chosen on login. |
| Open | double | The bar’s open price. |
| High | double | The bar’s high price. |
| Low | double | The bar’s low price. |
| Close | double | The bar’s close price. |
| Volume | decimal | The bar’s traded volume if available (only available for TRADES) |
| Count | int | The number of trades during the bar’s timespan (only available for TRADES) |
| WAP | decimal | The bar’s Weighted Average Price (only available for TRADES) |
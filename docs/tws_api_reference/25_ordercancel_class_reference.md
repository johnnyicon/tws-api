---
title: "OrderCancel Class Reference"
description: "TWS API Reference - OrderCancel Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "ordercancel-ref"
order: 25
prev_section: "OrderAllocation Class Reference"
next_section: "OrderComboLeg Class Reference"
prev_file: "24_orderallocation_class_reference.md"
next_file: "26_ordercomboleg_class_reference.md"
scraped_at: "2025-08-01T09:13:02.321927"
word_count: 267
paragraph_count: 7
subsection_count: 0
code_block_count: 0
format: "markdown"
---

# OrderCancel Class Reference

## OrderCancel Class Reference

The Order cancellation parameters when cancelling an order.

The Order cancellation parameters when cancelling an order.

NameTypeDescriptionextOperatorstringFollowingCME Rule 576, the ExtOperator field will signify the unique API operator at the time of trading for order management.manualOrderIndicatorintFollowingCME Rule 576, the ManualOrderIndicator field will signify if an order is manual (1) or automated (0).manualOrderCancelTimestringUsed by brokers and advisors when manually entering an order cancellation request. Format should be “YYYYMMDD-HH:mm:ss” using UTC as the timezone value.

| Name | Type | Description |
| --- | --- | --- |
| extOperator | string | Following CME Rule 576, the ExtOperator field will signify the unique API operator at the time of trading for order management. |
| manualOrderIndicator | int | Following CME Rule 576, the ManualOrderIndicator field will signify if an order is manual (1) or automated (0). |
| manualOrderCancelTime | string | Used by brokers and advisors when manually entering an order cancellation request. Format should be “YYYYMMDD-HH:mm:ss” using UTC as the timezone value. |

| Name | Type | Description |
| --- | --- | --- |
| extOperator | string | Following CME Rule 576, the ExtOperator field will signify the unique API operator at the time of trading for order management. |
| manualOrderIndicator | int | Following CME Rule 576, the ManualOrderIndicator field will signify if an order is manual (1) or automated (0). |
| manualOrderCancelTime | string | Used by brokers and advisors when manually entering an order cancellation request. Format should be “YYYYMMDD-HH:mm:ss” using UTC as the timezone value. |
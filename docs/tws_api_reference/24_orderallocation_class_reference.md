---
title: "OrderAllocation Class Reference"
description: "TWS API Reference - OrderAllocation Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "orderallocation-ref"
order: 24
prev_section: "Order Class Reference"
next_section: "OrderCancel Class Reference"
prev_file: "23_order_class_reference.md"
next_file: "25_ordercancel_class_reference.md"
scraped_at: "2025-08-01T09:13:02.321873"
word_count: 373
paragraph_count: 7
subsection_count: 0
code_block_count: 0
format: "markdown"
---

# OrderAllocation Class Reference

## OrderAllocation Class Reference

The OrderAllocation class to denote an advisor’s allocations while trading subaccounts.

The OrderAllocation class to denote an advisor’s allocations while trading subaccounts.

NameTypeDescriptionAccountStringReferences the Account ID, i.e. U1234567, being allocated to.PositionDecimalReferences the current position of the account being allocated to.PositionDesiredDecimalStates the full position increase intended by the current trade.PosiionAfterDecimalReferences the increase to position from the current trade. Unless the order is partially filled, this should reflect the PositionDesired value.DesiredAllocQtyDecimalReference the quantity to increase by based on allocation.AllowedAllocQtyDecimalReferences the maximum allowed quantity increase.IsMonetaryBooleanDenotes whether the order is a monetary allocation (true) or whole share allocation (false).

| Name | Type | Description |
| --- | --- | --- |
| Account | String | References the Account ID, i.e. U1234567, being allocated to. |
| Position | Decimal | References the current position of the account being allocated to. |
| PositionDesired | Decimal | States the full position increase intended by the current trade. |
| PosiionAfter | Decimal | References the increase to position from the current trade. Unless the order is partially filled, this should reflect the PositionDesired value. |
| DesiredAllocQty | Decimal | Reference the quantity to increase by based on allocation. |
| AllowedAllocQty | Decimal | References the maximum allowed quantity increase. |
| IsMonetary | Boolean | Denotes whether the order is a monetary allocation (true) or whole share allocation (false). |

| Name | Type | Description |
| --- | --- | --- |
| Account | String | References the Account ID, i.e. U1234567, being allocated to. |
| Position | Decimal | References the current position of the account being allocated to. |
| PositionDesired | Decimal | States the full position increase intended by the current trade. |
| PosiionAfter | Decimal | References the increase to position from the current trade. Unless the order is partially filled, this should reflect the PositionDesired value. |
| DesiredAllocQty | Decimal | Reference the quantity to increase by based on allocation. |
| AllowedAllocQty | Decimal | References the maximum allowed quantity increase. |
| IsMonetary | Boolean | Denotes whether the order is a monetary allocation (true) or whole share allocation (false). |
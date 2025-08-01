---
title: "PriceCondition Class Reference"
description: "TWS API Reference - PriceCondition Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "pricecondition-ref"
order: 29
prev_section: "PercentChangeCondition Class Reference"
next_section: "ScannerSubscription Class Reference"
prev_file: "28_percentchangecondition_class_reference.md"
next_file: "30_scannersubscription_class_reference.md"
scraped_at: "2025-08-01T09:13:02.322226"
word_count: 337
paragraph_count: 15
subsection_count: 2
code_block_count: 0
format: "markdown"
---

# PriceCondition Class Reference

## PriceCondition Class Reference

Used with conditional orders to cancel or submit order based on price of an instrument.

Used with conditional orders to cancel or submit order based on price of an instrument.

NameTypeDescriptionValueoverride stringPricestringPrice field used in conditional order logic.TriggerMethodTriggerMethod

| Name | Type | Description |
| --- | --- | --- |
| Value | override string |  |
| Price | string | Price field used in conditional order logic. |
| TriggerMethod | TriggerMethod |  |

| Name | Type | Description |
| --- | --- | --- |
| Value | override string |  |
| Price | string | Price field used in conditional order logic. |
| TriggerMethod | TriggerMethod |  |

### Public Member Functions

NameTypeDescriptionToString()override stringReturns string to display.Equals (object obj)override boolGetHashCode ()override intDeserialize (IDecoder inStream)override voidSerialize (BinaryWriter outStream)override void

| Name | Type | Description |
| --- | --- | --- |
| ToString() | override string | Returns string to display. |
| Equals (object obj) | override bool |  |
| GetHashCode () | override int |  |
| Deserialize (IDecoder inStream) | override void |  |
| Serialize (BinaryWriter outStream) | override void |  |

| Name | Type | Description |
| --- | --- | --- |
| ToString() | override string | Returns string to display. |
| Equals (object obj) | override bool |  |
| GetHashCode () | override int |  |
| Deserialize (IDecoder inStream) | override void |  |
| Serialize (BinaryWriter outStream) | override void |  |

### Protected Member Functions

NameTypeDescriptionTryParse(string cond)override boolValidates the price condition format is valid.

| Name | Type | Description |
| --- | --- | --- |
| TryParse(string cond) | override bool | Validates the price condition format is valid. |

| Name | Type | Description |
| --- | --- | --- |
| TryParse(string cond) | override bool | Validates the price condition format is valid. |
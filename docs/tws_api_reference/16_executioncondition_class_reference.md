---
title: "ExecutionCondition Class Reference"
description: "TWS API Reference - ExecutionCondition Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "execcondition-ref"
order: 16
prev_section: "Execution Class Reference"
next_section: "ExecutionFilter Class Reference"
prev_file: "15_execution_class_reference.md"
next_file: "17_executionfilter_class_reference.md"
scraped_at: "2025-08-01T09:13:02.321105"
word_count: 420
paragraph_count: 17
subsection_count: 2
code_block_count: 0
format: "markdown"
---

# ExecutionCondition Class Reference

## ExecutionCondition Class Reference

This class represents a condition requiring a specific execution event to be fulfilled. Orders can be activated or canceled if a set of given conditions is met. An ExecutionCondition is met whenever a trade occurs on a certain product at the given exchange.

This class represents a condition requiring a specific execution event to be fulfilled. Orders can be activated or canceled if a set of given conditions is met. An ExecutionCondition is met whenever a trade occurs on a certain product at the given exchange.

NameTypeDescriptionExchangestringExchange where the symbol needs to be traded.SecTypestringKind of instrument being monitored.SymbolstringInstrument’s symbol.

| Name | Type | Description |
| --- | --- | --- |
| Exchange | string | Exchange where the symbol needs to be traded. |
| SecType | string | Kind of instrument being monitored. |
| Symbol | string | Instrument’s symbol. |

| Name | Type | Description |
| --- | --- | --- |
| Exchange | string | Exchange where the symbol needs to be traded. |
| SecType | string | Kind of instrument being monitored. |
| Symbol | string | Instrument’s symbol. |

Inheritance diagram for ExecutionCondition:

Inheritance diagram for ExecutionCondition:

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
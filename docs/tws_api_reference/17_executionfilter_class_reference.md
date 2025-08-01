---
title: "ExecutionFilter Class Reference"
description: "TWS API Reference - ExecutionFilter Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "execfilter-ref"
order: 17
prev_section: "ExecutionCondition Class Reference"
next_section: "HistoricalTick Class Reference"
prev_file: "16_executioncondition_class_reference.md"
next_file: "18_historicaltick_class_reference.md"
scraped_at: "2025-08-01T09:13:02.321167"
word_count: 396
paragraph_count: 11
subsection_count: 1
code_block_count: 0
format: "markdown"
---

# ExecutionFilter Class Reference

## ExecutionFilter Class Reference

When requesting executions, a filter can be specified to receive only a subset of them

When requesting executions, a filter can be specified to receive only a subset of them

NameTypeDescriptionClientIdintThe API client which placed the order.AcctCodestringThe account to which the order was allocated to.TimestringTime from which the executions will be returned yyyymmdd hh:mm:ss Only those executions reported after the specified time will be returned.SymbolstringThe instrument’s symbol.SecTypestringThe Contract’s security’s type (i.e. STKExchangestringThe exchange at which the execution was produced.SidestringThe Contract’s side (BUY or SELL)

| Name | Type | Description |
| --- | --- | --- |
| ClientId | int | The API client which placed the order. |
| AcctCode | string | The account to which the order was allocated to. |
| Time | string | Time from which the executions will be returned yyyymmdd hh:mm:ss Only those executions reported after the specified time will be returned. |
| Symbol | string | The instrument’s symbol. |
| SecType | string | The Contract’s security’s type (i.e. STK |
| Exchange | string | The exchange at which the execution was produced. |
| Side | string | The Contract’s side (BUY or SELL) |

| Name | Type | Description |
| --- | --- | --- |
| ClientId | int | The API client which placed the order. |
| AcctCode | string | The account to which the order was allocated to. |
| Time | string | Time from which the executions will be returned yyyymmdd hh:mm:ss Only those executions reported after the specified time will be returned. |
| Symbol | string | The instrument’s symbol. |
| SecType | string | The Contract’s security’s type (i.e. STK |
| Exchange | string | The exchange at which the execution was produced. |
| Side | string | The Contract’s side (BUY or SELL) |

### Public Member Functions

NameTypeDescriptionEquals (object obj)override boolGetHashCode ()override int

| Name | Type | Description |
| --- | --- | --- |
| Equals (object obj) | override bool |  |
| GetHashCode () | override int |  |

| Name | Type | Description |
| --- | --- | --- |
| Equals (object obj) | override bool |  |
| GetHashCode () | override int |  |
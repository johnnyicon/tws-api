---
title: "EReaderSignal Interface Reference"
description: "TWS API Reference - EReaderSignal Interface Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "ers-ref"
order: 13
prev_section: "EReader Class Reference"
next_section: "EWrapper Interface Reference"
prev_file: "12_ereader_class_reference.md"
next_file: "14_ewrapper_interface_reference.md"
scraped_at: "2025-08-01T09:13:02.320766"
word_count: 185
paragraph_count: 8
subsection_count: 1
code_block_count: 0
format: "markdown"
---

# EReaderSignal Interface Reference

## EReaderSignal Interface Reference

Notifies the thread reading information from the TWS whenever there are messages ready to be consumed. Not currently used in Python API.

Notifies the thread reading information from the TWS whenever there are messages ready to be consumed. Not currently used in Python API.

### Public Member Functions

NameTypeDescriptionissueSignal ()voidIssues a signal to the consuming thread when there are things to be consumed.waitForSignal ()voidMakes the consuming thread waiting until a signal is issued.

| Name | Type | Description |
| --- | --- | --- |
| issueSignal () | void | Issues a signal to the consuming thread when there are things to be consumed. |
| waitForSignal () | void | Makes the consuming thread waiting until a signal is issued. |

| Name | Type | Description |
| --- | --- | --- |
| issueSignal () | void | Issues a signal to the consuming thread when there are things to be consumed. |
| waitForSignal () | void | Makes the consuming thread waiting until a signal is issued. |
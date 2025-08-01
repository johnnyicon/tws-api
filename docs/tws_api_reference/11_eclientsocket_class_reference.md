---
title: "EClientSocket Class Reference"
description: "TWS API Reference - EClientSocket Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "ecs-ref"
order: 11
prev_section: "EClient Class Reference"
next_section: "EReader Class Reference"
prev_file: "10_eclient_class_reference.md"
next_file: "12_ereader_class_reference.md"
scraped_at: "2025-08-01T09:13:02.320608"
word_count: 387
paragraph_count: 14
subsection_count: 2
code_block_count: 0
format: "markdown"
---

# EClientSocket Class Reference

## EClientSocket Class Reference

TWS/Gateway client class This client class contains all the available methods to communicate with IB. Up to 32 clients can be connected to a single instance of the TWS/Gateway simultaneously. From herein, the TWS/Gateway will be referred to as the Host.

TWS/Gateway client class This client class contains all the available methods to communicate with IB. Up to 32 clients can be connected to a single instance of the TWS/Gateway simultaneously. From herein, the TWS/Gateway will be referred to as the Host.

Inheritance diagram for EClient:

Inheritance diagram for EClient:

### Public Member Functions

NameTypeDescriptionserverVersion (int versionvoid EClientMsgSink.string time)eConnect (string hostvoidint porteConnect (string hostvoidint portredirect (string host)voidRedirects connection to different host.eDisconnect (bool resetState=true)override voidCloses the socket connection and terminates its thread.

| Name | Type | Description |
| --- | --- | --- |
| serverVersion (int version | void EClientMsgSink. | string time) |
| eConnect (string host | void | int port |
| eConnect (string host | void | int port |
| redirect (string host) | void | Redirects connection to different host. |
| eDisconnect (bool resetState=true) | override void | Closes the socket connection and terminates its thread. |

| Name | Type | Description |
| --- | --- | --- |
| serverVersion (int version | void EClientMsgSink. | string time) |
| eConnect (string host | void | int port |
| eConnect (string host | void | int port |
| redirect (string host) | void | Redirects connection to different host. |
| eDisconnect (bool resetState=true) | override void | Closes the socket connection and terminates its thread. |

### Protected Member Functions

NameTypeDescriptioncreateClientStream (string hostvirtual Streamint port)prepareBuffer (BinaryWriter paramsList)override uintNoneCloseAndSend (BinaryWriter requestoverride voiduint lengthPos)

| Name | Type | Description |
| --- | --- | --- |
| createClientStream (string host | virtual Stream | int port) |
| prepareBuffer (BinaryWriter paramsList) | override uint | None |
| CloseAndSend (BinaryWriter request | override void | uint lengthPos) |

| Name | Type | Description |
| --- | --- | --- |
| createClientStream (string host | virtual Stream | int port) |
| prepareBuffer (BinaryWriter paramsList) | override uint | None |
| CloseAndSend (BinaryWriter request | override void | uint lengthPos) |
---
title: "Next Valid ID"
description: "TWS API Documentation - Next Valid ID"
source: "Interactive Brokers TWS API Documentation"
nav_id: "next-valid-id"
order: 24
prev_section: "News"
next_section: "Order Management"
prev_file: "23_news.md"
next_file: "25_order_management.md"
scraped_at: "2025-08-01T09:13:29.315023"
word_count: 434
paragraph_count: 21
subsection_count: 9
code_block_count: 2
format: "markdown"
---

# Next Valid ID

## Next Valid ID

The nextValidId event provides the next valid identifier needed to place an order. It is necessary to use an order ID with new orders which is greater than all previous order IDs used to place an order. While requests such as EClient.reqMktData will not increment the minimum request ID value, more than one market data request cannot use the same request ID at the same time.
The nextValidId value may be queried on each request. However, it is often recommended to make a request once at the beginning of the session, and then locally increment the value for each request.

The nextValidId event provides the next valid identifier needed to place an order. It is necessary to use an order ID with new orders which is greater than all previous order IDs used to place an order. While requests such as EClient.reqMktData will not increment the minimum request ID value, more than one market data request cannot use the same request ID at the same time.
The nextValidId value may be queried on each request. However, it is often recommended to make a request once at the beginning of the session, and then locally increment the value for each request.

### Request Next Valid ID

#### EClient.reqIds (

numIds:int. This parameter will not affect the value returned to nextValidId but is required.)
Requests the next valid order ID at the current moment be returned to the EWrapper.nextValidId function.

#### EClient.reqIds (

numIds:int. This parameter will not affect the value returned to nextValidId but is required.)
Requests the next valid order ID at the current moment be returned to the EWrapper.nextValidId function.

#### EClient.reqIds (

```python
self.reqIds(-1)
```

### Receive Next Valid ID

#### EWrapper.nextValidId (

orderId:int. Receives next valid order id.)
Will be invoked automatically upon successful API client connection, or after call to EClient.reqIds.

#### EWrapper.nextValidId (

orderId:int. Receives next valid order id.)
Will be invoked automatically upon successful API client connection, or after call to EClient.reqIds.

#### EWrapper.nextValidId (

```python
def nextValidId(self, orderId: int):
    print("NextValidId:", orderId)
```

### Reset Order ID Sequence

The next valid identifier is persistent between TWS sessions.
If necessary, you can reset the order ID sequence within the API Settings dialogue. Note however that the order sequence Id can only be reset if there are no active API orders.

The next valid identifier is persistent between TWS sessions.
If necessary, you can reset the order ID sequence within the API Settings dialogue. Note however that the order sequence Id can only be reset if there are no active API orders.
---
title: "TWS UI Display Groups"
description: "TWS API Documentation - TWS UI Display Groups"
source: "Interactive Brokers TWS API Documentation"
nav_id: "display-groups"
scraped_at: "2025-08-01T00:35:12.588238"
word_count: 1095
paragraph_count: 55
subsection_count: 9
code_block_count: 6
format: "markdown"
---

# TWS UI Display Groups

## TWS UI Display Groups

Display Groups function allows API clients to integrate withTWS Color Grouping Windows.
TWS Color Grouping Windows are identified by a colored chain in TWS and by an integer number via the API. Currently that number ranges from 1 to 7 and are mapped to specific colors, as indicated in TWS.

Display Groups function allows API clients to integrate withTWS Color Grouping Windows.
TWS Color Grouping Windows are identified by a colored chain in TWS and by an integer number via the API. Currently that number ranges from 1 to 7 and are mapped to specific colors, as indicated in TWS.

### Query Display Groups

The IBApi.EClient.queryDisplayGroups method is used to request all available Display Groups in TWS. The IBApi.EWrapper.displayGroupList is a one-time response to IBApi.EClient.queryDisplayGroups.
It returns a list of integers representing visible Group ID separated by the “|” character, and sorted by most used group first. This list will not change during TWS session. In other words, user cannot add a new group, but only the sorting of the group numbers can change.
Example: “4|1|2|5|3|6|7”

The IBApi.EClient.queryDisplayGroups method is used to request all available Display Groups in TWS. The IBApi.EWrapper.displayGroupList is a one-time response to IBApi.EClient.queryDisplayGroups.
It returns a list of integers representing visible Group ID separated by the “|” character, and sorted by most used group first. This list will not change during TWS session. In other words, user cannot add a new group, but only the sorting of the group numbers can change.
Example: “4|1|2|5|3|6|7”

### Request Query Display Groups

#### EClient.queryDisplayGroups (

requestId:int. Request identifier used to track data.)
Requests all available Display Groups in TWS.

#### EClient.queryDisplayGroups (

requestId:int. Request identifier used to track data.)
Requests all available Display Groups in TWS.

#### EClient.queryDisplayGroups (

```python
self.queryDisplayGroups(requestId)
```

### Receive Query Display Groups

#### EWrapper.displayGroupList (

requestId:Request identifier used to track data.
groups:String. Returns a list of integers representing visible Group ID separated by the “|” character, and sorted by most used group first.)
A one-time response to querying the display groups.

#### EWrapper.displayGroupList (

requestId:Request identifier used to track data.
groups:String. Returns a list of integers representing visible Group ID separated by the “|” character, and sorted by most used group first.)
A one-time response to querying the display groups.

#### EWrapper.displayGroupList (

```python
def displayGroupList(self, reqId: int, groups: str):
  print("DisplayGroupList. ReqId:", reqId, "Groups", groups)
```

### Subscribe To Group Events

To integrate with a specific Group, you need to first subscribe to the group number by invoking IBApi.EClient.subscribeToGroupEvents. The IBApi.EWrapper.displayGroupUpdated call back is triggered once after receiving the subscription request, and will be sent again if the selected contract in the subscribed display group has changed.

To integrate with a specific Group, you need to first subscribe to the group number by invoking IBApi.EClient.subscribeToGroupEvents. The IBApi.EWrapper.displayGroupUpdated call back is triggered once after receiving the subscription request, and will be sent again if the selected contract in the subscribed display group has changed.

### Request Group Events Subscription

#### EClient.subscribeToGroupEvents (

requestId:int. Request identifier used to track data.
groupId:int. The display group for integration.)
Integrates API client and TWS window grouping.

#### EClient.subscribeToGroupEvents (

requestId:int. Request identifier used to track data.
groupId:int. The display group for integration.)
Integrates API client and TWS window grouping.

#### EClient.subscribeToGroupEvents (

```python
self.subscribeToGroupEvents(19002, 1)
```

### Receive Group Events Subscription

#### EWrapper.displayGroupUpdated (

requestId:int. Request identifier used to track data.
contractInfo:String. Contract information produced for the active display group.
)Call triggered once after receiving the subscription request, and will be sent again if the selected contract in the subscribed * display group has changed.

#### EWrapper.displayGroupUpdated (

requestId:int. Request identifier used to track data.
contractInfo:String. Contract information produced for the active display group.
)Call triggered once after receiving the subscription request, and will be sent again if the selected contract in the subscribed * display group has changed.

#### EWrapper.displayGroupUpdated (

```python
def displayGroupUpdated(self, reqId: int, contractInfo: str):
	print("DisplayGroupUpdated. ReqId:", reqId, "ContractInfo:", contractInfo)
```

### Unsubscribe From Group Events

#### EClient.unsubscribeFromGroupEvents (

requestId:int. Request identifier used to track data.)
Cancels a TWS Window Group subscription.

#### EClient.unsubscribeFromGroupEvents (

requestId:int. Request identifier used to track data.)
Cancels a TWS Window Group subscription.

#### EClient.unsubscribeFromGroupEvents (

```python
self.unsubscribeFromGroupEvents(19002)
```

### Update Display Group

#### EClient.updateDisplayGroup (

requestId:int. Request identifier used for tracking data.
contractInfo:String. An encoded value designating a unique IB contract.Possible values include:
none: Empty selectioncontractID: Any non-combination contract. Examples 8314 for IBM SMART; 8314 for IBM ARCAcombo: If any combo is selected Note: This request from the API does not get a TWS response unless an error occurs.)
Updates the contract displayed in a TWS Window Group.

#### EClient.updateDisplayGroup (

requestId:int. Request identifier used for tracking data.
contractInfo:String. An encoded value designating a unique IB contract.Possible values include:
none: Empty selectioncontractID: Any non-combination contract. Examples 8314 for IBM SMART; 8314 for IBM ARCAcombo: If any combo is selected Note: This request from the API does not get a TWS response unless an error occurs.)
Updates the contract displayed in a TWS Window Group.

Note:This request from the API does not get a response from TWS unless an error occurs.
In this sample we have commanded TWS Windows that chained with Group #1 to display IBM@SMART. The screenshot of TWS Mosaic to the right shows that both the pink chained (Group #1) windows are now displaying IBM@SMART, while the green chained (Group #4) window remains unchanged.

Note:This request from the API does not get a response from TWS unless an error occurs.
In this sample we have commanded TWS Windows that chained with Group #1 to display IBM@SMART. The screenshot of TWS Mosaic to the right shows that both the pink chained (Group #1) windows are now displaying IBM@SMART, while the green chained (Group #4) window remains unchanged.

#### EClient.updateDisplayGroup (

Note:This request from the API does not get a response from TWS unless an error occurs.
In this sample we have commanded TWS Windows that chained with Group #1 to display IBM@SMART. The screenshot of TWS Mosaic to the right shows that both the pink chained (Group #1) windows are now displaying IBM@SMART, while the green chained (Group #4) window remains unchanged.

Note:This request from the API does not get a response from TWS unless an error occurs.
In this sample we have commanded TWS Windows that chained with Group #1 to display IBM@SMART. The screenshot of TWS Mosaic to the right shows that both the pink chained (Group #1) windows are now displaying IBM@SMART, while the green chained (Group #4) window remains unchanged.

```python
self.updateDisplayGroup(19002, "8314@SMART")
```
---
title: "ComboLeg Class Reference"
description: "TWS API Reference - ComboLeg Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "comboleg-ref"
order: 4
prev_section: "Bar Class Reference"
next_section: "CommissionAndFeesReport Class Reference"
prev_file: "03_bar_class_reference.md"
next_file: "05_commissionandfeesreport_class_reference.md"
scraped_at: "2025-08-01T09:13:02.319432"
word_count: 1081
paragraph_count: 15
subsection_count: 1
code_block_count: 0
format: "markdown"
---

# ComboLeg Class Reference

## ComboLeg Class Reference

Class representing a leg within combo orders.

Class representing a leg within combo orders.

NameTypeDescriptionConIdintThe Contract’s IB’s unique id.RatiointSelect the relative number of contracts for the leg you are constructing. To help determine the ratio for a specific combination orderActionstringThe side (buy or sell) of the leg:For individual accounts, only BUY and SELL are available. SSHORT is for institutions.ExchangestringThe destination exchange to which the order will be routed.OpenCloseintSpecifies whether an order is an open or closing order. For institutional customers to determine if this order is to open or close a position. 0 – Same as the parent security. This is the only option for retail customers.1 – Open. This value is only valid for institutional customers.2 – Close. This value is only valid for institutional customers.3 – Unknown.ShortSaleSlotintFor stock legs when doing short selling.Set to 1 = clearing broker, 2 = third partyDesignatedLocationstringWhen ShortSaleSlot is 2, this field shall contain the designated location.ExemptCodeintMark order as exempt from short sale uptick rule.Possible values:0 – Does not apply the rule.-1 – Applies the short sale uptick rule.

| Name | Type | Description |
| --- | --- | --- |
| ConId | int | The Contract’s IB’s unique id. |
| Ratio | int | Select the relative number of contracts for the leg you are constructing. To help determine the ratio for a specific combination order |
| Action | string | The side (buy or sell) of the leg: For individual accounts, only BUY and SELL are available. SSHORT is for institutions. |
| Exchange | string | The destination exchange to which the order will be routed. |
| OpenClose | int | Specifies whether an order is an open or closing order. For institutional customers to determine if this order is to open or close a position. 0 – Same as the parent security. This is the only option for retail customers. 1 – Open. This value is only valid for institutional customers. 2 – Close. This value is only valid for institutional customers. 3 – Unknown. |
| ShortSaleSlot | int | For stock legs when doing short selling.Set to 1 = clearing broker, 2 = third party |
| DesignatedLocation | string | When ShortSaleSlot is 2, this field shall contain the designated location. |
| ExemptCode | int | Mark order as exempt from short sale uptick rule. Possible values: 0 – Does not apply the rule. -1 – Applies the short sale uptick rule. |

Set to 1 = clearing broker, 2 = third party
Set to 1 = clearing broker, 2 = third party
When ShortSaleSlot is 2, this field shall contain the designated location.
When ShortSaleSlot is 2, this field shall contain the designated location.

| Name | Type | Description |
| --- | --- | --- |
| ConId | int | The Contract’s IB’s unique id. |
| Ratio | int | Select the relative number of contracts for the leg you are constructing. To help determine the ratio for a specific combination order |
| Action | string | The side (buy or sell) of the leg: For individual accounts, only BUY and SELL are available. SSHORT is for institutions. |
| Exchange | string | The destination exchange to which the order will be routed. |
| OpenClose | int | Specifies whether an order is an open or closing order. For institutional customers to determine if this order is to open or close a position. 0 – Same as the parent security. This is the only option for retail customers. 1 – Open. This value is only valid for institutional customers. 2 – Close. This value is only valid for institutional customers. 3 – Unknown. |
| ShortSaleSlot | int | For stock legs when doing short selling.Set to 1 = clearing broker, 2 = third party |
| DesignatedLocation | string | When ShortSaleSlot is 2, this field shall contain the designated location. |
| ExemptCode | int | Mark order as exempt from short sale uptick rule. Possible values: 0 – Does not apply the rule. -1 – Applies the short sale uptick rule. |

Set to 1 = clearing broker, 2 = third party
Set to 1 = clearing broker, 2 = third party
When ShortSaleSlot is 2, this field shall contain the designated location.
When ShortSaleSlot is 2, this field shall contain the designated location.

### Public Member Functions

NameTypeDescriptionSAME = 0static intSame as the parent security. This is the only option for retail customers.OPEN = 1static intOpen. This value is only valid for institutional customers.CLOSE = 2static intClose. This value is only valid for institutional customers.UNKNOWN = 3static intUnknown

| Name | Type | Description |
| --- | --- | --- |
| SAME = 0 | static int | Same as the parent security. This is the only option for retail customers. |
| OPEN = 1 | static int | Open. This value is only valid for institutional customers. |
| CLOSE = 2 | static int | Close. This value is only valid for institutional customers. |
| UNKNOWN = 3 | static int | Unknown |

Same as the parent security. This is the only option for retail customers.
Same as the parent security. This is the only option for retail customers.
Open. This value is only valid for institutional customers.
Open. This value is only valid for institutional customers.
Close. This value is only valid for institutional customers.
Close. This value is only valid for institutional customers.
Unknown
Unknown

| Name | Type | Description |
| --- | --- | --- |
| SAME = 0 | static int | Same as the parent security. This is the only option for retail customers. |
| OPEN = 1 | static int | Open. This value is only valid for institutional customers. |
| CLOSE = 2 | static int | Close. This value is only valid for institutional customers. |
| UNKNOWN = 3 | static int | Unknown |

Same as the parent security. This is the only option for retail customers.
Same as the parent security. This is the only option for retail customers.
Open. This value is only valid for institutional customers.
Open. This value is only valid for institutional customers.
Close. This value is only valid for institutional customers.
Close. This value is only valid for institutional customers.
Unknown
Unknown
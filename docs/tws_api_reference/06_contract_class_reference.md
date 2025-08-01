---
title: "Contract Class Reference"
description: "TWS API Reference - Contract Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "contract-ref"
order: 6
prev_section: "CommissionAndFeesReport Class Reference"
next_section: "ContractDetails Class Reference"
prev_file: "05_commissionandfeesreport_class_reference.md"
next_file: "07_contractdetails_class_reference.md"
scraped_at: "2025-08-01T09:13:02.319823"
word_count: 1260
paragraph_count: 13
subsection_count: 1
code_block_count: 0
format: "markdown"
---

# Contract Class Reference

## Contract Class Reference

Class describing an instrument’s definition.

Class describing an instrument’s definition.

NameTypeDescriptionConIdintThe unique IB contract identifier.SymbolstringThe underlying’s asset symbol.SecTypestringThe security’s type: STK – stock (or ETF) OPT – option FUT – future IND – index FOP – futures option CASH – forex pair BAG – combo WAR – warrant BOND- bond CMDTY- commodity NEWS- news FUND- mutual fund.LastTradeDateOrContractMonthstringThe contract’s last trading day or contract month (for Options and Futures). Strings with format YYYYMM will be interpreted as the Contract Month whereas YYYYMMDD will be interpreted as Last Trading Day.LastTradeDatestringThe contract’s last trading day.StrikedoubleThe option’s strike price.RightstringEither Put or Call (i.e. Options). Valid values are P, PUT, C, CALL.MultiplierstringThe instrument’s multiplier (i.e. options, futures).ExchangestringThe destination exchange.CurrencystringThe underlying’s currency.LocalSymbolstringThe contract’s symbol within its primary exchange. For options, this will be the OCC symbolPrimaryExchstringThe contract’s primary exchange. For smart routed contracts, used to define contract in case of ambiguity.Should be defined as native exchange of contract. For exchanges which contain a period in name, will only be part of exchange name prior to period, i.e. ENEXT for ENEXT.BETradingClassstringThe trading class name for this contract. Available in TWS contract description window as well. For example, GBL Dec ’13 future’s trading class is “FGBL”IncludeExpiredboolIf set to true, contract details requests and historical data queries can be performed pertaining to expired futures contracts. Expired options or other instrument types are not available.SecIdTypestringSecurity’s identifier when querying contract’s details or placing orders ISIN – Example: Apple: US0378331005 CUSIP – Example: Apple: 037833100.SecIdstringIdentifier of the security type. More…DescriptionstringDescription of the contract.IssuerIdstringIssuerId of the contract.ComboLegsDescriptionstringDescription of the combo legs.ComboLegsListThe legs of a combined contract definition. More…DeltaNeutralContractDeltaNeutralContractDelta and underlying price for Delta-Neutral combo orders. Underlying (STK or FUT)

| Name | Type | Description |
| --- | --- | --- |
| ConId | int | The unique IB contract identifier. |
| Symbol | string | The underlying’s asset symbol. |
| SecType | string | The security’s type: STK – stock (or ETF) OPT – option FUT – future IND – index FOP – futures option CASH – forex pair BAG – combo WAR – warrant BOND- bond CMDTY- commodity NEWS- news FUND- mutual fund. |
| LastTradeDateOrContractMonth | string | The contract’s last trading day or contract month (for Options and Futures). Strings with format YYYYMM will be interpreted as the Contract Month whereas YYYYMMDD will be interpreted as Last Trading Day. |
| LastTradeDate | string | The contract’s last trading day. |
| Strike | double | The option’s strike price. |
| Right | string | Either Put or Call (i.e. Options). Valid values are P, PUT, C, CALL. |
| Multiplier | string | The instrument’s multiplier (i.e. options, futures). |
| Exchange | string | The destination exchange. |
| Currency | string | The underlying’s currency. |
| LocalSymbol | string | The contract’s symbol within its primary exchange. For options, this will be the OCC symbol |
| PrimaryExch | string | The contract’s primary exchange. For smart routed contracts, used to define contract in case of ambiguity.Should be defined as native exchange of contract. For exchanges which contain a period in name, will only be part of exchange name prior to period, i.e. ENEXT for ENEXT.BE |
| TradingClass | string | The trading class name for this contract. Available in TWS contract description window as well. For example, GBL Dec ’13 future’s trading class is “FGBL” |
| IncludeExpired | bool | If set to true, contract details requests and historical data queries can be performed pertaining to expired futures contracts. Expired options or other instrument types are not available. |
| SecIdType | string | Security’s identifier when querying contract’s details or placing orders ISIN – Example: Apple: US0378331005 CUSIP – Example: Apple: 037833100. |
| SecId | string | Identifier of the security type. More… |
| Description | string | Description of the contract. |
| IssuerId | string | IssuerId of the contract. |
| ComboLegsDescription | string | Description of the combo legs. |
| ComboLegs | List | The legs of a combined contract definition. More… |
| DeltaNeutralContract | DeltaNeutralContract | Delta and underlying price for Delta-Neutral combo orders. Underlying (STK or FUT) |

Either Put or Call (i.e. Options). Valid values are P, PUT, C, CALL.
Either Put or Call (i.e. Options). Valid values are P, PUT, C, CALL.
The instrument’s multiplier (i.e. options, futures).
The instrument’s multiplier (i.e. options, futures).

| Name | Type | Description |
| --- | --- | --- |
| ConId | int | The unique IB contract identifier. |
| Symbol | string | The underlying’s asset symbol. |
| SecType | string | The security’s type: STK – stock (or ETF) OPT – option FUT – future IND – index FOP – futures option CASH – forex pair BAG – combo WAR – warrant BOND- bond CMDTY- commodity NEWS- news FUND- mutual fund. |
| LastTradeDateOrContractMonth | string | The contract’s last trading day or contract month (for Options and Futures). Strings with format YYYYMM will be interpreted as the Contract Month whereas YYYYMMDD will be interpreted as Last Trading Day. |
| LastTradeDate | string | The contract’s last trading day. |
| Strike | double | The option’s strike price. |
| Right | string | Either Put or Call (i.e. Options). Valid values are P, PUT, C, CALL. |
| Multiplier | string | The instrument’s multiplier (i.e. options, futures). |
| Exchange | string | The destination exchange. |
| Currency | string | The underlying’s currency. |
| LocalSymbol | string | The contract’s symbol within its primary exchange. For options, this will be the OCC symbol |
| PrimaryExch | string | The contract’s primary exchange. For smart routed contracts, used to define contract in case of ambiguity.Should be defined as native exchange of contract. For exchanges which contain a period in name, will only be part of exchange name prior to period, i.e. ENEXT for ENEXT.BE |
| TradingClass | string | The trading class name for this contract. Available in TWS contract description window as well. For example, GBL Dec ’13 future’s trading class is “FGBL” |
| IncludeExpired | bool | If set to true, contract details requests and historical data queries can be performed pertaining to expired futures contracts. Expired options or other instrument types are not available. |
| SecIdType | string | Security’s identifier when querying contract’s details or placing orders ISIN – Example: Apple: US0378331005 CUSIP – Example: Apple: 037833100. |
| SecId | string | Identifier of the security type. More… |
| Description | string | Description of the contract. |
| IssuerId | string | IssuerId of the contract. |
| ComboLegsDescription | string | Description of the combo legs. |
| ComboLegs | List | The legs of a combined contract definition. More… |
| DeltaNeutralContract | DeltaNeutralContract | Delta and underlying price for Delta-Neutral combo orders. Underlying (STK or FUT) |

Either Put or Call (i.e. Options). Valid values are P, PUT, C, CALL.
Either Put or Call (i.e. Options). Valid values are P, PUT, C, CALL.
The instrument’s multiplier (i.e. options, futures).
The instrument’s multiplier (i.e. options, futures).

### Public Member Functions

NameTypeDescriptionToString()override string

| Name | Type | Description |
| --- | --- | --- |
| ToString() | override string |  |

| Name | Type | Description |
| --- | --- | --- |
| ToString() | override string |  |
---
title: "AccountSummaryTags Class"
description: "TWS API Reference - AccountSummaryTags Class"
source: "Interactive Brokers TWS API Documentation"
nav_id: "acctsumtags-ref"
order: 2
prev_section: "Introduction"
next_section: "Bar Class Reference"
prev_file: "01_introduction.md"
next_file: "03_bar_class_reference.md"
scraped_at: "2025-08-01T09:13:02.318536"
word_count: 1210
paragraph_count: 14
subsection_count: 1
code_block_count: 0
format: "markdown"
---

# AccountSummaryTags Class

## AccountSummaryTags Class

Class containing all existing values being reported by EClientSocket::reqAccountSummary.

Class containing all existing values being reported by EClientSocket::reqAccountSummary.

Public Attributes

| Name | Type | Description |
| --- | --- | --- |
| AccountType = “AccountType” | string |  |
| NetLiquidation = “NetLiquidation” | string |  |
| TotalCashValue = “TotalCashValue” | string | Total cash including futures pnl |
| SettledCash = “SettledCash” | string | For cash accounts, this is the same as TotalCashValue |
| AccruedCash = “AccruedCash” | string | Net accrued interest |
| BuyingPower = “BuyingPower” | string | The maximum amount of marginable US stocks the account can buy |
| EquityWithLoanValue = “EquityWithLoanValue” | string | Cash + stocks + bonds + mutual funds |
| PreviousDayEquityWithLoanValue = “PreviousDayEquityWithLoanValue” | string |  |
| GrossPositionValue = “GrossPositionValue” | string | The sum of the absolute value of all stock and equity option positions |
| ReqTEquity = “ReqTEquity” | string |  |
| ReqTMargin = “ReqTMargin” | string |  |
| SMA = “SMA” | string | Special Memorandum Account |
| InitMarginReq = “InitMarginReq” | string |  |
| MaintMarginReq = “MaintMarginReq” | string |  |
| AvailableFunds = “AvailableFunds” | string |  |
| ExcessLiquidity = “ExcessLiquidity” | string |  |
| Cushion = “Cushion” | string | Excess liquidity as a percentage of net liquidation value |
| FullInitMarginReq = “FullInitMarginReq” | string |  |
| FullMaintMarginReq = “FullMaintMarginReq” | string |  |
| FullAvailableFunds = “FullAvailableFunds” | string |  |
| FullExcessLiquidity = “FullExcessLiquidity” | string |  |
| LookAheadNextChange = “LookAheadNextChange” | string | Time when look-ahead values take effect |
| LookAheadInitMarginReq = “LookAheadInitMarginReq” | string |  |
| LookAheadMaintMarginReq = “LookAheadMaintMarginReq” | string |  |
| LookAheadAvailableFunds = “LookAheadAvailableFunds” | string |  |
| LookAheadExcessLiquidity = “LookAheadExcessLiquidity” | string |  |
| HighestSeverity = “HighestSeverity” | string | A measure of how close the account is to liquidation |
| DayTradesRemaining = “DayTradesRemaining” | string | The Number of Open/Close trades one could do before Pattern Day Trading is detected; a value of “-1” means user can do unlimited day trades. |
| Leverage = “Leverage” | string | GrossPositionValue / NetLiquidation |

Total cash including futures pnl
Total cash including futures pnl
For cash accounts, this is the same as TotalCashValue
For cash accounts, this is the same as TotalCashValue
Net accrued interest
Net accrued interest
The maximum amount of marginable US stocks the account can buy
The maximum amount of marginable US stocks the account can buy
Cash + stocks + bonds + mutual funds
Cash + stocks + bonds + mutual funds
The sum of the absolute value of all stock and equity option positions
The sum of the absolute value of all stock and equity option positions
Special Memorandum Account
Special Memorandum Account
Excess liquidity as a percentage of net liquidation value
Excess liquidity as a percentage of net liquidation value
Time when look-ahead values take effect
Time when look-ahead values take effect
A measure of how close the account is to liquidation
A measure of how close the account is to liquidation
The Number of Open/Close trades one could do before Pattern Day Trading is detected; a value of “-1” means user can do unlimited day trades.
The Number of Open/Close trades one could do before Pattern Day Trading is detected; a value of “-1” means user can do unlimited day trades.
GrossPositionValue / NetLiquidation
GrossPositionValue / NetLiquidation

Public Attributes

| Name | Type | Description |
| --- | --- | --- |
| AccountType = “AccountType” | string |  |
| NetLiquidation = “NetLiquidation” | string |  |
| TotalCashValue = “TotalCashValue” | string | Total cash including futures pnl |
| SettledCash = “SettledCash” | string | For cash accounts, this is the same as TotalCashValue |
| AccruedCash = “AccruedCash” | string | Net accrued interest |
| BuyingPower = “BuyingPower” | string | The maximum amount of marginable US stocks the account can buy |
| EquityWithLoanValue = “EquityWithLoanValue” | string | Cash + stocks + bonds + mutual funds |
| PreviousDayEquityWithLoanValue = “PreviousDayEquityWithLoanValue” | string |  |
| GrossPositionValue = “GrossPositionValue” | string | The sum of the absolute value of all stock and equity option positions |
| ReqTEquity = “ReqTEquity” | string |  |
| ReqTMargin = “ReqTMargin” | string |  |
| SMA = “SMA” | string | Special Memorandum Account |
| InitMarginReq = “InitMarginReq” | string |  |
| MaintMarginReq = “MaintMarginReq” | string |  |
| AvailableFunds = “AvailableFunds” | string |  |
| ExcessLiquidity = “ExcessLiquidity” | string |  |
| Cushion = “Cushion” | string | Excess liquidity as a percentage of net liquidation value |
| FullInitMarginReq = “FullInitMarginReq” | string |  |
| FullMaintMarginReq = “FullMaintMarginReq” | string |  |
| FullAvailableFunds = “FullAvailableFunds” | string |  |
| FullExcessLiquidity = “FullExcessLiquidity” | string |  |
| LookAheadNextChange = “LookAheadNextChange” | string | Time when look-ahead values take effect |
| LookAheadInitMarginReq = “LookAheadInitMarginReq” | string |  |
| LookAheadMaintMarginReq = “LookAheadMaintMarginReq” | string |  |
| LookAheadAvailableFunds = “LookAheadAvailableFunds” | string |  |
| LookAheadExcessLiquidity = “LookAheadExcessLiquidity” | string |  |
| HighestSeverity = “HighestSeverity” | string | A measure of how close the account is to liquidation |
| DayTradesRemaining = “DayTradesRemaining” | string | The Number of Open/Close trades one could do before Pattern Day Trading is detected; a value of “-1” means user can do unlimited day trades. |
| Leverage = “Leverage” | string | GrossPositionValue / NetLiquidation |

Total cash including futures pnl
Total cash including futures pnl
For cash accounts, this is the same as TotalCashValue
For cash accounts, this is the same as TotalCashValue
Net accrued interest
Net accrued interest
The maximum amount of marginable US stocks the account can buy
The maximum amount of marginable US stocks the account can buy
Cash + stocks + bonds + mutual funds
Cash + stocks + bonds + mutual funds
The sum of the absolute value of all stock and equity option positions
The sum of the absolute value of all stock and equity option positions
Special Memorandum Account
Special Memorandum Account
Excess liquidity as a percentage of net liquidation value
Excess liquidity as a percentage of net liquidation value
Time when look-ahead values take effect
Time when look-ahead values take effect
A measure of how close the account is to liquidation
A measure of how close the account is to liquidation
The Number of Open/Close trades one could do before Pattern Day Trading is detected; a value of “-1” means user can do unlimited day trades.
The Number of Open/Close trades one could do before Pattern Day Trading is detected; a value of “-1” means user can do unlimited day trades.
GrossPositionValue / NetLiquidation
GrossPositionValue / NetLiquidation

### Static Public Member Functions

NameTypeDescriptionGetAllTags ()static stringReturns All Tags

| Name | Type | Description |
| --- | --- | --- |
| GetAllTags () | static string | Returns All Tags |

| Name | Type | Description |
| --- | --- | --- |
| GetAllTags () | static string | Returns All Tags |
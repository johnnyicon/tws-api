---
title: "OrderState Class Reference"
description: "TWS API Reference - OrderState Class Reference"
source: "Interactive Brokers TWS API Documentation"
nav_id: "orderstate-ref"
order: 27
prev_section: "OrderComboLeg Class Reference"
next_section: "PercentChangeCondition Class Reference"
prev_file: "26_ordercomboleg_class_reference.md"
next_file: "28_percentchangecondition_class_reference.md"
scraped_at: "2025-08-01T09:13:02.322043"
word_count: 1174
paragraph_count: 11
subsection_count: 1
code_block_count: 0
format: "markdown"
---

# OrderState Class Reference

## OrderState Class Reference

Provides an active order’s current state.

Provides an active order’s current state.

NameTypeDescriptionStatusstringThe order’s current status.InitMarginBeforestringThe account’s current initial margin.MaintMarginBeforestringThe account’s current maintenance margin.EquityWithLoanBeforestringThe account’s current equity with loan.InitMarginChangestringThe change of the account’s initial margin.MaintMarginChangestringThe change of the account’s maintenance margin.EquityWithLoanChangestringThe change of the account’s equity with loan.InitMarginAfterstringThe order’s impact on the account’s initial margin.MaintMarginAfterstringThe order’s impact on the account’s maintenance margin.EquityWithLoanAfterstringShows the impact the order would have on the account’s equity with loan.InitMarginBeforeOutsideRTHfloatThe account’s expected initial margin outside of regular trading hours.MaintMarginBeforeOutsideRTHfloatThe account’s expected maintenance margin outside of regular trading hours.EquityWithLoanBeforeOutsideRTHfloatThe account’s expected equity with loan outside of regular trading hours.InitMarginChangeOutsideRTHfloatThe expected change of the account’s initial margin outside of regular trading hours.MaintMarginChangeOutsideRTHfloatThe expected change of the account’s maintenance margin outside of regular trading hours.EquityWithLoanChangeOutsideRTHfloatThe expected change of the account’s equity with loan outside of regular trading hours.InitMarginAfterOutsideRTHfloatThe order’s expected impact on the account’s initial margin outside of regular trading hours.MaintMarginAfterOutsideRTHfloatThe order’s expected impact on the account’s maintenance margin outside of regular trading hours.EquityWithLoanAfterOutsideRTHfloatShows the expected impact the order would have on the account’s equity with loan outside of regular trading hours.CommissiondoubleThe order’s generated commission.MinCommissiondoubleThe execution’s minimum commission.MaxCommissiondoubleThe executions maximum commission.CommissionCurrencystringThe generated commission currency.WarningTextstringIf the order is warranted, a descriptive message will be provided.CompletedTimestringCompletedStatusstring

| Name | Type | Description |
| --- | --- | --- |
| Status | string | The order’s current status. |
| InitMarginBefore | string | The account’s current initial margin. |
| MaintMarginBefore | string | The account’s current maintenance margin. |
| EquityWithLoanBefore | string | The account’s current equity with loan. |
| InitMarginChange | string | The change of the account’s initial margin. |
| MaintMarginChange | string | The change of the account’s maintenance margin. |
| EquityWithLoanChange | string | The change of the account’s equity with loan. |
| InitMarginAfter | string | The order’s impact on the account’s initial margin. |
| MaintMarginAfter | string | The order’s impact on the account’s maintenance margin. |
| EquityWithLoanAfter | string | Shows the impact the order would have on the account’s equity with loan. |
| InitMarginBeforeOutsideRTH | float | The account’s expected initial margin outside of regular trading hours. |
| MaintMarginBeforeOutsideRTH | float | The account’s expected maintenance margin outside of regular trading hours. |
| EquityWithLoanBeforeOutsideRTH | float | The account’s expected equity with loan outside of regular trading hours. |
| InitMarginChangeOutsideRTH | float | The expected change of the account’s initial margin outside of regular trading hours. |
| MaintMarginChangeOutsideRTH | float | The expected change of the account’s maintenance margin outside of regular trading hours. |
| EquityWithLoanChangeOutsideRTH | float | The expected change of the account’s equity with loan outside of regular trading hours. |
| InitMarginAfterOutsideRTH | float | The order’s expected impact on the account’s initial margin outside of regular trading hours. |
| MaintMarginAfterOutsideRTH | float | The order’s expected impact on the account’s maintenance margin outside of regular trading hours. |
| EquityWithLoanAfterOutsideRTH | float | Shows the expected impact the order would have on the account’s equity with loan outside of regular trading hours. |
| Commission | double | The order’s generated commission. |
| MinCommission | double | The execution’s minimum commission. |
| MaxCommission | double | The executions maximum commission. |
| CommissionCurrency | string | The generated commission currency. |
| WarningText | string | If the order is warranted, a descriptive message will be provided. |
| CompletedTime | string |  |
| CompletedStatus | string |  |

| Name | Type | Description |
| --- | --- | --- |
| Status | string | The order’s current status. |
| InitMarginBefore | string | The account’s current initial margin. |
| MaintMarginBefore | string | The account’s current maintenance margin. |
| EquityWithLoanBefore | string | The account’s current equity with loan. |
| InitMarginChange | string | The change of the account’s initial margin. |
| MaintMarginChange | string | The change of the account’s maintenance margin. |
| EquityWithLoanChange | string | The change of the account’s equity with loan. |
| InitMarginAfter | string | The order’s impact on the account’s initial margin. |
| MaintMarginAfter | string | The order’s impact on the account’s maintenance margin. |
| EquityWithLoanAfter | string | Shows the impact the order would have on the account’s equity with loan. |
| InitMarginBeforeOutsideRTH | float | The account’s expected initial margin outside of regular trading hours. |
| MaintMarginBeforeOutsideRTH | float | The account’s expected maintenance margin outside of regular trading hours. |
| EquityWithLoanBeforeOutsideRTH | float | The account’s expected equity with loan outside of regular trading hours. |
| InitMarginChangeOutsideRTH | float | The expected change of the account’s initial margin outside of regular trading hours. |
| MaintMarginChangeOutsideRTH | float | The expected change of the account’s maintenance margin outside of regular trading hours. |
| EquityWithLoanChangeOutsideRTH | float | The expected change of the account’s equity with loan outside of regular trading hours. |
| InitMarginAfterOutsideRTH | float | The order’s expected impact on the account’s initial margin outside of regular trading hours. |
| MaintMarginAfterOutsideRTH | float | The order’s expected impact on the account’s maintenance margin outside of regular trading hours. |
| EquityWithLoanAfterOutsideRTH | float | Shows the expected impact the order would have on the account’s equity with loan outside of regular trading hours. |
| Commission | double | The order’s generated commission. |
| MinCommission | double | The execution’s minimum commission. |
| MaxCommission | double | The executions maximum commission. |
| CommissionCurrency | string | The generated commission currency. |
| WarningText | string | If the order is warranted, a descriptive message will be provided. |
| CompletedTime | string |  |
| CompletedStatus | string |  |

### Public Member Functions

NameTypeDescriptionOrderState (string status, string initMarginBefore, string maintMarginBefore, string equityWithLoanBefore, string initMarginChange, string maintMarginChange, string equityWithLoanChange, string initMarginAfter, string maintMarginAfter, string equityWithLoanAfter, double commission, double minCommission, double maxCommission, string commissionCurrency, string warningText, string completedTime, string completedStatus)override boolEquals (object obj)override boolGetHashCode ()override int

| Name | Type | Description |
| --- | --- | --- |
| OrderState (string status, string initMarginBefore, string maintMarginBefore, string equityWithLoanBefore, string initMarginChange, string maintMarginChange, string equityWithLoanChange, string initMarginAfter, string maintMarginAfter, string equityWithLoanAfter, double commission, double minCommission, double maxCommission, string commissionCurrency, string warningText, string completedTime, string completedStatus) | override bool |  |
| Equals (object obj) | override bool |  |
| GetHashCode () | override int |  |

| Name | Type | Description |
| --- | --- | --- |
| OrderState (string status, string initMarginBefore, string maintMarginBefore, string equityWithLoanBefore, string initMarginChange, string maintMarginChange, string equityWithLoanChange, string initMarginAfter, string maintMarginAfter, string equityWithLoanAfter, double commission, double minCommission, double maxCommission, string commissionCurrency, string warningText, string completedTime, string completedStatus) | override bool |  |
| Equals (object obj) | override bool |  |
| GetHashCode () | override int |  |
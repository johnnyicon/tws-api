---
title: "TWS Settings"
description: "TWS API Documentation - TWS Settings"
source: "Interactive Brokers TWS API Documentation"
nav_id: "tws-settings"
order: 4
prev_section: "Download TWS or IB Gateway"
next_section: "Download the TWS API"
prev_file: "03_download_tws_or_ib_gateway.md"
next_file: "05_download_the_tws_api.md"
scraped_at: "2025-08-01T09:13:29.310867"
word_count: 2364
paragraph_count: 39
subsection_count: 13
code_block_count: 0
format: "markdown"
---

# TWS Settings

## TWS Settings

Some TWS Settings affect API.

Some TWS Settings affect API.

### TWS Configuration For API Use

The settings required to use the TWS API with the Trader Workstation are managed in the Global Configuration under “API” -> “Settings”
In this section, only the most important API settings for API connection are covered.
Please:
Enable “ActiveX and Socket Clients”Disable “Read-Only API”Verify the “Socket Port” value

The settings required to use the TWS API with the Trader Workstation are managed in the Global Configuration under “API” -> “Settings”
In this section, only the most important API settings for API connection are covered.
Please:
Enable “ActiveX and Socket Clients”Disable “Read-Only API”Verify the “Socket Port” value

### Best Practice: Configure TWS / IB Gateway

The information listed below are not required or necessary in order to operate the TWS API. However, these steps include many references which can help improve the day to day usage of the TWS API that is not explicitly offered as a callable method within the API itself.

The information listed below are not required or necessary in order to operate the TWS API. However, these steps include many references which can help improve the day to day usage of the TWS API that is not explicitly offered as a callable method within the API itself.

### "Never Lock Trader Workstation" Setting

Note: For IBHK API users, it is commended to use IB Gateway instead of TWS. It is because all IBHK users cannot choose “Never Lock Trader Workstation” in TWS – Global Configuration – Lock and Exit. If there is inactivity, TWS will be locked and there will be API disconnection.

Note: For IBHK API users, it is commended to use IB Gateway instead of TWS. It is because all IBHK users cannot choose “Never Lock Trader Workstation” in TWS – Global Configuration – Lock and Exit. If there is inactivity, TWS will be locked and there will be API disconnection.

### Memory Allocation

In TWS/ IB Gateway – “Global Configuration” – “General”, you can adjust theMemory Allocation (in MB)*.
This feature is to control how much memory your computer can assign to the TWS/ IB Gateway application. Usually, higher value allows users to have faster data returning speed.
Normally, it is recommended for API users to set 4000. However, it depends on your computer memory size because setting too high may cause High Memory Usage and application not responding.
For details, please visit:https://www.ibkrguides.com/traderworkstation/increase-tws-memory-size.htm
In IB Gateway Global Configuration – API – settings, there is no “Compatibility Mode: Send ISLAND for US stocks trading on NASDAQ”. Specifying NASDAQ exchange in contract details may cause error if connecting to IB Gateway. For this error, please specify ISLAND exchange.

In TWS/ IB Gateway – “Global Configuration” – “General”, you can adjust theMemory Allocation (in MB)*.
This feature is to control how much memory your computer can assign to the TWS/ IB Gateway application. Usually, higher value allows users to have faster data returning speed.
Normally, it is recommended for API users to set 4000. However, it depends on your computer memory size because setting too high may cause High Memory Usage and application not responding.
For details, please visit:https://www.ibkrguides.com/traderworkstation/increase-tws-memory-size.htm
In IB Gateway Global Configuration – API – settings, there is no “Compatibility Mode: Send ISLAND for US stocks trading on NASDAQ”. Specifying NASDAQ exchange in contract details may cause error if connecting to IB Gateway. For this error, please specify ISLAND exchange.

### Daily & Weekly Reauthentication

In TWS/ IB Gateway – “Global Configuration” – “Lock and Exit”, you can choose the time of your TWS being shut down.
For API users, it is recommended to choose “Never lock Trader Workstation” and “Auto restart”.
IBHK users do not have “Never lock Trader Workstation” and “Auto restart” in TWS. It is suggested for IBHK users to use IB Gateway in order to have stable API connection because IB Gateway won’t be locked due to inactivity. Also, IBHK users can choose “Auto restart” in IB Gateway.
The weekly authentication cycle starts on every Monday. If you receiveLogin failed = Soft token=0 received instead of expected permanent for zdc1.ibllc.com:4001 (SSL),  this means you need to manually login again to complete the weekly reauthentication task.

In TWS/ IB Gateway – “Global Configuration” – “Lock and Exit”, you can choose the time of your TWS being shut down.
For API users, it is recommended to choose “Never lock Trader Workstation” and “Auto restart”.
IBHK users do not have “Never lock Trader Workstation” and “Auto restart” in TWS. It is suggested for IBHK users to use IB Gateway in order to have stable API connection because IB Gateway won’t be locked due to inactivity. Also, IBHK users can choose “Auto restart” in IB Gateway.
The weekly authentication cycle starts on every Monday. If you receiveLogin failed = Soft token=0 received instead of expected permanent for zdc1.ibllc.com:4001 (SSL),  this means you need to manually login again to complete the weekly reauthentication task.

### Daily Reauthentication

### Weekly Reauthentication

### Order Precautions

In TWS – “Global Configuration” – “API” – “Precautions”, you can enable the following items to stop receiving the order submission messages.
Enable “Bypass Order Precautions for API orders”.Enable “Bypass Bond warning for API orders”.Enable “Bypass negative yield to worst confirmation for API orders”.Enable “Bypass Called Bond warning for API orders”.Enable “Bypass “same action pair trade” warning for API orders”.Enable “Bypass price-based volatility risk warning for API orders”.Enable “Bypass US Stocks market data in shares warning for API orders”.Enable “Bypass Redirect Order warning for Stock API orders”.Enable “Bypass No Overfill Protection precaution for destinations where implied natively”.

In TWS – “Global Configuration” – “API” – “Precautions”, you can enable the following items to stop receiving the order submission messages.
Enable “Bypass Order Precautions for API orders”.Enable “Bypass Bond warning for API orders”.Enable “Bypass negative yield to worst confirmation for API orders”.Enable “Bypass Called Bond warning for API orders”.Enable “Bypass “same action pair trade” warning for API orders”.Enable “Bypass price-based volatility risk warning for API orders”.Enable “Bypass US Stocks market data in shares warning for API orders”.Enable “Bypass Redirect Order warning for Stock API orders”.Enable “Bypass No Overfill Protection precaution for destinations where implied natively”.

### Connected IB Server Location in TWS

Each IB account has a pre-decided IB server. You can visit this link to know our IB servers’ locations:https://www.interactivebrokers.com/download/IB-Host-and-Ports.pdf
Yet, all IB paper accounts are connected to US server by default and its location cannot be changed.
As IB servers in different regions have different scheduled server maintenance time (https://www.interactivebrokers.com/en/software/systemStatus.php), you may need to change the IB server location in order to avoid service downtime.
For checking your connected IB server location, you can go to TWS and click “Data” to see your Primary server. In the below image, the pre-decided IB server location is: cdc1.ibllc.com
If you want to change your live IB account server location in TWS, please submit a web ticket to “Technical Assistance” – “Connectivity” in order to request changing the IB server location.
In the web ticket, you need to provide:
Which account do you want to have IB server location change?Which IB server location would you like to connect to?TWS AMERICA – EAST (New York)TWS AMERICA – CENTRAL (Chicago)TWS Europe (Zurich)TWS Asia (Hong Kong)TWS Asia – CHINA (For mainland China users, if the account server is hosted in Hong Kong, they will automatically connect with the Shenzhen Gateway mcgw1.ibllc.com.cn)Which IB scheduled maintenance time do you choose? (Recommended to choose the default schedule maintenance time of its own IB server location)North AmericaEuropeAsia
TWS AMERICA – EAST (New York)TWS AMERICA – CENTRAL (Chicago)TWS Europe (Zurich)TWS Asia (Hong Kong)TWS Asia – CHINA (For mainland China users, if the account server is hosted in Hong Kong, they will automatically connect with the Shenzhen Gateway mcgw1.ibllc.com.cn)
North AmericaEuropeAsia
After you submit the ticket, you will receive a web ticket reply whichrequire you to confirm and understand the migration request.
For Internet users, as the connection between IB server and Exchange goes through a dedicated line, it is commonly recommended to choose a IB server location which is closer to your TWS location. For IB connection types, please visit:https://www.interactivebrokers.co.uk/en/software/connectionInterface.phpThe pre-decided IB server location connected from TWS is different from the IB Server location connected from IB Client Portal and IBKR Mobile.IB server location connected from TWS is pre-decided. You can submit a web ticket to request the IB server relocation for the TWS connection.IB server location connected from Client Portal or IBKR Mobile is based on your nearest IB server location. You cannot request the IB server relocation for Client Portal and IBKR Mobile connections. OAuth CP API users now cannot specify which server they want to connect to by themselves.
IB server location connected from TWS is pre-decided. You can submit a web ticket to request the IB server relocation for the TWS connection.IB server location connected from Client Portal or IBKR Mobile is based on your nearest IB server location. You cannot request the IB server relocation for Client Portal and IBKR Mobile connections. OAuth CP API users now cannot specify which server they want to connect to by themselves.

Each IB account has a pre-decided IB server. You can visit this link to know our IB servers’ locations:https://www.interactivebrokers.com/download/IB-Host-and-Ports.pdf
Yet, all IB paper accounts are connected to US server by default and its location cannot be changed.
As IB servers in different regions have different scheduled server maintenance time (https://www.interactivebrokers.com/en/software/systemStatus.php), you may need to change the IB server location in order to avoid service downtime.
For checking your connected IB server location, you can go to TWS and click “Data” to see your Primary server. In the below image, the pre-decided IB server location is: cdc1.ibllc.com
If you want to change your live IB account server location in TWS, please submit a web ticket to “Technical Assistance” – “Connectivity” in order to request changing the IB server location.
In the web ticket, you need to provide:
Which account do you want to have IB server location change?Which IB server location would you like to connect to?TWS AMERICA – EAST (New York)TWS AMERICA – CENTRAL (Chicago)TWS Europe (Zurich)TWS Asia (Hong Kong)TWS Asia – CHINA (For mainland China users, if the account server is hosted in Hong Kong, they will automatically connect with the Shenzhen Gateway mcgw1.ibllc.com.cn)Which IB scheduled maintenance time do you choose? (Recommended to choose the default schedule maintenance time of its own IB server location)North AmericaEuropeAsia
TWS AMERICA – EAST (New York)TWS AMERICA – CENTRAL (Chicago)TWS Europe (Zurich)TWS Asia (Hong Kong)TWS Asia – CHINA (For mainland China users, if the account server is hosted in Hong Kong, they will automatically connect with the Shenzhen Gateway mcgw1.ibllc.com.cn)
North AmericaEuropeAsia
After you submit the ticket, you will receive a web ticket reply whichrequire you to confirm and understand the migration request.
For Internet users, as the connection between IB server and Exchange goes through a dedicated line, it is commonly recommended to choose a IB server location which is closer to your TWS location. For IB connection types, please visit:https://www.interactivebrokers.co.uk/en/software/connectionInterface.phpThe pre-decided IB server location connected from TWS is different from the IB Server location connected from IB Client Portal and IBKR Mobile.IB server location connected from TWS is pre-decided. You can submit a web ticket to request the IB server relocation for the TWS connection.IB server location connected from Client Portal or IBKR Mobile is based on your nearest IB server location. You cannot request the IB server relocation for Client Portal and IBKR Mobile connections. OAuth CP API users now cannot specify which server they want to connect to by themselves.
IB server location connected from TWS is pre-decided. You can submit a web ticket to request the IB server relocation for the TWS connection.IB server location connected from Client Portal or IBKR Mobile is based on your nearest IB server location. You cannot request the IB server relocation for Client Portal and IBKR Mobile connections. OAuth CP API users now cannot specify which server they want to connect to by themselves.

### SMART Algorithm

In TWS Global Configuration – Orders – Smart Routing, you can set your SMART order routing algorithm. For available SMART Routing via TWS API, please visit:https://www.interactivebrokers.com/campus/ibkr-api-page/contracts/#smart-routing

In TWS Global Configuration – Orders – Smart Routing, you can set your SMART order routing algorithm. For available SMART Routing via TWS API, please visit:https://www.interactivebrokers.com/campus/ibkr-api-page/contracts/#smart-routing

### Allocation Setup (For Financial Advisors)

In TWS Global Configuration – Advisor Setup – Presets, you can need to choose Allocation Preference in order to avoid wrong allocation result.

In TWS Global Configuration – Advisor Setup – Presets, you can need to choose Allocation Preference in order to avoid wrong allocation result.

### Intelligent Order Resubmission

The TWS Setting listed in the Global Configuration under API -> Setting forMaintain and resubmit orders when connection is restored, is enabled by default in TWS 10.28 and above. When this setting is checked, all orders received while connectivity is lost will be saved and automatically resubmitted when connectivity is restored. Please note, if the Trader Workstation is closed during this time, the orders are deleted regardless of the setting.

The TWS Setting listed in the Global Configuration under API -> Setting forMaintain and resubmit orders when connection is restored, is enabled by default in TWS 10.28 and above. When this setting is checked, all orders received while connectivity is lost will be saved and automatically resubmitted when connectivity is restored. Please note, if the Trader Workstation is closed during this time, the orders are deleted regardless of the setting.

### Disconnect on Invalid Format

The TWS Setting listed in the Global Configuration under API -> Setting forMaintain connection upon receiving incorrectly formatted fields, is enabled by default in TWS 10.28 and above. For clients operating on Client Version 100 and above, users will not disconnect from fields with invalid value submissions when the setting is enabled.

The TWS Setting listed in the Global Configuration under API -> Setting forMaintain connection upon receiving incorrectly formatted fields, is enabled by default in TWS 10.28 and above. For clients operating on Client Version 100 and above, users will not disconnect from fields with invalid value submissions when the setting is enabled.
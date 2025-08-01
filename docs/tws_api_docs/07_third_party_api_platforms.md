---
title: "Third Party API Platforms"
description: "TWS API Documentation - Third Party API Platforms"
source: "Interactive Brokers TWS API Documentation"
nav_id: "third-party-platforms"
order: 7
prev_section: "TWSAPI Basics Tutorial"
next_section: "Unique Configurations"
prev_file: "06_twsapi_basics_tutorial.md"
next_file: "08_unique_configurations.md"
scraped_at: "2025-08-01T09:13:29.311564"
word_count: 873
paragraph_count: 12
subsection_count: 2
code_block_count: 0
format: "markdown"
---

# Third Party API Platforms

## Third Party API Platforms

Third party software vendors make use of the TWS’ programming interface (API) to integrate their platforms with Interactive Broker’s. Thanks to the TWS API, well known platforms such as Ninja Trader or Multicharts can interact with the TWS to fetch market data, place orders and/or manage account and portfolio information.
It is important to keep in mind that most third party API platforms are not compatible with all IBKR account structures. Always check first with the software vendor before opening a specific account type or converting an IBKR account type. For instance, many third party API platforms such as NinjaTrader and TradeNavigator arenotcompatible with IBKR linked account structures, so it is highly recommended to first check with the third party vendor before linking your IBKR accounts.

Third party software vendors make use of the TWS’ programming interface (API) to integrate their platforms with Interactive Broker’s. Thanks to the TWS API, well known platforms such as Ninja Trader or Multicharts can interact with the TWS to fetch market data, place orders and/or manage account and portfolio information.
It is important to keep in mind that most third party API platforms are not compatible with all IBKR account structures. Always check first with the software vendor before opening a specific account type or converting an IBKR account type. For instance, many third party API platforms such as NinjaTrader and TradeNavigator arenotcompatible with IBKR linked account structures, so it is highly recommended to first check with the third party vendor before linking your IBKR accounts.

An ongoing list of commonThird Party Connectionsare available within our documentation. This resource will also link out to connection guides detailing how a user can connect with a given platform.
A non-exhaustive list of third party platforms implementing our interface can be found in ourInvestor’s Marketplace. As stated in the marketplace, the vendors’ list is in no way a recommendation from Interactive Brokers. If you are interested in a given platform that is not listed, please contact the platform’s vendor directly for further information.

An ongoing list of commonThird Party Connectionsare available within our documentation. This resource will also link out to connection guides detailing how a user can connect with a given platform.
A non-exhaustive list of third party platforms implementing our interface can be found in ourInvestor’s Marketplace. As stated in the marketplace, the vendors’ list is in no way a recommendation from Interactive Brokers. If you are interested in a given platform that is not listed, please contact the platform’s vendor directly for further information.

### Non-Standard TWS API Languages and Packages

Noted in further depth through ourArchitecturesection, the TWS API is built using standardized socket protocol. As a result, users may develop or access alternative third party modules and classes in place of Interactive Brokers default modules through theTWS API Download. While the API is adaptable for client implementations, please understand thatInteractive Brokers API Support cannot provide support for non-standard implementations.While we can review yourAPI logsto affirm what content is being submitted, any further assistance will need to take place with the module’s original developer.
This is neither an endorsement or admonishment of third party implementations. Interactive Brokers will always advise clients use our direct TWS API implementation whenever possible.

Noted in further depth through ourArchitecturesection, the TWS API is built using standardized socket protocol. As a result, users may develop or access alternative third party modules and classes in place of Interactive Brokers default modules through theTWS API Download. While the API is adaptable for client implementations, please understand thatInteractive Brokers API Support cannot provide support for non-standard implementations.While we can review yourAPI logsto affirm what content is being submitted, any further assistance will need to take place with the module’s original developer.
This is neither an endorsement or admonishment of third party implementations. Interactive Brokers will always advise clients use our direct TWS API implementation whenever possible.

### ib_insync and ib_async

While Interactive Brokers’ API Support is aware of the ib_insync package, wecannot provide coding assistancefor the package.
With that in mind, users should be aware that the original ib_insync package is built using a legacy release of the TWS API and is no longer updated. Users who wish to implement the ib_insync structure using supported releases of the Trader Workstation should migrate to theib_async package, which is a modernized implementation of the package by one of its original developers.
This is neither an endorsement or admonishment of either the ib_insync or ib_async library. Interactive Brokers will always advise clients use our direct TWS API implementation whenever possible.

While Interactive Brokers’ API Support is aware of the ib_insync package, wecannot provide coding assistancefor the package.
With that in mind, users should be aware that the original ib_insync package is built using a legacy release of the TWS API and is no longer updated. Users who wish to implement the ib_insync structure using supported releases of the Trader Workstation should migrate to theib_async package, which is a modernized implementation of the package by one of its original developers.
This is neither an endorsement or admonishment of either the ib_insync or ib_async library. Interactive Brokers will always advise clients use our direct TWS API implementation whenever possible.
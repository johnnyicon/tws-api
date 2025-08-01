---
title: "Notes & Limitations"
description: "TWS API Documentation - Notes & Limitations"
source: "Interactive Brokers TWS API Documentation"
nav_id: "notes-and-limitations"
scraped_at: "2025-08-01T00:35:09.478168"
word_count: 923
paragraph_count: 20
subsection_count: 5
code_block_count: 0
format: "markdown"
---

# Notes & Limitations

## Notes & Limitations

While Interactive Brokers does maintain a Python, Java, C#, and C++ offering for the TWS API, C# and our Excel offerings are exclusively available for Windows PC. As a result, these features are not available on Linux or Mac OS.

While Interactive Brokers does maintain a Python, Java, C#, and C++ offering for the TWS API, C# and our Excel offerings are exclusively available for Windows PC. As a result, these features are not available on Linux or Mac OS.

### Requirements

A funded and opened IBKR Pro accountThe current Stable or Latest release of the TWS or IB GatewayThe current Stable or Latest release of the TWS APIA working knowledge of the programming language ourTestbedsample projects are developed in.
A funded and opened IBKR Pro accountThe current Stable or Latest release of the TWS or IB GatewayThe current Stable or Latest release of the TWS APIA working knowledge of the programming language ourTestbedsample projects are developed in.

A funded and opened IBKR Pro accountThe current Stable or Latest release of the TWS or IB GatewayThe current Stable or Latest release of the TWS APIA working knowledge of the programming language ourTestbedsample projects are developed in.

The minimum supported language version is documented on the right for each of our supported languages.
Please be sure to toggle the indicated language to the language of your choosing.
PythonJavaC++C#
Minimum supported Python release is version 3.11.0.
The minimum supported Java version is Java 8 (JDK 8).
The minimum supported C++ version is C++ 14 Standard.
The C# implementation was built using:
.NET Core 3.1.NET Framework 4.8.NET Standard 2.0

The minimum supported language version is documented on the right for each of our supported languages.
Please be sure to toggle the indicated language to the language of your choosing.

PythonJavaC++C#
Minimum supported Python release is version 3.11.0.
The minimum supported Java version is Java 8 (JDK 8).
The minimum supported C++ version is C++ 14 Standard.
The C# implementation was built using:
.NET Core 3.1.NET Framework 4.8.NET Standard 2.0

PythonJavaC++C#
Minimum supported Python release is version 3.11.0.
The minimum supported Java version is Java 8 (JDK 8).
The minimum supported C++ version is C++ 14 Standard.
The C# implementation was built using:
.NET Core 3.1.NET Framework 4.8.NET Standard 2.0

PythonJavaC++C#
Minimum supported Python release is version 3.11.0.
The minimum supported Java version is Java 8 (JDK 8).
The minimum supported C++ version is C++ 14 Standard.
The C# implementation was built using:
.NET Core 3.1.NET Framework 4.8.NET Standard 2.0

### Limitations

Our programming interface is designed to automate some of the operations a user normally performs manually within the TWS Software such as placing orders, monitoring your account balance and positions, viewing an instrument’s live data… etc. There is no logic within the API other than to ensure the integrity of the exchanged messages. Most validations and checks occur in the backend of TWS and our servers. Because of this it is highly convenient to familiarize with the TWS itself, in order to gain a better understanding on how our platform works. Before spending precious development time troubleshooting on the API side, it is recommended to first experiment with the TWS directly.
Remember:If a certain feature or operation is not available in the TWS, it will not be available on the API side either!

Our programming interface is designed to automate some of the operations a user normally performs manually within the TWS Software such as placing orders, monitoring your account balance and positions, viewing an instrument’s live data… etc. There is no logic within the API other than to ensure the integrity of the exchanged messages. Most validations and checks occur in the backend of TWS and our servers. Because of this it is highly convenient to familiarize with the TWS itself, in order to gain a better understanding on how our platform works. Before spending precious development time troubleshooting on the API side, it is recommended to first experiment with the TWS directly.
Remember:If a certain feature or operation is not available in the TWS, it will not be available on the API side either!

### C# for MacOS

The TWS API C# source files are not available through the Mac and Unix distribution download as the language is built around Dynamic Link Library (DLL) files for execution. This is because DLL files are exclusively supported through Windows platforms.

The TWS API C# source files are not available through the Mac and Unix distribution download as the language is built around Dynamic Link Library (DLL) files for execution. This is because DLL files are exclusively supported through Windows platforms.

### Paper Trading

If your regular trading account has been approved and funded, you can use your Account Management page to open aPaper Trading Accountwhich lets you use the full range of trading facilities in a simulated environment using real market conditions. Using a Paper Trading Account will allow you not only to get familiar with the TWS API but also to test your trading strategies without risking your capital. Note the paper trading environment has inherentlimitations.

If your regular trading account has been approved and funded, you can use your Account Management page to open aPaper Trading Accountwhich lets you use the full range of trading facilities in a simulated environment using real market conditions. Using a Paper Trading Account will allow you not only to get familiar with the TWS API but also to test your trading strategies without risking your capital. Note the paper trading environment has inherentlimitations.
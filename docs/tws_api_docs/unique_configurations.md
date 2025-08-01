---
title: "Unique Configurations"
description: "TWS API Documentation - Unique Configurations"
source: "Interactive Brokers TWS API Documentation"
nav_id: "unqiue-configurations"
scraped_at: "2025-08-01T00:35:10.127908"
word_count: 1096
paragraph_count: 30
subsection_count: 10
code_block_count: 0
format: "markdown"
---

# Unique Configurations

## Unique Configurations

While all of the available Trader Workstation API default samples provide equivalent functionality, some languages have unique configurations that must be implemented in order to use our samples or program code with the underlying API.

While all of the available Trader Workstation API default samples provide equivalent functionality, some languages have unique configurations that must be implemented in order to use our samples or program code with the underlying API.

### Implementing the Intel Decimal Library for MacOS and Linux

Due to the malleability of the many Linux distributions including MacOS, Interactive Brokers is unable to provide a pre-built binary for the library. As such, users programming in C++ on a Linux machine must manually build the Intel® Decimal Floating-Point Math Library manually.
As described in the README file from the linked page, you can find the library’s build steps within the ~/IntelRDFPMathLib20U2/LIBRARY/README file.
Download the Intel® Decimal Floating-Point Math Library

Due to the malleability of the many Linux distributions including MacOS, Interactive Brokers is unable to provide a pre-built binary for the library. As such, users programming in C++ on a Linux machine must manually build the Intel® Decimal Floating-Point Math Library manually.
As described in the README file from the linked page, you can find the library’s build steps within the ~/IntelRDFPMathLib20U2/LIBRARY/README file.

### Updating The Python Interpreter

Python has a unique system for importing libraries into it’s IDEs. This extends even further when it comes to virtual environments. In order to utilize Python code with the TWS API, you must run our setup file in order to import the code.

Python has a unique system for importing libraries into it’s IDEs. This extends even further when it comes to virtual environments. In order to utilize Python code with the TWS API, you must run our setup file in order to import the code.

### 1. Open Command Prompt or Terminal

In order to update the Python IDE, these steps MUST be performed through Command Prompt or Terminal. This can not be done through an explorer interface.
As such, users should begin by launching their respective command line interface.
These samples will display Windows commands, though the procedure is identical on Windows, MacOS, and Linux.

In order to update the Python IDE, these steps MUST be performed through Command Prompt or Terminal. This can not be done through an explorer interface.
As such, users should begin by launching their respective command line interface.
These samples will display Windows commands, though the procedure is identical on Windows, MacOS, and Linux.

### 2. Navigate to Python Source

Customers should then change their directory to{TWS API}\source\pythonclient.
It is then recommend to display the contents of the directory with “ls” for Unix, or “dir” for Windows users.

Customers should then change their directory to{TWS API}\source\pythonclient.
It is then recommend to display the contents of the directory with “ls” for Unix, or “dir” for Windows users.

### 3. Run The setup.py File

Customers will now need to run the setup.py steps with the installation parameter. This can be done with the command:python setup.py install

Customers will now need to run the setup.py steps with the installation parameter. This can be done with the command:python setup.py install

### 4. Confirm Updates

After running the prior command, users should see a large block of text describing various values being updated and added to their system. It is important to confirm that the version installed on your system mirrors the build version displayed. This example represents 10.25; however, you may have a different version.

After running the prior command, users should see a large block of text describing various values being updated and added to their system. It is important to confirm that the version installed on your system mirrors the build version displayed. This example represents 10.25; however, you may have a different version.

### 5. Confirm your installation

Finally, users should look to confirm their installation. The simplest way to do this is to confirm their version with pip. Typing this command should show the latest installed version on your system:python -m pip show ibapi

Finally, users should look to confirm their installation. The simplest way to do this is to confirm their version with pip. Typing this command should show the latest installed version on your system:python -m pip show ibapi

### Protobuf UserWarning messages

After resolving the reference errors, using the TWSAPI may print a UserWarning upon connection. These warnings are predominantly cosmetic and can be ignored. These issues are caused by the Pypi release of protobuf running version 6.30.1 and above, while the TWS API is built with 5.29.3. The warning is simply notifying users that their version is 1 major version different. However, given protobuf is currently backgwards compatible, this should not present any issues with the implementation. Developers uncomfortable with the warning messages have a few options:
Recompile Protobufagainst theirGithub 5.29.3 versionto maintain parity with the TWS API implementations.Users can also modify the code source, linked by the protobuf warning, and simply remove lines 94 and on from the runtime_version.py file.

After resolving the reference errors, using the TWSAPI may print a UserWarning upon connection. These warnings are predominantly cosmetic and can be ignored. These issues are caused by the Pypi release of protobuf running version 6.30.1 and above, while the TWS API is built with 5.29.3. The warning is simply notifying users that their version is 1 major version different. However, given protobuf is currently backgwards compatible, this should not present any issues with the implementation. Developers uncomfortable with the warning messages have a few options:
Recompile Protobufagainst theirGithub 5.29.3 versionto maintain parity with the TWS API implementations.Users can also modify the code source, linked by the protobuf warning, and simply remove lines 94 and on from the runtime_version.py file.

### Implementing Visual Basic .NET

Our VB.NET code is provided for demonstration purposes only; there is no pure, standalone VB.NET-based TWS API library. Both our “VB_API_Sample” and the VB.NET “Testbed” projects included with our TWS API releases call the C# TWS API source. The provided VB.NET code only interfaces with the C# source. Please keep in mind that these samples are in VB.NET, not Visual Basic for Applications.

Our VB.NET code is provided for demonstration purposes only; there is no pure, standalone VB.NET-based TWS API library. Both our “VB_API_Sample” and the VB.NET “Testbed” projects included with our TWS API releases call the C# TWS API source. The provided VB.NET code only interfaces with the C# source. Please keep in mind that these samples are in VB.NET, not Visual Basic for Applications.
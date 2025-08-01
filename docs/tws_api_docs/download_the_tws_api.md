---
title: "Download the TWS API"
description: "TWS API Documentation - Download the TWS API"
source: "Interactive Brokers TWS API Documentation"
nav_id: "find-the-api"
scraped_at: "2025-08-01T00:35:09.807874"
word_count: 1553
paragraph_count: 18
subsection_count: 4
code_block_count: 0
format: "markdown"
---

# Download the TWS API

## Download the TWS API

It is recommended for API users to use same TWS API version to make sure the TWS version and TWS API version are synced in order to prevent version conflict issue.
Running the Windows version of the API installer creates a directory “C:\\TWS API\” for the API source code in addition to automatically copying two files into the Windows directory for the DDE and C++ APIs.It is important that the API installs to the C: drive, as otherwise API applications may not be able to find the associated files. The Windows installer also copies compiled dynamic linked libraries (DLL) of the ActiveX control TWSLib.dll, C# API CSharpAPI.dll, and C++ API TwsSocketClient.dll. Starting in API version973.07, running the API installer is designed to install an ActiveX control TWSLib.dll, and TwsRtdServer control TwsRTDServer.dll which are compatible with both 32 and 64 bit applications.
It is important to know that the TWS API isonlyavailable through the interactivebrokers.github.io MSI or ZIP file. Any other resource, including pip, NuGet, or any other online repository is not hosted, endorsed, supported, or connected to Interactive Brokers. As such, updates to the installation should always be downloaded from the github directly.
TWS API Download Page

It is recommended for API users to use same TWS API version to make sure the TWS version and TWS API version are synced in order to prevent version conflict issue.
Running the Windows version of the API installer creates a directory “C:\\TWS API\” for the API source code in addition to automatically copying two files into the Windows directory for the DDE and C++ APIs.It is important that the API installs to the C: drive, as otherwise API applications may not be able to find the associated files. The Windows installer also copies compiled dynamic linked libraries (DLL) of the ActiveX control TWSLib.dll, C# API CSharpAPI.dll, and C++ API TwsSocketClient.dll. Starting in API version973.07, running the API installer is designed to install an ActiveX control TWSLib.dll, and TwsRtdServer control TwsRTDServer.dll which are compatible with both 32 and 64 bit applications.
It is important to know that the TWS API isonlyavailable through the interactivebrokers.github.io MSI or ZIP file. Any other resource, including pip, NuGet, or any other online repository is not hosted, endorsed, supported, or connected to Interactive Brokers. As such, updates to the installation should always be downloaded from the github directly.

### Install the TWS API on Windows

Download the IB API for Windows to your local machineThis will direct you to Interactive BrokersAPI License Agreement, please review itOnce you have clicked “I Agree“, refer to theWindowssection to download the API Software version of your preferenceThis will downloadTWS APIfolder to your computerGo to your IDE and Open TerminalNavigate to the directory where the installer has been downloaded (normally it should be your C: drive or D: drive) and confirm the file is present. Now, let’s take an example: install TWS API Python$cd ~/TWS API/source/pythonclient$python3 setup.py install
Navigate to the directory where the installer has been downloaded (normally it should be your C: drive or D: drive) and confirm the file is present. Now, let’s take an example: install TWS API Python
$cd ~/TWS API/source/pythonclient$python3 setup.py install

Download the IB API for Windows to your local machineThis will direct you to Interactive BrokersAPI License Agreement, please review itOnce you have clicked “I Agree“, refer to theWindowssection to download the API Software version of your preferenceThis will downloadTWS APIfolder to your computerGo to your IDE and Open TerminalNavigate to the directory where the installer has been downloaded (normally it should be your C: drive or D: drive) and confirm the file is present. Now, let’s take an example: install TWS API Python$cd ~/TWS API/source/pythonclient$python3 setup.py install
Navigate to the directory where the installer has been downloaded (normally it should be your C: drive or D: drive) and confirm the file is present. Now, let’s take an example: install TWS API Python
$cd ~/TWS API/source/pythonclient$python3 setup.py install

### Windows:

### Install the TWS API on MacOs / Linux

Download the IB API for Mac/Unix zip file to your local machineThis will direct you to Interactive BrokersAPI License Agreement, please review itOnce you have clicked “I Agree“, refer to theMac / Unixsection to download the API Software version of your preference
This will downloadtwsapi_macunix.<Major Version>.<Minor Version>.zipto your computer(where <Major Version> and <Minor Version> are the major and minor version numbers respectively)Open Terminal (Ctrl+Alt+Ton most distributions)Navigate to the directory where the installer has been downloaded (normally it should be the Download folder within your home folder) and confirm the file is present$cd ~/Downloads$ls
Navigate to the directory where the installer has been downloaded (normally it should be the Download folder within your home folder) and confirm the file is present
$cd ~/Downloads$ls
Unzip the contents the installer into your home folder with the following command(if prompted, enter your password):NOTE:replace the values ‘n.m’ with the name of your installed file.$sudo unzip twsapi_macunix.n.m.zip -d $HOME/To access the sample and source files, navigate to theIBJtsdirectory and confirm the subfolders samples and source are present$cd ~/IBJts$ls
When running “python3 setup.py install“,  you may get “ModuleNotFoundError: No Module named ‘setuptools’“. As “setuptools” is deprecated, please grant the write permission on the target folder (e.g.source/pythonclient) using “sudo chmod -R 777” in order to avoid “error: could not create ‘ibapi.egg-info’: Permission denied“. After that, run “python3 -m pip install .“
Download the IB API for Mac/Unix zip file to your local machineThis will direct you to Interactive BrokersAPI License Agreement, please review itOnce you have clicked “I Agree“, refer to theMac / Unixsection to download the API Software version of your preferenceThis will downloadtwsapi_macunix.<Major Version>.<Minor Version>.zipto your computer(where <Major Version> and <Minor Version> are the major and minor version numbers respectively)Open MacOS Terminal (Command+Spaceto launch Spotlight, then typeterminaland pressReturn)Go to find the zipped TWS API file and Copy the zipped TWS API file path.Run the following command in MacOS Terminal.$ unziptwsapi_macunix.<Major Version>.<Minor Version>.zip
Go to find the zipped TWS API file and Copy the zipped TWS API file path.
$ unziptwsapi_macunix.<Major Version>.<Minor Version>.zip
Note: On MacOS, if you directly open thetwsapi_macunix.<Major Version>.<Minor Version>.zipfile, you will get an error: “Unable to expand…… It is an unsupported format“. It is required for users to unzip the zipped TWS API file using the above MacOS Terminal command.

Download the IB API for Mac/Unix zip file to your local machineThis will direct you to Interactive BrokersAPI License Agreement, please review itOnce you have clicked “I Agree“, refer to theMac / Unixsection to download the API Software version of your preference
This will downloadtwsapi_macunix.<Major Version>.<Minor Version>.zipto your computer(where <Major Version> and <Minor Version> are the major and minor version numbers respectively)Open Terminal (Ctrl+Alt+Ton most distributions)Navigate to the directory where the installer has been downloaded (normally it should be the Download folder within your home folder) and confirm the file is present$cd ~/Downloads$ls
Navigate to the directory where the installer has been downloaded (normally it should be the Download folder within your home folder) and confirm the file is present
$cd ~/Downloads$ls
Unzip the contents the installer into your home folder with the following command(if prompted, enter your password):NOTE:replace the values ‘n.m’ with the name of your installed file.$sudo unzip twsapi_macunix.n.m.zip -d $HOME/To access the sample and source files, navigate to theIBJtsdirectory and confirm the subfolders samples and source are present$cd ~/IBJts$ls
When running “python3 setup.py install“,  you may get “ModuleNotFoundError: No Module named ‘setuptools’“. As “setuptools” is deprecated, please grant the write permission on the target folder (e.g.source/pythonclient) using “sudo chmod -R 777” in order to avoid “error: could not create ‘ibapi.egg-info’: Permission denied“. After that, run “python3 -m pip install .“
Download the IB API for Mac/Unix zip file to your local machineThis will direct you to Interactive BrokersAPI License Agreement, please review itOnce you have clicked “I Agree“, refer to theMac / Unixsection to download the API Software version of your preferenceThis will downloadtwsapi_macunix.<Major Version>.<Minor Version>.zipto your computer(where <Major Version> and <Minor Version> are the major and minor version numbers respectively)Open MacOS Terminal (Command+Spaceto launch Spotlight, then typeterminaland pressReturn)Go to find the zipped TWS API file and Copy the zipped TWS API file path.Run the following command in MacOS Terminal.$ unziptwsapi_macunix.<Major Version>.<Minor Version>.zip
Go to find the zipped TWS API file and Copy the zipped TWS API file path.
$ unziptwsapi_macunix.<Major Version>.<Minor Version>.zip
Note: On MacOS, if you directly open thetwsapi_macunix.<Major Version>.<Minor Version>.zipfile, you will get an error: “Unable to expand…… It is an unsupported format“. It is required for users to unzip the zipped TWS API file using the above MacOS Terminal command.

### Unix/ Linux:

### MacOS:

### TWS API File Location & Tools

#### TWS API Folder Files Explanation:

“API_VersionNum.txt”
File Path:~\TWS API\API_VersionNum.txt
You can check your API version in this file.
“IBSampleApp.exe”
File Path:~\TWS API\samples\CSharp\IBSampleApp\bin\Release\IBSampleApp.exe
You can manually use the IBSampleApp to test the API functions.
“ApiDemo.jar”
File Path:~\TWS API\samples\Java\ApiDemo.jar
This is built with Java. Java users can use it to quickly test the IB TWS API functions.

#### TWS API Folder Files Explanation:

“API_VersionNum.txt”
File Path:~\TWS API\API_VersionNum.txt
You can check your API version in this file.
“IBSampleApp.exe”
File Path:~\TWS API\samples\CSharp\IBSampleApp\bin\Release\IBSampleApp.exe
You can manually use the IBSampleApp to test the API functions.
“ApiDemo.jar”
File Path:~\TWS API\samples\Java\ApiDemo.jar
This is built with Java. Java users can use it to quickly test the IB TWS API functions.

#### TWS API Folder Files Explanation:
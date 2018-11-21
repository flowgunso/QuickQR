![QuickQR logo](resources/icons/quickqr.svg)
# QuickQR

[![Linux/OSX build status](https://travis-ci.org/flowgunso/QuickQR.svg)](https://travis-ci.org/flowgunso/QuickQR)
[![Windows build status](https://ci.appveyor.com/api/projects/status/ym9ls83a7r3hja8q?svg=true)](https://ci.appveyor.com/project/flowgunso/quickqr)

__Quickly generate QR codes.__

# Introduction

*QuickQR* is a Qt application that lives in your system tray.
It generate a QR code from your current clipboard data.

# Installation

# Roadmap

This application works, but does not offer much features.
The following important features are planned:

- Display the QR code directly in the system tray menu

    Due to specific Desktop Environments limitations, a new window is shown to display the QR code.
    While most _DE_ allow complex object in the system tray, some don't.  
    Unsupported _DE_ will show a new window, all the other will display the QR code in the system tray menu.

- Generate content-specific QR codes

    Displayed QR code in __QuickQR__ are raw text only.  
    But QR do support different content, such as WiFi connection, geolocation, SMS, Deep Linking and more.

- Save the QR image file with a right click

- Build system specific installer packages
    
    Build installable *.deb*, *.rpm*, *.dmg* and *.msi* packages 

You can check the [TODO list](TODO.md) for more details.



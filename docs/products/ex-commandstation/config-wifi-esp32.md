---
tags:
    - _C_WIFI_AP_ssid_password_channel
    - _C_WIFI_AP_ssid_password
    - _C_WIFI_DEFAULT
    - _C_WIFI_HIDDENAP_ssid_password_channel
    - _C_WIFI_HIDDENAP_ssid_password
    - _C_WIFI_HOSTNAME_hostname
    - _C_WIFI_OFF
    - _C_WIFI_ON
    - _C_WIFI_ssid_password
    - _C_WIFI_TEMP_ssid_password
---

# WiFi configuration <br/><small>(EX-CSB1 or ESP32 ONLY. v5.7.0+ ONLY)</small>

This page is exclusively for users of **EX-CommandStation** version 5.7.0 and later. Version 5.7.0 is currently in the experimental / development (DEVEL) phase and is not recommended for general users.

<span style="color:red;">The ``config.h`` options for WiFi configuration from EX-CommandStation versions prior to 5.7.0 are now ignored by the EX-CSB1 or ESP32 command stations.</span>

If you are using an **EX-CSB1**, ESP32 based EX-CommandStation and are are using the latest DEVEL versions of the  EX-CommandStation code (versions from 5.7.0),</span> the ``config.h`` options for WiFi configuration are ignored by CSB1 or ESP32 command stations. Instead you must use the instructions on this page.

Also see the [WiFi Configuration for version 5.7.0+ - Graphical User Interface Options](config-wifi-esp32-gui-options_not_in_nav.md) for detailed instructions on how, and why, to change these settings using EX-WebThrottle or EX-Toolbox.

## Operating Modes

WiFi has two operating modes:

- **AP** (Access point) means the **EX-CommandStation** acts as its own private WiFi network so throttle devices must connect first to the Command Station WiFi network.
- **STA** (Station mode) means the **EX-CommandStation** connects to your existing WiFi router and appears as a device on that network. If the WiFi is configured for STA mode, but fails to connect to your router, it will fall back to AP mode in much the same way as smart plugs, lights etc.

As shipped, or without prior configuration, the ESP32 WiFi default to operate in AP mode with an ssid/Password combination generated from the internal chip (mac) address. The ssid and password will be shown on the oLED display (typically something like "DCCEX_123abc"[^1] and "PASS_123abc") so you can connect you phone or tablet immediately and start running.
d
[^1]: Where `123abc`` will be the last 6 digits of the mac address of the wifi board on the device. As such it will be unique for every EX-CommandStation.

Later, you may wish to reset the connection to use your home router as this avoids the need to reconnect your normal phone WiFi before using a throttle.

WiFi configuration changes are made by running commands from the USB serial (IDE, PaltformIO, EXWebThrottle) or from a connected WiFi throttle such as Engine Driver or EXToolbox.

The commands below are stored on the ESP32 (except for the TEMP command). Please be aware that if you issue a command to change the WiFi settings from a WiFi device, this will mean you lose connection and need to reconnect before continuing.

Its is recommended that you don't do this while running trains.

## Changing to Station Mode (ie your home router)

```cpp
<C WIFI "routerSSID" "routerPassword">
```

The command station will attempt this connection immediately, and on each rerstart. If it fails to connect, it will revert to AP mode.

## Changing the Access Point defaults

To give the Access point a known name and a password that will not be revealed on the OLED use the command:

```cpp
<C WIFI AP "MyCSB1" "SpamWonderfulSpam">
```

The AP mode password must be at least 8 characters long.

The default channel is set to "11". Use a phone WiFi analyser app to see which channels are relatively quiet in your area. If you need to use an
alternate channel (we recommend using only 1,6, or 11) you may change it here.

```cpp
<C WIFI AP "MyCSB1" "SpamWonderfulSpam" 6>
```

In some environments you may want to hide the SSID from phones scanning for access points. If you do hide the SSID, it is still possible to connect by entering the SSID manually on the phone/tablet.

```cpp
<C WIFI HIDDENAP "MyCSB1" "SpamWonderfulSpam" 6>
```

## Configuring the Host Name

The default is "DCCEX" but you can change this if you have more than one CS on you home router to make them show up with different names on the network.
Host names starting with "DCCEX" are more readily found by WiFi throttles.

```cpp
<C WIFI HOSTNAME "DCCEX-MYCSB1">
```

## Turning WiFi On/Off

```cpp
<C WIFI OFF>
or
<C WIFI ON>
```

WARNING If you switch WiFi OFF you will only be able to switch it on again over the USB serial connection.

## Clearing WiFi settings

```cpp
<C WIFI DEFAULT>
```

WiFi will revert to the internally generated ssid and password.

## Visiting another router

Should you wish to visit a friend and temporarily connect to their home network you can use the TEMP setting that will be checked first but only until the ESP32 is powered off. After that it will revert to your regular settings.

```cpp
<C WIFI TEMP "fredsRouter" "Wilmer!!">
```

## Displaying WiFi settings

```cpp
<D WIFI SHOW>
```

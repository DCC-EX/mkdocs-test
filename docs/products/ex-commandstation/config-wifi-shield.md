# Wifi configuration <br/><small>(Excluding **EX-CSB1** or ESP32 v5.7.0+)</small>

WiFi has two operating modes:

- AP (Access point) means the **EX-CommandStation** acts as its own private WiFi network so throttle devices must connect first to the **EX-CommandStation** Wifi network.
- STA (Station mode) means the **EX-CommandStation** connects to your WiFi router and appears as a device on that network. If the WiFI is configured for STA mode, but fails to connect to your router, it will fall back to AP mode in much the same way as smart plugs, lights etc.

<span style="color:red">NOTE: If you are using an **EX-CSB1** or ESP32 based EX-CommandStation ***AND*** you are are using the latest DEVEL versions of the  EX-CommandStation code (versions from 5.7.0),</span> the ``config.h`` options for WiFi configuration described here are ignored by the **EX-CSB1** or ESP32 EX-CommandStations. Instead see the [WiFi configuration (EX-CSB1 or ESP32 ONLY. Version 5.7.0+ ONLY) page](config-wifi-esp32.md).

## Operating Modes

WiFi has two operating modes:

- **AP** (Access point) means the **EX-CommandStation** acts as its own private WiFi network so throttle devices must connect first to the **EX-CommandStation**'s WiFi network.
- **STA** (Station mode) means the **EX-CommandStation** connects to your existing WiFi router and appears as a device on that network. If the WiFi is configured for STA mode, but fails to connect to your router, it will fall back to AP mode in much the same way as smart plugs, lights etc.

## Setup STA (Station) mode

```cpp
#define ENABLE_WIFI true
#define WIFI_SSID "deadBudgie"
#define WIFI_PASSWORD "myHovvercraftIsFullOfEels"
```

## Setup AP (Access Point) default mode

```cpp
#define ENABLE_WIFI true
```

The WiFi chip will first try to connect to the previously
configured network and if that fails fall back to Access Point mode.

The SSID of the AP will be automatically set to `DCCEX_*`[^1] where the `*` part is taken from an internal device number (for example `DCCEX_12b7c`) to try and avoid duplications. The password will be set to `PASS_*` where the `*` part matches the generated SSID name.

[^1]: Where `123abc`` will be the last 6 digits of the mac address of the wifi board on the device. As such it will be unique for every EX-CommandStation.

## Setup AP (Access Point) advanced mode

```cpp
#define ENABLE_WIFI true
#define WIFI_FORCE_AP true
#define WIFI_SSID "MyCSB1"
#define WIFI_PASSWORD "Don't tell him Pike!"
#define WIFI_CHANNEL 1
```

The AP mode password must be at least 8 characters long.

The default channel is set to "1". Use a phone WiFi analyser app to see which channels are relatively quiet in your area. If you need to use an
alternate channel (we recommend using only 1,6, or 11) you may change it here.

- WIFI_HOSTNAME: The default is "dccex" but you can change this if you have more than one
CS on you home router to make them show up with different names on the network.
Host names starting with "dccex" are more readily found by WiFi throttles.

```cpp
#define WIFI_HOSTNAME "dccex-csb1"
```

In some environments you may want to hide the SSID from phones scanning for access points. If you do hide the SSID, it is still possible to connect by entering the SSID manually on the phone/tablet.

```cpp
#define WIFI_HIDE_SSID
```

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

# ``<C WIFI [«various parameters»]>`` <br/> Setup the WiFi

Serial command to setup the WiFi on the EX-Command Stations.
<span style="color:red">For EX-CSB1 and ESP32 based command stations only. Version 5.7.0 or later only.</span>

See [WiFi configuration](../../products/ex-commandstation/config-wifi-esp32.md) for more infomation on these commands.

See the [WiFi Configuration for version 5.7.0+](https://dcc-ex.com/ex-commandstation/advanced-setup/supported-wifi/wifi-config_v5_7.html) page on the old web site for detailed instructions on how, and why, to change these settings using EX-WebThrottle or EX-Toolbox.

## Command

* ``/ WIFI``

### Command Variations

* ``<C WIFI AP "«ssid»" "«password»" [«channel»]>`` set Wifi to AP mode with given ssid and password
* ``<C WIFI AP "«ssid»" "«password»">`` set Wifi to AP mode with given ssid and password
* ``<C WIFI DEFAULT>`` set Wifi to default credentials
* ``<C WIFI HIDDENAP "«ssid»" "«password»" [«channel»]>`` set Wifi to AP mode with given ssid and password
* ``<C WIFI HIDDENAP "«ssid»" "«password»>`` set Wifi to AP mode with given ssid and password
* ``<C WIFI HOSTNAME "«hostname»">`` set Wifi hostname
* ``<C WIFI OFF>`` Disable Wifi
* ``<C WIFI ON>`` Enable Wifi
* ``<C WIFI "«ssid»" "«password»">`` set Wifi ssid and password
* ``<C WIFI TEMP "«ssid»" "«password»">`` set Wifi ssid and password temporarily

## Parameters

* **ssid**: ssid to set the commandstation to use or connect to
* **password**: password to set the commandstation to use or to use whne connecting to an existing ssid
* **channel**: *optional* - channel to set the commandstation to use ``1``-``11``

    The default channel is set to “11”. If you need to use an alternate channel (we recommend using only 1,6, or 11) you may change it with the command

* **hostname**: the name that appears in your Throttle app, once you have connected to the appropriate network for the Command Station

## *Response*

N/A. The command station will restart.

## *Notes*

* In every case above, the Command Station will restart to apply the new settings. You will need to reconnect to the Command Station with whatever interface you are using.
* Only Station (STA) mode and the HOSTNAME can be changed over WiFi.
* Access Point (AP) mode changes require a serial/USB connection. This is a security feature. If you could change AP mode settings over WiFi, then anyone who could connect to the Command Station’s WiFi network could change the AP settings and potentially lock you out of your Command Station. By requiring a USB connection for AP mode changes, we ensure that only someone with physical access to the Command Station can modify these critical settings.
* Hidden AP mode: If enabled, the Command Station’s WiFi network will not be visible in the list of available networks on devices. This can enhance security by making it less obvious to potential attackers, but it also means that users will need to manually enter the network name (SSID) to connect.

    Note that this does not provide any performance advantages.

* Temporary STA mode: If enabled, the Command Station will start in Station mode and connect to an existing Wifi network. But will forget this setting the next time the EX‑CommandStation is restarted.

    This may be useful if visiting a location with a different WiFi network which you would like to connect to without changing the permanent WiFi settings on the Command Station.

----

## *Examples*

[Also search for 'WiFi'](?_wifi)

### *Example Commands*

* See [WiFi configuration](../../products/ex-commandstation/config-wifi-esp32.md)
* See [WiFi Configuration for version 5.7.0+](https://dcc-ex.com/ex-commandstation/advanced-setup/supported-wifi/wifi-config_v5_7.html)

### *Example Responses:*

N/A
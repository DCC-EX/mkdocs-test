# Optionally install Wifi

This page does not apply to CSB1 or other ESP32-based command stations which have Wi-Fi built in.

If you intend to use an ESP-01 development board, please skip to [ESP01](#esp-01-or-esp-01s)

## EX-WiFiShield8266

![WiFiShield8266](/_static/images/wifi/makerfabs-esp8266-wifi-shield.png){ align=right }
We recommend you purchase an EX-WiFiShield8266 (a joint venture with Makerfabs) which has been designed to make the installation easy.

You can find installation instructions here [WiFiShield8266 install](/diy/20-mega-easy.md#optionally-install-wifishield)

<div style="clear: both;"></div>
## Other shields
![wangtongze](/_static/images/wifi/wangtongze_jumpered.png){ align=right }

Most other Arduino ESP8266 Wi-Fi shields, including the dodgy ones with "Shiald" and "Arbuino" spelling mistakes, will work well with a DCC-EX command station but must be modified slightly to bypass the useless design based on UNOs with one user and no USB connection. They are frequently shipped with firmware versions that do not work well with DCC-EX (latest is not always best!) and it's non-trivial to rectify this.

In addition, the shield size overlaps the standard Arduino motor-shield terminal blocks which is a pain if you failed to follow the Command Station build suggestions at the time.

1. Ensure that the WiFi shield is physically modified to avoid it communicating over the standard Arduino Tx/Rx Serial pins, by removing pins 0 and 1. If it has any DIP switches, set them all off.

2. Mount the shield above the command station motor shield making sure the tab end of the WiFi shield is away from the power connector end of the motor shield.

3. Use two male-female Dupont wires to connect the WiFi Shield to your Command Station. (Pay Attention... we get a lot of support calls from users who have not noticed that the wires cross!)

```bash
- Arduino      Shield
- Rx1  -------> Tx
- TX1  -------> Rx
```

<div style="clear: both;"></div>

## ESP-01 or ESP-01S

![ESP01](/_static/images/wifi/esp-01s_2.png){ align=right }
These devices are not recommended because there are power consumption issues that may cause random Command Station brown-out failure while attempting to connect in a low WiFi signal area.  They will probably NOT work without a non-trivial firmware update.

The ESP-01 should be connected with dupont wires to the Command Station with wiring as follows:

```bash
- Arduino      ESP-01
- 3.3V  -----> Vcc
- 3.3V  -----> CH_PD
- Gnd   -----> Gnd
- Tx1   -----> Rx
- Rx1   -----> Tx
```

Incorrect wiring can destroy this device.

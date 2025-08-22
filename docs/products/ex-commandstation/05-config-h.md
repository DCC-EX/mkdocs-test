# Build configuration (config.h)

During compilation and build, there are a number of settings that control the way the code is constructed and important features are configured.

Most configuration takes place in EXRAIL but some things just need setting before that.

If you are using the EX-Installer, the important options will be automatically managed and configured but this reference is here for more advanced users with particular requirements.

These options should be coded in the file `config.h` which will be automatically included in the compilation process.

## Motor shield definition (Mandatory)

```cpp
#define MOTOR_SHIELD_TYPE typeName
```

The motor shield definition tells the code how many tracks your command station has and which pins are used to talk to the motor shield(s).
It also describes the electrical characteristics of the current sensing and the current limits to be applied to each track.

There are a number of pre-defined motor shield typeNames available of which the most common are:

- STANDARD_MOTOR_SHIELD : Arduino Motor shield Rev3 based on the L298 with 18V 2A per channel
- EX8874_SHIELD         : DCC-EX TI DRV8874 based motor shield
- EXCSB1                : DCC-EX CSB-1 hardware
- EXCSB1_WITH_EX8874    : DCC-EX CSB-1 hardware with DCC-EX TI DRV8874 shield
- NO_SHIELD             : CS without any motor shield (as an accessory only CS)

Further pre-defined shield names can be found in the code file MotorDrivers.h although their presence there does not necessarily mean that we can provide support for issues.

### User defined motor shield hardware definition (Advanced)

In extreme cases, it is possible to craft your own definition
for example:

```cpp
#define MY_SHIELD F("MINE"), \
 new MotorDriver( 3, 12, UNUSED_PIN, 9, A0, 5.08, 3000, A4), \
 new MotorDriver(11, 13, UNUSED_PIN, 8, A1, 5.08, 1500, A5)
#define MOTOR_SHIELD_TYPE MY_SHIELD
```

refer to MotorDrivers.h for details of parameter meanings. Do NOT attempt to alter MotorDrivers.h or you will face versioning difficulties.

NOTE: Before connecting these boards and selecting one in this software
check the quick install guides! Some of these boards require a voltage
generating resistor on the current sense pin of the device. Failure to select
the correct resistor could damage the sense pin on your Arduino or destroy
the device.

### Motor shield max current

If you want to restrict the maximum current LOWER than what your
motor shield can provide, you can do that here. For example if you
have a motor shield that can provide 5A and your power supply can
only provide 2.5A then you should restrict the maximum current to
2.25A (90% of 2.5A) so that DCC-EX shuts off the track before
your PS does shut DCC-EX. MAX_CURRENT is in mA so for this example
it would be 2250, adjust the number according to your PS. If your
PS has a higher rating than your motor shield you do not need this.
You can use this as well if you are cautious and your trains do not
need full current.

```cpp
#define MAX_CURRENT 2250
```

## WiFi settings

Ignore this if you do not have WiFi on your command station or choose to avoid it.

WiFi has two operating modes:

- AP (Access point) means the Command station acts as its own private WiFi network so throttle devices must connect first to the Command Station Wifi network.
- STA (Station mode) means the command station connects to your WiFi router and appears as a device on that network. If the WiFI is configured for STA mode, but fails to connect to your router, it will fall back to AP mode in much the same way as smart plugs, lights etc.

### Setup STA (Station) mode

```cpp
#define ENABLE_WIFI true
#define WIFI_SSID "deadBudgie"
#define WIFI_PASSWORD "myHovvercraftIsFullOfEels"
```

### Setup AP (Access Point) default mode

```cpp
#define ENABLE_WIFI true
```

The WiFi chip will first try to connect to the previously
configured network and if that fails fall back to Access Point mode.

The SSID of the AP will be automatically set to `DCCEX_*` where the `*` part is taken from an internal device number (for example `DCCEX_12b7c`) to try and avoid duplications. The password will be set to `PASS_*` where the `*` part matches the generated SSID name.

### Setup AP (Access Point) advanced mode

```cpp
#define ENABLE_WIFI true
#define WIFI_FORCE_AP true
#define WIFI_SSID "MyCSB1"
#define WIFI_PASSWORD "Don't tell him Pike!"
#define WIFI_CHANNEL 1
```

The AP mode password must be at least 8 characters long.

The default channel is set to "1". If you need to use an
alternate channel (we recommend using only 1,6, or 11) you may change it here.

### Advanced settings

- Control of IP port (default 2560). We cant think of any reason why this would ever need to be changed.

```cpp
#define IP_PORT 2560
```

- DONT_TOUCH_WIFI_CONF means WIFI config will be done with
the <+> commands and this sketch will not change anything over
AT commands and the other WIFI_* defines do not have any effect.

```cpp
#define ENABLE_WIFI true
#define DONT_TOUCH_WIFI_CONF
```

- WIFI_HOSTNAME: The default is "dccex" but you can change this if you have more than one
CS on you home router to make them show up with different names on the network.
Host names starting with "dccex" are more readily found by WiFi throttles.

```cpp
#define WIFI_HOSTNAME "dccex-csb1"
```

## Ethernet settings

It is not valid to enable Ethernet and WiFi at the same time.

```cpp
#define ENABLE_ETHERNET true
```

### Advanced Ethernet settings

- IP_ADDRESS can be set but it is preferable to omit this and have the router assign an address using DHCP.

```cpp
#define IP_ADDRESS { 192, 168, 1, 200 }
```

- MAX_NUM_TCP_CLIENTS: If you on STM32 Ethernet (and only there) want more than
 9 (*) TCP clients, change this number to for example 20 here **AND** in
 STM32lwiopts.h and follow the instructions in STM32lwiopts.h

 (*) It would be 10 if there would not be a bug in LwIP by STM32duino.

```cpp
#define MAX_NUM_TCP_CLIENTS 20
```

## LCD/OLED support

The LCD feature requires an I2C enabled LCD screen using a Hitachi HD44780
controller and a commonly available PCF8574 based I2C 'backpack'.
To define LCD_DRIVER for I2C address 0x27, 16 cols, 2 rows

```cpp
#define LCD_DRIVER  0x27,16,2
```

For an OLED display define OLED_DRIVER width,height\[,address\] in pixels (address auto detected if not supplied)

128x32 or 128x64 I2C SSD1306-based devices are supported.
Use 132,64 for a SH1106-based I2C device with a 128x64 display.

For example

```cpp
#define OLED_DRIVER 0x3c,128,32
```

Define scroll mode as 0, 1 or 2

- 0 is scroll continuous (fill screen if poss),
- 1 is by page (alternate between pages),
- 2 is by row (move up 1 row at a time).

```cpp
#define SCROLLMODE 1
```

In order to avoid wasting memory the current scroll buffer is limited
to 8 lines.  Some users wishing to display additional information
such as TrackManager power states have requested additional rows aware
of the warning that this will take extra RAM.  if you wish to include additional rows

```cpp
#define MAX_CHARACTER_ROWS 12
```

## Disable EEPROM

The EEPROM feature is only there for backward support of deprecated methods of turnout, sensor and output creation inherited from DCC++.
You are advised to turn this off to save memory.

```cpp
 #define DISABLE_EEPROM
```

## Disable PROG

If you do not need programming capability, you can disable all program track related commands. You might want to do that if you are building a command station that drives multiple tracks and you do not have a spare track output for programming.

```cpp
 #define DISABLE_PROG
```

## Redefine DCC boundary between SHORT and LONG loco addresses

According to NMRA the last short address is 127 and the first long address is 128.
There are manufacturers which have another view.
Lenz CS, for example, have considered addresses long from 100. If
 you want to change to that mode, do

```cpp
#define HIGHEST_SHORT_ADDR 99
```

If you want to run all your locos addressed long format, you could even do

```cpp
#define HIGHEST_SHORT_ADDR 0
```

DCC-EX does not support to use the same address, for example 100(long) and 100(short) at the same time, there must be a border.

## Redefine locomotive state table size

This is the maximum number of locos that can be controlled at the same time.
This defaults to 50 (8 on a UNO/NANO).
If you have enough free memory you can increase this to a maximum of 255.
If you are short of memory (typically a Mega with WiFi and lots of accessories)
you can decrease it  to a minimum of 2.

```cpp
#define MAX_LOCOS 100
```

## Delayed startup

Some newer 32bit microcontrollers boot very quickly, so powering on I2C and other peripheral devices at the same time may result in the CommandStation booting too quickly to detect them.

To work around this, set STARTUP_DELAY to a value in milliseconds that works for your environment.

```cpp
 #define STARTUP_DELAY 3000
```

## Define TURNOUTS and ACCESSORIES to follow norm RCN-213

According to norm RCN-213 a DCC packet with a 1 is closed-straight
and one with a 0 is thrown-diverging.  In DCC++ Classic, and in previous
versions of DCC++EX, a turnout throw command was implemented in the packet as
'1' and a close command as '0'. The #define below makes the states
match with the norm.  But we don't want to cause havoc on existent layouts,
so we define this only for new installations. If you don't want this,
don't add it to your config.h.

```cpp
#define DCC_TURNOUTS_RCN_213
```

By default, the driver which defines a DCC accessory decoder
does send out the same state change on the DCC packet as it
receives. This means a VPIN state=1 sends D=1 (close turnout
or signal green) in the DCC packet. This can be reversed if
necessary.

```cpp
#define HAL_ACCESSORY_COMMAND_REVERSE
```

If you have issues with that the direction of the accessory commands is
reversed (for example when converting from another CS to DCC-EX) then
you can use this to reverse the sense of all accessory commands sent
over DCC-EX. This #define likewise inverts the behaviour of the <a> command
for triggering DCC Accessory Decoders, so that <a addr subaddr 0> generates a
DCC packet with D=1 (close turnout) and <a addr subaddr 1> generates D=0
(throw turnout).

```cpp
#define DCC_ACCESSORY_COMMAND_REVERSE
```

## Handling multiple serial throttles

The command station always operates with the default Serial port.
Diagnostics are only emitted on the default serial port and not broadcast.
Other serial throttles may be added to the Serial1...Serial6 ports which may or may not exist on your CPU. (Mega has 3, CSB1 has 1, and STM32 have up to 6.)

To monitor a throttle on one or more serial ports, supply a #define for each serial port required.

NOTE: DO NOT define here the WiFi shield serial port or your Wifi will not work.

```cpp
// SERIAL1 in use by Wifi
#define SERIAL2_COMMANDS
#define SERIAL3_COMMANDS
#define SERIAL4_COMMANDS
#define SERIAL5_COMMANDS
#define SERIAL6_COMMANDS
```

## Bluetooth serial ON ESP32

On ESP32 you have the possibility to use the builtin BT serial to connect to
the CS.

The CS shows up as a pairable BT Classic device. Name is "DCCEX-hexnumber".
BT is as an additional serial port, debug messages are still sent over USB,
not BT serial.

If you enable this there are some implications:

1. WiFi will sleep more (as WiFi and BT share the radio). So WiFi performance may suffer
2. The app will be bigger that 1.2MB, so the default partition scheme will not
    work any more. You need to choose a partition scheme with 2MB (or bigger).
    For example "NO OTA (2MB APP, 2MB SPIFFS)" in the Arduino IDE.
3. There is no securuity (PIN) implemented. Everyone in radio range can pair
    with your CS.

```cpp
#define SERIAL_BT_COMMANDS
```

## Booster input pin on ESP32 CS

On ESP32 you have the possibility to define a pin as booster input

Arduino pin D2 is GPIO 26 is Booster Input on ESPDuino32

```cpp
#define BOOSTER_INPUT 26
```

GPIO 32 is Booster Input on EX-CSB1

```cpp
#define BOOSTER_INPUT 32
```

## ESP32 LED Wifi Indicator

GPIO 2 on ESPduino32

```cpp
#define WIFI_LED 2
```

GPIO 33 on EX-CSB1

```cpp
#define WIFI_LED 33
```

## SABERTOOTH

This is a very special option and only useful if you happen to have a
Sabertooth motor controller from Dimension Engineering configured to
take commands from and ESP32 via serial at 9600 baud from GPIO17 (TX)
and GPIO16 (RX, currently unused).

The number defined is the DCC address for which speed controls are sent
to the sabertooth controller _as_well_. Default: Undefined.

```cpp
#define SABERTOOTH 1
```

## Tuning for deprecated UNO/NANO

By default VDPY and DIAGs are disabled on a Uno/Nano to reduce PROGMEM and RAM requirements.

They can be re-enebled if you have space by the commands

```cpp
#define ENABLE_VDPY
#define ENABLE_DIAG
```

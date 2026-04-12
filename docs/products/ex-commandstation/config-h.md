# Build configuration (config.h)

During compilation and build, there are a number of settings that control the way the code is constructed and important features are configured.

Most configuration takes place in EXRAIL but some things just need setting before that.

If you are using the EX-Installer, the important options will be automatically managed and configured. There are several more advanced options covered in the [config.h advanced](/reference/advanced-config-h.md) but these should not trouble the vast majority of users.

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

## WiFi settings

Ignore this if you do not have WiFi on your command station or choose to avoid it.

The CSB1 and other ESP32-based command stations use a completely different method to define WiFi settings. This is to allow WiFi configuration without having to reinstall the software.

[WiFi setup for CSB1 or ESP32](/products/ex-commandstation/config-wifi-esp32.md)

[WiFi setup for WiFi shield](/products/ex-commandstation/config-wifi-shield.md)

## Ethernet settings

It is not valid to enable Ethernet and WiFi at the same time.

```cpp
#define ENABLE_ETHERNET true
```

## LCD/OLED support

The LCD feature requires an I2C enabled LCD screen using a Hitachi HD44780
controller and a commonly available PCF8574 based I2C 'backpack'.
To define LCD_DRIVER for I2C address 0x27, 16 cols, 2 rows

```cpp
#define LCD_DRIVER  0x27,16,2
```

For an OLED display define OLED_DRIVER \[address,\]width,height in pixels (address auto detected if not supplied)

128x32 or 128x64 I2C SSD1306-based devices are supported.
Use 132,64 for a SH1106-based I2C device with a 132x64 display.

For example

```cpp
#define OLED_DRIVER 132,64
```

OR

```cpp
#define OLED_DRIVER 0x3c,132,64
```

Define scroll mode as 0, 1 or 2

- 0 is scroll continuous (fill screen if possible),
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

## Delayed startup

Some newer 32bit microcontrollers boot very quickly, so powering on I2C and other peripheral devices at the same time may result in the CommandStation booting too quickly to detect them.

To work around this, set STARTUP_DELAY to a value in milliseconds that works for your environment.

```cpp
 #define STARTUP_DELAY 3000
```

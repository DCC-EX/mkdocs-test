# EX-CSB1 FAQ

## CH340 USB Drivers

Windows USB driver is required.  
  CH340 driver info [https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all)

Note that only one program can use the USB connection simultaneously.  Close the device monitor or other programs when uploading.

## Track voltage

DCC is a square wave signal.  The voltage of the track power supply will be present on each rail 50% of the time.  Use the DC scale to measure voltage -- each rail vs GND should be 50% of track power supply.  

Few digital multimeters will provide a consistent/useful reading on the AC scale.

## OLED

Select 132x64 or 128x64  
If one results in blank screen or image is shifted, try the other.

## Power supply

If your power supply is less than 5A, add a line in config.h to set overcurrent reporting lower - 90% of track power supply.  
[motor-shield-max-current](../advanced-config-h.md#motor-shield-max-current)

## Fault reporting

Continuous faults will be reported with power on, if track power supply is not connected.

An initial fault report at power-on is not an issue.

## Overcurrent reporting

Some - 600mA or less - overcurrent reporting on the programming track is not unusual.  This is due to lack of precision of the ESP32-WROOM ADC, and the 250mA trip current for the programming track when not reading/writing CVs.

There is a command `<C PROGBOOST>` to override the 250mA limit.  Do not use it unless you are comfortable that your loco/decoder do not have issues (which 250mA is designed to protect).  
Note that `<C PROGBOOST>` remains in effect until the command station is restarted.

## WiFi

WiFi configuration is different, starting with version 5.7.0.  
config.h is used for WiFi configuration in earlier versions.  
Link to [5.7.0 WiFi Configuration](../../products/ex-commandstation/config-wifi-esp32.md)

Note that if the new WiFi configuration commands are sent via a WiFi connection, your existing connection will drop.  Current connection info should be reported on the OLED.

## Discord

Join the discussion on the discord server.  
[https://dcc-ex.com/mkdocs-test/support/discord/](../../support/discord.md)

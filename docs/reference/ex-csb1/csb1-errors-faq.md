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

Some CSB1 may have had screen display customized to display track status.  
[myTrackStatus.example.h](../../products/ex-commandstation/exrail/cookbooks/advanced/display-track-status.md)

## Power supply

If your power supply is less than 5A, add a line in config.h to set overcurrent reporting lower - 90% of track power supply.  
[motor-shield-max-current](../advanced-config-h.md#motor-shield-max-current)

## EX8874 on CSB1

EX8874 on CSB1 requires no modifications to the EX8874 solder pads.  
A second identical power supply or Y-cable will be needed for the EX88874 track power.

## Startup - Tracks / Power

Add lines to myAutomation.h to define track modes and power state at startup.  
Note that the power command is placed after the change in track mode.  
[Startup - Define Tracks](../../products/ex-commandstation/exrail/cookbooks/startup/startup-set-track.md)

## Fault reporting

Continuous faults will be reported with power on, if track power supply is not connected.

An initial fault report at power-on is not an issue.

## Overcurrent reporting

Some - 600mA or less - overcurrent reporting on the programming track is not unusual.  This is due to lack of precision of the ESP32-WROOM ADC, and the 250mA trip current for the programming track when not reading/writing CVs.

There is a command `<C PROGBOOST>` to override the 250mA limit.  Do not use it unless you are comfortable that your loco/decoder does not have issues (which 250mA is designed to protect).  
Note that `<C PROGBOOST>` remains in effect until the **EX-CommandStation** is restarted.

## WiFi

WiFi configuration is different, starting with version 5.7.0.  
config.h is used for WiFi configuration in earlier versions.  
Link to [5.7.0 WiFi Configuration](/products/ex-commandstation/config-wifi-esp32.md)

Note that if the new WiFi configuration commands are sent via a WiFi connection, your existing connection will drop.  Current connection info should be reported on the OLED.

## More

- [The general support FAQ page](../../support/faq.md)

- [EX-CSB1 Getting Started Guide](../../products/ex-commandstation/ex-csb1.md)

## Discord

Join the discussion on the discord server.  
[https://dcc-ex.com/mkdocs-test/support/discord/](../../support/discord.md)

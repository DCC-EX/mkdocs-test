# EX-CSB1 FAQ

## CH340 USB Drivers

Windows USB driver is required.  
  CH340 driver info [https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all)

Note that only one program can use the USB connection simultaneously.  Close the device monitor or other programs when uploading.

## Track voltage

Unlike AC, DCC is a square wave signal.  The voltage of the track power supply will be present on each rail 50% of the time and off for the other 50%.

***Most multimeters cannot read the DCC voltage correctly on the 'AC' setting.***

Use the 'DC' setting on the multimeter and connect one probe to one rail (or output of the motor shield) and the other to a ground GPIO on the motor shield or microcontroller board.  Double whatever result you see to get the *actual voltage*.

## OLED

Suppliers of the **EX-CSB1** may ship it with one of a number of different types of oLED screen.

You may not be able to tell which type it is by looking at it. So, if you are uncertain which it is, when installing the **EX-CommandStation** software, select one of the options (commmonly either the ``128x64`` or ``132x64``).

If one results in blank screen or image is shifted, try the other.

Some **EX-CSB1**s may have had the screen display customized to display track status.  
[myTrackStatus.example.h](../../../products/ex-commandstation/exrail/cookbooks/advanced/display-track-status.md)

## OLED Power Status

By default, the oLED will display the state of the power to the track/outputs.

Older versions of the **EX-CommandStation** software will display ``Power On``, ``Power Off``, ``Power SC``

``SC`` refers to to 'Status Conflict' and simply means that one track/output is on and the other is off.  ***This completely normal*** and is **not** an error or fault.

Later versions of the **EX-CommandStation** software will display ``Power On``, ``Power Off``, ``Power Ab`` or ``Power bA``. Where the uppercase 'A' or 'B' means the power is on for that track. And the lowercase 'a' or 'b' means that the power is off for that track.

i.e. ``Power SC`` means the same as either ``Power Ab`` or ``Power bA``.

## Power supply

If your power supply is less than 5A, add a line in config.h to set overcurrent reporting lower - 90% of track power supply.  
[motor-shield-max-current](../../advanced-config-h.md#motor-shield-max-current)

## EX8874 on CSB1

EX8874 on CSB1 requires no modifications to the EX8874 solder pads.  
A second identical power supply or Y-cable will be needed for the EX88874 track power.

## Startup - Tracks / Power

Add lines to myAutomation.h to define track modes and power state at startup.  
Note that the power command is placed after the change in track mode.  
See [Startup - Define Tracks](../../../products/ex-commandstation/exrail/cookbooks/startup/startup-set-track.md) for more information.

## Fault reporting

Continuous faults will be reported with power on, if track power supply is not connected.

An initial fault report at power-on is not an issue.

## Overcurrent reporting

Some - 600mA or less - overcurrent reporting on the programming track is not unusual.  This is due to lack of precision of the ESP32-WROOM ADC, and the 250mA trip current for the programming track when not reading/writing CVs.

There is a command `<C PROGBOOST>` to override the 250mA limit.  Do not use it unless you are comfortable that your loco/decoder does not have issues (which 250mA is designed to protect).  
Note that `<C PROGBOOST>` remains in effect until the **EX-CommandStation** is restarted.

## WiFi

### Prior to Version 5.7.0

``config.h`` is used for WiFi configuration in earlier versions of the **EX-CommandStation** software. This can be done as part of the configuration in **EX-Installer**.

See [WiFi Configuration](../../../products/ex-commandstation/config-wifi-shield.md) for more information.

### Version 5.7.0 and Later

WiFi configuration is different starting with version 5.7.0 and is done after the **EX-CommandStation** software is loaded (via **EX-Installer**).

See [5.7.0 WiFi Configuration](../../../products/ex-commandstation/config-wifi-esp32.md) for more information.

Note that if the new WiFi configuration commands are sent via a WiFi connection, your existing connection will drop.  Current connection info should be reported on the OLED.

---

## More

- [The general support FAQ page](../../../support/faq.md)

- [EX-CSB1 Getting Started Guide](../../../products/ex-commandstation/ex-csb1.md)

## Discord

Join the discussion on the discord server.  
[https://dcc-ex.com/mkdocs-test/support/discord/](../../../support/discord.md)

--8<-- "snippets/abbr.md"
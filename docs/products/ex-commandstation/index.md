# EX-CommandStation - Overview

![EX-CommandStation Logo](../../_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light width=400px align=right }
![EX-CommandStation Logo](../../_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark width=400px align=right }

A DCC Command Station powers your track and sends digital signals to the locos and accessories through the track. All commercial command stations do that, but we think we do it a lot better for a lot less money.

<span style="font-size: larger;">Our outstanding free, open source, **EX-CommandStation** software is at the core of our [ready-to-run](../ex-csb1/index.md) and [self-build](../../diy/diy.md) systems.</span>

## Features

An **EX‑CommandStation** is powerful, DCC and DC Command Station software which you can purchase on a ready-to-run [**EX-CSB1**](../ex-csb1/index.md) or install on self built hardware made from widely available parts.

It supports almost all of the [NMRA](https://nmra.org) [Digital Command Control (DCC)](https://dcc-ex.com/reference/hardware/dcc-vs-dc.html) standards, including:

- Simultaneous control of multiple locomotives
- Control of all cab/loco functions (F0-F28 and F29-F68)
- Control of accessory / function decoders
- Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
- Programming Track: Same as the main track with the addition of reading CV bytes

It also includes advanced features, such as:

- Works on a variety of different [microcontroller](../../reference/microcontrollers/index.md) and [motor driver](../../reference/hardware/motorboards/index.md) hardware
- A [wiThrottle Server](../../throttles/withrottle-vs-native-protocol.md) implementation for compatibility with popular WiFi throttles (controllers)
- A [Native Serial Server](../../throttles/withrottle-vs-native-protocol.md) implementation for use with advanced WiFi and hardware throttles (controllers)
- General purpose inputs and outputs (I/O) for extensibility (Self Build only)
- I2C bus for controlling accessories with I2C capability
- [JMRI](https://dcc-ex.com/throttles/software/jmri.html) integration
- [EXRAIL](../../enhance/exrail/index.md) Automation and Animation scripting that can control everything on your layout, including the locos
- Any output can be used as a [DCC Auto Reverser](../../enhance/trackmanager/index.md)
- Can be used as a [DCC booster](../../enhance/trackmanager/booster.md) (EX-CSB1 only)

It also supports:

- [Direct Current (DC)](../../enhance/dc-running.md) locomotive control using Pulse Width Modulation (PWM)

## Ready to Run or Self Build

Our primary solution is the [**EX-CommandStation/Booster 1 Express (CSB1**)](../ex-csb1/index.md) DCC Command Station which provides a ready-to-run system with integrated WiFi. You can start running trains from your Android or iOS phone in a couple of minutes if you plug your track in one end and a power supply in the other.

- If you want to *buy a ready built* **EX-CommandStation**, see [Purchase a EX-CommandStation](/purchasing/official-sellers.md).  
To follow the basic setup process, you can use the `next` button seen at the bottom right of each page.

- If you want to *build your own* **EX-CommandStation** and are prepared to learn about Arduinos, ESP32s (and other microcontrollers) see [Building your own EX-CommandStation](/diy/diy.md). But you are advised to read the basic guidance that follows so you will have a better understanding of what you want to achieve, and what will be possible.

--8<-- "snippets/abbr.md"

# Build Your Own Command Station

A command station consists of a processor and a shield/board to convert the low voltage digital signal from the processor into the high powered track output.

**DCC-EX** started life creating home-built command stations using Arduino UNO and Arduino Mega microcontrollers with the standard Arduino motor shields. This was attractive to users that liked to experiment and was exceptionally cheap to create.

Our [Command Station Booster 1 Express (EX-CSB1)](/products/ex-commandstation/ex-csb1.md) is now available as a complete ready-to-run, plug-and-go, solution. ***However, if wish you build your own, or even buy a pre-built stack from a third party***, you can still do so using our open source **EX-CommandStation** software and commonly available parts. However, you will need to learn quite a lot more than using our plug-and-go solution the **EX-CSB1**.

## Before You Start

!!! warning "Buyer beware!"

    There are many different brands and clones of various different microcontrollers, shields/boards, and power supplies on the market, particularly when using marketplaces such as AliExpress and Amazon. Sometimes the prices on these marketplaces seem too good to be true for a genuine item, and they usually, and you will end up with a clone or inferior product, potentially with quality, reliability, and compatibility issues.

    When reading through these self-build options, we endeavour to be as clear as we can on the specific options we recommend, but we cannot possibly tell you all the options of where to purchase reliably, so you must take care when purchasing that you are buying the correct component. If in doubt, ask via our [Discord server](/support/discord.md) for a second opinion before spending your money.
    
    Further, should you select a different microcontrollers, or progress to adding accessories, you will find that lots of "standards" are not at all standard, and that apparently attractive alternatives to the recommended items are totally incompatible. You may need to configure the software or even modify hardware shields.

## Components

In addition to the command station components, you will also need

- a [power supply](power.md) appropriate you your track and locos.
- a **"Main"** track, aka "Operations" track - most people already have this: it’s your layout! If you don't yet have this, no problem you can still test on the programming track (below).
- a **"Programming"** track, aka "PROG" or “Service” track - an isolated short section of track that you will use to program locomotives
- a Train - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder). Ideally, it should be a loco already proven to work on DCC. Otherwise, if you have a problem, you may not be able to tell if the problem is the decoder or the **EX-CommandStation**

Like any command station, you will want some kind of throttle but you can start to drive trains with just the basic system and your PC using [EX-WebThrottle](/products/ex-webthrottle/ex-webthrottle.md).

## Getting the EX-CommandStation Software

All builds will require the **EX-CommandStation** software to be configured and loaded onto the Arduino microcontroller from your PC. This is best done using the [EX-Installer](/installer/installer.md)

## Quick and Easy Arduino Mega

If you build our standard Arduino Mega-based **EX-CommandStation** and use our [EX-MotorShield8874](../products/ex-motorshield8874/ex-motorshield8874.md)  and, optionally, the [EX-WiFiShield8266](../products/ex-wifishield8266/ex-wifishield8266.md) which have been specifically designed to meet our requirements, then you will be up and running quickly. [Easy Build Instructions](mega-easy.md)

## Slightly more difficult Mega

Using other supported motor or WiFi shields requires a slightly [more complex setup](mega-harder.md).

You will eventually require a multimeter, a soldering iron, and a variety of dupont wires or similar and you will probably collect a bucket-load of connectors, adapters, and gizmos that you thought might be useful but don't have time to try.

In fact, TIME is the thing you will need most, and time spent building your **EX-CommandStation** is just too easy an excuse for not building your layout!

The following documentation pages can only take you through the basics and should you contact us for support it is well to remember that we do this for fun, we don't get paid, and we don't all have access to the same weird but cheap gizmo you found on the web with an instruction sheet in Klingon.

Apart from that... it's great fun!

--8<-- "snippets/abbr.md"

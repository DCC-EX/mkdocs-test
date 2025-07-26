# Build Your Own Command Station

A command station consists of a processor and a shield/board to convert the low voltage digital signal from the processor into the high powered track output.

DCC-EX started life on home-built command stations using Arduino UNO and Mega processors and the standard Arduino motor shield. This was attractive to users that liked to experiment and was exceptionally cheap to create. However, if you build your own, or even buy a pre-built stack from a third party, you will need to learn quite a lot more than using our plug-and-go solution the [Command Station Booster 1 Express (CSB1)](?CSB1).

Of course you will also need

- a “Main” track, aka “Operations” track - most people already have this: it’s your layout! If you don't yet have this, no problem you can still test on the programming track (below).
- a “Programming” track, aka "PROG" or “Service” track - an isolated short section of track that you will use to program locomotives
- a Train - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder). Ideally, it should be a loco already proven to work on DCC. Otherwise, if you have a problem, you may not be able to tell if the problem is the decoder or the EX-CommandStation

Like any command station, you will want some kind of throttle but you can start to drive trains with just the basic system and your PC.

## Getting the DCC-EX Software

All builds will require the DCC-EX software to be configured and loaded onto the Arduino processor from your PC. This is best done using the EX-Installer and the following build instructions assume you have already downloaded and installed this by following the [getting started](/getting-started/01-getting-started.md) instructions.

## Quick and Easy Arduino Mega

If you build our standard Mega-based Command station and use our EX-MotorShield8874  and, optionally, the EX-WiFiShield8266 which have been specifically designed to meet our requirements, then you will be up and running quickly. [Easy Build Instructions](20-mega-easy.md)

## Slightly more difficult Mega

Using other supported motor or WiFi shields requires a slightly [more complex setup](21-mega-harder.md).

!!! warning "Buyer beware!"

    Should you select a different processor, or progress to adding accessories, you will find that lots of "standards" are not at all standard, and that apparently attractive alternatives to the recommended items are totally incompatible. You may need to configure the software or even modify hardware shields.

You will require a multimeter, a soldering iron, and a variety of dupont wires or similar and you will probably collect a bucket-load of connectors, adapters, and gizmos that you thought might be useful but don't have time to try.

In fact, TIME is the thing you will need most, and time spent building your command station is just too easy an excuse for not building your layout!

The following documentation pages can only take you through the basics and should you contact us for support it is well to remember that we do this for fun, we don't get paid, and we don't all have access to the same weird but cheap gizmo you found on the web with an instruction sheet in Klingon.

Apart from that... it's great fun!

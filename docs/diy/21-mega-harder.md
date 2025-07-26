# Alternative build - Arduino Mega

TODO This page needs pictures inserting.


These instructions assume a slightly more competent user who has made the decision to trade simplicity for price. It is assumed that you are comfortable modifying devices, soldering etc. and are not going to make costly mistakes such as mixing up the power supplies.

There are a limited number of suitable motor or WiFi shields available and each has its own quirks.

## What you need

To build a basic DIY Command Station you will need:

- A PC or laptop (Not A Raspberry Pi) running a reasonably recent versions of Windows, Linux or MacOS
- an Arduino Mega microprocessor running our free Open Source software
- USB cable to your PC for the processor.
- an Arduino standard (or others as noted in details) motor-shield to power the track.
- A double-insulated DC power supply with a voltage suitable for your layout/locos.
- An additional double-insulated DC Power supply of 5 to 8 volts suitable to drive the Arduino logic. (This may also be fed through the USB cable, and old phone charger is suitable or if you intend to use JMRI your computer will supply this power.)
- Optionally
    - a female barrel connector to match the plug on your chosen track power supply
    - a suitable WiFi shield to use WiFi throttles (Recommended) with 2 suitable M-F Dupont wires.
    - OR an Ethernet Shield

## Step By Step Build

### Prepare your Mega

1. Use sticky tape or similar to cover the top of the USB connector on the mega. This prevents any accidental contact with the underside of the motor shield.  

### Optionally mount your Ethernet Shield

Note, you can't have Ethernet and WiFi running on the same command station, but you can install both shields and choose one or the other when installing the software.
See [Ethernet Install](23-mega-hard-ethernet.md)


### Prepare your motor shield

FAILURE TO DO THIS CAN DESTROY YOUR MEGA.

1. Unless you are using an EX8874 shield, you MUST prevent the shield from feeding track voltage into your Mega. This is done by cutting the VIN trace and/or removing the pin that feeds the Mega.
![VIN trace](/_static/images/mega-hard/mega2.png)

2. Ensure shield pins are straight and correctly aligned.

### Mount the motor shield

1. Align the motor shield so that the power connectors are at the same end as the Mega power/usb connectors. It is normal for you to see a few millimetres of the pins between the bottom of the motor board and the top of the headers.
![Orientation](/_static/images/mega-hard/mega3.png)
![Orientation](/_static/images/mega-hard/mega4.png)

### Connect your track

Don't skip this step if you don't yet have any track because the WiFi shield will cover the connectors.

It's best to create fly leads with a suitable pluggable connectors for later. It makes it much easier to detach your command station from your layout when you need to fiddle with it or throw it against the wall out of sheer frustration.

If you only have one piece of track for testing, wire it to the PROG track plug.

 1. Your PROG track is wired to the B channel output.
 2. The MAIN track is wired to the A channel output.
![Orientation](/_static/images/mega-hard/mega5.png)

### Connect your track power supply

1. Wire your track power supply to the input turrets of the motor shield, observing polarity. It is best to create short wire with a female barrel connector.
![Orientation](/_static/images/mega-hard/mega6.png)

### Optionally install a WiFi Shield

See [WiFi Install](22-mega-hard-wifi.md)

TODO Photo.

### Load the software

Software loading is best done with the [EX-Installer](80-installer.md)

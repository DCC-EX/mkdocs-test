# Using Your Command Station

You need just two things that work together to operate your model railroad/railway:

- The **EX‑CommandStation** (aka the DCC Command Station)
- [A Throttle/Controller](#the-throttle-controller) (also referred to as a Front-end or Cab)

Additionally you may want to [program decoder/CVs](../throttles/loco-programming/index.md), [control DCC Accessories](dcc-accessories.md), [use (Direct Current) DC](../enhance/dc-running.md).  These will be covered later in the [Enhance](../enhance/index.md) section of the website.

----

## The EX-CommandStation

The **EX‑CommandStation** is explained in detail in the EX-CommandStation ([ready to run](../products/ex-csb1/index.md) or [self build](../diy/diy.md)) pages. It is either an **EX‑CommandStation/Booster One Express** or an microcontroller with a motor driver and a WiFi shield.

The Command Station accepts instructions from a throttle/controller and generates packets that are transmitted to your track and subsequently your trains.

----

## The Throttle (Controller)

!!! note inline end "Connection Types"

    Your throttle (controller) can connect to the **EX‑CommandStation** a number of different ways, such as:

    - WiFi
    - Direct connection using a USB cable
    - 2 wires to an Arduino serial port
    - Ethernet
    - Bluetooth
    - Remote connection (VNC, MQTT, etc.)

Since the **EX‑CommandStation** simply accepts commands to turn into signals for your layout, you need something that sends those commands to run your trains - a controller. (It isn’t very practical to type something like <t 1 3 75 1> into a serial monitor to tell your train to move each time! 😉)

A controller can be a hardware device like a handheld throttle (also called a Controller or Cab), an App that runs on your phone, a Web Page, or front-end software like JMRI or Rocrail that runs on a computer or Raspberry Pi.

### Throttle (Controller) Options

For further throttle and connection options, refer to the [Throttle List](throttles.md) page.

----

### DCC Accessory Operation

==TODO== HIGH - Overview of DCC Accessory Operation

For further information, refer to the [DCC Accessory Operation](dcc-accessories.md) page.



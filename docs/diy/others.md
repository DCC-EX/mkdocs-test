# DIY - Other Devices

We are unable to support you self building with devices other than those described in the earlier pages. In some cases we do know about devices that simply don't work or have so little market penetration that it is not worth the considerable effort required to develop, test and maintain software for them.

DCC-EX is not a simple Arduino program, it requires precise access to the internals of each processor type. This means development time is taken and support issues rise whenever we take on a new processor.

We are unable to rely on third party libraries which are generally designed to be the only thing on your Arduino and do not play well in such a demanding scenario.

## Supported DCC Decoders

**EX-CommandStation** supports all 'standards compliant' DCC loco and accessory decoders.  Note that some DCC decoders do not fully comply with the DCC standards. (See [Modify System PROG track settings](../reference/serial-commands/serial-command-dd_ack_not_in_nav.md) for more information on workarounds for some of these.)

## Supported Microcontrollers

Refer to the [microcontroller boards](../reference/microcontrollers/index.md) list for information on supported microcontrollers.

## Supported Motor Drivers

Refer to the [motor drivers](../reference/hardware/motorboards/index.md) list for information on supported motor drivers.

## Other Supported devices

See the [Supported Device List](../enhance/accessories/hardware-list.md) and [I2C (I<sup>2</sup>C) pages](../enhance/accessories/i2c/index.md) for some of the other devices the **EX-CommandStation** currently supports.

RAILCOM support is currently being investigated.

----

## Not Supported Devices

The following devices are NOT supported:

- Arduino UNO and Nano. We have supported them in the past but the increase in **EX-CommandStation** features has outstripped their miniscule memory capabilities.
- Mega Wifi. Some users have had success with this but we have had approximately 50% failure rate on these devices. Its just not worth it.
- Arduino Giga. This has a very high cost and some strange WiFi limitations.
- Teensy (various models). These have been made to work in the past but without help we are unable to update or support them.
- Most ESP32 versions. There are dozens of ESP32 versions and the vast majority of them will not be able to run **EX-CommandStation**. We can only support the explicitly recommended *ESP32 Wroom* version.
- UNO R4 WiFi. Useless and expensive.
- Nano Every.  Not enough FLASH memory.
- Pi Pico.  Lack of demand and awkward form factor for shields.
- [Motor shields](../reference/hardware/motorboards/index.md) other than those recommended.

Many of these require modification or simply do not provide the features we need. Even the Arduino standard motor shield (which we do support) is not capable of the full range of the newer **DCC-EX** functions and requires physical modification to avoid melting your processor.

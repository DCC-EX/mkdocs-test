# Programming DCC locos

The EX-CommandStation is capable of programming CVs of mobile decoders on the PRG track (Service Mode) and on the MAIN track (Ops mode / Programming on the Main - PoM).

## The PROG track

In normal DCC operation, running locos happens on a MAIN track (your layout) and programming takes place on a separate piece of track (typically just long enough for your loco) called a PROG track. You loco will not respond to throttles if it is on the PROG track, and the command station will not send programming commands to the MAIN track.

Some command stations are not able to do programming and running at the same time, this restriction does not apply to **DCC-EX**.

DCC-EX provides some tricks to switch tracks in software, perhaps because you only have a single loco or your PROG track is actually an isolated siding on a layout. See the [Track Manager](/products/ex-commandstation/trackmanager/trackmanager.md) pages for more information.

## Reading/Writing decoder settings

Simple programming usually involves detecting or changing the DCC address of a loco. More advanced programming, especially involving sound locos can be very complex and varies from decoder to decoder, even when they are made by the same manufacturer.

The **EX-CommandStation** provides the underlying technology to read and write individual decoder settings (called CVs) plus some higher-level functions to simplify this process for common problems like reading or writing a loco address which involves many reads or writes.

There are a number of ways you can program decoders:

* With [serial input commands](#programming-using-serial-input-commands)
* With the [Engine Driver](#programming-using-engine-driver) app
* With the [EX-Toolbox](#programming-using-ex-toolbox) app
* With [JMRI Decoder Pro](#programming-with-jmri-decoderpro)
* With other [smart device](#programming-with-smart-devicethrottle-apps) apps, or PC apps

----

## Programming using Serial input commands

This requires access to the [serial monitor](../../../reference/tools/serial-monitor_not_in_nav.md). It is the most flexible method and can provide diagnostics when things don't work. It also has the flexibility to adjust the tuning parameters to cope with decoders that are way outside the normal decoder electronic standards.

See [Programming with Serial commands](/products/ex-commandstation/loco-programming/serial-programming.md)

## Programming using Engine Driver

The Engine Driver throttle includes simple programming dialogs, including the "Drive Away" feature that allows a throttle to obtain the loco address from a prog track and drive the loco directly without having to re-enter the address.

See [Programming with Engine Driver](/products/ex-commandstation/loco-programming/engine-driver-programming.md)

## Programming using EX-Toolbox

The **EX-Toolbox** Android application, includes simple programming dialogs and some more advanced features such as a speed matching tool used to adjust loco speed tables to match with another loco so that they can be coupled together in a consist.

See [Programming with EX-Toolbox](/products/ex-commandstation/loco-programming/toolbox-programming.md)

## Programming with JMRI DecoderPro

There are very few "standards" relating to DCC decoders and there are hundreds of incompatible devices in use around the world. JMRI DecoderPro contains a massive database of decoder types, and their quirks, built up over many years of experience.

For advanced programming, this is the tool of choice.

See [Programming with DecoderPro](/products/ex-commandstation/loco-programming/decoderpro.md)

## Programming with Smart Device/Throttle Apps

A number of Throttle apps for iOS and Android are capable of reading and writing to decoders. There are also a few for Microsoft Windows and Apple MacOS.

Refer to the [Throttles](../../../throttles/throttles.md#comparison-table) lists to see which apps can.  Then refer to the specific documentation of that app to find out how.

--8<-- "snippets/abbr.md"

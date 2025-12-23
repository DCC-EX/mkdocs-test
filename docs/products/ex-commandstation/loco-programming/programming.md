# Programming DCC locos

## The PROG track

In normal DCC operation, running locos happens on a MAIN track (your layout) and programming takes place on a separate piece of track (typically just long enough for your loco) called a PROG track. You loco will not respond to throttles if it is on the PROG track, and the command station will not send programming commands to the MAIN track.

Some command stations are not able to do programming and running at the same time, this restribction does not apply to DCC-EX.

DCC-EX provides some tricks to switch tracks in software, perhaps because you only have a single loco or your PROG track is actually an isolated siding on a layout. See [Track Manager](/products/ex-commandstation/trackmanager/trackmanager.md)

## Reading/Writing decoder settings

Simple programming usually involves detecting or changing the DCC address of a loco. More advanced programming, especially involving sound locos can be very complex and varies from decoder to decoder, even when they are made by the same manufacturer.

The EX_Command station provides the underlying technology to read and write individual decoder settings (called CVs) plus some higher-level functions to simplify this process for common problems like reading or writing a loco address which involves many reads or writes.

## Programming using Serial input commands

This requires access to the serial monitor. It is the most flexible method and can provide diagnostics when things dont work. It also has the flexibility to adjust the tuning parameters to cope with decoders that are way outside the normal decoder electronic standards.

See [Programming with Serial commands](/products/ex-commandstation/loco-programming/serial-programming.md)

## Programming using Engine Driver

The Engine Driver throttle includes simple programming dialogs, including the "Drive Away" feature that allows a throttle to obtain the loco address from a prog track and drive the loco directly without having to re-enter the address.

See [Programming with Engine Driver](/products/ex-commandstation/loco-programming/engine-driver-programming.md)

## Programming using EX-Toolbox

The EX-Toolbox Android application, includes simple programming dialogs and some more advanced features such as a speed matching tool used to adjust loco speed tables to match with another loco so that they can be coupled together in a consist.

See [Programming with EX-Toolbox](/products/ex-commandstation/loco-programming/toolbox-programming.md)

## Programming with JMRI DecoderPro

There are very few "standards" relating to DCC decoders and there are hundreds of incompatible devices in use around the world. JMRI DecoderPro contains a massive database of decoder types, and their quirks, built up over many years of experience.

For advanced programming, this is the tool of choice.

See [Programming with DecoderPro](/products/ex-commandstation/loco-programming/decoderpro.md)

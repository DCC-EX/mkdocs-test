# Testing your commnd station

 (LOTS OF TODO in this file)

 ## In Summary

(Ian note: I have only made a start on this summary section. I hope it gives everyone a sense for what I would have loved to find in one place as a conductor.)
We hope your Command Station works out of the box. If it doesn't, don't worry, we know a bunch of this stuff can be unfamiliar and we're here to help you get it working. This guide is your first port of call. The key steps to check first, in this order, are:
1. Is the LED on the circuitboard showing a functioning microcontroller? (if it isn't try unplugging from power and plugging it back in again).
2. Have you been able to assemble it all together OK or are you worried that something "doesn't look right"? Double check here: to see our reference visuals. If you're using a CSB1, then you can skip this step.
3. Have you been able to connect your computer to the Command Station via a USB connector, and then been able to successfully load the DCC-EX software? You might have had issues finding a "com port" (see link). Possibly the installer came up with errors and now your stuck? If you are, here's the link to get that working as easily as possible: abc link (don't forget the CH340 driver issue).
4. If you've done the above, have you been able to connect up your computer to the Command Station and get any information from it via USB? If you can't connect and get error messages about COM ports, 'no port available' or somesuch, close any other programs that may be using it. The classics are to leave either the Arduino IDE or JRMI open and then your Command Station may be connect at all! If all else fails, turn your Command Station off, turn your computer off, disconnect the USB cable, reconnect the cable and power up again.
5. If you are brand new to the world of DCC, and have left the installer loading with our default configuration, have you connected your track power to the 'A Output/MAIN' from the controller? The other output, 'B/PROG' will not run locos forwards or backwards without more changes to your system! It is there solely to program and test the DCC decoders on your locos. Welcome to some of the differences of DCC. You can change all these settings in your Command Station but that's for later. Connect the track up to 'MAIN'.

If you have tried these steps and you still can't get the Command Station to work, head over to our Discord server and chat to the community and the suppor team.
(Ian's edits finish here - moving forward with this once I've got a bit of feedback. There may well be more common problematic steps to get started. Having these spelled-out would have made things so much more reassuring for me. I had pretty much all of them when building a MEGA-based CS)

The simplest and most direct testing method is to use a serial monitor to talk directly to the USB connection of you command station. This is a fundamental aspect of the Arduino system and thus avoids issues such as wifi connections. Indeed, this is the only way to see what's going wrong if your problems are wifi related.

## Serial Monitors

There are several serial monitors available:

--8<-- "includes/ex-installer/device-monitor.md"

- Built in to the [EX-Installer](?EX-Installer)
    ??? TODO EX INSTALLER showing serial log
- Built in to VSCode is you are using that as an IDE.
- Built in to the Arduino IDE (We do not recommend that for development)
- Built in to the EX-WebThrottle
- Built in to JMRI or other train control software.
(TODO.. above provide links to individual side-pages showing how to get at the serial monitor in each case)

Whichever you use, please ensure the baud rate is set to 115200 so that it matches that used by the command station. (Installer anf WebThrottle do this automatically)

Its important to note that only one program on your PC can be connected to the Command Station USB. It is a common cause of error messages if you try and open a serial monitor when one of the other programs is still running.

In most cases, connecting a serial monitor causes the Command station to restart.

## Simple testing commands (Main track)

Commands are entered as shown, complete with the `< >` markers. Case is important because `<T` is a compl;etely different command to `<t`

### Check communication and version

```cpp
<s>
```

TODO... pic

### Turn on track power

`<1>` will turn on all 4 leds that lie behind the track output sockets.

`<0>` Will turn the tracks off.

### Move a loco

You can only drive a loco if you know the loco DCC address. For a brand new loco or decoder this is normally preset to 3.
If you don't know the loco address, then you can find out using the [simple programming commands](/reference/serial-commands.md)

Assuming you know the loco address is 3, the following commands may be useful:  

`<!>` Emergency stop all locos

`<t 3 50 1>`  Move loco 3 speed 50 forward.

`<t 3 20 0>`  Move loco 3 speed 20 referse.

`<t 3 0 1>`  Stop loco 3 (decoder may stop loco realistically)

`<t 3 -1 1>`  Emergency Stop loco 3

### Test loco functions

`<F 3 0 1>`   Turn on loco 3 function 0

`<F 3 0 0>`   Turn off loco 3 function 0

## Things to remember

The commands `<t` and `<F` will normally reply with a `<l` response when something about a loco is changed. This response is designed for throttles to share information and not generally for human reading.

A response of `<X>` indicates the command was not understood by the command station, so check your typing as `<T` and `<f` are not the same as `<t` and `<F`.

DCC generally has no way of knowing whether the loco exists, is listening or has dirty wheels. If you get no movement the first thing to do is check the track is clean.

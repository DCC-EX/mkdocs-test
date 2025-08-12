# Testing your Command Station

 (LOTS OF ==TODO== in this file)

The simplest and most direct testing method is to use a serial monitor to talk directly to the USB connection of you command station. This is a fundamental aspect of the Arduino system and thus avoids issues such as wifi connections. Indeed, this is the only way to see what's going wrong if your problems are wifi related.

## Serial Monitors

There are several serial monitors available:

--8<-- "snippets/ex-installer/device-monitor.md"

- Built in to the [EX-Installer](?EX-Installer)
    ??? ==TODO== EX INSTALLER showing serial log
- Built in to VSCode is you are using that as an IDE.
- Built in to the Arduino IDE (We do not recommend that for development)
- Built in to the EX-WebThrottle
- Built in to JMRI or other train control software.
(==TODO==.. above provide links to individual side-pages showing how to get at the serial monitor in each case)

Whichever you use, please ensure the baud rate is set to 115200 so that it matches that used by the command station. (Installer anf WebThrottle do this automatically)

Its important to note that only one program on your PC can be connected to the Command Station USB. It is a common cause of error messages if you try and open a serial monitor when one of the other programs is still running.

In most cases, connecting a serial monitor causes the Command station to restart.

## Simple testing commands (Main track)

Commands are entered as shown, complete with the `< >` markers. Case is important because `<T` is a completely different command to `<t`

### Check communication and version

```cpp
<s>
```

==TODO==... pic

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

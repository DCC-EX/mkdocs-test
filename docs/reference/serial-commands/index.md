# DCC-EX Serial Commands Overview

- Serial commands are accepted as input from the USB serial connection or a TCP/IP connection.
- Commands have a single case dependent character opcode and optionally parameters.
- Keyword parameters are shown in upper case but may be entered in mixed case.
- Value parameters are decimal numeric (unless otherwise noted)
- Not all commands have a response, and broadcasts mean that not all responses come from the last commands that you have issued.
- Commands entered like ```<JA>``` are actually read as ```<J A>```, so ```<Ja>``` is also acceptable.
- Commands that produce diagnostic information (which is intended for human reading rather than code) only write to the USB Serial output.
- Commands that cause state changes (such as loco speeds, turnout position) cause broadcasts to all serial connections and, where appropriate, WiThrottle protocol connections.

## Conventions used for command descriptions

- ``<`` and ``>`` - All DCC-EX commands are surrounded by these characters to indicate the beginning and end, these must always be included
- First letter or number - These are called OPCODES, are case sensitive, and must be specified as directed, e.g. ``1``, ``c``, or ``-``
- CAPITALISED words - These are parameters referred to as keywords, and should be specified as directed, e.g. ``MAIN`` (note these are not case sensitive, however capitalising makes them easier to distinguish from other parameters)
- lowercase words - These are parameters that must be provided or are returned, with multiple parameters separated by a space " ", e.g. ``loco`` or ``«loco»``
- Square brackets ``[]`` - Parameters within square brackets ``[]`` are optional and may be omitted, and if specifying these parameters, do not include the square brackets themselves
- \| - Use of the \| character means you need to provide one of the provided options only, for example ``<0|1 MAIN|PROG|JOIN>`` becomes either ``<0 MAIN>`` or ``<1 MAIN>``
- ``0|1`` DIRECTION: 1=forward, 0=reverse.

## Common Elements / Parameters

The following are element / parameters that are common across multiple commands and are described here for ease of reference.

| Parameter | Description |
| -- | -- |
| **cab** or <br/>**loco** | The short (1-127) or long (128-10293) address of the engine decoder. <br/> (This has to be already programmed in the decoder.) <br/> Note: DCC-EX commands do not distinguish between short and long DCC addresses, so you can use the same command format for both. |
| **dir** or <br/>**direction** | One of <br/>- 1=forward <br/>- 0=reverse |
| **tSpeed** | 0-127 or -1 for Emergency Stop |
| **speedByte** | Speed in DCC speedstep format. This is an encoded (1-7 bits) byte. <br/>The single value incorporates both speed and direction, with the following values: <br/>- reverse - 2-127 = speed 1-126, 0 = stop, 1 = Emergency Stop <br/>- forward - 130-255 = speed 1-126,  128 = stop, 129 = Emergency Stop |
| **id** | The numeric ID (0-32767) assigned to an element to control. <br/>*ids* are generally unique within the element type, but not across element types. <br/>(NOTE: *ids* are shared between Turnouts/Points, Sensors and Outputs) |
| **vpin** | Generally, the pin number of the physical input or output GPIO to receive information from or to control. <br/>*vpins* are normally assigned to an *id* to use in subsequent commands. <br/><br/>For GPIOs on the microcontroller, this is the same as the pin number.  For servo outputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module, 200-215 for the second PCA9685 Servo Controller module, 300-315 for the first PCA9685 I/O Expander module, and 400-415 for the second PCA9685 I/O  Expander module. |

## Notes

*DCC-EX Serial Commands* are also referred to as *Native DCC-EX Commands/Protocol* or *DCC-EX Native Commands/Protocol*.

Refer to the [WiThrottle VS Native Serial Protocol](../../throttles/withrottle-vs-native-protocol.md) page for information on the differences to the WiThrottle protocol/commands.

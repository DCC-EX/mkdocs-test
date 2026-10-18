# DCC-EX Native/Serial Commands - Overview

When the **DCC-EX** team designed the **DCC-EX EX-CommandStation** they found the 'WiThrottle Protocol' too limiting and came up with a new protocol referred to originally as **DCC++** but later as [DCC-EX Native Serial Protocol or DCC-EX Native Serial Commands](/reference/serial-commands/serial-command-list.md).

The [EXRAIL Full Command List](serial-command-list.md) page contains the full list of supported commands and is automatically updated from the source code.

The [Grouped DCC-EX Serial Command Reference](serial-commands.md) page contains a list of supported commands, broadly group by what they relate to.  This list is manually updated and may a) be incomplete and b) may lag behind the full list.

## Usage

**Engine Driver**, **EX-WebThrottle**, **EX-Toolbox**, **JMRI** and a few other apps can use the more powerful **DCC-EX Native Serial Protocol** (rather than WiThrottle) when connecting to a **DCC-EX** **EX-CommandStation**.

**Engine Driver** can also use the **DCC-EX Native Protocol** to connect to a **DCC-EX** **EX-CommandStation** via **JMRI** but you need to enable the **'DCC++ over TCP Server'** in the **'DCC++'**' menu in **Decoder-Pro**.

See the [WiThrottle Protocol VS DCC-EX Native/Serial Commands](../../throttles/withrottle-vs-native-protocol.md) page for general information.

--8<-- "snippets/abbr.md"

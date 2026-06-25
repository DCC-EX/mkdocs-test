# WiThrottle Protocol VS DCC-EX Native/Serial Commands

**EX-CommandStation** supports both the **WiThrottle protocol** and the **DCC-EX Native Serial protocol/commands**.

This page describes the difference between the **WiThrottle Protocol** and the **DCC-EX Native Serial protocol/commands**.

## WiThrottle

'WiThrottle' is a trademark owned by Brett Hoffman.

'WiThrottle' is also an [iOS app](https://www.withrottle.com/html/home.html) developed by Brett Hoffman which has similar capabilities to **Engine Driver** on Android.

The 'WiThrottle protocol' is a communications protocol developed by Brett Hoffman.  It is used by **JMRI**, **Engine Driver**, the **WiThrottle** app and a number of other apps and commercial DCC Command Stations.

### WiThrottle Servers

WiThrottle stands for 'WiFi Throttle', and a 'WiThrottle Server' is just software running on your **JMRI** computer, **DCC-EX EX-CommandStation**, or dedicated device. It's called a 'Server' because it allows you to connect to it and it 'serves', or services, requests from another application. That application is called a 'Client'.

The 'WiThrottle Protocol' itself is a standard for how WiFi throttles can communicate with the WiThrottle Server, much like the DCC standard is a standard for how data packets communicate with decoders. What this means for you, is that **Engine Driver** and other apps can talk to any WiThrottle compatible server, which in turn can talks to your DCC encoders in your locos.

## DCC-EX Native protocol / commands

When the **DCC-EX** team designed the **DCC-EX EX-CommandStation** they found the 'WiThrottle Protocol' too limiting and came up with a new protocol referred to originally as **DCC++** but later as [DCC-EX Native Serial Protocol or DCC-EX Native Serial Commands](/reference/serial-command-list.md).

**Engine Driver**, **EX-WebThrottle**, **EX-Toolbox**, **JMRI** and a few other apps can use the more powerful **DCC-EX Native Serial Protocol** when connecting to a **DCC-EX** **EX-CommandStation**.

**Engine Driver** can also use the **DCC-EX Native Protocol** to connect to a **DCC-EX** **EX-CommandStation** via **JMRI** but you need to enable the **'DCC++ over TCP Server'** in the **'DCC++'**' menu in **Decoder-Pro**.

----

## Which Should You Use?

The **WiThrottle Protocol** is adequate for running trains, throwing turnouts/points and selecting Routes.

What the **WiThrottle Protocol** can't do is *CV programming*, *Track Manager changes*, and *system configuration*.

The **DCC-EX Native Commands** can do these and a lot more.

So if you have the option to use a throttle/controller that uses the **DCC-EX Native Commands** it is worthwhile doing so.  However if you can't then the **WiThrottle protocol** is just fine for *running* the average layout.

You can refer the [throttle/controller list](/throttles/throttles.md) to see which controllers support **DCC-EX Native Serial Commands**.

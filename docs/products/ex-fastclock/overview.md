# EX-FastClock

Welcome to the home of EX-FastClock, a fully integrated Fast Clock for EX-CommandStation.

EX-FastClock is a standalone adjustable speed clock built using an additional Arduino Uno microcontroller and a plug-in shield type TFT touch screen.  The commands built into the DCC_EX Command Station make it possible to also integrate an existing microcontroller based fast clock.

Note: if you only want a real-time clock to make things happen at certain times of day, then the [DS1307](?DS1307) is a simpler/cheaper alternative.

## Background

This project is based on a project originally written by Jim Gifford (Hallet Cove Southern) in June 2017.  This project used a 32 x 8 LED matrix to display the time and was controlled by a number of pushbuttons.

[See Jim's Original Project here.](https://www.hallettcovesouthern.com/track-plan-design-info/arduino-projects/fast-clock/)

I felt that this project was ripe for an update and decided to convert Jim's code to operate using a cheap TFT/LCD touch screen to run on my own layout. This project is the result.  Much of the code has been rewritten into smaller functions with additional features added, but the time clock calculations are the originals.

This project has now been extended to add the capability of integrating the clock to the DCC-EX Command Station and more specifically the EXRAIL automation feature which now allows time based control. This feature is optional and can be controlled by the config.h file.

## What is EX-FastClock?

EX-FastClock is a standalone microprocessor based fast adjustable speed clock, using an additional Arduino Uno in conjunction with a shield based TFT touchscreen. Features have been added to EX-CommandStation to allow the clock to integrate to the EX-CommandStation and control EXRAIL based on time events.

![EX-FastClock](/_static/images/ex-fastclock/Fastclock.png){ align=right }

Each time the time changes the EX-CommandStation looks for a time change event and if it finds a match it executes the commands recorded for that event as defined in the EXRAIL myAutomation.h file.  Additionally the EX-CommandStation will issue a time broadcast so that other devices such as clock repeaters can capture the time.  Also where WiThrottle devices are connected a WiThrottle broadcast is made which means that connected devices such as Engine Driver can display the time.

EX-FastClock allows the FastClock device to connect to the EX-CommandStation via either Serial Communications or I2C.  Even though EX-FastClock provides the code for an Uno based Clock it should be possible for tinkerer level users to add the relevant code if they already have a working clock that they wish to integrate to EX-CommandStation.

To make full use of EX-FastClock**, you will need a basic understanding of EX-RAIL automation, but we'll share the details and some examples to help with this.

**NOTE**: EX-FastClock is in public Beta testing, and as such, we encourage regular feedback on the success or otherwise of both the software and documentation. Please reach out via any of our support methods and help us get EX-FastClock as easy to use and reliable as possible.

The EX-FastClock integration includes:

- A ready-made Arduino program for an Arduino Uno based Fast Clock
- Support for Serial connection
- |I2C| device driver
- EX-RAIL automation support
- Time Broadcast for time display on WiThrottle controllers such as |Engine Driver|
- Debug output to Serial Monitor

## Credit where credit is due

*The EX-FastClock is based on a project originally written by Jim Gifford (Hallet Cove Southern) in June 2017. That project used a 32 x 8 LED matrix to display the time and was controlled by a number of pushbuttons. You can see [Jim's Original Project here](https://www.hallettcovesouthern.com/track-plan-design-info/arduino-projects/fast-clock/).

- MCUFRIEND.kbv credit: This library was written by David Prentice and has become the De-Facto standard for the shield based TFT screens used in this project. This library inherits from the Adafruit GFX library.
- Adafruit for the Adafruit GFX Library.

## Next Steps

Now that you have a general overview of EX-FastClock's features and capabilities, click the "next" button see what is needed to create an EX-FastClock.

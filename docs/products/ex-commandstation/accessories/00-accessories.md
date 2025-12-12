# Connecting Accessories

Once you go beyond just wanting to run trains, and want to control turnouts, signals, and potentially automate other various parts of your layout, you will need to know how to connect accessories to your Command Station.

This includes our other products such as EX-FastClock, EX-IOExpander, EX-SensorCAM, and EX-Turntable.

## Accessory Types

There are generally three ways accessories can be connected to and controlled by your Command Station:

- I2C
- Serial
- DCC accessories attached to a DCC main track output

Throughout these pages, we will be focusing on accessories connected via I2C only.

Most devices connected via Serial are typically throttles or controllers rather than accessories.

When purchasing DCC accessories, you will have received a user manual for these, so follow that for instructions on how to connect them.

## Voltage Differences

!!! danger

    It is essential to be aware that hardware devices may operate at different voltage levels, meaning simply connecting an accessory to your Command Station may lead to damage or incorrect operation should this situation occur.

    This applies to any peripheral device connected directly to your Command Station via either serial or I2C interfaces.

    The most common issue is connecting an accessory designed for 5V operation to a Command Station that operates at 3.3V, such as our EX-CSB1. This will cause damage!

## What is I2C?

If you want the nitty gritty of what I2C is, you can refer to the [Wikipedia article](https://en.wikipedia.org/wiki/I%C2%B2C), which covers more detail than we will here.

To keep it simple and in the context of DCC-EX, I2C is a bus that allows multiple accessories or peripherals to be connected to your Command Station, utilising two signal lines/connections and a common ground connection. While power can be provided by your Command Station, it is recommended to have your accessories powered separately.

Each I2C device must have a unique address in order to be detected and configured by the software.

You will typically see these addresses in hexadecimal format, for example ``0x40``.

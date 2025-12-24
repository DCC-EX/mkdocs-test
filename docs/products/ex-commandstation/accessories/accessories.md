# Overview - What are Accessories?

Once you go beyond just wanting to run trains, and want to control turnouts (points), signals, turntables, and potentially automate other parts of your layout, you will need to know how to connect accessories to your Command Station.

Within the DCC-EX ecosystem, an accessory is anything you can connect to or control from your EX-CommandStation which also includes our other products such as EX-FastClock, EX-IOExpander, EX-SensorCAM, and EX-Turntable.

## Accessory Types

Accessories are broadly divided into two categories:

- Outputs:

    - Turnouts or points
    - Signals
    - Turntables
    - Lighting
    - Servos

- Inputs:

    - Sensors
    - Push buttons
    - Keypads
    - Rotary encoders
    - Clocks

Note that we consider throttles/controllers differently to accessories, so these are not covered in this section. See our [Throttles](/throttles/throttles.md) section instead.

## Connecting Accessories

There are generally three ways accessories can be connected to and controlled by your Command Station:

- I2C
- Serial
- DCC accessories attached to a DCC main track output

Throughout these pages, we will primarily be focusing on accessories connected via I2C.

Most devices connected via Serial are typically throttles or controllers rather than accessories.

When purchasing DCC accessories, you will have received a user manual for these, so follow that for instructions on how to connect them.

## Voltage Differences

!!! danger

    It is essential to be aware that hardware devices may operate at different voltage levels, meaning simply connecting an accessory to your Command Station may lead to damage or incorrect operation should this situation occur.

    This applies to any peripheral device connected directly to your Command Station via either serial or I2C interfaces.

    The most common issue is connecting an accessory designed for 5V operation to a Command Station that operates at 3.3V, such as our EX-CSB1. This will cause damage!

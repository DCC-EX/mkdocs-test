# Frequently Answered Questions  (FAQ)

This page contains a summary of answers that are frequently asked and answered in support tickets and on our Discord server.

We encourage our users to reference this ahead of requesting support as there's a good chance your question has been answered many times before!

## Controlling and Running Trains

- Why isn't my train responding to my throttle commands?

    - A loco must be on a DCC **MAIN** track to respond to throttle commands, this is typically output A on an EX-CSB1, EX8874 shield, or Arduino R3 motor shield
    - The DCC **MAIN** track must be powered on either via your throttle software or `<1>` in the serial console
    - If your DCC loco has been configured for a consist, you must control it from the consist address, not the loco address. The lights can be switched on/off at the loco address but the loco will not move unless you use the consist address.

## Programming and reading DCC decoders

- How do I change the DCC address of my loco?

    - Place the loco on the programming track and issue `<W address>` or use the programming screen in Engine Driver.

- Why does programming my decoder result in an error (eg. a JMRI 308 error)?

    - Loco must be on prog track
    - Dirty track, wheels or pickups
    - Issue the `<D ACK ON>` and repeat the programming, copy resulting diagnostic trace to support (or learn to read it yourself)

## Throttle apps and software

- I'm using the free WiThrottle Lite app on iOS, how can I turn track power on?

    - You can't turn track power on with the free WiThrottle Lite app for iOS, you must turn it on via the serial console with `<1>`
    - Alternatively, you can enable the `Start with power on` option in EX-Installer

## My CSB1 OLED display isnt working or looks "wrong"

- The CSB1 is shipped with whichever OLED display is available and although they look alike, they have different internals. The EX-Installer provides a dropdown list, if yours doesnt work, try selecting the other option.

## Why do I get FAULT pin warnings

- You may have a short on your layout. Most common causes are
  
    - Loco driven into turnout set for the other track
    - Screwdriver or other tools left lying on layout

- You forgot to switch on the track power supply
- When switched on, there is an inrush of power to the loco decoders which temporarily exceeds the current limits. This is automatically fixed and the state should revers to NORMAL within a second or so.

## Why do my I2C connections fail

This can be complex but

- At startup, the Command Station lists all the I2C devices it can see... If yours is not in that list there is nothing that you can change or configure in the software to make it work.
- Do not twist the SCL and SDA wires together
- Avoid running SCL/SD in parallel with the track power (or track)
- Refer to [I2C Wiring](/reference/wiring/i2C/i2c-wiring.md)

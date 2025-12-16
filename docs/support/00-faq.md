# Frequently Answered Questions

This page contains a summary of answers that are frequently asked and answered in support tickets and on our Discord server.

We encourage our users to reference this ahead of requesting support as there's a good chance your question has been answered many times before!

## Controlling and Running Trains

- Why isn't my train responding to my throttle commands?

    - A loco must be on a DCC **MAIN** track to respond to throttle commands, this is typically output A on an EX-CSB1, EX8874 shield, or Arduino R3 motor shield
    - The DCC **MAIN** track must be powered on either via your throttle software or `<1>` in the serial console
    - If your DCC loco has been configured for a consist, you must control it from the consist address, not the loco address

## Programming and reading DCC decoders

- How do I change the DCC address of my loco?

    - Place the loco on the programming track and issue `<W address>`

- Why does programming my decoder result in an error (eg. a JMRI 308 error)?

    - Must be on prog track
    - `<D ACK ON>` for diagnostic info

## Throttle apps and software

- I'm using the free WiThrottle Lite app on iOS, how can I turn track power on?

    - You can't turn track power on with the free WiThrottle Lite app for iOS, you must turn it on via the serial console with `<1>`
    - Alternatively, you can enable the `Start with power on` option in EX-Installer

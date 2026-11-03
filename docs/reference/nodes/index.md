# Introduction to Using Distributed Layout Nodes

Distributed Layout **Nodes** offer a simple way of physically distributing layout control (usually wirelessly) over a wide area, using additional microprocessors, running essentially the same **EX-CommandStation** software in each node.

## Basic Principles

Traditionally, a layout is controlled entirely by a single microprocessor, known as the Command Station (**EX-CommandStation**), which performs many tasks simultaneously:

- Communicating with throttles
- Controlling and generating the track output
- Running **EXRAIL** scripts
- Handling accessories
- Displaying on oLED displays
- Lighting
- Sounds
- Turntable operations
- Making coffee

In some cases, particularly large layouts, it would be preferable to offload some of these functions to separate microprocessors, mostly for ease of wiring... performance is rarely an issue.

By using the Distributed Layout **Node** system, the separate microprocessors will automatically intercommunicate. They use essentially the same **EX-CommandStation** code, including **EXRAIL** and HAL drivers in each node.

For example, in addition to the normal **EX-CommandStation**, a node may be established to handle a group of turnouts/points on one area of your layout. The physical turnouts/points would be connected to the node using the usual hardware (MCP32017, PCA9685 etc) and usual **EXRAIL** definitions but there would not be any need to wire the **Node** to the **EX-CommandStation** or deal with long I2C connections.

The **EX-CommandStation** would automatically know about the turnouts/points connected the other node, and can still throw/close the turnout/point in the same way as normal, and keep throttles informed, but the remote node would perform the physical movement.

## Shared Objects

Object sharing is generally done for things that have an id that is separate from the VPIN associated with some particular hardware implementation.

The following object types are shared amongst the nodes automatically

- Turnouts/points can be thrown, closed or monitored from any node.
- Signals can be set or monitored from any node
- Turntables (code pending)

Sensors (a sensor definition is actually a VPIN monitoring task, not the actual sensor hardware) are only shared by consent. The node with the sensor hardware needs to share the sensor with a suitable unique id to avoid clashes with other nodes hardware.

- Input (sensor) VPINs can be monitored by any node
- Output VPINSs can be set by any node... The implication of this is that most devices like DFPlayers, NeoPixels, Leds can be controlled by any node as long as the node with the real device has deliberately accepted the VPIN numbers using the SHARED_WRITE_VPINS macro.  

## Node Processors

Because the nodes do not have to handle the creation of the DCC waveform (i.e. power track and drive trains), or deal with the weird and wonderful assortment of throttle connections, a node can be created using a much cheaper processor than the **EX-CommandStation** and without the motor driver requirement.

However, a **EX-CSB1** being used as a booster is effectively a node and can handle other devices as well.

## Node Configuration

Every effort has been made to minimise the configuration/scripting changes but this is best seen by viewing the cookbook entries that follow.

In particular, there is no visible concept of a node id or targetting commands to a particular node.

It is assumed that the reader intending to implement nodes is familiar with the **EX-CommandStation** way of defining and using devices with **EXRAIL**.

## Flashing Nodes

Each node will need its own ``myAutomation.h`` but otherwise operates exactly the same **EX-CommandStation** code. A definition (or possibly runtime switch) prevents the node from advertising itself to throttles or trying to generate a DCC waveform.

( ==TODO== Installer assist in managing this?)

## Node WiFi

The node must be able to identify the WiFi SSID/Password to get on to the same network as the other devices. Since we now have a **EX-CSB1** way of setting WiFi from a command , the node can be configured over USB (or any other viable input such as a browser, throttle or toolbox connected to the node's Access Point (AP)) with the `<C WIFI "ssid" "password">`  command and it will stick.
(without the Node code, you would have had to code that manually somewhere.)

- It is very convenient to use `<C WIFI HOSTNAME "nodename">` to set the nodes hostname so that you can easily open a browser to `http://nodename/` and monitor the node as for the **EX-CommandStation**.

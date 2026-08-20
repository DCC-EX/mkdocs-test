# Throttle Developers Guide - Overview

These pages are a brief set of notes to help people write/create their own software or physical/hardware throttle/controllers to use the **DCC-EX** EX-CommandStations.

The EX-CommandStation can communicate with either Native/Serial Protocol or the WiThrottle protocol.  Only the Native/Serial Protocol is discussed here. If you wish to use the WiThrottle protocol see the [JMRI Web Site](https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml) for more information.

## General

If you are creating a physical throttle using an ESP32 microcontroller, you are strongly advised to make use of the [DCCEXProtocol library](https://github.com/DCC-EX/DCCEXProtocol).

The commonly used speed, function, loco programming and diagnostic commands are discussed elsewhere with users in mind. However, there are a large number of commands designed only to be used by other programs such as JMRI, Engine Driver or other throttles specifically aimed at the **DCC-EX** Native/Serial Protocol. (not WiThrottle)

Many commands that have been implemented to assist throttle authors to obtain information from the **EX-CommandStation** in order to implement turnout/point, route/automation and roster features.
Some of these commands are deliberately multi-stage requests to avoid timing and blocking issues caused by massive transmissions (e.g. a full list of turnouts/points with descriptions) that can cause **EX-CommandStation** issues.

Broadcast replies are also designed so that a throttle can maintain loco speed and function states, turnout/point positions and route states.

--8<-- "snippets/abbr.md"

---
tags:
  - _9T9
  - _9J9_9T9
  - _9J9_9T9_id
  - _9J9_9A9
  - _9J9_9A9_id
  - _9J9_9R9
  - _9J9_9R9_id
  - _m_9LINEAR9
  - _m_loco_accelerating_braking
  - _m_loco_momentum
  - _m_9POWER9
---

# Throttle Writers Guide (doc incomplete)

This page is a brief set of notes to help people write/create their own software or physical/hardware throttle/controllers to use the **DCC-EX** EX-CommandStations.

The EX-CommandStation can communicate with either Native/Serial Protocol or the WiThrottle protocol.  Only the Native/Serial Protocol is discussed here. If you wish to use the WiThrottle protocol see the [JMRI Web Site](https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml) for more information.

## General

If you are creating a physical throttle using an ESP32 microcontroller, you are strongly advised to make use of the [DCCEXProtocol library](https://github.com/DCC-EX/DCCEXProtocol).

The commonly used speed, function, loco programming and diagnostic commands are discussed elsewhere with users in mind. However, there are a large number of commands designed only to be used by other programs such as JMRI, Engine Driver or other throttles specifically aimed at the **DCC-EX** Native/Serial Protocol. (not WiThrottle)

Many commands that have been implemented to assist throttle authors to obtain information from the **EX-CommandStation** in order to implement turnout/point, route/automation and roster features.
Some of these commands are deliberately multi-stage requests to avoid timing and blocking issues caused by massive transmissions (e.g. a full list of turnouts/points with descriptions) that can cause **EX-CommandStation** issues.

Broadcast replies are also designed so that a throttle can maintain loco speed and function states, turnout/point positions and route states.

## Considerations for throttle developers

For anyone developing a throttle or controller application, these considerations should be taken into account:

* Refer to the [DCC-EX Native/Serial Commands List](./serial-command-list.md)
* A throttle/controller MUST accept and ignore anything it does not understand
* Track power state has three possible states: On, Off, and Unknown
* There is no concept of a throttle 'acquiring' a loco.
Simply, commands for a loco are sent to the **EX-CommandStation**, and the **EX-CommandStation** 'broadcasts' the status of any/every loco to every throttle any time a change is made to a loco.
* There is no concept of the throttle disconnecting from the **EX-CommandStation**.

## Key Throttle/Controller Commands

Key throttle/controller specific commands are summarised here, refer below for elaboration on the details with examples. Refer to the [DCC-EX Native/Serial Commands List](./serial-command-list.md) for a complete list, or [search for the 'T'](?_T) or ['J R'](?_J_R) commands.

| Command | Response | Description |
| -------------------------------- | -------------------------------- | --------------------- |
| ``<t loco tSpeed dir>`` | ``<l loco slot speedbyte functionMap>`` (Broadcast) | Sets a cab (loco) speed[^1] and direction. (See below for the response) |
| ``<t loco>`` | ``<l loco slot speedbyte functionMap>`` (Broadcast) | Requests a deliberate update of cab (loco) speed[^1]/functions |
| ``<F loco funct state>`` | ``<l loco slot speedbyte functionMap>`` (Broadcast) | Turns cab (loco) decoder functions ON and OFF (See below for the response.) |
| ``<JT>`` | ``<jT id1 id2 id3 ...>`` | Returns the defined turnout/point IDs |
| ``<JT id>`` | ``<jT id state "[description]">`` | Returns the ID, state, and description of the specified turnout/point ID |
| ``<JA>`` | ``<jA id1 id2 id3 ...>`` | Returns the defined automation and route IDs |
| ``<JA id>`` | ``<jA id type "[description]">`` | Returns the ID, type (A=automation or R=route), and description of the specified automation/route ID |
| ``<JR>`` | ``<jR id1 id2 id3 ...>`` | Returns the defined roster entry IDs |
| ``<JR id>`` | ``<jR id "description" "function1/function2/function3/...">`` | Returns the ID, description, and function map of the specified roster entry ID |

[^1]: *tSpeed* VS *speed* VS *speedByte* <br/>**tSpeed** = 0-127 or -1 for Emergency Stop <br/>**speedByte** = <br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; reverse - 2-127 = speed 1-126, 0 = stop, 1 = Emergency Stop <br/>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; forward - 130-255 = speed 1-126, 128 = stop, 129 = Emergency Stop <br/>**speed** is the same as **speedByte**

## Roster Information

The ``<JR>`` command requests a list of cab ids from the roster.
e.g. responding ``<jR 3 200 6336>``
or <jR> for none.

Each Roster entry had a name and function map obtained by:
``<JR 200>``  reply like ``<jR 200 "Thomas" "whistle/*bell/squeal/panic">``

Refer to **EXRAIL** ROSTER command for function map format.

Obtaining throttle status.

``<t loco>``  Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.
    ``<l loco slot speedbyte functionMap>``

**NOTE:** A slot of -1 indicates that the cab is not in the reminders table and this command will not reserve a slot until such time as the cab is throttled.

## Controlling Locos

==TODO== Controlling Locos

### Momentum

The **EX-CommandStation** can apply momentum to throttle movements in the same way that a standards compliant DCC decoder can be set to do. This momentum can be defaulted system wide and overridden on individual locos. It does not use or alter the loco CV values and so it also works when driving DC locos.
The momentum is applied regardless of the throttle type used (or even **EXRAIL**).

Momentum is specified in mS / throttle_step.

There is a new command `<m loco accelerating [brake]>`
where the brake value defaults to the accelerating value.

For example:
`<m 3 0>`   sets loco 3 to no momentum.
`<m 3 21>`   sets loco 3 to 21 mS/step.
`<m 3 21 42>`   sets loco 3 to 21 mS/step accelerating and 42 mS/step when decelerating.

`<m 0 21>`  sets the default momentum to 21mS/Step for all current and future locos that have not been specifically set.
`<m 3 -1>`   sets loco 3 to track the default momentum value.

**EXRAIL**
  A new macro `MOMENTUM(accel [, decel])` sets the momentum value of the current tasks loco ot the global default if loco=0.

Note: Setting Momentum 7,14,21 etc is similar in effect to setting a decoder CV03/CV04 to 1,2,3.

As an additional option, the momentum calculation is based on the difference in throttle setting and actual speed. For example, the time taken to reach speed 50 from a standing start would be less if the throttle were set to speed 100, thus increasing the acceleration.

`<m LINEAR>` - acceleration is uniform up to selected throttle speed.
`<m POWER>`  - acceleration depends on difference between loco speed and selected throttle speed.

----

## Turnouts/Points

The conventional turnout/point definition commands and the ``<H>`` responses do not contain information about the turnout/point description which may have been provided in an **EXRAIL** script. A turnout/point description is much more user friendly than T123 and having a list helps the throttle UI build a suitable set of buttons.

``<JT>`` command returns a list of turnout/point ids. The throttle should be uninterested in the turnout/point technology used but needs to know the ids it can throw/close and monitor the current state.
e.g.  response ``<jT 1 17 22 19>``

``<JT 17>`` requests info on turnout/point 17.
e.g. response ``<jT 17 T "Coal yard exit">`` or ``<jT 17 C "Coal yard exit">``
(T=thrown, C=closed)
or ``<jT 17 C "">`` indicating turnout/point description not given.
or ``<jT 17 X>`` indicating turnout/point unknown (or possibly hidden.)

**NOTE:** It is still the throttles responsibility to monitor the status broadcasts. There is no intention of providing a command that indicates the turnout/point list has been updated since the throttle started.

**NOTE:** Turnouts/Points marked in **EXRAIL** with the HIDDEN keyword instead of a "description" will NOT show up in these commands.

----

## DCC Accessories

==TODO== DCC Accessory Control

----

## Automations/Routes

 A throttle need to know which **EXRAIL** Automations and Routes it can show the user.

 ``<JA>`` Returns a list of Automations/Routes
 e.g. ``<jA 13 16 23>``
 Indicates route/automation ids.
 Information on each id needs to be obtained by
 ``<JA 13>``
 returns e.g. ``<jA 13 R "description">`` for a route
 or  ``<jA 13 A "description">`` for an automation.
 or ``<jA 13 X>`` for id not found

 What's the difference:

   A Route is just a call to an **EXRAIL** ROUTE, traditionally to set some turnouts or signals but can be used to perform any kind of **EXRAIL** function... but its not expecting to know the loco.
   Thus, a route can be triggered by sending in for example ``</START 13>``.

   An Automation is a handoff of the last accessed loco id to an **EXRAIL** AUTOMATION which would typically drive the loco away.
   Thus, an Automation expects a start command with a cab id
   e.g. ``</START 13 3>``

Routes and Automations can also have their current status and caption altered dynamically by **EXRAIL** (docs ==TODO==)

### Route Status

==TODO== Route Status

----

## COMMANDS TO AVOID ==TODO==

``<f cab func1 func2>``     Use ``<F cab function 1/0>``

``<t  slot cab speed dir>`` Just drop the slot number

``<T commands>`` other than ``<T id 0/1>``

``<s>``

``<c>``

----

## Gauges

==TODO== Gauges

----

## TCP vs UDP

==TODO== TCP VS UDP

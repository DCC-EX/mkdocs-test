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

# Considerations for throttle developers

For anyone developing a throttle or controller application, these considerations should be taken into account:

* Generally speaking, most commands do not have direct 'responses'. What generally happens that commands will cause something to be 'broadcast' to **all** throttles/controllers, not just the throttle/controller that sent the command.
* Commands and responses/broadcast are asynchronous (not serial). <br/>i.e. When you issue a command, any response/broadcast caused by the command, if there is one, may not be the next thing that the throttle sees.
* There is no concept of a throttle 'acquiring' a loco.<br/>
Simply, commands for a loco are sent to the **EX-CommandStation**, and the **EX-CommandStation** 'broadcasts' the status of any/every loco to every throttle any time a change is made to any/every loco.
* A throttle/controller MUST accept and ignore anything it does not understand.
* There is no concept of the throttle disconnecting from the **EX-CommandStation**.
* Track power state has three possible states: On, Off, and Unknown.

Refer to the [DCC-EX Native/Serial Commands List](../serial-commands/serial-command-list.md) for more information on all commands.

## Key Throttle/Controller Commands

Key throttle/controller specific commands are summarised here, refer below for elaboration on the details with examples. Refer to the [DCC-EX Native/Serial Commands List](../serial-commands/serial-command-list.md) for a complete list, or [search for the 'T'](?_T) or ['J R'](?_J_R) commands.

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

The ``<JR>`` command requests a list of cab ids from the roster.<br/>
e.g. responding ``<jR 3 200 6336>``<br/>
or ``<jR>`` for none.

Each Roster entry had a name and function map obtained by:<br/>
``<JR 200>``  reply like ``<jR 200 "Thomas" "whistle/*bell/squeal/panic">``

Refer to **EXRAIL** ROSTER command for function map format.

Obtaining throttle status.

``<t loco>``  Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.<br/>
``<l loco slot speedbyte functionMap>``

**NOTE:** A slot of -1 indicates that the cab is not in the reminders table and this command will not reserve a slot until such time as the cab is throttled.

## Controlling Locos

==TODO== Controlling Locos

### Momentum

The **EX-CommandStation** can apply momentum to throttle movements in the same way that a standards compliant DCC decoder can be set to do. This momentum can be defaulted system wide and overridden on individual locos. It does not use or alter the loco CV values and so it also works when driving DC locos.<br/>
The momentum is applied regardless of the throttle type used (or even **EXRAIL**).

Momentum is specified in mS / throttle_step.

There is a new command `<m loco accelerating [brake]>` where the brake value defaults to the accelerating value.

For example:

`<m 3 0>`   sets loco 3 to no momentum.<br/>
`<m 3 21>`   sets loco 3 to 21 mS/step.<br/>
`<m 3 21 42>`   sets loco 3 to 21 mS/step accelerating and 42 mS/step when decelerating.

`<m 0 21>`  sets the default momentum to 21mS/Step for all current and future locos that have not been specifically set.<br/>
`<m 3 -1>`   sets loco 3 to track the default momentum value.

**EXRAIL**
  A new macro `MOMENTUM(accel [, decel])` sets the momentum value of the current tasks loco ot the global default if loco=0.

Note: Setting Momentum 7,14,21 etc is similar in effect to setting a decoder CV03/CV04 to 1,2,3.

As an additional option, the momentum calculation is based on the difference in throttle setting and actual speed. For example, the time taken to reach speed 50 from a standing start would be less if the throttle were set to speed 100, thus increasing the acceleration.

`<m LINEAR>` - acceleration is uniform up to selected throttle speed.<br/>
`<m POWER>`  - acceleration depends on difference between loco speed and selected throttle speed.

----

## Turnouts/Points

The conventional turnout/point definition commands and the ``<H>`` responses do not contain information about the turnout/point description which may have been provided in an **EXRAIL** script. A turnout/point description is much more user friendly than T123 and having a list helps the throttle UI build a suitable set of buttons.

``<JT>`` command returns a list of turnout/point ids. The throttle should be uninterested in the turnout/point technology used but needs to know the ids it can throw/close and monitor the current state.<br/>
e.g.  response ``<jT 1 17 22 19>``

``<JT 17>`` requests info on turnout/point 17.<br/>
e.g. response ``<jT 17 T "Coal yard exit">`` or ``<jT 17 C "Coal yard exit">`` (T=thrown, C=closed)<br/>
or ``<jT 17 C "">`` indicating turnout/point description not given.<br/>
or ``<jT 17 X>`` indicating turnout/point unknown (or possibly hidden.)

**NOTE:** It is still the throttles responsibility to monitor the status broadcasts. There is no intention of providing a command that indicates the turnout/point list has been updated since the throttle started.

**NOTE:** Turnouts/Points marked in **EXRAIL** with the HIDDEN keyword instead of a "description" will NOT show up in these commands.

----

## Signals

A variety of signals can be defined in **EXRAIL** but they all operate using the same basic logic.

``<JS>`` command returns a list of signal ids. The throttle should be uninterested in the signal technology used but needs to know the ids it can throw/close and monitor the current state.<br/>
e.g.  response ``<jS 1 17 22 19>``

``<JS 17>`` requests info on signal 17.<br/>
e.g. response ``<jS 17 R "Up Home, platform 1">``  (R=red, A=amber, G=Green)<br/>
or ``<jS 17 C "">`` indicating signal description not given.<br/>
or ``<jS 17 X>`` indicating signal unknown (or possibly hidden.)

**NOTE:** It is still the throttles responsibility to monitor the status broadcasts. There is no method to update the signal list once the throttle started.

Signal status changes are reported with the ``<h id state>`` command for example ``<h 17 G>`` meaning signal 17 set green.

**NOTE:** Signals marked in **EXRAIL** with the HIDDEN keyword instead of a "description" will NOT show up in these commands.

----

## DCC Accessories

==TODO== DCC Accessory Control

----

## Automations/Routes

A throttle need to know which **EXRAIL** Automations and Routes it can show the user.

``<JA>`` Returns a list of Automations/Routes<br/>
e.g. ``<jA 13 16 23>``<br/>
Indicates route/automation ids.<br/>

Information on each id needs to be obtained by<br/>
``<JA 13>``<br/>
returns e.g. ``<jA 13 R "description">`` for a route<br/>
or  ``<jA 13 A "description">`` for an automation.<br/>
or ``<jA 13 X>`` for id not found

What's the difference:

* A Route is just a call to an **EXRAIL** ROUTE, traditionally to set some turnouts or signals but can be used to perform any kind of **EXRAIL** function... but its not expecting to know the loco.<br/>
Thus, a route can be triggered by sending in for example ``</START 13>``.
* An Automation is a handoff of the last accessed loco id to an **EXRAIL** AUTOMATION which would typically drive the loco away.<br/>
Thus, an Automation expects a start command with a cab id<br/>
e.g. ``</START 13 3>``

Routes and Automations can also have their current status and caption altered dynamically by **EXRAIL** (docs ==TODO==)

### Route Status

==TODO== Route Status

### Turntables/Traversers

A feature is available to support control of turntables/traversers from throttles, including the ability for throttles to "draw" turntable positions as defined to support graphical operation. If **EXRAIL**** commands are used to define turntables and their associated positions, a description for the turntable as well as each position is able to be defined.

Note that to obtain a complete definition for a turntable/traverser, the turntable object needs to be queried first (``<JO id>``) followed by the position query (``<JP id>``) to obtain all defined positions for the object.

``<JO>`` - Returns a list of turntable IDs.

Example response:

* ``<jT 1 2>`` - Turntable IDs 1 and 2 are defined.

``<JO 1>`` - Returns details of turntable ID 1.

Example responses:

* ``<jO 1 0 1 5 "DCC Turntable">`` - DCC turntable type currently at position 1, with 5 defined positions and a description "DCC Turntable".
* ``<jO 1 1 0 11 "EX-Turntable">`` - EX-Turntable type currently at the home position (0), with 11 defined positions and a description "EX-Turntable"

``<JP 1>`` - Returns all positions for turntable ID 1.

Example responses (will return all positions):

* ``<jP 1 0 0 "">`` - Position 0, unused for DCC turntables, "home" for EX-Turntable
* ``<jP 1 1 100 "Turntable position 1">`` - Position 1, 10 degrees from home
* ``<jP 1 2 1800 "Turntable position 2">`` - Position 2, 180 degrees from home

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

--8<-- "snippets/abbr.md"

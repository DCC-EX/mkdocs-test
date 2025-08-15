# Throttle Writers Guide (doc incomplete)
==TODO==

The commonly used speed, function, loco programming and diagnostic commands are discussed elsewhere with users in mind. However, there are a large number of commands designed only to be used by other programs such as JMRI, Engine Driver or other throttles specifically aimed at the DCC-EX protocol. (not WiThrottle)

Many commands that have been implemented to assist throttle authors to obtain information from the Command Station in order to implement turnout, route/automation and roster features.
Some of these commands are deliberately milti-stage requests to avoid timing and blocking issues caused by massive transmissions (e.g. a full list of turnouts with descriptions) that can cause Command Station issues.

Broadcast replies are also designed so that a throttle can maintain loco speed and function states, turnout poisitions and route states.

## Turnouts

The conventional turnout definition commands and the ``<H>`` responses do not contain information about the turnout description which may have been provided in an EXRAIL script. A turnout description is much more user friendly than T123 and having a list helps the throttle UI build a suitable set of buttons.

``<JT>`` command returns a list of turnout ids. The throttle should be uninterested in the turnout technology used but needs to know the ids it can throw/close and monitor the current state.
e.g.  response ``<jT 1 17 22 19>``

``<JT 17>`` requests info on turnout 17.
e.g. response ``<jT 17 T "Coal yard exit">`` or ``<jT 17 C "Coal yard exit">``
(T=thrown, C=closed)
or ``<jT 17 C "">`` indicating turnout description not given.
or ``<jT 17 X>`` indicating turnout unknown (or possibly hidden.)

**NOTE:** It is still the throttles responsibility to monitor the status broadcasts. There is no intention of providing a command that indicates the turnout list has been updated since the throttle started.

**NOTE:** Turnouts marked in EXRAIL with the HIDDEN keyword instead of a "description" will NOT show up in these commands.

## Automations/Routes

 A throttle need to know which EXRAIL Automations and Routes it can show the user.

 ``<JA>`` Returns a list of Automations/Routes
 e.g. ``<jA 13 16 23>``
 Indicates route/automation ids.
 Information on each id needs to be obtained by
 ``<JA 13>``
 returns e.g. ``<jA 13 R "description">`` for a route
 or  ``<jA 13 A "description">`` for an automation.
 or ``<jA 13 X>`` for id not found

 What's the difference:

   A Route is just a call to an EXRAIL ROUTE, traditionally to set some turnouts or signals but can be used to perform any kind of EXRAIL function... but its not expecting to know the loco. 
   Thus, a route can be triggered by sending in for example ``</START 13>``.

   An Automation is a handoff of the last accessed loco id to an EXRAIL AUTOMATION which would typically drive the loco away.
   Thus, an Automation expects a start command with a cab id
   e.g. ``</START 13 3>``

Routes and Automations can also have their current status and caption altered dynamically by EXRAIL (docs ==TODO==)

## Roster Information

The ``<JR>`` command requests a list of cab ids from the roster.
e.g. responding ``<jR 3 200 6336>``
or <jR> for none.

Each Roster entry had a name and function map obtained by:
``<JR 200>``  reply like ``<jR 200 "Thomas" "whistle/*bell/squeal/panic">``

Refer to EXRAIL ROSTER command for function map format.

Obtaining throttle status.

``<t cabid>``  Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.
    ``<l cabid slot speedbyte functionMap>``

**NOTE:** A slot of -1 indicates that the cab is not in the reminders table and this command will not reserve a slot until such time as the cab is throttled.

## COMMANDS TO AVOID ==TODO==

``<f cab func1 func2>``     Use ``<F cab function 1/0>``

``<t  slot cab speed dir>`` Just drop the slot number
  
``<T commands>`` other than ``<T id 0/1>``
  
``<s>``

``<c>``

## doc ==TODO==

- Route status
- Momentum
- Gauges

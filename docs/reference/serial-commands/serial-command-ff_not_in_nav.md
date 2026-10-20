---
tags:
  - _9F9_loco_9DCCFREQ9_freqValue
  - _9F9_loco_function_onoff
  - _f_loco_byte1
  - _f_loco_group_byte2

search:
  boost: 3
---

# Serial commands to: Set decoder functions or set PWM frequency

Serial command to turn loco decoder functions ON or OFF or set the DC PWM frequency of a track.

``<F «loco» «function» «onOff»>``
``<F «loco» DCCFREQ «freqValue»>``

----

## Commands

* ``<F «loco» «function» «state»>`` = set the function on or off
* ``<F «loco» DCCFREQ «freqValue»>`` = set the PWM frequency

## Parameters

* **loco** *Required*<br/> Loco to set the function or PWM frequency

* If **function** plus **state** are supplied - To set the function on or off
    * **function*: Function to set. ``0``-``68`` (Support for the RCN-212 Functions)
    * **onOff** - one of:
        * ``1`` = on
        * ``0`` = off
* If **DCCFREQ** plus **«freqValue»** are supplied - to set the PWM frequency
    * **«freqValue»** = one of:
        * ==TODO== MEDIUM X = Mid frequency - 490Hz
        * ==TODO== MEDIUM X = High frequency - 3400Hz
        * ==TODO== MEDIUM X = Supersonic - 62500Hz

## Response

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

--8<-- "snippets/serial-commands/broadcast_l.md"

----

## Notes

* Setting requests are transmitted directly to mobile loco decoder.
* Current state of loco functions (as known by commands issued since power on) is stored by the CommandStation - All functions within a group get set all at once per NMRA DCC standards.
* The **EX-CommandStation** knows about the previous settings in the same group and will not, for example, unset F2 because you change F1. If, however, you have never set F2, then changing F1 WILL unset F2
* ``<f «loco» «byte1»>`` is a deprecated version of the command. It is not documented here.
* ``<f «loco» «group» «byte2»>`` is a deprecated version of the command. It is not documented here.

----

## Examples

[Also search for 'F'](?_F)

### Example Commands

* ``<F 3 0 1>`` Turns the headlight ON for CAB (loco address) 3
* ``<F 126 0 0>`` Turns the headlight OFF for CAB 126
* ``<F 1330 1 1>`` Turns the horn ON for CAB 1330

### Example Responses

* ==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

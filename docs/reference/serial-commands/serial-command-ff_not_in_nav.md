---
tags:
  - _F_loco_DCCFREQ_freqvalue
  - _F_loco_function_onoff
  - _f_loco_byte1
  - _f_loco_group_byte2
---

# ``<F «loco» [«function» «state»]|[DCCFREQ «freqValue»]>`` <br/>Set decoder functions or set PWM frequency

Serial command to Turn loco decoder functions ON or OFF or set the DC PWN frequency of the track.

## Command

* ``F``

## Parameters

* **loco** *Required*<br/> Loco to set the function or PWM frequency

* If **function** plus **state** are supplied - To set the function on or off
    * **function*: Function to set. ``0``-``68`` (Support for the RCN-212 Functions)
    * **state** - one of:
        * ``1`` = on
        * ``0`` = off
* If **DCCFREQ** plus **«freqValue»** are supplied - to set the PWM frequency
    * **«freqValue»** = one of:
        * ==TODO== = Mid frequency - 490Hz
        * ==TODO== = High frequency - 3400Hz
        * ==TODO== = Supersonic - 62500Hz

## *Response*

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

--8<-- "snippets/serial-commands/broadcast_l.md"

## *Notes*

* Setting requests are transmitted directly to mobile loco decoder.
* Current state of loco functions (as known by commands issued since power on) is stored by the CommandStation - All functions within a group get set all at once per NMRA DCC standards.
* The command station knows about the previous settings in the same group and will not, for example, unset F2 because you change F1. If, however, you have never set F2, then changing F1 WILL unset F2
* ``<f «loco» «byte1»>`` is a depricated version of the command. It is not documented here.
* ``<f «loco» «group» «byte2»>`` is a depricated version of the command. It is not documented here.

----

## *Examples*

[Also search for !](?_F)

### *Examples Commands*

* ``<F 3 0 1>`` Turns the headlight ON for CAB (loco address) 3
* ``<F 126 0 0>`` Turns the headlight OFF for CAB 126
* ``<F 1330 1 1>`` Turns the horn ON for CAB 1330

### *Example Responses:*

* ==TODO==

---
tags:
  - _F_loco_DCCFREQ_freqvalue
  - _F_loco_function_onoff
  - _f_loco_byte1
  - _f_loco_group_byte2
---

# ``<F «loco» [«function» «state»]|[DCCFREQ «freqValue»]>``<br/>- Set decoder functions or set PWM frequency

Serial command to Turn loco decoder functions ON or OFF or set the DC PWN frequency of the track.

## Command

* ``F``

## Parameters

* **loco:** *Required*<br/> Loco to set the function or PWM frequency

    * ``option`` = explanation of option
    * ...

* **function** plus **state** or **DCCFREQ** plus **direction**
    * **function** plus **state** set the function
        * **function* = function to set. ``0``-``68`` (Support for the RCN-212 Functions)
        * **state** = one of:
            * ``1`` = on
            * ``0`` = off
    * if **DCCFREQ** plus **«freqValue»** are supplied
        * **«freqValue»** = one of:
            * ==TODO== = Mid frequency - 490Hz
            * ==TODO== = High frequency - 3400Hz
            * ==TODO== = Supersonic - 62500Hz

## *Response*

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

``<l «loco» «reg» «speedByte» «functMap»>``

    * **loco** = DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder (this has to be already programmed in the decoder)
    * **reg** not used. We no longer use this but need something here for compatibility with legacy systems. Enter any single digit. > * **speedbyte**:** Speed in DCC speedstep format
        * reverse - ``2``-``127`` = speed ``1``-``126``, ``0`` = stop, ``1`` = Emergency Stop
        * forward - ``130``-``255`` = speed ``1``-``126``, ``128`` = stop, ``129`` = Emergency Stop
    * **FunctMap** individual function states represented by the bits in a byte


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

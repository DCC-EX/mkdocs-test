---
tags:
    - _C_PROGBOOST
    - _D_ACK_LIMIT_value
    - _D_ACK_MAX_value_MS
    - _D_ACK_MAX_value
    - _D_ACK_MIN_value_MS
    - _D_ACK_MIN_value
    - _D_ACK_OFF
    - _D_ACK_ON
    - _D_ACK_RETRY_value
---

# <small>``<D ACK LIMIT|MAX|MIN|OFF|ON [«value» [MS]]>`` <br/>``<C PROGBOOST>``</small> <br/>Modify System PROG track settings

Serial commands to modify the system PROG track settings.

## Commands

* ``D ACK``
* ``C PROGBOOST``

### Command Variations

* ``<D ACK LIMIT «value»>`` Set ACK detection limit mA
* ``<D ACK MAX «value» MS>`` Set ACK maximum duration mS
* ``<D ACK MAX «value»>`` Set ACK maximum duration µS
* ``<D ACK MIN «value» MS>`` Set ACK minimum duration mS
* ``<D ACK MIN «value»>`` Set ACK minimum duration µS
* ``<D ACK ON|OFF>`` Enable/Disable PROG track diagnostics
* ``<D ACK RETRY «value»>`` Set ACK retry count
* ``<C PROGBOOST>`` Configute PROG track boost

## Parameters

* **value**: value to set. 

    For time base commands values are in microseconds (µS) unless the parameter ``MS`` is added, in which case the value will be in milliseconds (ms).

## Response

N/A

## Notes

* The Ack current limit is set according to the DCC standard(s) of 60mA. Most decoders send a quick back and forth current pulse to the motor to generate this ACK. However, some modern motors (N and Z scales) may not be able to draw that amount of current. You can adjust down this limit. Or, if for some reasons your acks seem to be too “trigger happy” you can make it less sensitive by raising this limit.

* The NMRA specifies that the ACK pulse duration should be 6 milliseconds, which is 6000 microseconds (µS), give or take 1000 µS. That means the minimum pulse duration is 5000 µS and the maximum is 7000 µS. There are many poorly designed decoders in existence so DCC-EX extends this range from 4000 to 8500 µS. If you have any decoders that still do not function within this range, you can adjust the ACK MIN and ACK MAX parameters.

* When reading/writing CVs, the program will try again upon failure. The default is ``<D ACK RETRY 2>``, which means 3 attempts before a failure is reported. Each of the unsuccessful attempts is reported in the Serial Monitor or JMRI monitor log. The last unsuccessful attempt remains on the display if in use. To reset the running total, send the command manually: ``<D ACK RETRY 2>``.

    When combined with the ``<D ACK ON>`` Command, the ``<R>`` Command (with or without parameters) can be used for diagnostics, for example when you get a ``-1`` response.

* By default, the programming track has a current limit enabled of 250mA, so any programming activities requiring more than this value will cause power to the programming track to be cut for 100ms. Run the ``C PROGBOOST>`` command to override this if programming decoders trigger current limiting on the programming track.

    When the programming track is switched on with ``<1>`` or ``<1 PROG>`` it will normally be restricted to 250mA according to NMRA standards. Some loco decoders require more than this, especially sound versions. ``<C PROGBOOST>`` temporarily removes this limit to allow the decoder to use more power. The normal limit will be re-imposed when the programming track is switched off with ``<0>`` or ``<0 PROG>`` or the Command Station is reset.

----

## Examples

[Also search for `D ACK`](?_D_ACK)

### Example Commands

==TODO==

### Example Responses

==TODO==

----

## *Hints and Tips*

### **Hornby HM7000 decoders**

The HM7000's DCC implementation has a bug in that the ACK response to a DCC CV read from the decoder on the programming track is far, far too long. So much so, the DCC-EX developers added a feature to cater specifically for the HM7000.

* Make sure the loco is on the PROG output which is typically channel B on the EX-CommandStation.
* Bring up a serial console to the EX-CommandStation, or use the command entry features in EX-Toolbox, EX-WebThrottle or Engine Driver.
* Type and send ``<D ACK MAX 20000>``
* Then try reading the decoder. <br/>Either from the console with <R>, <br/>or with the appropriate buttons in EX-Toolbox, EX-WebThrottle or Engine Driver, <br/>to watch for a response.
* If this isn't working, then also add ``<D ACK MIN 150>``

If this isn't working, then ``<D ACK ON>`` will enable diagnostic output from the CSB1 to show what the <R> is doing.

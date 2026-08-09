---
tags:
  - _/_9LATCH9_latch
  - _/_9UNLATCH9_latch
---

# <small>``</ LATCH «latch»>`` ``</ UNLATCH «latch»>``</small> <br/> Set or remove a latch

Serial command(s) to set or remove a latch.

## Command(s)

* ``</ LATCH «latch»>`` Set pin latch
* ``</ UNLATCH «latch»>`` Remove pin latch

## Parameters

* **latch**: *Required* identifier of the Sensor (0-255)

## Response

==TODO== MEDIUM - Responses

## Notes

==TODO== LOW - Notes

Also refer to the EXRAIL Sensor commands:

* ``JMRI_SENSOR(vpin [,count])`` - Creates ``<S>`` type sensors visible to JMRI
* ``AT( vpin )`` - Causes a sequence to wait until a sensor is active/triggered
* ``AFTER( vpin )`` - Causes a sequence to wait until after a sensor has been triggered
* ``ATTIMEOUT( vpin, timeout_ms )`` - Causes a sequence to wait until either a sensor is active/triggered, or if the timer runs out
* ``IF( vpin )`` - If sensor activated or latched, continue
* ``IFNOT( vpin )`` - If sensor NOT activated and NOT latched, continue
* ``IFTIMEOUT`` - Tests if “timed out” flag has been set by an ATTIMEOUT() sensor reading attempt
* ``ATGTE( vpin, value )`` - Waits for an analog pin to reach a value
* ``ATLT ( vpin, value )`` - Waits for an analog pin to go below a value
* ``IFGTE( vpin, value )`` - Test if analog pin reading is greater than or equal to value
* ``IFLT( vpin, value )`` - Test if analog pin reading is less than value
* ``ATTIMOUT1 ( vpin, value )`` - TBA
* ``ATTIMOUT2 ( vpin, value )`` - TBA
* ``DRIVE ( vpin )`` - TBA
* ``LATCH( vpin )`` - Latches a sensor on
* ``UNLATCH( vpin )`` - Remove LATCH on sensor
* ``ONBUTTON( vpin )`` - Event handler for debounced button presses
* ``ONSENSOR( vpin )`` - Event handler for sensors

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ==TODO== LOW - Example Commands

### *Example Responses:*

* ==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

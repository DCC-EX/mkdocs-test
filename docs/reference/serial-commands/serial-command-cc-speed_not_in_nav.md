---
tags:
  - _9C9_9SPEED289
  - _9C9_9SPEED1289
---

# Serial commands to: Set DCC speed commands number of steps

Serial command to set DCC speed commands number of steps.

``<cmd SPEED28>``
``<cmd SPEED128>``

----

## Commands

* ``<C SPEED128>`` = Set all DCC speed commands to 128 step (default)
* ``<C SPEED28>`` = Set all DCC speed commands as 28 step to old decoders

## Parameters

none

## Response

Response sent to the Serial Monitor only (not WiFi clients).

One of:

* 28 Speedsteps
* 128 Speedsteps

----

## Notes

* Default for the **EX-CommandStation** is 28 Steps
* Responses are sent to the Serial Monitor only (not WiFi clients).

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ``<C SPEED128>`` Set all DCC speed commands to 128 step (default)
* ``<C SPEED28>`` Set all DCC speed commands as 28 step to old decoders

### *Example Responses:*

N/A



<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

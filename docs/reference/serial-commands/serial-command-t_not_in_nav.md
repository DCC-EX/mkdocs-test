---
tags:
  - _t_loco
  - _t_loco_tSpeed_direction
  - _t_ignore_loco_tSpeed_direction
  - 
---

# <small>``<t «loco» [«tSpeed» «direction»]>``</small> <br/>Request or set loco status

Serial commands to request information about a loco or set its speed and direction

## Commands

* ``<t «loco»>`` Request a deliberate update on the loco speed/functions
* ``<t «loco» [«tSpeed» «direction»]>`` Set a loco's speed and direction

## Parameters

* **loco** *Required* <br/> Loco to request information about a loco or set its speed and direction
* **tSpeed**: ``0``-``127`` or ``-1`` for Emergency Stop
* **direction** - one of:
    * ``1`` = forward
    * ``0`` = reverse

## Response

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

--8<-- "snippets/serial-commands/broadcast_l.md"

## Notes

* The speedbyte value is different to the speed sent, as it is an encoded (1,7 bits) byte.
* This starts a reminder process for any external updates to the loco's status.
``<t «reg» «loco» «speed» «direction»>`` is a depricated version of the command. It is not documented here.

----

## Examples

[Also search for 'T'](?_T)

### Example Commands

* ==TODO== LOW - Example Commands

### Example Responses

* ==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

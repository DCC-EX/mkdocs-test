---
tags:
  - _9M9_ignore_d0_d1_d2_d3_d4_d5
  - _9P9_ignore_d0_d1_d2_d3_d4_d5
  - _9M9_ignore_d0_d1_d2_d3_d4
  - _9P9_ignore_d0_d1_d2_d3_d4
---

# <small>``<M «ignore» «d0» «d1» [«d2» [«d3» [«d4» [«d5»]]]]>`` <br/> ``<P «ignore» «d0» «d1» [«d2» [«d3» [«d4»] [«d5»]]]]>``</small> <br/> Send up to 6 byte DCC packet to MAIN or PROG

Serial commands to Send up to 6 byte DCC packet to MAIN or PROG.

!!! warning "These commands can reprogram your decoders"

    THESE ARE FOR DEBUGGING AND TESTING PURPOSES ONLY. DO NOT USE UNLESS YOU KNOW HOW TO CONSTRUCT NMRA DCC PACKETS - YOU CAN INADVERTENTLY RE-PROGRAM YOUR DECODERS

## Command(s)

* ``<M «ignore» «d0» «d1» [«d2» [«d3» [«d4» [«d5»]]]]>`` Send up to 6 byte DCC packet on MAIN track
* ``<P «ignore» «d0» «d1» [«d2» [«d3» [«d4» [«d5»]]]]>`` Send up to 6 byte DCC packet on PROG track

## Parameters

* **ignore**: *Required* not used
* **d0**..**D1**: *Required* - values *in hex* to send
* **d2**..**D5**: *Optional* - values *in hex* to send

## Response

N/A

## Notes

==TODO== LOW - Notes

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ==TODO== LOW - Example Commands

### *Example Responses:*

N/A

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

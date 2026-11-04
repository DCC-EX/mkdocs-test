---
tags:
  - _▪M▪_▫ignore▫_▫d0▫_▫d1▫_▫[d2▫_▫d3▫_▫d4▫_▫d5]▫
  - _▪P▪_▫ignore▫_▫d0▫_▫d1▫_▫[d2▫_▫d3▫_▫d4▫_▫d5]▫
  - _▪M▪_▫ignore▫_▫d0▫_▫d1▫_▫d2▫_▫d3▫_▫d4▫_▫d5▫
  - _▪P▪_▫ignore▫_▫d0▫_▫d1▫_▫d2▫_▫d3▫_▫d4▫_▫d5▫
  - _▪M▪_▫ignore▫_▫d0▫_▫d1▫
  - _▪P▪_▫ignore▫_▫d0▫_▫d1▫

search:
  boost: 3
---

# Serial commands to: Send up to 6 byte DCC packet to MAIN or PROG

Serial commands to Send up to 6 byte DCC packet to MAIN or PROG.

``<M «ignore» «d0» «d1» [«d2» [«d3» [«d4» [«d5»]]]]>``  
``<P «ignore» «d0» «d1» [«d2» [«d3» [«d4» [«d5»]]]]>``

!!! warning "These commands can reprogram your decoders"

    THESE ARE FOR DEBUGGING AND TESTING PURPOSES ONLY. DO NOT USE UNLESS YOU KNOW HOW TO CONSTRUCT NMRA DCC PACKETS - YOU CAN INADVERTENTLY RE-PROGRAM YOUR DECODERS

----

## Commands

* ``<M «ignore» «d0» «d1» [«d2» [«d3» [«d4» [«d5»]]]]>`` = Send up to 6 byte DCC packet on MAIN track
* ``<P «ignore» «d0» «d1» [«d2» [«d3» [«d4» [«d5»]]]]>`` = Send up to 6 byte DCC packet on PROG track

## Parameters

* **ignore**: *Required* but not used
* **d0**..**D1**: values *in hex* to send
* **d2**..**D5**: values *in hex* to send

## Response

none

----

## Notes

==TODO== LOW - Notes

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ==TODO== LOW - Example Commands

### *Example Responses:*

N/A



<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

---
tags:
  - _!
  - _!_P
  - _!_R
  - _!_Q
  - _!_Q
---

# ``<! [P|Q|R]>`` <br/>Emergency Stop (ESTOP) or Pause

Serial command to Emergency Stop all locos, pause all locos, or query the Estop pause status.

## Commands

* ``<!>`` ESTOP all locos
* ``<! [«pauseType»]>`` ESTOP pause or query pause

## Parameters

* **pauseType** *optional* - one of:

    * ``P`` = ESTOP pause the layout
    * ``R`` = ESTOP resume paused layout
    * ``Q`` = query the ESTOP paused status

## Response

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

### Response for  ``<!>``

Repeated for each loco in the reminders list <br/> ``<l «loco» «reg» «speedByte» «functMap»>``

* see the ``<t .. >`` command for information opn this response

### Response for ``<! P>``

``<!PAUSED>``

### Response for ``<! R>``

``<!RESUMED>``

### Response for ``<! Q>``

``<!PAUSED>`` or ``<!RESUMED>`` depending on the current status

## Notes

* any throttle apps and devices using the WiThrottle protocol will receive alterts with the pause is activated or deactivated

----

## Examples

[Also search for '!'](?_!)

### Example Commands

* ``<!>``  ESTOP all locos
* ``<! P>`` Pause all locos

### Example Responses

* TBA

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

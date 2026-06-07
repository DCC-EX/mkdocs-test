---
tags:
  - _!
  - _!_P
  - _!_R
  - _!_Q
  - _!_Q
---

# ``<! [«pauseType»]>``<br/> Emergence Stop or Pause

Serial command to Emergency stop all locos, pause all locos, or query the pause status.

## Command

* ``!``

## Parameters

* **pauseType:** *optional*

    * ``P`` = ESTOP pause the layout
    * ``R`` = ESTOP resume paused layout
    * ``Q`` = query the ESTOP paused status

## *Response*

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

For ``<!>``:<br/> 
Repeated for each loco in the reminders list <br/> ``<l «loco» «reg» «speedByte» «functMap»>``

* see the ``<t .. >`` command for information opn this response

For ``<! P>``<br/>
``<!PAUSED>``

For ``<! R>``<br/>
``<!RESUMED>``

For ``<! Q>``<br/>
``<!PAUSED>`` or ``<!RESUMED>`` depending on the current status

## *Notes*

* any throttle apps and devices using the WiThrottle protocol will receive alterts with the pause is activated or deactivated

----

## *Examples*

[Also search for !](?_!)

### *Examples Commands*

* ``<!>``  ESTOP all locos
* ``<! P>`` Pause all locos

### *Example Responses:*

* TBA


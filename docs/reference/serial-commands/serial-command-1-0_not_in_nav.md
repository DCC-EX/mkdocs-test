---
tags:
  - _1
  - _1_MAIN
  - _1_PROG
  - _1_JOIN
  - _1_track
  - _0
  - _0_MAIN
  - _0_PROG
  - _0_track
---

# ``<1|0 «track»>``<br/> Turn track power on or off

Serial command to turn power on or off to all or specific tracks.  Also allows joining the MAIN and PROG tracks together.

## Command

* ``1`` = on<br/>or
* ``0`` = off

## Parameters

* **track:** one of

    * blank = Both Main and Programming Tracks (All tracks)
    * ``MAIN`` = Main track
    * ``PROG`` = Programming Track
    * ``JOIN`` = Join the Main and Programming tracks temporarily <br/>Note: While ``<1 JOIN>`` is valid, ``<0 JOIN>`` is not.

    * ``A`` through ``H`` representing one of the outputs of the/a motor shield.

## *Response*

The following is not a direct response, but rather a broadcast that will be triggered as a result of any power state changes.

* ``<p«onOFF» «track»>``

    * ``p`` = the 'message identifer'
    * **onOff** = one of: ``1`` = On or ``0`` = off
    * **track** = balnk = all tracks <br/> or one of ``A`` through ``H`` representing one of the outputs of the/a motor shield.

## *Notes*

* The use of the JOIN function allows the DCC signal for the MAIN track to also be sent to the PROG track. This allows the prog track to act as a siding (or similar) in the main layout even though it is isolated electrically and connected to the programming track output.
  
    However, it is important that the prog track wiring be in the same phase as the main track i.e. when the left rail is high on MAIN, it is also high on PROG. You may have to swap the wires to your prog track to make this work.
  
* If you drive onto a programming track that is "joined" and enter a programming command, the track will automatically switch to a programming track. If you use a compatible Throttle, you can then send the join command again and drive off the track onto the rest of your layout!

    * In some split motor shield hardware configurations JOIN will not be able to work.
    * While ``<1 JOIN>`` is valid, ``<0 JOIN>`` is not.

----

## *Examples*

[Also search for !](?_1) or [search for !](?_0)

### *Examples Commands*

* all tracks off: ``<0>``
* all tracks on ``<1>``
* join: ``<1 JOIN>``

### *Example Responses:*

* all tracks off: ``<p0>``
* all tracks on ``<p1>``
* join: ``<p1 JOIN>``

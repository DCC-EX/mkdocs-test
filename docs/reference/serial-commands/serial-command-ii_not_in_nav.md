---
tags:
    - _I
    - _I_id_ADD_position_value_angle
    - _I_id_DCC_home
    - _I_id_EXTT_vpin_home
    - _I_id_position_activity
    - _I_id_position
    - _I_id
    - _D_TT_vpin_steps_activity
    - _D_TT_vpin_steps
    - _J_O_id
    - _J_O
    - _J_P_id
---

# <small>``<I [«id»] [«various parameters»]>``</small> <br/><small>``<D TT «vpin» «steps» [«activity]>``</small> <br/><small>``<J O [«id»]>``</small> &nbsp; <small>``<J P «id»>``</small><br/>Manage Turntables

Serial commands to manage Turntables.

The Turntable/Traverser commands provide a more flexible and functional way of operating turntables/traversers. These require that the turntable/traverser be pre-defined through the ``<I ...>`` commands, described below.

Also refer to the [legacy EX-Turntable documentation](https://dcc-ex.com/legacy-docs/ex-turntable/index.html).

## Commands

* ``<I>`` List all turntables
* ``<I «id» ADD «position» «value» «angle»>`` Add turntable position
* ``<I «id» DCC «home»>`` Create DCC turntable
* ``<I «id» EXTT «vpin» «home»>`` Create an EXTT turntable
* ``<I «id» «position» «activity»>`` Rotate an EXTT turntable
* ``<I «id» «position»>`` Rotate a DCC turntable
* ``<I «id»>`` Broadcast turntable type and current position
* ``<D TT «vpin» «steps» «activity»>`` Test turntable
* ``<D TT «vpin» «steps»>`` Test turntable
* ``<J O>`` List turntable IDs
* ``<J O «id»>`` List turntable state
* ``<J P «id»>`` list turntable positions

## Parameters

* **id**: numeric ID (1-32767) of the turntable to manage
* **position**: Position number of the turntable to assign or move to
* **value**:  Either the number of steps from home for EX-Turntable (1 - 32767), or the linear DCC address for a DCC accessory turntable/traverser
* **angle**: The angle from home for the position (0 - 3600 to allow for partial angles)
* **activity**: The activity for EX-Turntable to perform (refer EX-Turntable activity reference)

## Responses

### Response for ``<I>``

(If any turntables defined) Repeated for each defined Turtable/traverser
``<I «id» «position» >`` <br/>
(If no defined turntables/traversers): ``X``

* **id**: The numeric ID (1-32767) of the turntable
* **position**: The current position of the turntable

### Response for ``<I «id»>``

(If any turntables defined) Repeated for each defined Turtable/traverser
``<I «id» «position» >`` <br/>
(If id not defined): ``X``

* **id**: The numeric ID (1-32767) of the turntable
* **position**: The current position of the turntable

### Response for ``<I «id» «position»>`` or  ``<I «id» «activity»>``

``<I «id» «position» «moving»>``

* **id**: one of
    * identifier of the Turntable/traverser, or
    * ``X`` if the command fails
* **position**: one of
    * position rotating to, or
    * blank = command failed
* **moving**: one of
    * ``0`` (no feedback can be returned from a DCC turntable), or
    * blank = command failed

### Response for ``<J O>``

(has defined Turnouts/Points) ``<jO «id1» «id2» «id3» ...>`` <br/>
(has no defined Turnouts/Points) ``<jO>``

* **id?**: unique id of the turntable(s)/traverser(s)

### Response for ``<J O «id»>``

Response (id is defined): ``<jO «id» «type «position» «position_count» ["«desc»"]>``
Response (id not defined): ``<jO «id» X>``

* **id**: unique id of the turntable/traverser
* **type**: one of
    * ``0`` = DCC
    * ``1`` = EX-Turntable
    * ``X`` = unknown id or hidden
* **position**: one of
    * index of the current position (0 - 48)
    * blank = unknown or hidden id
* **position_count**: one of
    * number of defined positions, including home (0)
    * blank = unknown or hidden id
* **desc**: one of
    * "desc" = description of the turntable or traverser (including surrounding quotes)
    * blank = unknown or hidden id

  Note: The turntable or traverser information does not include the list of defined positions, and this must be requested separated as outlined in the following section.

### Response for ``<J P «id»>``

(id is defined): ``<jO «id» «index» «angle» ["«desc»"]>``
(id not defined): ``<jO «id» X>``

* **id**: unique id of the turntable/traverser
* **index**: one of
    * the position index (0 - 48)
    * X = unknown or hidden id
* **angle**: one of
    * the angle from home for the position (0 - 3600 to allow for partial angles)
    * blank = unknown or hidden id
* **desc**: one of
    * desc = description of the position (including surrounding quotes)
    * blank = unknown or hidden id

### Response for ``<I «id» ADD «position» «value» «angle»>``, ``<I «id» DCC «home»>``, ``<I «id» EXTT «vpin» «home»>``

(Successful): ``<I>`` <br/>
(Fail): ``<X>``

## Notes

* When a DCC accessory turntable is rotated or moved, no feedback is sent to EX‑CommandStation, and therefore the moving variable will always be ``0``, and a second response will therefore never be sent to indicate the completion of a rotation or move, unlike how EX‑Turntable operates.
* When EX-Turntable commences rotating/moving, the device driver flags this using the moving variable above in the response (1 indicates moving, 0 indicates stationary), and when a rotation or move is complete, it will generate an additional response broadcast to indicate that the rotation or move has completed. Further to this, a new rotate/move command will error when a rotation or move is currently in progress.
* Note that a turntable/traverser object must be created using the appropriate ``<I ...>`` command, and then each desired position must be added using the ``<I id ADD ...>`` command.
* Turntables/traversers may be located at positions from 0 (also known as home) through 48. A common angle of separation for tracks radiating out from the turntable is 7.5 degrees, hence the need for allowing up to 48 positions to be defined.
* It is anticipated that throttle developers will be able to “draw” turntables with a visual representation of the location of the home and various defined positions, hence the reason for including an angle or home variable when defining turntables and positions below. Valid angles are from 0 to 3600, where 3600 = the full 360 degrees, allowing for a single decimal place to be used if partial angles are required. Throttle developers simply need to divide by 10 to obtain the appropriate angle.
* General notes:
    * If there is no desire for throttles to know or understand a position's angle from home, simple set any instance of the angle or home variable to 0 (zero).

----

## Examples

[Also search for 'turntable'](?_turntable)

### *Example Commands*

* ==TODO== Example Commands

* ``<I 1 DCC 0>`` defines a DCC accessory turntable/traverser with a 0 degree home angle.
* ``<I 2 DCC 50>`` defines a DCC accessory turntable/traverser with a 5 degree home angle.
* ``<I 1 EXTT 600 0>`` defines an EX-Turntable turntable/traverser at Vpin 600 with a 0 degree home angle.
* ``<I 2 EXTT 600 50>`` defines an EX-Turntable turntable/traverser at Vpin 600 with a 5 degree home angle.

This example defines a DCC accessory device, with 3 positions:

```cpp
<I 1 DCC 0>          // defines a DCC accessory turntable/traverser with a 0 degree home angle.
<I 1 ADD 1 201 100>  // adds position 1, which is at linear DCC address 201, and 10 degrees from home.
<I 1 ADD 2 202 450>  // adds position 2, which is at linear DCC address 202, and 45 degrees from home.
<I 1 ADD 3 203 1900> // adds position 3, which is at linear DCC address 203, and 190 degrees from home.
```

Example: This example defines an EX-Turntable device, with 3 positions:

```cpp
<I 2 EXTT 50>         // defines an EX-Turntable turntable/traverser with a 5 degree home angle.
<I 2 ADD 1 200 100>   // adds position 1, which is 200 steps from home, and 10 degrees from home.
<I 2 ADD 2 1500 450>  // adds position 2, which is 1500 steps from home, and 45 degrees from home.
<I 2 ADD 3 8000 1900> // adds position 3, which is 8000 steps from home, and 190 degrees from home.
```

### *Example Responses:*

* ==TODO== Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

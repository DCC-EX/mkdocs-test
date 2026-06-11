---
tags:
  - _J_A_id
  - _J_A
  - _/
  - _/_START_loco_route
  - _/_START_route
  - _/_PAUSE
  - _/_RESUME
  - _/_KILL_ALL
  - _/_KILL_id 
---

# <small>``<J A [«id»]>``</small> <br/><small>``</ [START|PAUSE|RESUME|KILL] [«various parameters»]>``</small> <br/> List, Start or Stop Automations/Sequences

Serial commands to list, start, pause or stop automations/sequences including routes and animations.

## Commands

* ``J A``
* ``/``
* ``/ START``
* ``/ PAUSE``
* ``/ RESUME``
* ``/ KILL``

### Command Variations

* ``<J A>`` List all automations/routes
* ``<J A «id»>`` list automation details
* ``</ START [«loco»] «route»>`` Start a sequence, or an automation with a loco
* ``</ PAUSE>`` Pause all EXRAIL tasks
* ``</ RESUME>`` Resume all EXRAIL tasks
* ``</ KILL ALL>`` Kill all EXRAIL tasks
* ``</ KILL «taskId»>`` Kill specific EXRAIL tasks
* ``<`` ``/`` ``>`` Stream EXRAIL status

## Parameters

* **id** & **taskId**: id of the automation/sequence
* **loco**: *optional* DCC address of the loco to be used by the automation. <br/> not relevant to routes and automations.
* **route**: automation/sequence (includeing routes and animations) to start or kill.

## Responses

**Response for** ``<J A>``

(Successful) ``<jA [id0 id1 id2 ..]>``

* **id?**: identifier of the Route/Automation(s)

**Response for** ``<J «id»>``

(Successful) ``<jA id X|type |"desc">``

* **id**: identifier of the Route/Automation
* **type**: one of
    * ``R`` = Route
    * ``A`` = Automation
* **desc**: Textual description of the route/automation always surrounded in quotes (")

(fail - is not defined): ``<jA id X>``

**Response for** ``</ START ...>``, ``</ PAUSE>``, ``</ RESUME>``, ``</ KILL ...>``, ``<`` ``/`` ``>``

N/A

## Notes

* ==TODO==

----

## Examples

[Also search for 'J A'](?_J_) or [search for '/'](?_/)

### *Example Commands*

* ==TODO==

### *Example Responses:*

* ==TODO==

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

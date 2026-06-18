---
tags:
  - _9J9_9A9_id
  - _9J9_9A9
  - _/
  - _/_9START9_loco_route
  - _/_9START9_route
  - _/_9PAUSE9
  - _/_9RESUME9
  - _/_9KILL9_9ALL9
  - _/_9KILL9_id 
---

# <small>``<J A [«id»]>``</small> <br/><small>``</ [START|PAUSE|RESUME|KILL] [«various parameters»]>``</small> <br/> List, Start or Stop Automations/Sequences

Serial commands to list, start, pause or stop automations/sequences including routes and animations.

## Commands

* ``<J A>`` List all automations/routes
* ``<J A «id»>`` list automation details
* ``</ START [«loco»] «route»>`` Start a sequence, or an automation with a loco
* ``</ PAUSE>`` Pause all **EXRAIL** tasks
* ``</ RESUME>`` Resume all **EXRAIL** tasks
* ``</ KILL ALL>`` Kill all **EXRAIL** tasks
* ``</ KILL «taskId»>`` Kill specific **EXRAIL** tasks
* ``<`` ``/`` ``>`` Stream **EXRAIL** status

## Parameters

* **id** & **taskId**: id of the automation/sequence
* **loco**: *optional* DCC address of the loco to be used by the automation. <br/> not relevant to routes and automations.
* **route**: automation/sequence (includeing routes and animations) to start or kill.

## Responses

### Response for ``<J A>``

(Successful) ``<jA [id0 id1 id2 ..]>``

* **id?**: identifier of the Route/Automation(s)

### Response for ``<J «id»>``

(Successful) ``<jA id X|type |"desc">``

* **id**: identifier of the Route/Automation
* **type**: one of
    * ``R`` = Route
    * ``A`` = Automation
* **desc**: Textual description of the route/automation always surrounded in quotes (")

(fail - is not defined): ``<jA id X>``

### Response for ``</ START ...>``, ``</ PAUSE>``, ``</ RESUME>``, ``</ KILL ...>``, ``<`` ``/`` ``>``

N/A

## Notes

* None at this time

----

## Examples

[Also search for 'J A'](?_J_) or [search for '/'](?_/)

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

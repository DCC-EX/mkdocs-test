---
tags:
  - _9J9_9M9
  - _9J9_9M9_9CLEAR9_9ALL9
  - _9J9_9M9_9CLEAR9_9ANY9_loco
  - _9J9_9M9_9CLEAR9_stashId
  - _9J9_9M9_stashId
  - _9J9_9M9_stashId_loco
---

# <small>``<J M [«various parameters»]>``</small> <br/> Manage Stash Values

Serial command to manage Stash values.

## Command(s)

* ``<J M>`` List stash values
* ``<J M CLEAR ALL>`` Clear all stash values
* ``<J M CLEAR ANY «locoId»>`` Clear all stash entries that contain * locoId
* ``<J M CLEAR «stashId»>`` Clear given stash
* ``<J M «stashId»>`` Get stash value
* ``<J M «stashId» «locoId»>`` Stash the specified loco in the numbered stash

## Parameters

* **locoId**: loco Id to set or clear
* **StashId**: Id of the stash to set, clear or get (``0`` - ==TODO==)

## Response

### Response for ``<J M «stashId»>``

``<jM «stashId» «loco»>``

* **StashId**: Id of the stash
* **locoId**: loco Id in that stash

### Response for ``<J M>``

Repeated for each defined Stash where loco is not zero:

``<jM «stashId» «loco»>``

* **StashId**: Id of the stash
* **locoId**: loco Id in that stash

## Notes

* A negative locoId value may be stashed to indicate that the loco will operate with inverted direction.

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

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

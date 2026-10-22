---
tags:
  - _9J9_9C9
  - _9J9_9C9_mmmm_nn

search:
  boost: 3
---

# Serial commands to:  Get/Set the Fastclock Time

Serial commands to get or set the Fastclock time.

``<J C>``
``<J C «mmmm» «nn»>``

----

## Commands

* ``<J C «mmmm» [«nn»]>`` = Set fastclock time
* ``<J C>`` = Get fastclock time

## Parameters

* **mmmm**: minutes (hours * 60)
* **nn**: *optional* speed factor. Default is 1

## Responses

==TODO== LOW - Responses

----

## Notes

* None

----

## Examples

Also see the [EXRAIL Time Control Cookbooks](../../enhance/exrail/cookbooks/timecontrol.md).

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* Set the time to 6:25 with a speed factor of 4: ``<J C 375 4>``
* Request the current time: ``<J C>``

### *Example Responses:*

* Response to ``<JC 375 4>`` : ``<jC 375>``
* Response to ``<JC>`` if the current time is 6:15 : ``<jC 375>``

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

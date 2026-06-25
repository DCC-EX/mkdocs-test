---
tags:
  - _9J9_9C9
  - _9J9_9C9_mmmm_nn
---

# <small>``<J C [«mmmm» [«nn»]]>``</small> <br/> Get/Set the Fastclock Time

Serial commands to get or set the Fastclock time.

## Command(s)

* ``<J C [«mmmm» [«nn»]]>`` Set fastclock time
* ``<J C>`` get fastclock time

## Parameters

* **mmmm**: minutes (hours * 60)
* **nn**: speed factor. Default is 1

* **parameter**: *Required*|*optional* description - one of:
    * ``option`` = explanation of option
    * ``option`` = explanation of option
    * ...

* ...

## Response

``J C [«mmmm»>``

## Notes

* None

----

## Examples

Also see the [EXRAIL Time Control Cookbooks](../../products/ex-commandstation/exrail/cookbooks/timecontrol.md).

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

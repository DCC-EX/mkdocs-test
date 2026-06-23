---
tags:
  - _9D9_9WIFI9_9ON9
  - _9D9_9WIFI9_9OFF9
  - _9D9_9WIFI9_9SHOW9
---

# <small>``<D WIFI ON|OFF|SHOW>``</small> <br/> WiFi diagnostics

Serial commands to provide WiFi diagnostica.

## Command(s)

* ``<D WIFI ON|OFF>`` Enable/Disable Wifi diagnostics
* ``<D WIFI SHOW>`` Show Wifi status

## Response

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

``<response>``

N/A

### Response for ``<cmd>``

## Notes

* When enabled, diagnostic messages will be shown on the the [serial monitor](../tools/serial-monitor_not_in_nav.md).

----

## Examples

### *Example Commands*

* ``<D WIFI OFF>`` Disable Wifi diagnostics
* ``<D WIFI ON>`` Enable Wifi diagnostics
* ``<D WIFI SHOW>`` Show Wifi status

### *Example Responses:*

N/A

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

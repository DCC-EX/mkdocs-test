---
tags:
  - _9D9_9WIFI9_onoff
  - _9D9_9WIFI9_9SHOW9

search:
  boost: 3
---

# Serial commands to: WiFi diagnostics

Serial commands to provide WiFi diagnostics.

``<D WIFI onOff>``
``<D WIFI SHOW>``

----

## Commands

* ``<D WIFI onOff>`` = Enable/disable Wifi diagnostics
* ``<D WIFI SHOW>`` = Show Wifi status

## Parameters

* **onOff** One of:
    * ``ON``: Enable
    * ``OFF``: Disable

## Responses

==TODO== MEDIUM - Responses

----

## Notes

* When enabled, diagnostic messages will be shown on the the [serial monitor](../tools/serial-monitor.md).

----

## Examples

### *Example Commands*

* ``<D WIFI OFF>`` Disable Wifi diagnostics
* ``<D WIFI ON>`` Enable Wifi diagnostics
* ``<D WIFI SHOW>`` Show Wifi status

### *Example Responses:*

==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

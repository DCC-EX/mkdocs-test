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

* Response to ``<D WIFI ON>``
    * ``<D WIFI ON>``

* Response to ``<D WIFI OFF>``
    * ``<D WIFI OFF>``
* Response to ``<D WIFI SHOW>``
    * ``<* C HOSTNAME "xxxx" *>`` <br/>``<* C WIFI onOff *>`` <br/>``<* C WIFI AP "nnnn" "pppp" 11 *>`` <br/>``<* C WIFI "mmmm" "********" *>``
        * "xxxx" = the actual hostname
        * onOff = `ON` or `OFF`
        * "nnnn" = Access Point SSID / network name
        * "pppp" = password
        * "mmmm" = Station mode SSID / network name

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

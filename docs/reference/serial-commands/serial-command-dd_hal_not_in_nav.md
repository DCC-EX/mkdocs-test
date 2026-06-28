---
tags:
  - _9d9_9hal9_9show9
  - _9d9_9hal9_9reset9
---

# <small>``<D HAL SHOW|RESET>``</small> <br/> List or Reset the HAL Devices

Serial commands to list or reset the HAL devices.

## Command(s)

* ``<D HAL SHOW>`` Show HAL devices table
* ``<D HAL RESET>`` Reset all HAL devices
board config and used pins

## Parameters

* **showReset**: *Required* - one of:
    * ``SHOW`` = Show HAL devices table
    * ``RESET`` = Reset all HAL devices

## Response

### Response for ``<D HAL SHOW>``

Lists the configured I/O drivers in the Hardware Abstraction Layer (HAL). See Examples below

### Response for ``<D HAL RESET>``

==TODO== LOW - Responses

## Notes

* 'SHOW' Shows all configured servo board and GPIO extender board config and used pins, etc.

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

See commands above.

### *Example Responses:*

* ``<D HAL SHOW>`` Example output showing a connected PCA9685 Servo controller and an MCP23017 I/O expander:

```text
<* PARSING:D HAL SHOW * >
<* Arduino Vpins:2-69 * >
<* PCA9685 I2C:x40 Configured on Vpins:100-115 * >
<* PCA9685 I2C:x41 Configured on Vpins:116-131 OFFLINE * >
<* MCP23017 I2C:x20 Configured on Vpins:164-179 * >
<* MCP23017 I2C:x21 Configured on Vpins:180-195 * >
```

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

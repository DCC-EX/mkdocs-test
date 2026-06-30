---
tags:
  - _9D9_9SERVO9_vpin_position_profile
  - _9D9_9SERVO9_vpin_position
---

# <small>``<D SERVO «vpin» «position» [«profile»]>``</small> <br/> Servo Motor Testing

Serial command for servo motor testing.

## Command(s)

* ``<D SERVO «vpin» «position» [«profile»]>`` Test servo

## Parameters

* **vpin**: *Required* vpin to which the servo is attached
* **position**: *Required* position to move the servo to
* **profile**: one of
    * ``0`` = instant
    * ``1`` = fast
    * ``2`` = medium
    * ``3`` = slow

## Response

Successful: ``<O>``
Fail: ``<X>`` (vpin does not exist)

## Notes

* Vpin is the pin number of the output to be controlled by the turnout/point object. For Arduino output pins, this is the same as the digital pin number. For servo outputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module, 116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module.

----

## Examples

[Also search for '_D_SERVO'](? _9D9_9SERVO9_vpin_position)

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

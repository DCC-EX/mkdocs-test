---
tags:
  - _s
  - _#
  - _9C9_9RESET9
  - _9D9_9RESET9
  - _9J9_9I9
  - _c
---

# <small>``<s>`` &nbsp; ``<#>`` <br/> ``<C RESET>`` ``<D RESET>`` </small> <br/> Query or Reset the EX-CommandStation

Serial commands to query or reset the EX-CommandStation

## Commands

* ``<s>`` Request the **EX-CommandStation** status
* ``<#>`` Request the number of simultaneously supported locos
* ``<C RESET>`` Reset and restart **EX-CommandStation**
* ``<D RESET>`` Reset and restart **EX-CommandStation**
* ``<J I>`` Report currents
* ``<c>`` (Deprecated) Report main track currect

## Parameters

N/A

## Responses

### Response for ``<s>``

 ``<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>`` <br/> plus (repeated for each defined Turnout/Point): ``<H id state>``

* **version: **EX-CommandStation** version
* **microprocessorType**: microprocessor type (e.g. MEGA)
* **MotorControllerType**: Motor Driver type (e.g. STANDARD_MOTOR_SHIELD)
* **buildNumber**: **EX-CommandStation** build number
* **id**: unique identifier for the Turnout/Point
* **state**: one of:
    * ``1`` = thrown
    * ``0`` = Closed

### Response for ``<J I>``

==TODO== Response for ``<J I>``

### Response for ``<c>``

``<c "CurrentMAIN" current C "Milli" "0" max_ma "1" trip_ma>``

* **CurrentMAIN**: Static text for software like JMRI (in quotes)
* **current**: Current in MilliAmps
* **C**: Designator to signify this is a current meter (V would be for voltage)
* **Milli: Unit of measure for external software with a meter like JMRI (Milli, Kilo, etc.) (in quotes)
* **0**: numbered parameter for external software (1,2,3, etc.) (in quotes)
* **max_ma**: The maximum current handling of the Motor Driver in MilliAmps
* **1**: number parameter for external software (we use 2 parameters here, 0 and 1) (in quotes)
* **trip_ma** - The overcurrent limit that will trip the software circuit breaker in mA

### Response for ``<#>``

``<# noCabs>``

* **noCabs**: maximum number of Cabs(Locos) supported by the **EX-CommandStation**

## Notes

* ==TODO== Notes

----

## Examples

[Also search for 's'](?_s) or [search for 'D'](?_d) or [search for 'J I'](?_d)

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

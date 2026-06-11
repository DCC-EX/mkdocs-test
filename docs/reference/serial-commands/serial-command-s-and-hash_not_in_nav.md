---
tags:
  - _s
  - _#
  - _C_RESET
  - _D_RESET
  - _J_I
  - _c 
---

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

# <small>``<s>`` &nbsp; ``<#>`` <br/> ``<C RESET>`` ``<D RESET>`` </small> <br/> Query or Reset the Command Station

Serial commands to query or reset the EX-CommandStation

## Command(s)

* ``s``
* ``#``
* ``C RESET``
* ``D RESET``
* ``c``

### Command Variations

* ``<s>`` Request the command station status
* ``<#>`` Request the number of simultaneously supported locos
* ``<C RESET>`` Reset and restart command station
* ``<D RESET>`` Reset and restart command station
* ``<J I>`` Report currents
* ``<c>`` (Deprecated) Report main track currect 

## Parameters

N/A

## Response

**Response** to ``<s>``

 ``<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>`` <br/> plus (repeated for each defined Turnout/Point): ``<H id state>``

* **version: Command Station version
* **microprocessorType**: microprocessor type (e.g. MEGA)
* **MotorControllerType**: Motor Driver type (e.g. STANDARD_MOTOR_SHIELD)
* **buildNumber**: Command Station build number
* **id**: unique identifier for the Turnout/Point
* **state**: one of:
    * ``1`` = thrown
    * ``0`` = Closed

**Response** to ``<J I>``

==TODO==

**Response** to ``<c>``

``<c "CurrentMAIN" current C "Milli" "0" max_ma "1" trip_ma>``

* **CurrentMAIN**: Static text for software like JMRI (in quotes)
* **current**: Current in MilliAmps
* **C**: Designator to signify this is a current meter (V would be for voltage)
* **Milli: Unit of measure for external software with a meter like JMRI (Milli, Kilo, etc.) (in quotes)
* **0**: numbered parameter for external software (1,2,3, etc.) (in quotes)
* **max_ma**: The maximum current handling of the Motor Driver in MilliAmps
* **1**: number parameter for external software (we use 2 parameters here, 0 and 1) (in quotes)
* **trip_ma** - The overcurrent limit that will trip the software circuit breaker in mA

**response to** ``<#>``

``<# noCabs>``

* **noCabs**: maximum number of Cabs(Locos) supported by the command station

## Notes

* ==TODO==

----

## Examples

[Also search for 's'](?_s) or [search for 'D'](?_d) or [search for 'J I'](?_d)

### *Example Commands*

* ==TODO==

### *Example Responses:*

* ==TODO==

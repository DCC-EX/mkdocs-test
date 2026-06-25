---
tags:
  - _m_9LINEAR9
  - _m_loco_accelerating_braking
  - _m_loco_momentum
  - _m_9POWER9
---

# <small>``<m POWER|POWER|[«loco» «momentum»|«accelerating» [«braking»]]>``</small> <br/> Set the server based momentum

Serial commands to Server based momentum for a specific loco.

## Command(s)

* ``<m «loco» «accelerating» «braking»>`` set momentum for loco
* ``<m «loco» «momentum»>`` set momentum for loco (acceleration and braking)
* ``<m LINEAR>`` Set Momentum algorithm to linear acceleration
* ``<m POWER>`` Set momentum algorithm to very based on difference between current speed and throttle setting

## Parameters

* **loco**: Loco (DCC Address) to set the momentum for
* **accelerating**: ==TODO==
* **braking**: ==TODO==
* **momentum**: ==TODO==

## Response

N/A

## Notes

* The momentum calculation is based on the difference in throttle setting and actual speed. For example, the time taken to reach speed 50 from a standing start would be less if the throttle were set to speed 100, thus increasing the acceleration.
* Setting Momentum 7,14,21 etc is similar in effect to setting a decoder CV03/CV04 to 1,2,3.

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ``<m 3 0>`` - sets loco 3 to no momentum.
* ``<m 3 21>`` - sets loco 3 to 21 mS/step.
* ``<m 3 21 42>`` - sets loco 3 to 21 mS/step accelerating and 42 mS/step when decelerating.
* ``<m LINEAR>`` - acceleration is uniform up to selected throttle speed.
* ``<m POWER>`` - acceleration depends on difference between loco speed and selected throttle speed.

### *Example Responses:*

N/A

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

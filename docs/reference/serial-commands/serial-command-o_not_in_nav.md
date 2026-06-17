---
tags:
    - _o_vpin_count
    - _o_vpin_r_g_b_count
    - _o_vpin_r_g_b
    - _o_vpin
---

# <small>``<o «vpin» [«count»]|[«r» «g» «b» [«count»]]>``</small> <br/> Set Neopixels

Serial commands to provide the ability to set neopixels on or off or change the colour either individually or over a range of pixels.

## Commands

* ``<o «vpin» «count»>`` Set multiple neopixels on(vpin>0) or off(vpin<0)
* ``<o «vpin» «r» «g» «b» «count»>`` Set multiple neopixels colour
* ``<o «vpin» «r» «g» «b»>`` Set neopixel colour
* ``<o «vpin»>`` Set neopixel on(vpin>0) or off(vpin<0)

## Parameters

* **vpin**: *optional* The pin number of the output to be controlled. For Arduino output pins, this is the same as the digital pin number.
* **count**: number of pixels to set, starting at vpin. Default = ``1``
* **r**: 0..255 intensity of the red channel
* **g**: 0..255 intensity of the green channel
* **b**: 0..255 intensity of the blue channel

## Response

==TODO== Responses

## Notes

* ==TODO== Notes

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ==TODO== Example Commands

### *Example Responses:*

* ==TODO== Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

---
tags:
    - _y_vpin_EQ_eq
    - _y_vpin_FOLDER_folder
    - _y_vpin_PAUSE
    - _y_vpin_PLAY_tracknumber_volume
    - _y_vpin_PLAY_tracknumber
    - _y_vpin_REPEAT_tracknumber_volume
    - _y_vpin_REPEAT_tracknumber
    - _y_vpin_RESET
    - _y_vpin_RESUME
    - _y_vpin_STOP
    - _y_vpin_VOL_volume
---

# <small>``<y «vpin» EQ|FOLDER|PAUSE|PLAY|REPEAT|RESET|RESUME|STOP|VOL [«various parameters»]>``</small> <br/> Play DF Player sounds

Serial commands to play sounds on a DFPlayer.

The DFPlayer device can be used to play pre-recorded sounds from an onboard SD-card.

See the [DFPlayer page](/products/ex-commandstation/accessories/various-devices/dfplayer/dfplayer.md) for more information.

## Command(s)

* ``<y «vpin» EQ «eq»>`` Set sound EQ
* ``<y «vpin» FOLDER «folder»>`` Switch to sound track folder
* ``<y «vpin» PAUSE>`` Pause sound
* ``<y «vpin» PLAY «tracknumber» «volume»>`` Play sound track with volume
* ``<y «vpin» PLAY «tracknumber»>`` Play sound track with default volume
* ``<y «vpin» REPEAT «tracknumber» «volume»>`` Repeat sound track with volume
* ``<y «vpin» REPEAT «tracknumber»>`` Repeat sound track with default volume
* ``<y «vpin» RESET>`` Reset sound module
* ``<y «vpin» RESUME>`` Resume sound
* ``<y «vpin» STOP>`` Stop playing sound
* ``<y «vpin» VOL «volume»>`` Set sound volume

## Parameters

* **vpin**: *Required* vpin of the DFPlayer
* **eq**: ==TODO==
* **folder**: folder on the SD Card to switch to / play from
* **tracknumber**: track/file on the SD Card to play
* **volume**: ==TODO==

## Response

==TODO==

## Notes

* See the [DFPlayer page](/products/ex-commandstation/accessories/various-devices/dfplayer/dfplayer.md) for more information.

----

## Examples

[Also search for 'DFPlayer'](?DFPLayer) or [search for 'sounds'](?sounds)

### *Example Commands*

* ==TODO==

### *Example Responses:*

* ==TODO==

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

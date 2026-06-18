---
tags:
    - _y_vpin_EQ_eq
    - _y_vpin_FOLDER_folder
    - _y_vpin_PAUSE
    - _y_vpin_PLAY_trackNumber_volume
    - _y_vpin_PLAY_trackNumber
    - _y_vpin_REPEAT_trackNumber_volume
    - _y_vpin_REPEAT_trackNumber
    - _y_vpin_RESET
    - _y_vpin_RESUME
    - _y_vpin_STOP
    - _y_vpin_VOL_volume
---

# <small>``<y «vpin» EQ|FOLDER|PAUSE|PLAY|REPEAT|RESET|RESUME|STOP|VOL [«various parameters»]>``</small> <br/> Play DF Player sounds

Serial commands to play sounds on a DFPlayer or UDPAudio device.

Theese devices can be used to play pre-recorded sounds from an onboard SD-card.

See the [Sounds page](/products/ex-commandstation/accessories/various-devices/sounds/sounds.md) for more information.

## Commands

* ``<y «vpin» FOLDER «folder»>`` Switch to sound track folder
* ``<y «vpin» PLAY «tracknumber»>`` Play sound track with default volume
* ``<y «vpin» PLAY «tracknumber» «volume»>`` Play sound track with volume
* ``<y «vpin» REPEAT «tracknumber»>`` Repeat sound track with default volume
* ``<y «vpin» REPEAT «tracknumber» «volume»>`` Repeat sound track with volume
* ``<y «vpin» PAUSE>`` Pause playing sound
* ``<y «vpin» RESUME>`` Resume playing sound
* ``<y «vpin» STOP>`` Stop playing sound
* ``<y «vpin» VOL «volume»>`` Set default volume
* ``<y «vpin» EQ «eq»>`` Set sound EQ
* ``<y «vpin» RESET>`` Reset sound module

## Parameters

* **vpin**: *Required* vpin of the DFPlayer
* **eq**: Equalizer profile. one of:
    * ``NORMAL``
    * ``POP``
    * ``ROCK``
    * ``JAZZ``
    * ``CLASSIC``
    * ``BASS``
* **folder**: folder on the SD Card to switch to / play from
* **tracknumber**: track/file on the SD Card to play
* **volume**: Volume to play the track at (``0``-``30``)

## Responses

==TODO== Responses

## Notes

* See the [DFPlayer page](/products/ex-commandstation/accessories/various-devices/sounds/dfplayer.md) for more information.

----

## Examples

[Also search for 'DFPlayer'](?DFPLayer) or [search for 'sounds'](?sounds)

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

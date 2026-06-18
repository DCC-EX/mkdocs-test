---
tags:
  - _y_vpin_9PLAY9_track
  - _y_vpin_9PLAY9_track_volume
  - _y_vpin_9REPEAT9_track
  - _y_vpin_9REPEAT9_track_volume
  - _y_vpin_9PAUSE9
  - _y_vpin_9RESUME9
  - _y_vpin_9STOP9
  - _y_vpin_9FOLDER9_folder
  - _y_vpin_9VOL9_volume
  - _y_vpin_9EQ9_eq
  - _y_vpin_9RESET9
---

# Sounds

There are two sound devices supported.

- [DFPlayer devices](dfplayer.md)
- [UDPAudio devices](udpaudio.md)

These have very different electronic characteristics but are operated by the same set of commands and **EXRAIL** funtions designed for simple sound control.
Refer to the relevant page for device specific details.

## Sound Commands

The <y> command is specifically designed for easy testing and control of sounds from the serial monitor. Every command is directed towards the previously defined vpin.

- `<y vpin PLAY track [volume]>` Plays given track number and specified (or default) volume
- `<y vpin REPEAT track [volume]>` Plays track repeatedly
- `<y vpin PAUSE >` Pauses playing
- `<y vpin RESUME>` Resumes playing
- `<y vpin STOP>` Stops playing
- `<y vpin FOLDER folder>` Switches future play commands to a different folder
- `<y vpin VOL volume>` Changes default play volume (Does not affect currently playing track)
- `<y vpin EQ eq>` Changes sound equalisation
- `<y vpin RESET>` Resets the DFPlayer

## Sound in EXRAIL

Refer to the [EXRAIL cookbooks](/products/ex-commandstation/exrail/cookbooks/sounds/sounds.md) for examples.

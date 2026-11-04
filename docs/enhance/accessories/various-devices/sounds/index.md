---
tags:
  - _▫y▫_▫vpin▫_▪PLAY▪_▫track▫
  - _▫y▫_▫vpin▫_▪PLAY▪_▫track▫_▫volume▫
  - _▫y▫_▫vpin▫_▪REPEAT▪_▫track▫
  - _▫y▫_▫vpin▫_▪REPEAT▪_▫track▫_▫volume▫
  - _▫y▫_▫vpin▫_▪PAUSE▪
  - _▫y▫_▫vpin▫_▪RESUME▪
  - _▫y▫_▫vpin▫_▪STOP▪
  - _▫y▫_▫vpin▫_▪FOLDER▪_▫folder▫
  - _▫y▫_▫vpin▫_▪VOL▪_▫volume▫
  - _▫y▫_▫vpin▫_▪EQ▪_▫eq▫
  - _▫y▫_▫vpin▫_▪RESET▪
---

# Sounds

There are two sound devices supported.

- [DFPlayer devices](dfplayer.md)
- [UDPAudio devices](udpaudio.md)

These have very different electronic characteristics but are operated by the same set of commands and **EXRAIL** functions designed for simple sound control.
Refer to the relevant page for device specific details.

## Sound Commands

The <y> command is specifically designed for easy testing and control of sounds from the [serial monitor](../../../../reference/tools/serial-monitor.md). Every command is directed towards the previously defined vpin.

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

Refer to the [EXRAIL cookbooks](/enhance/exrail/cookbooks/sounds/sounds.md) for examples.

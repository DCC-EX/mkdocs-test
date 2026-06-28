---
tags:
  - _=
  - _equals
  - _equals_track_9MAIN9
  - _equals_track_9MAIN9_9INV9
  - _equals_track_9MAIN9_9AUTO9
  - _equals_track_9PROG9
  - _equals_track_9OFF9
  - _equals_track_9NONE9
  - _equals_track_9EXT9
  - _equals_track_9AUTO9
  - _equals_track_9INV9
  - _equals_track_9DC9_loco
  - _equals_track_9DC9_9INV9_loco
  - _equals_track_9DC9_9X9_loco
---

# TrackManager

TrackManager is what lets you dynamically configure the outputs of your **EX-CommandStation** as either:

- Main DCC track output
- Programming DCC track output
- DC mode
- DCC Auto Reverse
- DCC Booster

## Defaults

Track A defaults to MAIN.  Track B defaults to PROG.

## myAutomation.h

Track mode can be defined in myAutomation.h  
 &nbsp; &nbsp; &nbsp; &nbsp; [Example: Set a track to DC](../exrail/cookbooks/dc-tracks.md)

## Engine Driver

This screen shows where track modes can be set with Engine Driver:  
 &nbsp; &nbsp; &nbsp; &nbsp; ![TrackManager ED](../../../_static/images/engine-driver/ed-trackmanager02.png){: style="width: 40%"}

## Notes

**NOTE:** &nbsp; DC output is only available with specific hardware requirements.

TrackManager  -  [reference document](/reference/trackmanager/trackmanager.md)  
Multi-district DC mode track sync -  [additional detail](/reference/trackmanager/dc-track-sync.md)  
As these pages are under development, you may also want to refer to the [legacy documentation](https://dcc-ex.com/legacy-docs/trackmanager/index.html)

==TODO== move legacy docs

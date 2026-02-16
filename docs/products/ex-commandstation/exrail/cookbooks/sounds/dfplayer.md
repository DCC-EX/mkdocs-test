# Controlling Sounds in EXRAIL

There are multiple `PLAY_` commands in EXRAIL is used to control sound. The first parameter is always the VPIN of the device, the meaning of the argumants depend on the command.

Note: Timing and race conditions may occur with multiple EXRAIL tasks sending commands to the same DFPlayer to the extent that commands could be overwritten before they are executed or not executed in the desired order, possibly leaving the DFPlayer module in an unknown state or causing a timeout.

## Playing a sound (PLAY_TRACK, PLAY_REPEAT)

Command to play a track (file) in the current selected folder and set the volume level. The folder on the microSD card default to folder 01 unless set with the FOLDER directive.

This requires the file number on the DFPlayer microSD card (see DFPlayer manual) and optionally the volume (0-30)

```cpp
PLAY_TRACK(3500,1,20) // plays file 1 at volume 20
PLAY_TRACK(3501,4)    // plays file 4 on a different DFplayer at default volume
```

A file may also be played with automatic repeats by using the `PLAY_REPEAT`

```cpp
PLAY_REPEAT(3500,4,20) // repeat plays file 2 at volume 20
PLAY_TRACK(3501,3)    // repeat plays file 3 on a different DFplayer at default volume
```

## Pause and Resume (PLAY_PAUSE, PLAY_RESUME)

Playing may be paused and resumed 

```cpp
PLAY_PAUSE(3500) // pause playing
PLAY_RESUME(3500) // resume playing
```

## Changing default volume (PLAY_VOLUME)

To change the default volume (0-30). 

```cpp
PLAY_VOLUME(3500,15) // change defualt volume to 15
```

Not all DFPlayers use the same chip, quality varies. Some will change the volume of a currently playing file, others may only change for the next file played.

## Stop playing (PLAY_STOP)

```cpp
PLAY_STOP(3500) // My ears are hurting
```

## Changing current folder (PLAY_FOLDER)

To change the folder (1-99) from which sounds will be selected

```cpp
PLAY_FOLDER(3500,2) // change folder to 2
```

### Set the Equalizer proile (PLAY_EQ)

The profiles available are NORMAL, POP, ROCK, JAZZ, CLASSCS, BASS

```cpp
PLAY_EQ(3500,BASS) // Bring the Noise!
```

### Reset the player (PLAY_RESET)

When you reset the DFPLayer module. Add a `DELAY(1000)` command after the reset to give the DFPlayer time to complete the reset. The volume level is also reset to the default of 30, you may want to add a command to set the volume to a desired level.

```cpp
PLAY_RESET(3500)      // Reset the player
DELAY(1000)           // let it settle
PLAY_VOLUME_(3500,15) // set more sensible volume 15
```

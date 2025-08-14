# Startup - Define Tracks

By default the Command station will start with  
&nbsp; &nbsp; Track A - `MAIN`  
&nbsp; &nbsp; Track B - `PROG`

These lines can be added to myAutomation.h to define tracks as needed.

```cpp
AUTOSTART 
  SET_TRACK(A,MAIN)
  SET_TRACK(B,PROG)
  SET_TRACK(C,MAIN)
  SET_TRACK(D,MAIN)
  POWEROFF
 DONE
```

`POWEROFF` is the default.  

`POWERON` will set MAIN tracks ON.  

Other track modes require the `SET_POWER` command, for each track.  
     &nbsp; &nbsp; [Example: Set a track to DC](./dc-tracks.md)  
     &nbsp; &nbsp; &nbsp; &nbsp; **NOTE:** The use of the `SET_LOCO` command for DC mode tracks.

# Startup - Define Tracks

By default the Command station will start with  

- Track A - `MAIN`  
-  Track B - `PROG`

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

For DC mode operation, please see [DC Running](/products/ex-commandstation/dc-running.md)

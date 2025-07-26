# DC mode track sync

This is additional information on how to sync adjacent districts when using DC mode tracks.

The DCC signal for all tracks uses a single timer; the tracks in multiple DCC districts will be in sync.  The only issue is that the tracks must have the same phase when crossing to another district.

With DC tracks and PWM voltages and frequencies, there are multiple timers to consider.  
In the case of a reversing loop, there are also hardware considerations.  
DC mode is not compatible with the DCC two signal pin method. (see below)  

## Timers / brake pins

**CSB1 / ESP32**  
 -- Tracks with the same throttle will be in sync.  

**Mega**  
 -- Tracks where the brake pin is on the same timer will be in sync when using the same throttle or speed.  
 -- Frequency updates will impact all tracks using the same timer.

```cpp
timers/pins defined for DC mode on Mega 2560
  Pins 9, 10      :  timer 2   Track A
  Pins 6, 7, 8    :  timer 4   Tracks D, C, B
  Pins 44, 45, 46 :  timer 5
```

**Nucleo-F4**  
 -- Tracks with the same PWM frequency and throttle or speed will be in sync when updated code is used.  
 -- Frequency updates will impact all tracks using the same timer.

 -- Timers 1-4, 9, 13 have been tested for use with Nucleo-F4.  Those timers should not be used for other purposes.  
 -- Further discussion on the Discord server may be helpful to gain an understanding of the issues.

## Hardware considerations

Brake pin provides the PWM signal.  
Signal-1 pin provides direction in DC mode.  

The two signal pin method is used with some motor boards for DCC.  Those boards do not work for DC mode, unless logic gate circuitry is added.

**CSB1** and **EX8874** provide low side brake in both directions.

**Low side brake in both directions - -**  
 -- The XNOR gate of the standard motor shield and clones will have high side brake in one direction and low side brake in the other.  This precludes a reversing loop, as the reverse does not result in tracks being in sync in the adjacent district.  

The voltage between the rails results in the engine's direction.  
 -- With low side brake, one rail is low and the other has the PWM voltage.  
 -- With high side brake, one rail is high and the other has a PWM voltage offset.    

 &nbsp; &nbsp; &nbsp; &nbsp; Example with voltages at 25% throttle.  
 &nbsp; &nbsp; &nbsp; &nbsp; ![TrackManager ED](/_static/images/trackmanager/low-side-brake.png){: style="width: 70%"}  

Additional detail  -  [DC mode - Logic gate circuit](./05-dc-mode-logic.md)  

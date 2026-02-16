# Emergency stop button

An emergency stop is a way of stopping all locos immediately. DCC locos often have sustainers that are there to allow the loco to move over short sections of dirty track or insulated turnout frogs. Because of these sustainers, turning off the track power is not a reliable way of stopping trains, those with sustainers may continue moving for serveral metres/yards.
To stop a loco immediately, the powewr must remain on and we must send it a particular DCC packet and the decoder will know to stop.  

## ESTOPALL

The ESTOPALL command will stop all locos and inform all throttles.
In this example, ONBUTTON(173) will start a sequence at this point when a button on vpin 173 is pressed.
The DONE command completes/terminates the process started by ONBUTTON.

```cpp
ONBUTTON(173) ESTOPALL DONE
```

However, ESTOPALL does have disadvantages:

- Nothing prevents a throttle or EXRAIL script sending in a speed command a fraction of a second later
- Users can throttle up when they are ready, but an EXRAIL script may be stuck waiting for a loco to arrive somewhere and with no way of restarting it.

## ESTOP_PAUSE

The ESTOP_PAUSE command can be used to stop all traffic and block all train movement. Perfect for things like pausing all traffic after a derailment.

```cpp
ONBUTTON(173) ESTOP_PAUSE DONE
```

When paused:

- the speed of each loco at the time of the pause is not forgotten
- throttles can be moved, perhaps to adjust a train that was causing the panic, but all locos will remain stopped.

## ESTOP_RESUME

ESTOP_RESUME is used to restart the locos at their previous speed, or at the speed that was modified during the pause.

```cpp
ONBUTTON(174) ESTOP_RESUME DONE
```

## Advanced scenarios

Of course you may wish to enhance the control by adding flashing lights, sounds or other effects.

```cpp
ONBUTTON(173) 
  ESTOP_PAUSE 
  BLINK(180,250,250)
  PLAY_SOUND(8000,6) // "Don't Panic"
  DONE

ONBUTTON(174) 
  PLAY_SOUND(8000,7) // "Stand clear of the layout, resuming"
  DELAY(2000)
  RESET(180) 
  DELAY(1000)
  ESTOP_RESUME 
  DONE
```

In some cases you may prefer that the system is locked but movement does not restart automatically when the resume is issued. This can be achieved by performing an ESTOPALL immediately before resuming. This forces all locos to have a current speed of 0 before releaseing the speed reminders onto the track.

```cpp
ONBUTTON(174) 
  ESTOPALL
  ESTOP_RESUME 
  DONE
```

You may have a situation, like a lifting gate on your layout, where you need to prevent movement when the Command Station is started with the gate open.

This example runs at startup and will check the gate switch on pin 174 to block all movement if it is open.

```cpp
AUTOSTART 
  IF(174) 
    ESTOP_PAUSE
    ENDIF
  DONE
```

## ESTOP serial commands

For convenience thare are also serial commands that have the same function:

- `<!>` equivalent to ESTOPALL
- `<!P>` equivalent to ESTOP_PAUSE
- `<!R>` equivalent to ESTOP_RESUME
- `<!Q>` used by throttles to request the esop status (When a throttle starts up, it will not have seen any previous status broadcast messages)

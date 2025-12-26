# Running a DC layout

Using a DCC-EX Command Station to run a DC layout provides a number of advantages over conventional DC systems.

- All Wifi and connected throttles will operate the same for DC and DCC
- Momentum can be defined for acceleration and braking.
- Multiple DC blocks can be independently controlled and reconfigured to allow crossing between blocks and polarity reversal.
- EXRAIL automation can be used to run trains, create routes, switch block relays, control signals, manage reversing loops etcetera.
- PWM Frequency can be adjusted to suit your locos and/or reduce noise.

## Basic funtionality

The command station has Track Manager commands that can change each track output to DC with appropriate polarity.  By associating a numeric locoid with each track output the command station accepts incoming DCC throttle commands (Or EXRAIL automation commands) for that locoid and converts it to a DC output on every track output with the same locoid. 

The throttles or EXRAIL are unaware that they are driving a DC track and so any DCC Throttle such as Engine Driver that can talk to DCC-EX will work for DC.

Although the CSB-1 can be switched to DC operation by commands from the throttle (Engine Driver has a Track Manager panel to help do this) it is generally easier, for a fully DC layout, to configure it so that it starts up in the desired mode.

## Configuring Default Outputs

The same configuration method for DCC-EX Command Station is to use EXRAIL to define things like: 

- What turnouts or signals you have and how they are electronically driven
- What happens at startup
- What routes can a throttle set
- What automations can a throttle send a loco along
- Buttons and lights on a mimic panel

all of which apply equally to DC operation, plus: 

- How track blocks are set for DC and which locoid thay are mapped to

To start this you need to follow the [Installer process described here](/docs/installer/overview.md) and create an AUTOSTART section in your myAutomation.h file to set the track manager options suitable for your layout:

```cpp
AUTOSTART 
   SETLOCO(1)
   SET_TRACK(A,DC)
   SETLOCO(2)
   SET_TRACK(B,DC)
   POWERON
   DONE
```

This sequence will run as the command station starts up it will 

- associate locoid 1 with track A and switch it to DC.
- associate locoid 2 with track B and switch it to DC.
- turn track power on. No power will be seen on the track until a throttle is used, but unless you POWERON the track will never receive power.

Where the command station has 4 or more track outputs, you can also setup tracks C to H as appropriate.

## Switching between tracks

In a simple DC double-track oval, the tracks are wired in opposite directions so that driving "forward" is in opposite directions on each oval.

If you introduce turnouts that allow a train to cross from one track to another, it is necessary to switch the polarity of the "to" track to match that of the "from" track, switch the turnouts and associate the "to" track with the same locoid as the "from" track so that the throttle user can simply drive across the join.

EXRAIL ROUTEs (they go in the same file as the configuration setup above) are ideal for this and can be activated from throttle buttons. For example, we assume the outer loop is track A locoid 1 and the inner Track B locoid 2.

```cpp
ROUTE(12,"Drive from outer to inner loop")
  SETLOCO(1)
  SET_TRACK(B,DCX)  // reverse polarity on track B and treat as loco 1
  THROW(100) THROW(101) // throw the turnouts that join the tracks
  DONE
  
ROUTE(21,"Drive from inner to outer loop")
  SETLOCO(2)
  SET_TRACK(A,DCX)  // reverse polarity on track B and treat as loco 1
  THROW(100) THROW(101) // throw the turnouts that join the tracks
  DONE
  
ROUTE(99,"Restore tracks to normal")
  CLOSE(100) CLOSE(101)  // close the turnouts  
  SETLOCO(1)
  SET_TRACK(A,DC)  
  SETLOCO(2)
  SET_TRACK(B,DC)
  DONE
```

Notice that when you apply ROUTE(12), you are now driving on both tracks with the same loco id 1. Throttles attempting to drive loco id 2 will be ignored.

As you get more advanced, the routes can be programmed to happen automatically or contain additional items such as signals, sounds, mimic panel control and so on.

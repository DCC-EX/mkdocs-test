# Running a Legacy DC layout

Using a DCC-EX Command Station to run a DC layout provides a number of advantages over conventional DC systems.

- All Wifi and wired connected throttles will operate the same for DC and DCC locos using Cab road numbers 'loco addresses' from 1 to 10239.
- Using this range of Cab locoid addresses you can assign any DC district/track any locoid to run in that DC district, i.e # 2.
- Multiple DC Districts (maximum four on EX-CSB1 & maximum eight on Mega2560 system) can be independently controlled and reconfigured to allow crossing between districts and polarity reversal.
- Any DC District can be further subdivided into smaller blocks and energized or powerd via turnout points and or SPDT switches If desired, i.e. staging or fiddle yard..  
- Momentum of a loco can be defined in number of seconds of travel for acceleration and braking distances.
- EXRAIL automation can be used to run trains, create routes, switch block relays, control signals, control accessory special effects, manage reversing loops, etcetera.
- Pulse Width Modulation PWM 'Frequency' can be adjusted to suit your locos and/or reduce DC noise with a touch of the throttles function F29-F31 button.
- With our Track Manager features it is possible to run parts of the layout with DC and other parts with DCC at the same time, and through a single wifi throttle controller with both DC & DCC locos shown & controlled at the same time.  (But do not leave a DC loco sitting idle on a track configured for DCC).
- No DC legacy Transformers are used, only standard Laptop battery supplies from 12vdc to 24vdc and from 2A, 5A or 10Amps are used depending on your scale requirements.
- Note: Each Power District section must have 'dual insulated rail joiners' between each track section that connect and travel between one districts to another.

## Basic functionality

The DCC-EX command station has TrackManager commands that can change each district/track output to DC with appropriate polarity.  By associating a numeric road number as locoid (1..10239 the same range as DCC) with each district/track output the command station accepts incoming DCC throttle commands (Or EXRAIL automation commands) for that locoid and converts it to a DC output on every district/track output with the same locoid.

The throttles or EXRAIL are unaware that they are driving a DC districts/tracks and so any DCC Throttle such as Engine Driver that can talk to DCC-EX will work for DC. In effect, in DC mode, the throttle drives the track compared with DCC mode where the throttle drives the loco.

Although the EX-CSB1 can be switched to DC operation by commands from the throttle (Engine Driver has a Track Manager panel to help do this) it is generally easier, for a fully DC layout, to configure it so that it starts up in the desired mode of DC Districts.

Warning: The sometimes-alternate suggested technique of using a DCC decoder to output directly to a DC track instead internally to the loco motor is NOT RECOMMENDED as most decoders are not tolerant of a short between the motor outputs. This means a common track short could damage an expensive decoder.

## Configuring Default Outputs

The normal configuration method for DCC-EX Command Station is to use EXRAIL to define things like:

- What type of Districts/tracks do I want to use DC, DCC or both
- What are the locoids or Cab# defined in the Roster for throttles to see and use.
- What turnouts or signals you have and how they are electronically driven
- What happens at startup
- What routes can a throttle set
- What automations can a throttle send a loco along
- Buttons and lights on a mimic panel

all of which apply equally to DC operation, plus:

- How track Districts are set for DC and which locoid addresses they are mapped to

To start this you need to follow the [Installer process described here](/installer/overview.md) and create an AUTOSTART section in your myAutomation.h file to set the track manager options suitable for your layout.

Two districts A & B are set to DC mode and initially powered On:

```cpp
AUTOSTART 
   SETLOCO(1)
   SET_TRACK(A,DC)
   SET_POWER(A,ON)
   SETLOCO(2)
   SET_TRACK(B,DC)
   SET_POWER(B,ON)
   DONE
```

This sequence will run as the command station starts up it will

- associate locoid 1 with district track A and switch it to DC.
- associate locoid 2 with district track B and switch it to DC.
- turn track power on. No power will be seen on the tracks until a throttle is used, but unless you SET_POWER ON the track will never receive power.

Where the command station has 4 or more district/track outputs, you can also setup tracks C to D as appropriate using locoid or cab addresses 1 .. 10239.

## Switching between tracks

In a simple DC double-track oval, the tracks are wired in opposite directions so that driving "forward" is in opposite directions on each oval.

If you introduce turnouts that allow a train to cross from one track to another, it is necessary to switch the polarity of the "to" track to match that of the "from" track, switch the turnouts and associate the "to" track with the same locoid as the "from" track so that the throttle user can simply drive across the join.

EXRAIL ROUTEs (they go in the same file as the configuration setup above) are ideal for this and can be activated from throttle buttons. For example, we assume the outer loop is track A locoid 1 and the inner Track B locoid 2.

```cpp
ROUTE(12,"Drive from outer to inner loop")
  SETLOCO(1)
  SET_TRACK(B,DCX)  // reverse polarity on track B and treat as loco 1
  SET_POWER(B,ON)
  THROW(100) THROW(101) // throw the turnouts that join the tracks
  DONE
  
ROUTE(21,"Drive from inner to outer loop")
  SETLOCO(2)
  SET_TRACK(A,DCX)  // reverse polarity on track B and treat as loco 1
  SET_POWER(A,ON)
  THROW(100) THROW(101) // throw the turnouts that join the tracks
  DONE
  
ROUTE(99,"Restore tracks to normal")
  CLOSE(100) CLOSE(101)  // close the turnouts  
  SETLOCO(1)
  SET_TRACK(A,DC)
  SET_POWER(A,ON)

  SETLOCO(2)
  SET_TRACK(B,DC)
  SET_POWER(B,ON)
  DONE
```

Notice that when you apply ROUTE(12), you are now driving on both tracks with the same loco id 1. Throttles attempting to drive loco id 2 will be ignored.

As you get more advanced, the routes can be programmed to happen automatically or contain additional items such as signals, sounds, mimic panel control and so on.

## Reversing Loops

In contrast to DCC, a DC reversing loop must have the polarity to correctly represent the direction of the loco. Thus the loop part will require the polarity to control the direction of the train around the loop.
while the train is in the loop, the main track leading into the loop must be switched to allow the train to exit the loop and continue back along the track without reversing the locomotive.
There is no automatic polarity reversing for DC layouts, this must be programmed using EXRAIL track mode DCX using SET_TRACK (B, DCX) to suit the topology of your layout.

## More blocks

The separate track outouts supplied by the Command Station represent the number of separate throttle ids that may be operating. Like any large DC layout, the switching of throttle outputs to multiple other blocks can still take place using mechanical switches or relays which can be controlled by suitable EXRAIL sequences. Power routing turnouts operate as normal but may be awkward if you are building a new layout with tyhe intention of running DCC later.

If you have several throttles operating the same locoid, they will automatically synchronise with each other.

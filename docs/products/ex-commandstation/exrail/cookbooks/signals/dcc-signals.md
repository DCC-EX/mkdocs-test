# DCC Signals

## Common signals

Most DCC signals have an inbuilt decoder and genarally only have a RED and GREEN aspect. They are driven by dcc accessory packets sent over the track signal.

To define a DCC signal use

```cpp
DCC_SIGNAL(555,20,0)
```

defines a DCC encoder signal with a signal_id of 555 and encoder address/subaddress of 20/0.

Thus it can be changed by a `RED(555)` or `GREEN(555)` command.

## Advanced aspect signals

More advanced multi-aspect DCC based signals may have a variety of aspect choices to reperesent the common red/amber/green states, for example aspect 17 might show 2 green lamps with a flashing amber and aspect 18 might show 2 ambers with an illuminated cow-on-track warning sign in Klingon. There are no rules here!

This kind of signal can be defined as follows

```cpp
DCCX_SIGNAL(666,1,18,2)
```

 where 666 is the DCC linear address and the signal_id used for EXRAIL commands, the 1,18,2 represents the choice of aspects the signal supports to represent the red, amber and green states.

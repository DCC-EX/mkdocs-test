# LED Signals

LED based signals are defined using the SIGNALH macro (For LEDS with common cathode) or SIGNAL macro (for leds with common annode)

For example 

```cpp  
SIGNALH(110,111,112)
```

defines a common cathode signal with a RED led on vpin 110, Amber LED on vpin 111 and Green LED on vpin 112.
This signal is also automatically given a signal_id matching the red vpin.

Thus it can be changed by a `RED(110)`, `AMBER(110)` or `GREEN(110)` command.

For a signal with no amber or green led, the relevant vpin can be specified as zero.


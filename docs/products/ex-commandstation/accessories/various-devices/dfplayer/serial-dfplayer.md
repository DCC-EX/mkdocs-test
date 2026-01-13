# Serial connected DFPlayer

A serial connected DFPlayer is defined in EXRAIL (myAutomation.h) using the HAL command

```cpp
HAL(DFPlayer,vpin,serial)
```

For Example:

```cpp
HAL(DFPlayer,3500,Serial2)  // Use tx2/rx2 Arduino Serial2
```

## CSB1 and ESP32 Serial connections

Note that the ESP32/CSB1 does not by default have a configured Serial2 so it is necessary to provide the spare pins to be used for the setup.

```cpp
HAL(DFPLayer,3500,Serial2,16,17)  // For an ESP32 
```

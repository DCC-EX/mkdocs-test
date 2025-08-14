# Things that happen at startup

When the command station starts:

- Definitions of HAL drivers, Turnouts and Signals will take place first regardless of where they are found in the myAutomation.h file.
- EXRAIL will run through all its sequences to detect any VPIN that has been used for input, perhaps by an AT, AFTER, ONBUTTON, ONSENSOR etc. These pins are then set to the Arduino INPUT_PULLUP mode. This is necessary so that EXRAIL can actually read the input pins.

Where VPINS are mapped to external expanders (such as an MCP23017), the HAL driver will pass on the relevant commands to the expander.

- EXRAIL will then automatically start tasks at any point in the myAutomation.h file where and AUTOSTART command is found. There may be several, they will all run simultaneously and in no particular priority.

To create commands that will automatically run at startup:

```cpp
AUTOSTART
  POWERON
  THROW(1)
  CLOSE(2)
  PRINT("Ready to Rumble")
  DONE
```

# Time Control

## EXRAIL Commands

Commands have been included in EXRAIL allow events to be controlled by the clock.  The new commands are:

```cpp
ONCLOCKTIME( hour, mins)
```

and

```cpp
ONCLOCKMINS( mins )
```

For details of how to use these commands see the [Clock Control Cookbook](/products/ex-commandstation/exrail/cookbooks/timecontrol.md).

## Testing Timed Sequences

If one is testing out a sequence using a timed command it can be done quickly without using the clock by entering commands from the System Monitor.  The form of the command is:

```cpp
<JC mmmm ss> 
```

Details are again on the [Clock Control Cookbook](/products/ex-commandstation/exrail/cookbooks/timecontrol.md).

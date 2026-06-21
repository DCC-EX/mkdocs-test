# Defining PIN Turnouts/Points

PIN Turnouts/Points operate by detecting the state of an output pin.

Define pin based turnouts/points using **EXRAIL**.

```cpp
PIN_TURNOUT(id, vpin, "description")
```

id = Unique turnout/point ID within the CommandStation. All other turnout/point commands will refer to this turnout/point by this id.

vpin- the pin to be set HIGH for thrown and LOW for closed  

description = A human-friendly description of the turnout/point that will appear in WiThrottle apps and Engine Driver. Note that this must be enclosed in quotes “”. In some cases the HIDDEN keyword can be used here to prevent the turnout/point being visible to the throttles.

For example:

```cpp
PIN_TURNOUT(6,201,"Round the bend")
```

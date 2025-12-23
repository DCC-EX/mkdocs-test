# Random selection

EXRAIL provides a number of randomising functions that make it easy to create more interesting automations that behave in unpredictable ways. This may be as simple as a random delay time at a station, choosing a different route to follow or selecting a train from a fiddle yard.

Some layout builders have used this to create non-train animations such as flickering camp fires, welding flashes and crane movements.

## Random time delay

The `DELAYRANDOM(mindelay,maxdelay)` delays a random time between two millisecond values, for example between 5 and 10 seconds use

```cpp
DELAYRANDOM(5000,10000)
```

## Random choice on a given percentage

The `IFRANDOM(percent)` command will return true a given percentage of the time.

## Random selection of a path to follow

The `RANDOM_FOLLOW(sequence1,sequence2.....)` command will randomly choose between sequences with equal probability. Since this will always `FOLLOW` one of the specified sequences, this will never return to the next command.

The `RANDOM_CALL(sequence1,sequence2.....)` command will randomly choose between sequences with equal probability and since they are CALLed they should `RETURN` and processing continues at the statement after `RANDOM_CALL`.

Up to 8 sequences can be passed to these commands. If you need more than 8 just let us know and it can be extended but it's not as simple as changing a single number because the C++ pre-processor does not have macro parameter enumeration.

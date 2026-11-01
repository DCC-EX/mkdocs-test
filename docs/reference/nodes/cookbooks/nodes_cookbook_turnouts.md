# Handling turnouts in a node

This example shows how an existing turnout definition  can be moved to a node processor.

## Existing EXRAIL for turnout connected to Command Station

```cpp
SERVO_TURNOUT(22,400,350,120,Slow,"Mountain pass")
```

This provides :

- full EXRAIL support for THROW/CLOSE ONTHROW/ONCLOSE IF etc
- Throttle support for turnout/point names

## turnout/point Moved to remote node

This involves moving the hardware-aspect of the turnout/point definition to the myAutomation.h in the node..

```cpp
// turnout/point definition in node copy of myAutomation.h
SERVO_TURNOUT(22,400,350,120,Slow,"Mountain pass")
```

Notice that the turnout/point ID does not change but the vpin 400 may well change to suit whatever HAL device is driving the turnout/point.

The Command Station will automatically know that the turnout/point is defined elsewhere so does not need the turnout/point definition.

This is particularly powerful if you are building a modular layout. If for example a bunch of turnouts/points are on a particular module handled by a node, then the throttles will automatically know if the module is present or absent and will not show turnouts/points for the module unless it is powered up.

Notice that this is all you need to do... Any EXRAIL in the Command station that needs to handle the turnout/point can remain unchanged.

You can have any number of turnouts/points in a node or split them over several nodes, and still manage some from the CS if needed..

In effect, turnout/point numbers are unique across all nodes so only one node should have the hardware-aware turnout/point definition.

## DCC turnouts/points

FOR THE TIME BEING a DCC turnout/point can't be moved to a node because its "wired" to the CS/Track.

That doesn't stop a node throwing or closing it as the id is shared automatically between all nodes.

## Local node processing

Because the node has almost the full EXRAIL capability, its possible to use EXRAIL in the node to monitor ONTHROW/ONCLOSE to perform local signals, switch lights, make sounds and so on.

# Defining Servo Turnouts/Points

(This does not include servos driven from track connected DCC decoders. See [DCC Decoders](/products/ex-commandstation/exrail/cookbooks/turnouts/defining-dcc-turnouts.md))

## Important considerations for servo operation

Servo turnouts/points are driven through a [PCA9685](?PCA9685) servo control board or an [EX-IOExpander](?ioexpander).

Test, test, test your servo parameters prior to connecting to an actual turnout/point. If you have defined angles that exceed the physical limits of your turnout/point, you will likely damage it and/or the servo mechanism.

Treat each servo and turnout/point as an individual as not all servos (or turnouts/points for that matter) are created equal. An angle that works with one servo and associated turnout/point will not necessarily provide the exact same result with another. Differences in servo brands, mounting methods, and even normal manufacturing tolerances will need to be factored in to the servo angles in use.

The **EX-Toolbox** Android application provides a servo movement testing tool to help you discover the necessary values for the angles below.

Use flexible wire to connect your servo arm to the turnout/point. Using a flexible connection between the turnout/point and the servo mechanism means if anything does go wrong such as the turnout/point getting jammed or an incorrect servo angle being sent, it reduces the chance of damaging the turnout/point or servo.

## Defining servo based turnout/point objects

Define servo based turnouts/points using **EXRAIL**.

```cpp
SERVO_TURNOUT(id, vpin, active_angle, inactive_angle, profile, "description")
```

id = Unique turnout/point ID within the CommandStation. All other turnout commands will refer to this turnout/point by this id.

pin = The ID of the pin the servo is connected to, which would typically be the VPin ID of the PCA9685 controller board.

active_angle = The angle to which the servo will move when the turnout/point is thrown (This is a value passed to the servo driver, it is not in degrees).

inactive_angle = The angle to which the servo will move when the turnout/point is closed.

profile = The speed at which a turnout/point will move: Instant, Fast, Medium, Slow.

description = A human-friendly description of the turnout/point that will appear in WiThrottle apps and Engine Driver. Note that this must be enclosed in quotes “”. In some cases the HIDDEN keyword can be used here to prevent the turnout/point being visible to the throttles.

An example definition for a servo connected to the second control pins of the first PCA9685 connected to the CommandStation, using the slow profile for prototypical operation:

```cpp
SERVO_TURNOUT(200, 101, 450, 110, Slow, "Coal yard exit")
```

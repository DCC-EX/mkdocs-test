# Sensors

Sensors become necessary when you wish to add automated control of accessories or trains, or you wish to add a control panel separate from the functions of your throttle. Each sensor device can trigger actions or be read in [EXRAIL](?EXRAIL) or be passed up to a PC controller such as JMRI, RocRail or iTrain.

Sensor devices include

- Switches and buttons on a control panel
- InfraRed or ultrasonic detectors when a train crosses a point on the track
- Video camera using AI to detect train position or children's hands reaching over the layout
- Block Occupancy (or Train-on-track, TOTI) detectors that detect the current consumed by a loco decoder or resistor-fitted rolling stock when present in an isolated track block.

## Track/Layout sensors for automation

There are basically 2 very different types of track sensor.....

- Block occupancy sensors, described above.

- Position sensors (IR, reed switch, or camera) that detect something reaching a specific point on the layout.

The problem with BOTH these systems is that the sensors do not know the DCC address of the loco involved. Unlike the old DC system, you cant just have a bit of track switch off to stop a loco.... you need to send a message to it when you know its id.

Also block occupancy is no help if you think in terms of "the block isn't occupied so I can go into it" because you don't know if another train is already heading towards that block at 300kph.. (single line working or anything involving a crossover)

Automation in DCC-EX is much simpler if you forget the "Oh, a train is approaching signal x which is red so I now need to find out which train it is and tell it to stop" and start thinking from the perspective of a driver...

It's much simpler to think "Im proceeding along track 4 in a westerly direction and when I get to the footbridge I must look ahead at signal x and start braking, then carry on to the coal yard and stop at the buffers."
Position sensors are ideal for this kind of thing, block occupancy just doesnt cut it.

EXRAIL makes this stuff easy.... 😁  but you have to start with the right perspective.

## Defining sensors

EXRAIL is used to describe how the sensor devices are wired to the command station (usually via I2C) and what [VPIN](?VPIN) is to be assigned to each sensor

The most common method of connecting sensor devices to your command station is through an [MCP23017](?MCP23017) device which offers up to 14 input pins (or 16 output pins, or a mix of both) through a single I2C connection. For more inputs you can add more MCP23017 devices to the I2C chain.

The [EX-IOExpander](?IOExpander) can be used to connect multiple sensors over a single I2C connection depending on the microprocessor used to build it.

The [EX-SensorCam](?SensorCam) can be used to offer up to 80 sensor points on a single I2C connection.  

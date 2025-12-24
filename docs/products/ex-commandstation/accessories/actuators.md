# Actuators - to make stuff happen

Actuators are devices that you can add to make things happen under the control of the Command station. For example throwing a turnout, setting a signal or switching lights. There are basically two types of actuator that will commonly be used:

- PWM output used for Servo movement of turnouts, semaphore signals, crossing gates, fancy animations and LED fading.
- Digital output (On/Off) mostly used for LEDs, relays and some turnout types.

Other actuator types include:

- NeoPixel output used for advanced lighting, mimic panels, signals etc.
- Sound players
- Turntable control systems

## Servo actuators

Servo actuators generally use a [PCA9685](?PCA9685) device which can connect up to 16 Servos or LEDs over a single I2C connection. This device also acts to provide servo movement power separately from the movement control signal.

[EXRAIL](?EXRAIL) is used to

- Define the PCA9685 connection and its address so that each output can be given a unique [VPIN](?VPIN) to control it.
- For turnouts define a [SERVO_TURNOUT](?SERVO_TURNOUT) for each VPIN so that the rest of DCC-EX can throw or close this turnout without knowledge of the underlying mechanism.
- For semaphore signals, define a [SERVO_SIGNAL](?SERVO_SIGNAL) to that the rest of DCC-EX can control the signal.
- Control animation servos directly, such as crossing gates or shed doors.

## Digital actuators

Digital outputs are generally connected via an [MCP23017](?MCP23017) device which offers up to 16 output pins on a single I2C connection.

EXRAIL is used to

- Define the MCP23017 connection and its address so that each output can be given a unique [VPIN](?VPIN) to control it.
- Set or reset the pin output when appropriate

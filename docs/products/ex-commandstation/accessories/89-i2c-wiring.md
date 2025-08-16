# I2C Wiring

I2C expansion modules provide accessory pins, but I2C wiring requires a lot of attention to detail.

## I2C concepts

- Keep I2C wiring short
- Use Qwiic cables
- Know the combined resistance of connected I2C modules
- Avoid using excess power from the microprocessor's power source

## I2C bus voltage

- I2C bus voltage is determined by the voltage used for the pullups on the SDA and SCL pins, which should not exceed the voltage of the microprocessor.
- Mega 2560 is 5V; CSB1, ESP32-WROOM, Nucleo-F4 are 3.3V.

## Qwiic/STEMMA QT

- Qwiic a.k.a. STEMMA QT - connectors and wiring are designed for 3.3V.
- When using a Mega:  the Qwiic connector on EX8874 the power pin is 3.3V, but the SDA SCL pins have pullups to 5V. For most cases, use the I2C headers on the EX8874 when using a Mega.

## I2C wire length</strong>

- Length increases capacitance and reduces signal quality.
- Plan to include LTC4311 or other options when length exceeds 2 meters, for example the [Adafruit LTC4311 I2C Extender/Active-terminator](https://learn.adafruit.com/adafruit-ltc4311-i2c-extender-active-terminator)

## Combined parallel resistance

- Lower resistance results in a stronger signal and helps offset higher capacitance.
- If resistance is too low, the uC will be unable to overcome it.

This table shows the parallel resistance values with multiple I2C modules.  
Note that Mega has 10k onboard; EX-CSB1 has 5.1k; others are weak or disabled.  
I2C modules, such as PCA9685, MCP23017 and LCD will generally have 10k pullups. OLED may have none.  
Add/remove pullups to result in 2.5-3.0 mA.  
With LTC4311 the need to adjust resistance may be less important, unless resistance is too low.  

![I2C Resistance](/_static/images/i2c-devices/i2c-pullup-resistance.png){ width=70% }

## Wiring pattern for lower capacitance

[https://www.nxp.com/docs/en/user-guide/UM10204.pdf](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)  

![I2C Wiring Pattern](/_static/images/i2c-devices/i2c-wiring-pattern.jpg){ width=70% }

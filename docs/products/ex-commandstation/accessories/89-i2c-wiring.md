# I2C Wiring

I2C expansion modules provide accessory pins, but I2C wiring requires a lot of attention to detail.

## I2C concepts

- Keep I2C wiring short.
- Use Qwiic cables.
- Know the combined resistance of connected I2C modules.
- Avoid using excess power from the microprocessor's power source.  Separate power sources can avoid degrading the I2C bus by low voltage spikes/sags or overloading the source.

## I2C bus voltage

- I2C bus voltage is determined by the voltage used for the pullups on the SDA and SCL pins, which should not exceed the voltage of the microprocessor.
- Mega 2560 is 5V; CSB1, ESP32-WROOM, Nucleo-F4 are 3.3V.

## Qwiic/STEMMA QT

![ Qwiic ](/_static/images/i2c-devices/i2c-qwiic-wiring-pattern.png){ width=40% align="right" }

- Qwiic a.k.a. STEMMA QT - connectors and wiring are designed for 3.3V.
- When using a Mega:  the Qwiic connector on EX8874 the power pin is 3.3V, but the SDA SCL pins have pullups to 5V. For most cases, use the I2C headers on the EX8874 when using a Mega.
- Qwiic wiring pattern is used for the [Adafruit STEMMA QT / Qwiic connectors](https://learn.adafruit.com/introducing-adafruit-stemma-qt/technical-specs#stemma-4-pin-i2c-both-standard-and-stemma-qt-3035230) - and is different from the [NXP pattern *below*](89-i2c-wiring.md/#wiring-pattern-for-lower-capacitance).
  
## I2C wire length</strong>

- Length increases capacitance and reduces signal quality.
- Plan to include LTC4311 or other options when length exceeds 2 meters, for example the [Adafruit LTC4311 I2C Extender/Active-terminator](https://learn.adafruit.com/adafruit-ltc4311-i2c-extender-active-terminator)

## Combined parallel resistance

- Lower resistance results in a stronger signal and helps offset higher capacitance.
- If resistance is too low, the uC will be unable to overcome it.

This table shows the parallel resistance values with multiple I2C modules.  
\- Note that Mega has 10k onboard; EX-CSB1 has 5.1k; others are weak or disabled.  
\- I2C modules, such as PCA9685 and MCP23017, will generally have 10k pullups. LCD and OLED displays may have 4.7k or 10k.  
\- Add/remove pullups to result in 2.5-3.0 mA.  
\- With LTC4311 the need to adjust resistance may be less important, unless resistance is too low.  

![I2C Resistance](/_static/images/i2c-devices/i2c-pullup-resistance167.png){ width=70% }

## Wiring pattern for lower capacitance

[https://www.nxp.com/docs/en/user-guide/UM10204.pdf](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)  

![I2C Wiring Pattern](/_static/images/i2c-devices/i2c-wiring-pattern.jpg){ width=70% }

## Power sources

- A separate power source for the VCC pin of the I2C bus avoids potential voltage spikes/sags and noise into the power circuit of the microprocessor, and should make the I2C accessory bus more resilient.  
- Additional/separate power source is required for the +5V servo power on the PCA9685 module.  
- When using separate power sources, there is potential for a ground loop.  ==TODO== 

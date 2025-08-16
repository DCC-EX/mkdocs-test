# Buying I2C devices

There are many I2C devices available and the price/availability can vary widely depending on your location and delivery options. Where devices are very cheap, you may find quality issues and so expect a few duds.

Some devices come with [QWiic](https://learn.adafruit.com/introducing-adafruit-stemma-qt/technical-specs) connectors which makes them easier to plug-and-play with the QWiic connector on your EX-CSB1 or EX8874 motor shield.

In general, the Adafruit devices below are high quality and well documented but that is usually reflected in the price.

- MCP23017 provides 16 pins for mixed input or output.[(see details)](https://www.adafruit.com/product/5346#technical-details). This is good for:

    - Up to 14 inputs from push-buttons, switches, sensors.
    - Up to 16 outputs to LEDs and signals (which require current limiting resistors) and relays.

- PCA9685 provides up to 16 outputs for servos and LEDs (PWM pins used for V+ include resistors) [(See details)](https://www.adafruit.com/product/815).

- PCA9548 multiplexor allows for I2C devices that must share the same I2C address [(See details)](https://learn.adafruit.com/adafruit-pca9548-8-channel-stemma-qt-qwiic-i2c-multiplexer/overview).

- NeoDriver provides an interface to NeoPixel chains of LEDs [(See details)](https://learn.adafruit.com/adafruit-pca9548-8-channel-stemma-qt-qwiic-i2c-multiplexer/overview).

- LTC4311 resolves electronic issues when the total of I2C wiring is greater than approximately 2m or 6ft [(See details)](https://www.adafruit.com/product/4756).

- QWiic wires make it easy to plug these devices together[(See details)](https://www.adafruit.com/product/4210).

## Rosscoe Trains

Rosscoe supplies I2c devices with QWiic sockets and additional power feeds which makes wiring much easier.

The Rosscoe Shop is linked from our [Third Party Products and Sellers](/purchasing/02-third-party-sellers.md#rosscoe) page.

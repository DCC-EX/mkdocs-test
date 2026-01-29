# MCP23017, PCA955x and TCA955x devices

These devices are functionally very similar and provide a variety of pins for digital input or output over an I2C address.

Essentially, there is no automatic hardware type detection so it is necessary for the user to provide the information about:

- Hardware chip type
- I2C address (including path through a multiplexor if used)
- [VPIN](?VPIN) to number the first pin on the device
- number of consecutibe VPINS on this device

Once the driver and its information have been correctly defined, the pins on the device are addressed purely by VPIN number in the same way as any other Arduino pin. This significantly simplifies any code that has to set or test the pins.

In addition, it is not necessary to define each pin as input or output as EXRAIL will work this out automatically and configure the device. However, youy can't use the same pin for output and input. 

## Device variations

- MCP23017 has 17 pins but pins 7 and 15 (A7 and B7 on the pcb) are unsuitable for input due to a chip design fauilt found some years after production. This fault is very unlikely to affect you but it is best to avoid these pins. It is sometimes assumed that older chips are Ok and newer ones have the fault, but in fact they are all identical and only the datasheet was changed to warn users to avoid the 7 and 15 pins for inpiut.
- The PCA9554 and TCA9554 have only 8 pins
- The PCA9555 and TCA9555 have 16 pins
- The PCA and TCA models are identical but manufactured by different companies. You can use either driver name because its all the same code.

## Defining devices

These devices are defined by using HAL statements in your EXRAIL script (myAutomation.h or its included files).

First step is to run the Command Station software without the drivers and note what addresses the I2C scan comes up with.

```text
<* License GPLv3 fsf.org (c) dcc-ex.com >
< I2C Device found at 0x20, GPIO Expander? >
```

The driver is created with a HAL command:

```cpp
HAL(drivername,firstVpin,numberOfVpins,i2cAddress)
```

Some examples:

```cpp
// simple example vpins 160-175 on address 0x20
HAL(MCP23017,160,16,0x20)

// as above but for a different chip type
HAL(PCA9555,160,16,0x20) // easy isnt it...
```

For devices behind multiplexors see [multiplexors](/products/ex-commandstation/exrail/cookbooks/various-devices/multiplexors.md)

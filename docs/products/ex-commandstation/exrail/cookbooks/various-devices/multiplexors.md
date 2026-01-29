# I2C Multiplexors

A Multiplexor allows for multiple i2c devices with the same address to be separately addressed so that messages pass through the multiplexor and it routes them to the correct channel to find the device you want.

Multiplexors are handled automatically by dcc-ex and all drivers for i2c devivces can take a multiplexed address when being defined.

When the command dtstion starts, it scans the i2c network for all devices it can find, including those behid one or more multiplexors. Although the list can only guess the device type (there is no automatic device recognition, nor rigid standards that associate addresses with device types) it will give the fully qualified I2C address of each device and it is this that must be copied to the HAL device definition.

First step is to run the Command Station software without the drivers and note what addresses the I2C scan comes up with. This is especially important when using devices behind a multiplexor as the I2C address must include the multiplexor channel path.
The scan will look something like this:

```text
<* License GPLv3 fsf.org (c) dcc-ex.com >
< I2C Device found at 0x71, I2C Mux? >
< I2C Device found at {I2CMux_1,SubBus_7,0x20}, GPIO Expander? >
```

So the HAL definition will copy the {mux} information exactly as the I2C address. 

```cpp
// This would be a example vpins 160-175 on address 0x20  (no Mux)
HAL(MCP23017,160,16,0x20)

// Same device with address 0x20 but beyond a multiplexor
HAL(MCP23017,160,16,{I2CMux_1,SubBus_7,0x20})
```

IMPORTANT: You can't have two devices with address 0x20 (for example) where one is behind the multiplexor and the other is not... that can't be made to work.
So if you have two devices with the same address thay must BOTH be behind separate multiplexor channels.

You can have multiple multiplexors, but each must have a separate address.
You cant have a multiplexor behind another multiplexor.
  
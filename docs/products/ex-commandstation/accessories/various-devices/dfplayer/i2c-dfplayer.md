# I2C Connected DFPlayer

The UART on the SC16IS752 has 2 UARTS so can drive 2 DFplayers independently, the SC16IS750 has only one UART.

The breakout boards out in the wild have been discovered being fitted with either a 1.8432Mhz or 14.7456Mhz Crystal. The driver will automatically detect the frequency to make sure the correct baud rate is generated for each UART individually.

## SC16IS750 - SC16IS752 Breakout board hookup

![SC16IS750](/_static/images/DFPlayer/SC16IS750.png)
SC16IS750 breakout board hookup

![SC16IS752](/_static/images/DFPlayer/SC16IS752.png)
SC16IS750 breakout board hookup

## I2C address selection

The I2C addresses shown in Table 2 are different from the addresses shown in the datasheet, this is because the datasheet include the LSB in the address, the DCC-EX system start the I2C address at bit 1 (shifted). The I2C addresses in Table 2 are correct for the DCC-EX system and for the examples in section 3.

| A1  | A0  | I2C Address |
|-----|-----|-------------|
| Vdd | Vdd | 0x48        |
| Vdd | Vss | 0x49        |
| Vdd | SCL | 0x4A        |
| Vdd | SDA | 0x4B        |
| Vss | Vdd | 0x4C        |
| Vss | Vss | 0x4D        |
| Vss | SCL | 0x4E        |
| Vss | SDA | 0x4F        |
| SCL | Vdd | 0x50        |
| SCL | Vss | 0x51        |
| SCL | SCL | 0x52        |
| SCL | SDA | 0x53        |
| SDA | Vdd | 0x54        |
| SDA | Vss | 0x55        |
| SDA | SCL | 0x56        |
| SDA | SDA | 0x57        |

A total of 16 I2C addresses can be selected. The number of serial controllers can be significantly increased when they are installed on a PCA9548 multiplexer SubBus as each SubBus is its own I2C bus.

## Configuring in myAutomation.h

The I2C connected DFplayer is defined in EXRAIL using the HAL command

```cpp
HAL(DFPlayer,firstVpin,numVpins,i2cAddress)
```

- firstVpin is First virtual pin that EXRAIL can control to play a sound, or sent a command
- numVpins=1 indicates only one DFPLayer attached at UART channel 0,
numpins=2 indicates two DFPlayers attached, the second player will have a vipin of firstVpin+1.
- i2cAddress is the connected i2cAddress of the UART device

Typicaal examples

```cpp
HAL(DFPlayer,10000,1,0x48)
```

Where the connection is made through a multiplexor, the i2cAddress will reflect that, as for all other I2C HAL drivers.

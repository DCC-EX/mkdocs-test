---
hide:
  - toc
---

# Keyestudio IOT ESP32 PLUS Development Board *+* EX8874

![Keyestudio ESP32](/_static/images/esp32/keyestudio-iot-esp32-plus.png){ width=30% align=right }

## Keyestudio IOT ESP32 PLUS Development Board

- Limited testing has been done with this board.
- Please report any anomalies when using the pins in the suggested custom motor defines.
- A custom motor define is required when using the Keyestudio IOT ESP32 PLUS Development board, as the pins are in different locations vs. the WeMos ESP32.

## Keyestudio IOT ESP32 PLUS Development Board *vs* WeMos R1 D32

- Fewer modifications are required.  
- WiFi does not need the resistor.  
- Pin locations A0, A1 can be used for current sensing.  
- The default pins can be used on EX8874.  

## Incorrect IOREF voltage

The IOREF GPOI is labeled a `5V` on the board.

![ACEBOTT IOREF](/_static/images/esp32/esp32-keyestudio-ioref.png){ width=15% }

The IOREF voltage will not be correct. The ADC inputs will receive up to 5V when the IOREF pin is 5V wich will damage the board and likely destroy it.  As such it is vital that the modifications below are made.

![EX8874 IOREF](/_static/images/esp32/esp32-keyestudio-bent-pin.png){ width=25% align=right }

![EX8874 IOREF](/_static/images/esp32/ioref-override.png){ width=25% align=right }

### Option A (Recommended)

- The prefered work-around for the incorrect 5V pin is to modify the EX8874, using the **3V3 IOREF Override** solder pad on the EX8874.
- When using the 3V3 IOREF Override:

    1. Bend the IOREF pin out, *or*
    2. Confirm that the trace connecting the 5v pad is completely cut. (The red line in the image.) Scratch it with a blade till there is no contact between the two pads and check with a multimeter. Then solder from the center pad to the 3.3v pad.
    3. or both the above to be really sure

Double check that that you have it correct by checking wth a multimeter on the EX8874 before you connect it to the ES32:

- There should be an open circuit between the IOREF GPIO and the GND pin on the I2C pins
- There should be an open circuit between the other 5v GPIO (beside the two GND GPIOs) and the Vdd pin on the I2C pins
- There should be a closed circuit between the 3.3v GPIO and the Vdd pin on the I2C pins

### Option B (not recommneded)

- The IOREF pin location is the 5V GPIO pin.  If the pin on the EX8874 is bent out, the IOREF could be jumpered to 3V3 pin on the EX8874.

---

## One EX8874

Note:

- Keyestudio IOT ESP32 PLUS Development Board motor defines are not included in `MotorDrivers.h`
- Do not edit `MotorDrivers.h`; a custom motor define should be added in `config.h`
- Note how the ESP32 GPIO pin numbers are used, and the Arduino pin locations are shown/commented.

Add the following lines to your `config.h` and remove any existing `#define MOTOR_SHIELD_TYPE ...` line.

```
  #define EX8874_KEYES_ESP32 F("EX8874_KEYES_ESP32"),\
    new MotorDriver(25/* 3*/, 19/*12*/, UNUSED_PIN, 13/*9*/, 32/*A0*/, 1.52, 5000, 36 /*A4*/), \
    new MotorDriver(23/*11*/, 18/*13*/, UNUSED_PIN, 12/*8*/, 33/*A1*/, 1.52, 5000, 39 /*A5*/)
    #define MOTOR_SHIELD_TYPE EX8874_KEYES_ESP32
```

```
MotorDriver(int16_t power_pin, byte signal_pin, byte signal_pin2, int16_t brake_pin, 
                byte current_pin, float senseFactor, unsigned int tripMilliamps, int16_t fault_pin);
```

- When one EX8874 motor shield is used with Keyestudio IOT ESP32 PLUS Development Board, the default EX8874 pins are used.  

|output|Current<br/>Sense|PWM<br/>Enable|DIR<br/>Signal|Brake|Fault|Notes|
|:--:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|A|32 pA0|25 p3|19 p12|9 p9|36 pA4||
|B|33 pA1|23 p11|18 p13|8 p8|39 pA8||

### Single EX8874 Checklist

- [ ] Cover the barrel connector on Keyestudio IOT ESP32 PLUS Development Board, as VIN power will be provided by EX8874  
- [ ] IOREF Override set to 3v3  
- [ ] Confirm that IOREF pin is bent *or* trace is cut *or* both
- [ ] Add the custom motor define - 4 lines in `config.h`

---

## Stacked EX8874

==TODO==

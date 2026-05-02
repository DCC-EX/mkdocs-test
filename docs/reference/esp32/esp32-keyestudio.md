---
hide:
  - toc
---

# Keyestudio IOT ESP32 PLUS Development Board *+* EX8874

![Keyestudio ESP32](/_static/images/esp32/keyestudio-iot-esp32-plus.png){ width=30% align=right }

!!! note "Keyestudio ESP32 Beta Testing"

    Please note that the Keyestudio ESP32 board is currently in Beta testing, so this information may change at any time. If using this board, we highly recommend joining our [Discord server](/support/discord.md) and request access to the `#beta-testing` channel.

## Keyestudio IOT ESP32 PLUS Development Board

- Please report any anomalies when using the pins in the suggested custom motor defines.
- A custom motor define is required when using the **Keyestudio IOT ESP32 PLUS Development board**, as the pins are in different locations *VS* the WeMos ESP32.
- Do not be fooled by the `V` pin on the I²C header block as it is 5V, and there is no onboard level shifting of the SDA SCL pins.

## Keyestudio IOT ESP32 PLUS Development Board *VS* WeMos R1 D32

- Fewer modifications may be required.  
- WiFi does not need the resistor.  
- Pin locations A0, A1 can be used for current sensing.  
- The default pins can be used on EX8874.  

## Incorrect IOREF voltage

The IOREF pin is labeled a `5V` on the board.

![ACEBOTT IOREF](/_static/images/esp32/esp32-keyestudio-ioref.png){ width=15% }

The IOREF voltage will not be correct for this board combination.

<span style="color:red">Warning:</span> Without modification the ADC inputs will receive up to 5V when the IOREF pin is 5V which will damage the board and likely destroy it. ***As such it is vital that the modifications below are made.***

- Option A: The prefered work-around to the incorrect 5V pin is to modify the EX8874, using the `3V3 IOREF Override` solder pad on the EX8874.

- Option B: The `IOREF` pin location has the 5V pin.  An acceptable workaround is for the pin on the EX8874 to be bent out, and the `IOREF` to be jumpered to `3V3` pin on the EX8874.

See the [Incorrect IOREF voltage page](ioref-incorrect-voltage-fix_not_in_nav.md) for details on how to correct the IOREF voltage for this board combination.

---

## One EX8874

Note:

- *Keyestudio IOT ESP32 PLUS Development Board motor* defines are not included in `MotorDrivers.h`
- Do not edit `MotorDrivers.h`; a custom motor define should be added in `config.h`
- Note how the ESP32 GPIO pin numbers are used, and the Arduino pin locations are shown/commented.

Add the following lines to your `config.h` and remove any existing `#define MOTOR_SHIELD_TYPE ...` line.

```cpp
  #define EX8874_KEYES_ESP32 F("EX8874_KEYES_ESP32"),\
    new MotorDriver(25/* 3*/, 19/*12*/, UNUSED_PIN, 13/*9*/, 32/*A0*/, 1.52, 5000, 36 /*A4*/), \
    new MotorDriver(23/*11*/, 18/*13*/, UNUSED_PIN, 12/*8*/, 33/*A1*/, 1.52, 5000, 39 /*A5*/)
  #define MOTOR_SHIELD_TYPE EX8874_KEYES_ESP32
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

- Reminder: No modifications are needed when stacking an EX8874 on an EX-CSB1 for 4 track outputs.
- **IOREF:** The IOREF override is also needed for the top shield. See the [Incorrect IOREF voltage page](ioref-incorrect-voltage-fix_not_in_nav.md) for details.
- **VIN:** Refer to instructions on [cutting the VIN trace and disabling the regulator](/products/ex-motorshield8874/ex-motorshield8874.md/#steps-to-stack) for the top shield.

![ACEBOTT IOREF](/_static/images/esp32/keyestudio-ex-8874-stacked-pads.png){ width=12% align=right }

- Stacking motor shields on Keystudio ESP32 requires:

      a. Use of solder pad for 8 alternate pins
      
      b. \^ for Fault pins, the pins on the ESP32 board labeled `io2` and `io4` will need to be bent about 90 degrees so that jumpers can be put on them.  `io2` will need to be jumpered to `A4` on the EX8874. `io4` will need to be jumpered to `A5` on the EX8874.

First EX8874

|output|Current<br/>Sense|PWM<br/>Enable|DIR<br/>Signal|Brake|Fault|Notes|
|:--:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|A|32 pA0|25 p3|19 p12|9 p9|36 pA4|Default pins|
|B|33 pA1|23 p11|18 p13|8 p8|39 pA8||

Second EX8874

|output|Current<br/>Sense|PWM<br/>Enable|DIR<br/>Signal|Brake|Fault|Notes|
|:--:|:-----:|:-----:|:-----:|:-----:|:-----:|:-------------:|
|C|34 pA2|26 p2|5 p10|14 p7|<span style="color:green">2 </span><span style="color:red">pA4</span>|use alternates for 8 pins|
|D|35 pA3|16 p5|17 p4|27 p6|<span style="color:green">4 </span><span style="color:red">pA5</span>|\^ <span style="color:red">Bend</span> & <span style="color:green">jumper</span>. See notes|

- A custom motor define will be needed in `config.h`

```cpp
  #define EX8874X2_KEYES_ESP32 F("EX8874X2_KEYES_ESP32"), \  
    new MotorDriver(25/* 3*/, 19/*12*/, UNUSED_PIN, 13/*9*/, 32/*A0*/, 1.52, 5000, 36/*A4*/), \  
    new MotorDriver(23/*11*/, 18/*13*/, UNUSED_PIN, 12/*8*/, 33/*A1*/, 1.52, 5000, 39/*A5*/), \  
    new MotorDriver(26/* 2*/,  5/*10*/, UNUSED_PIN, 14/*7*/, 34/*A4*/, 1.52, 5000, 2 /*A4*/), \  
    new MotorDriver(16/* 5*/, 17/* 4*/, UNUSED_PIN, 27/*6*/, 35/*A5*/, 1.52, 5000, 4 /*A5*/)  
  #define MOTOR_SHIELD_TYPE EX8874X2_KEYES_ESP32
```

### Stacked EX8874 Checklist

- [ ] Cover the barrel connector on Keyestudio IOT ESP32 PLUS Development Board, as VIN power will be provided by one EX8874  
- [ ] IOREF Override set to 3v3 on both EX8874 boards  
- [ ] Confirm that IOREF pin is bent or trace is cut
- [ ] VIN trace cut and regulator disabled on top EX8874  
- [ ] Alternate pins enabled via solder pads  
- [ ] Jumpers added for GPIO 2 and 4  
- [ ] Add the custom motor define - 6 lines in config.h  

==TODO==

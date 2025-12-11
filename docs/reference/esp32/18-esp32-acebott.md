# ACEBOTT + EX8874

!!! note "ACEBOTT Beta Testing"

    Please note that the ACEBOTT board is currently in Beta testing, so this information may change at any time. If using this board, we highly recommend joining our [Discord server](/support/05-discord.md) and request access to the `#beta-testing` channel.

![ACEBOTT ESP32](/_static/images/esp32/esp32-acebott.png){ width=40% align=right }

## ACEBOTT ESP32 Max v1.0

- Limited testing has been done with this board.
- Please report any anomalies when using the pins in the suggested custom motor defines.
- A custom motor define is required when using the ACEBOTT ESP32 board, as the pins are in different locations vs. the WeMos ESP32.
- There is another version of the ACEBOTT ESP32 which has not been tested.  ACEBOTT focus is on STEM education kits and robotics; uncertain if their quality is better than the WeMos boards, but recent prices are comparable.
- Do not be fooled by the 5V pin on the I2C header block; there is no onboard level shifting.

## ACEBOTT vs. WeMos R1 D32

- Fewer modifications may be required.  
- WiFi does not need the resistor.  
- Pin locations A0, A1 can be used for current sensing.  
- Default pins can be used on EX8874.  

![ACEBOTT IOREF](/_static/images/esp32/esp32-acebott-ioref.png){ width=10% align=right }
![EX8874 IOREF](/_static/images/esp32/ioref-override.png){ width=25% align=right }

## IOREF voltage

- The IOREF pin location has the 5V pin.  If the pin on the EX8874 is bent, the IOREF could be jumpered to 3V3 pin on the EX8874.
- The preferable work-around to the incorrect 5V pin is to modify the EX8874, using the **3V3 IOREF Override** solder pad on the EX8874. If voltage is not correct, the ADC inputs will receive up to 5V when the IOREF pin is 5V.
- When using the 3V3 IOREF Override, bend the IOREF pin or confirm that the trace connecting the pin is completely cut.

---

## One EX8874

- ACEBOTT ESP32 motor defines are not included in MotorDrivers.h
- Do not edit MotorDrivers.h; a custom motor define should be added in config.h
- Note how the ESP32 GPIO pin numbers are used, and the Arduino pin locations are shown/commented.

```cpp
  #define EX8874_ACEBOTT_ESP32 F("EX8874_ACEBOTT_ESP32"), \  
    new MotorDriver(26/* 3*/, 16/*12*/, UNUSED_PIN, 19/*9*/, 32/*A0*/, 1.52, 5000, 36/*A4*/), \  
    new MotorDriver(17/*11*/,  5/*13*/, UNUSED_PIN, 23/*8*/, 33/*A1*/, 1.52, 5000, 39/*A5*/)  
  #define MOTOR_SHIELD_TYPE EX8874_ACEBOTT_ESP32
```

- When one EX8874 motor shield is used with ACEBOTT ESP32 Max v1.0, the default EX8874 pins are used.  
  
&nbsp; &nbsp; &nbsp; &nbsp;![ACEBOTT table](/_static/images/esp32/acebott-ex8874-x1b.png){ width=80% }

### Single EX8874 Checklist

- [ ] Cover the barrel connector on ACEBOTT ESP32, as VIN power will be provided by EX8874  
- [ ] IOREF Override set to 3v3  
- [ ] Confirm that IOREF pin is bent or trace is cut  
- [ ] Add the custom motor define - 4 lines in config.h  

---

## Stacked EX8874

- Reminder: No modifications are needed when installing EX8874 for 4 track outputs on EX-CSB1.
- **IOREF:** The IOREF override is also needed for the top shield.
- **VIN:** Refer to instructions on [cutting the VIN trace and disabling the regulator](/products/ex-motorshield8874/00-ex-motorshield8874.md/#steps-to-stack) for the top shield.

- Stacking motor shields on ACEBOTT ESP32 requires  
    a. use of solder pad for 8 alternate pins  
    b. for Fault pins, bend A4 and A5 pins and jumper to the GPIO headers  

&nbsp; &nbsp; &nbsp; &nbsp;![ACEBOTT table](/_static/images/esp32/acebott-ex8874-x2b.png){ width=80% }

- A custom motor define will be needed in config.h

```cpp
  #define EX8874X2_ACEBOTT_ESP32 F("EX8874X2_ACEBOTT_ESP32"), \  
    new MotorDriver(26/* 3*/, 16/*12*/, UNUSED_PIN, 19/*9*/, 32/*A0*/, 1.52, 5000, 36/*A4*/), \  
    new MotorDriver(17/*11*/,  5/*13*/, UNUSED_PIN, 23/*8*/, 33/*A1*/, 1.52, 5000, 39/*A5*/), \  
    new MotorDriver(27/* 2*/, 18/*10*/, UNUSED_PIN, 12/*7*/, 34/*A4*/, 1.52, 5000, 2 /*A4*/), \  
    new MotorDriver(14/* 5*/, 25/* 4*/, UNUSED_PIN, 13/*6*/, 35/*A5*/, 1.52, 5000, 4 /*A5*/)  
  #define MOTOR_SHIELD_TYPE EX8874X2_ACEBOTT_ESP32
```

### Stacked EX8874 Checklist

- [ ] Cover the barrel connector on WeMos R1 D32, as VIN power will be provided by one EX8874  
- [ ] IOREF Override set to 3v3 on both EX8874 boards  
- [ ] Confirm that IOREF pin is bent or trace is cut
- [ ] VIN trace cut and regulator disabled on top EX8874  
- [ ] Alternate pins enabled via solder pads  
- [ ] Jumpers added for GPIO 2 and 4  
- [ ] Add the custom motor define - 6 lines in config.h  

==TODO==

---
hide:
  - toc
---

# Nucleo 144 - EX8874

Review of **motor shield define** from MotorDrivers.h for F429ZI or F439ZI

```cpp
  #if defined(ARDUINO_NUCLEO_F429ZI) || defined(ARDUINO_NUCLEO_F439ZI) || defined(ARDUINO_NUCLEO_F4X9ZI)  
  // EX 8874 based shield connected to a 3V3 system with 12-bit (4096) ADC  
  // The Ethernet capable STM32 models cannot use Channel B BRAKE on D8, and must use the ALT pin of D6,  
  // AND cannot use Channel B PWN on D11, but must use the ALT pin of D5  
  #define EX8874_SHIELD F("EX8874"), \  
    new MotorDriver( 3, 12, UNUSED_PIN, 9, A0, 1.27, 5000, A4), \  
    new MotorDriver( 5, 13, UNUSED_PIN, 6, A1, 1.27, 5000, A5)  
```

Alternate pins D5 and D6 are required for the Nucleo-144 boards with Ethernet.  
One EX8874 motor shield would use the standard motor define EX8874_SHIELD, and update the solder pads to use D5 and D6.  

 &nbsp; &nbsp; &nbsp; &nbsp; ![EX8874 Nucleo-144 pins](/_static/images/nucleo/ex8874-nucleo-144.png){: style="width: 70%"} &nbsp; &nbsp; &nbsp; &nbsp; ![EX8874 Nucleo-144 track B](/_static/images/nucleo/ex8874-nucleo144-pins-track-b.png){: style="width: 20%"}

## Stacked EX8874 motor shields on F429ZI F439ZI

- When using two EX8874 motor shields, the VIN on one shield can be used to power the Nucleo-144.  
  Cut two traces to disable VIN on the stacked/second shield. &nbsp; [Link to Hardware EX8874 page](/products/ex-motorshield8874/ex-motorshield8874.md/#steps-to-stack)

 &nbsp; &nbsp; &nbsp; &nbsp; ![Stacked EX8874 Nucleo-144](/_static/images/nucleo/ex8874x2-nucleo-144.png){: style="width: 50%" align=right}

- Review where jumpers will be required, due to pin conflict/function/availability.

&nbsp; &nbsp; &nbsp; &nbsp; ![Stacked EX8874 Nucleo-144](/_static/images/nucleo/ex8874-f439zi-stacked-pins.png){: style="width: 50%" align=right}

- Tracks A and B can use the same alternate pins D5 and D6 as they would if only one shield was used.  
  Pins were selected so that the stacked motor shield pins D11,D9,D8,A4,A5 can be bent out, and short jumpers added to connect pins D7,D28,D29,D64,D65.

 <div style="clear: both;"></div>
- A custom motor define will be needed in config.h

```cpp
  #define EX8874_SHIELDX2 F("EX8874_SHIELDX2"), \  
    new MotorDriver( 3, 12, UNUSED_PIN,  9, A0, 1.27, 5000, A4), \  
    new MotorDriver( 5, 13, UNUSED_PIN,  6, A1, 1.27, 5000, A5), \  
    new MotorDriver( 2, 10, UNUSED_PIN, 28, A2, 1.27, 5000, 64), \  
    new MotorDriver( 7,  4, UNUSED_PIN, 29, A3, 1.27, 5000, 65)  
  #define MOTOR_SHIELD_TYPE EX8874_SHIELDX2
```

## EX8874 - F413ZH F446ZE

- If using two EX8874 motor shields, the VIN on one shield can be used to power the Nucleo-144.  
  Cut two traces to disable VIN on the stacked/second shield. &nbsp; [Link to Hardware EX8874 page](/products/ex-motorshield8874/ex-motorshield8874.md/#steps-to-stack)

- D11 can be used as there is no Ethernet conflict.  
Brake and Fault pin updates as shown for F429ZI F439ZI.

==TODO== - update MotorDrivers.h for D8

- This motor define can be used with E8874 and F413ZH F446RE  
  \- alternate Brake pin is used for Track B  
  \- presently a custom motor define is needed in config.h

```cpp
 #define EX8874_F413ZH F("EX8874_F413ZH"), \  
    new MotorDriver( 3, 12, UNUSED_PIN, 9, A0, 1.27, 5000, A4), \  
    new MotorDriver(11, 13, UNUSED_PIN, 6, A1, 1.27, 5000, A5)  
 #define MOTOR_SHIELD_TYPE EX8874_F413ZH
```

&nbsp; &nbsp; &nbsp; &nbsp; ![Stacked EX8874 Nucleo-144](/_static/images/nucleo/ex8874-f446ze-stacked-pins.png){: style="width: 50%" align=right}

- Stacked EX8874 shields on F413ZH F446ZE  
  \- Very similar to modifications/jumpers of F429ZI F439ZI  
  \- D11 can be used for track B; D5 can be used for track D  
  \- Brake and Fault pin modifications/jumpers as above  
  \- A custom motor define will be needed in config.h

```cpp
  #define EX8874_F413ZH_X2 F("EX8874_F413ZH_X2"), \  
    new MotorDriver( 3, 12, UNUSED_PIN,  9, A0, 1.27, 5000, A4), \  
    new MotorDriver(11, 13, UNUSED_PIN,  6, A1, 1.27, 5000, A5), \  
    new MotorDriver( 2, 10, UNUSED_PIN, 28, A2, 1.27, 5000, 64), \  
    new MotorDriver( 5,  4, UNUSED_PIN, 29, A3, 1.27, 5000, 65)  
  #define MOTOR_SHIELD_TYPE EX8874_F413ZH_X2
```

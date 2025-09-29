# Nucleo 144 - Pins

## Pin diagrams

- Pin diagrams of Zio headers are edited to include Arduino style pin numbers.  
  These are F429ZI/F439ZI; F446ZE and F413ZH are quite similar.  Refer to varaint files to confirm.

&nbsp; &nbsp; &nbsp; &nbsp; ![EX8874 Nucleo-144 pins](/_static/images/nucleo/f429zi-left-cn8-cn9.jpg){: style="width: 80%"}  
&nbsp; &nbsp; &nbsp; &nbsp; ![EX8874 Nucleo-144 pins](/_static/images/nucleo/f429zi-right-cn7-cn10.jpg){: style="width: 80%"}

- Links to st.com for each Nucleo-144 and the UM1974 pdf  
  [https://os.mbed.com/platforms/ST-Nucleo-F429ZI/](https://os.mbed.com/platforms/ST-Nucleo-F429ZI/)  
  [https://os.mbed.com/platforms/ST-Nucleo-F446ZE/](https://os.mbed.com/platforms/ST-Nucleo-F446ZE/)  
  [https://os.mbed.com/platforms/ST-Nucleo-F413ZH/](https://os.mbed.com/platforms/ST-Nucleo-F413ZH/)  
  [UM1974 Nucleo-144](https://www.st.com/resource/en/user_manual/um1974-stm32-nucleo144-boards-mb1137-stmicroelectronics.pdf)  
  [UM1724 Nucleo-64](https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf)

- Location of variant files  
  C:\Users\username\\.platformio\packages\framework-arduinoststm32\variants\STM32F4xx\F427Z(G-I)T_F429ZET_F429Z(G-I)(T-Y)_F437Z(G-I)T_F439Z(G-I)(T-Y)  
  C:\Users\username\AppData\Local\Arduino15\packages\STMicroelectronics\hardware\stm32\2.9.0\variants\STM32F4xx\F427Z(G-I)T_F429ZET_F429Z(G-I)(T-Y)_F437Z(G-I)T_F439Z(G-I)(T-Y)

## 8 District PCB

This is a prototype/development board - - almost plug-n-play, once the headers and other components are soldered.  Motor shields are installed without modifications.

- Table of pins used in motor define
  &nbsp; &nbsp; &nbsp; &nbsp; ![motor define pins](/_static/images/nucleo/nucleo-8track-003-0041-pins.jpg){: style="width: 30%" align=center}

- Link to pdf with pins assigned for 8 districts and other accessories  
  [Nucleo-144 pin use table - pdf](/_static/images/nucleo/pin-use-table-f446ze-f429zi-20240402.pdf)

- Add custom motor define in config.h  
  Example shows two EX8874 and two L298 motor shields

```cpp
  #define F439_4X2 F("F439_4X2"), \
    new MotorDriver(16, 21, UNUSED_PIN, 10, A13, 1.27, 5000, 20), \  
    new MotorDriver(22, 23, UNUSED_PIN, 5, A6, 1.27, 5000, 25), \  
    new MotorDriver(26, 43, UNUSED_PIN, 28, A2, 1.27, 5000, 27), \  
    new MotorDriver(30, 44, UNUSED_PIN, 29, A8, 1.27, 5000, 49), \  
    new MotorDriver(39, 36, UNUSED_PIN, 38, A3, 0.73, 1500, UNUSED_PIN), \  
    new MotorDriver(34, 35, UNUSED_PIN, 58, A4, 0.73, 1500, UNUSED_PIN), \  
    new MotorDriver(57, 64, UNUSED_PIN, 59, A5, 0.73, 1500, UNUSED_PIN), \  
    new MotorDriver(66, 65, UNUSED_PIN, 61, A14, 0.73, 1500, UNUSED_PIN)  
  #define MOTOR_SHIELD_TYPE F439_4X2
```

![8 district pcb](/_static/images/nucleo/8track-4x-01.png){: style="width: 45%"}
![8 district pcb](/_static/images/nucleo/8track-pcb-02.jpg){: style="width: 46%"}  
&nbsp; &nbsp;  
![8 district pcb](/_static/images/nucleo/pcb-nucleo-144-0031-2024062901.png){: style="width: 92%"}

- [Schematic](/_static/images/nucleo/schematic-nucleo-144-0031-20240629.pdf)

- Limited availability upon request - open a ticket on the discord server

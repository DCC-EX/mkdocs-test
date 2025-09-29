# Nucleo 64 - WiFi and Pins

## MakerFabs WiFi shield

- ![MakerFabs WiFi shield](/_static/images/nucleo/makerfabs-wifi-3v3.png){: style="width: 30%" align=right}
  Remove the shorting jumpers to disconnect pins D0/D1.  
  <BR>
  3.3V headers can be installed on the WiFi shield and flying wire jumpers used to connect USART6 or UART2 pins.  (remove the shorting jumpers)  
  <BR>
  The defined serial pins are 5V tolerant on the Nucleo-F4 boards; jumpers might be used to connect the 5V RxTx pins.
  
## Serial pins

- Specific pins are defined for the Nucleo-64 boards.  
  This shows how 3 serial ports are defined for some Nucleo-144 boards; two are polled to see if WiFi is connected.

```cpp
  #if defined(ARDUINO_NUCLEO_F401RE)  
    HardwareSerial Serial1(PB7, PB6);  // Rx=PB7, Tx=PB6 -- CN7 pin 17 and CN10 pin 17  
    HardwareSerial Serial6(PA12, PA11);  // Rx=PA12, Tx=PA11 -- CN10 pins 12 and 14 - F401RE  
  #elif defined(ARDUINO_NUCLEO_F411RE)  
    HardwareSerial Serial1(PB7, PA15);  // Rx=PB7, Tx=PA15 -- CN7 pins 17 and 21 - F411RE  
    HardwareSerial Serial6(PA12, PA11);  // Rx=PA12, Tx=PA11 -- CN10 pins 12 and 14 - F411RE  
  #elif defined(ARDUINO_NUCLEO_F446RE)  
    HardwareSerial Serial3(PC11, PC10);  // Rx=PC11, Tx=PC10 -- USART3 - F446RE  
    HardwareSerial Serial5(PD2, PC12);  // Rx=PD2, Tx=PC12 -- UART5 - F446RE   
```

- WiFi Polling alias  
  The SERIAL1 or SERAIL3 alias would be used in config.h, if Serial1, Serial6, Serial3 or Serial5 are used for other purposes.

```cpp
  #if defined(ARDUINO_NUCLEO_F401RE) || defined(ARDUINO_NUCLEO_F411RE)  
    #define SERIAL1 Serial1  
    #define SERIAL3 Serial6  
  #elif defined(ARDUINO_NUCLEO_F446RE)  
    #define SERIAL1 Serial3  
    #define SERIAL3 Serial5  
```

- Serial pins for Nucleo-64 and Nucleo-144 boards  
  ![Nucleo serial pins](/_static/images/nucleo/nucleo-wifi-pins.png){: style="width: 80%"}  

## Pin diagram

- Pin diagram for Nucleo-64 boards  
  ![Nucleo 64 serial pins](/_static/images/nucleo/f411re-f446re-pins.png){: style="width: 80%"}  

- Links to st.com for each Nucleo-64 and the UM1724 pdf  
  [https://os.mbed.com/platforms/ST-Nucleo-F411RE/](https://os.mbed.com/platforms/ST-Nucleo-F411RE/)  
  [https://os.mbed.com/platforms/ST-Nucleo-F446RE/](https://os.mbed.com/platforms/ST-Nucleo-F446RE/)  
  [UM1724 Nucleo-64](https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf)  
  [UM1974 Nucleo-144](https://www.st.com/resource/en/user_manual/um1974-stm32-nucleo144-boards-mb1137-stmicroelectronics.pdf)

- Location of variant files  
  C:\Users\username\\.platformio\packages\framework-arduinoststm32\variants\STM32F4xx\F411R(C-E)T  
  C:\Users\username\\.platformio\packages\framework-arduinoststm32\variants\STM32F4xx\F446R(C-E)T  
  C:\Users\username\AppData\Local\Arduino15\packages\STMicroelectronics\hardware\stm32\2.9.0\variants\STM32F4xx\F411R(C-E)T  
  C:\Users\username\AppData\Local\Arduino15\packages\STMicroelectronics\hardware\stm32\2.9.0\variants\STM32F4xx\F446R(C-E)T

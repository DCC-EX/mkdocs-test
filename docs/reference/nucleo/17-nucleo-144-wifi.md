# Nucleo 144 - WiFi

## MakerFabs WiFi shield
TODO - HowTo connect MakerFabs WiFi shield -- which shield pins to use for 3.3V uC

## Serial pins

- Specific pins are defined for the Nucleo-144 boards.  
  This shows how 3 serial ports are defined for some Nucleo-144 boards; two are polled to see if WiFi is connected.

```cpp
  HardwareSerial Serial6(PG9, PG14);  // Rx=PG9, Tx=PG14 -- USART6  
  HardwareSerial Serial2(PD6, PD5);  // Rx=PD6, Tx=PD5 -- UART2  
  #if !defined(ARDUINO_NUCLEO_F412ZG)  // F412ZG does not have UART5  
    HardwareSerial Serial5(PD2, PC12);  // Rx=PD2, Tx=PC12 -- UART5  
```

- WiFi Polling alias  
  The SERIAL1 or SERAIL3 alias would be used in config.h, if Serial6 or Serial2 are used for other purposes.

```cpp
  #define SERIAL1 Serial6  
  #define SERIAL3 Serial2  
```

- Serial pins for Nucleo-64 and Nucleo-144 boards  
  ![8 district pcb](/_static/images/nucleo/nucleo-wifi-pins.png){: style="width: 80%"}  

## Pin diagram

- Pin diagram for Nucleo-144 boards  
  Read the notes added to the diagram.  
  ![8 district pcb](/_static/images/nucleo/serial-nucleo144.png){: style="width: 80%"}  

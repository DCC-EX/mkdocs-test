# Complex Build - ESP32

ESP32-WROOM-32 was selected as the microprocessor for the EX-CSB1. Although folks are encouraged to use the [EX-CSB1](/products/ex-commandstation/ex-csb1.md), the information on this page should assist in building an ESP32-based DCC-EX command station.

!!! warning "ESP32 Wroom Only!"

    The only Espressif ESP32 microprocessor we support is the ESP32 Wroom. Espressif has released numerous ESP32 modules and variants (S2, S3, C3 etc.) but these are **NOT** supported. Other variants do not have the necessary RMT hardware, or do not have enough such hardware to run DCC-EX.

![ESPDuino-32](/_static/images/esp32/esp32-wroom32-mark.png){: style="width: 30%" align=right}  

- ESP32-WROOM-32 advantages  

    - Built-in WiFi  
    - Memory  
    - Sniffer/Booster capable (with additional optocoupler circuit)  

- ESP32-WROOM-32 is more complex than using the Arduino Mega  

    - GPIO pin numbers are used (vs. Arduino style pin location numbers)  
    - ESP32 pins are not 5V tolerant  
    - I2C bus is 3.3V  
    - Soldering is required to modify the WeMos D1 R32/ESPDuino-32 board  
    - Modifications are required for motor shields to protect ADC input pins  
    - ADC input range begins at 0.15V  
    - ESP32 Espressif boards package version 2.0.17 is required

![ESPDuino-32](/_static/images/esp32/espduino-32.png){: style="width: 25%" align=right}  

## WeMos D1 R32

- WeMos D1 R32/ESPDduino-32 has the Uno form factor.
- WeMos D1 R32 boards have some obvious hardware errors:  

    - Pullup voltage to the IO0 pin is too high (4.2v instead of 3.3-3.8v) which leads to unreliable WiFi.  
    - IOREF pin does not output 3v3, but instead breaches the UNO R3 specification and outputs 5V.  
    - A0 and A1 pins cannot be used for ADC input when WiFi is used.

- There are other ESP32-WROOM-32 boards with the Uno form factor which might work, but these will require a custom motor define when there are differences in GPIO pin locations.

## ESP32-WROOM-32 Development boards

![ESPDuino-32](/_static/images/esp32/esp32-dev-boards.png){: style="width: 30%" align=right}

- ESP32-WROOM-32 Development boards come in various sizes and pin configurations.
- 38-pin and 30-pin boards are common.
- Only the ESP32-WROOM-32 variants can be used.

## Reference ESP32

- Assembly and other information: [Reference - ESP32](/reference/esp32/esp32-ex8874.md)
- [Legacy ESP32 documentation](https://dcc-ex.com/legacy-docs/reference/hardware/microcontrollers/esp32.html#esp32-recommended)

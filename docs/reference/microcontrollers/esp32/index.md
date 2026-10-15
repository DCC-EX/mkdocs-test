# ESP32 Microcontrollers - Overview

!!! warning inline end "ESP32 Wroom Only!"

    The only Espressif ESP32 microprocessor we support is the ESP32 Wroom. Espressif has released numerous ESP32 modules and variants (S2, S3, C3 etc.) but these are **NOT** supported. Other variants do not have the necessary RMT hardware, or do not have enough such hardware to run **EX-CommandStation**.

ESP32-WROOM-32 was selected as the microprocessor for the EX-CSB1. Although folks are encouraged to use the EX-CSB1, the information on these pages should assist in building an ESP32-based DCC-EX EX-CommandStation.

Also refer to [Complex Build - ESP32](../../../diy/esp32.md) for a general overview.  

## Known Working Boards

- [WeMos D1 R32 + EX8874](esp32-ex8874.md). Also described in the WeMos D1 R32/ESPDUINO-32 section below
- [ACEBOTT ESP32 Max v1.0 + EX8874](esp32-acebott.md)  This requires fewer hardware modifications than the WeMos D1 R32
- [Keyestudio IOT ESP32 PLUS Development Board + EX8874](esp32-keyestudio.md)  This requires fewer hardware modifications than the WeMos D1 R32
- [ESP32 + L298 Shields (Genuine Arduino R3)](esp32-l298-shield.md)

--8<-- "snippets/abbr.md"

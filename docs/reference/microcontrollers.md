# Microcontroller Boards - Overview

## Current list of Microcontrollers

**EX-CommandStation** currently is designed for Atmel AVR based Arduino and compatible microcontrollers, some ESP32 based boards and the STM32 Nucleo based boards. Out of the box, it is compatible with the following boards:

* [EX-CSB1](../products/ex-commandstation/ex-csb1.md)
* Arduino [Mega2560](../diy/mega-easy.md)
* [ESP32-WROOM](./esp32/esp32-acebott.md)
* [STM32 Nucleo](./nucleo/nucleo-drivers.md)
* Arduino [Mega+WiFi](https://dcc-ex.com/legacy-docs/reference/hardware/microcontrollers/wifi-mega.html) (Not Recommended)

## Choosing a microcontroller

With a number of microcontrollers to choose from, how do you know which is the best for your needs?

We've compiled this simple summary table to help with this:

<style>
.md-typeset .md-typeset__scrollwrap {
    overflow-x: auto !important;
    overflow-y: visible !important;
}

.md-typeset__scrollwrap table {
    display: table !important;
    width: 100% !important;
    border-collapse: separate !important;
    border-spacing: 0 !important;
}

.md-typeset__scrollwrap th:first-child,
.md-typeset__scrollwrap td:first-child,
.md-typeset table tr th:first-child,
.md-typeset table tr td:first-child {
    position: sticky;
    left: 0;
    z-index: 3; /* Keeps the column on top of the scrolling content */
    background: var(--md-default-bg-color--light);
}

.md-typeset table td,
.md-typeset table th {
    font-size: smaller !important;
    padding-top: 2px !important;
    padding-bottom: 2px !important;
    padding-left: 2px !important;
    padding-right: 2px !important;
    line-height: 110% !important;
    font-family: 'Roboto Condensed', sans-serif !important;
 }
</style>

| Type / Brand | Recommended | Supported | Level | Shield[^9] | HAL/I2C | EEPROM | EX-RAIL<br/>Support | Track Manager<br/>Support | D C<br/>Sup-<br/>port | WiFi | WiFi no.<br/> Connections[^6] | Comments / Notes |
| -- | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :-- |
| [EX-CSB1](../products/ex-commandstation/ex-csb1.md) | Yes | Yes | Easy | Mega | Yes | No | Yes | Yes | Yes | Yes | ~11 | This is our stable, well supported platform |
| Arduino [Mega2560](../diy/mega-easy.md) | Yes | Yes | Intermediate | UNO | Yes | Yes | Yes | Yes | Yes [^2] | yes [^1] | 4 | This is our stable, well supported platform |
| [ESP32-WROOM](./esp32/esp32-acebott.md) | Yes | Yes | Complex | UNO | Yes [^4] | No | Yes | Yes | Yes [^2] | Yes | ~11 | Inexpensive and includes both WiFi and Bluetooth connectivity, limited in I/O pins. Most require hardware modifications to work. |
| [STM32 Nucleo](./nucleo/nucleo-drivers.md) | Yes | Yes | Complex | UNO | Yes | No | Yes | Yes | Yes [^2] [^3] | Yes [^1] [^3] | 4 | Lots of memory and 32 bit architecture, still in the convenient Uno form factor but with more I/O pins |
| Arduino [Mega+WiFi](https://dcc-ex.com/legacy-docs/reference/hardware/microcontrollers/wifi-mega.html) | No [^5] | Yes | Intermediate | Mega | Yes | Yes | Yes | Yes | Yes [^2] | Yes | 4 | This is our stable, well supported platform, but with WiFi on board, but beware quality issues |

[^1]: Requires an additional [WiFi shield](./hardware/wifi-boards/index.md)
[^2]: Requires a supported motor driver that supports [TrackManager](../products/ex-commandstation/trackmanager/trackmanager.md)
[^3]: Features and support in Beta testing can and will change regularly, be sure to keep up to date with developments on our [Discord server](https://discord.gg/y2sB4Fp)
[^4]: HAL/I2C connectivity is only available via the blocking Arduino Wire library at present
[^5]: While the Mega+WiFi boards seem like a good option and are based on our well-known, stable Mega2560 platform, there are many reports of quality issues with these, so buyer beware, and use of these is not recommended
[^6]: Number of *direct* WiFi connections.  If connected via JMRI, more are are supported
[^9]: If the board supports stackable shields.  UNO, Mega = Supports both Uno/Mega shields, - = no shield format

## Will you support other microcontrollers in the future?

New microcontrollers are constantly being developed and released, and we continue to monitor those to see if they are beneficial for our users.

Right now, however, we have a good selection of microcontrollers with the Mega2560 and the newer generation ESP32 and STMicroelectronics Nucleo, so we're not looking to add more in the immediate future.

Note the Arduino Giga and Arduino Uno R4 are still not on our roadmap and probably will never be.

## Notes on 3v3 vs 5V microcontrollers

It's important to note that the newer generations of microcontrollers almost always operate at 3.3 volts rather than 5 volts.

### Digital IO

For some, like the STM32F4xx range, this is largely a non-issue as many of their digital I/O pins are designed to be 5V tolerant, meaning your existing digital sensors, serial devices, and I2C devices running at 5V are expected to be compatible. Outputs may need further consideration though, as while a "high" signal at 3v3 will trigger most 5V input logic devices, in some rare instances it can potentially not provide a high enough voltage. Using level shifters for digital outputs will resolve these issues, and if you want an extra layer of caution, you can use level shifters for the digital inputs as well.

For others that are not 5V tolerant, such as the ESP32, connecting accessories with 5V outputs to the ESP32's input **will** cause damage to the microcontroller. Therefore, for ESP32 and similar 3v3-only microcontrollers digital input level shifters is **mandatory**. For digital outputs from 3v3 microcontrollers you may find most accessories with 5V inputs will accept 3v3 as a correct "logic 1".

### Analog IO

However, **ALL** 3v3 microcontrollers require analog inputs to be restricted to no more than 3.3V. This means only some Motor Driver boards are compatible unmodified with 3v3 microcontrollers to read output current. For the moment we recommend the genuine Ardiuno Motor Driver R3, and only the R3 version of it. Motor Drivers such as the Deek Robot can be modified readily enough. We will document this, but in the meantime ask on the Discord server.

!!! note "Some devices are already 3v3v"

    Some devices such as the ESP01 WiFi board and HC05/06 Bluetooth boards are already 3v3 devices, so if you have set these up with level shifters, the level shifters will no longer be required when using 3v3 microcontrollers.

## Boards for which support has been discontinued

These boards were previously supported, but current versions of the **EX-CommandStation** software no longer do.

You can still flash these boards with older versions of the **EX-CommandStation** software if you so wish.

* Arduino UNO
* SMD21
* Nano Every
* Teensy

## Boards that *will NOT work*

**WAVGAT Uno clone** - This board is NOT 100% Uno compatible. It uses a LGT8F328P processor from a company in China called "Logic Green". It has no EEPROM and requires a bit of configuration in the Arduino IDE to get it to be seen correctly and compile sketches. It is, however, a good board for developing other applications on because it can be switched to run at 32mHz instead of 16. It also has 12 bit analog pins instead of 10 bit. That means higher resolution readings, 0-4096 instead of 0-1024. It could potentially work as a Command Station with more testing and some code changes, but we will leave that to someone else to attempt. Various other microcontrollers offer more memory, more serial ports and more GPIO pins and are just a better way to go for the future.

**Arduino Uno R4** - Despite the name, this is not simply a new release of the tried and true Arduino Uno platform, and is a major redesign using a totally different CPU architecture and is expensive. Refer to the :doc:`/news/posts/20230728` News article.

**Arduino Giga** - Like the above Uno R4, this is not just an enhanced version of our recommended Arduino Mega2560 but rather an entirely new (and also very expensive) board that just happens to share the same footprint. Refer to the :doc:`/news/posts/20230728` News article.

--8<-- "snippets/abbr.md"

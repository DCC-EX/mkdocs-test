---
hide:
  - toc
---

# Incorrect IOREF voltage for 3.3v Microcontrollers

![ACEBOTT IOREF](/_static/images/esp32/esp32-keyestudio-ioref.png){ width=15% }

For the 3.3v microcontrollers such as the ESP32 board, if the IOREF voltage is not be correct the ADC inputs will receive up to 5V when the IOREF pin is 5V which will damage the board and likely destroy it.  

***As such it is vital that the modifications below are made.***

Thear are two options for correcting this issue, explained in detail below:

- Option A - 3V3 IOREF Override pad changes on the EX8874
- Option B - Bend the IOREF pin + Jumper the 3v3 pin the IOREF on the EX8874

Reminder: These modifications are *not* needed when installing a single EX8874 on an EX-CSB1.

----

## Option A - 3V3 IOREF Override pad changes (Recommended)

![EX8874 IOREF](/_static/images/esp32/esp32-keyestudio-bent-pin.png){ width=25% }

![EX8874 IOREF](/_static/images/esp32/ioref-override.png){ width=22% }

- The prefered work-around for the incorrect `IOREF`/`5V` pin is to modify the EX8874, using the **3V3 IOREF Override** solder pad on the EX8874.
- When using the 3V3 IOREF Override:

    1. Bend the IOREF pin out, <br/> *or*

    2. Confirm that the trace connecting the 5v pad is completely cut. (The red line in the image.) Scratch it with a blade till there is no contact between the two pads and check with a multimeter. Then solder from the center pad to the 3.3v pad. <br/> *or*
    3. Both the above, to be really sure

Double check that that you have it correct by checking wth a multimeter on the EX8874 before you connect it to the ES32:

- [ ] There should be an open circuit between the IOREF pin and the GND pin on the I2C pins
- [ ] There should be an open circuit between the other `5v` pin (beside the two GND pins) and the `Vdd` pin on the I²C pins
- [ ] There should be a closed circuit between the `3.3v` pin and the Vdd pin on the I2C pins

----

## Option B - bend + Jumper (Acceptable solution)

![EX8874 IOREF](/_static/images/esp32/ioref-to-3v3-jumper.png){ width=15%}

![EX8874 IOREF](/_static/images/esp32/esp32-keyestudio-bent-pin.png){ width=25%}

*This option does not require soldering.*

- Locate the IOREF pin. (On many clone boards it will be labeled `5V`) and bend the corresponding pin on the EX8874 out.
- Add a Jjumper from the `3V3` pin to the `IOREF` pin on the EX8874.

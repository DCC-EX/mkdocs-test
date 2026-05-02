---
hide:
  - toc
---

# Incorrect IOREF voltage

![ACEBOTT IOREF](/_static/images/esp32/esp32-keyestudio-ioref.png){ width=15% }

If the IOREF voltage will not be correct. The ADC inputs will receive up to 5V when the IOREF pin is 5V which will damage the board and likely destroy it.  

***As such it is vital that the modifications below are made.***

![EX8874 IOREF](/_static/images/esp32/esp32-keyestudio-bent-pin.png){ width=25% align=right }

![EX8874 IOREF](/_static/images/esp32/ioref-override.png){ width=25% align=right }

## Option A - 3V3 IOREF Override** pad (Recommended)

- The prefered work-around for the incorrect 5V pin is to modify the EX8874, using the **3V3 IOREF Override** solder pad on the EX8874.
- When using the 3V3 IOREF Override:

    1. Bend the IOREF pin out, *or*
    2. Confirm that the trace connecting the 5v pad is completely cut. (The red line in the image.) Scratch it with a blade till there is no contact between the two pads and check with a multimeter. Then solder from the center pad to the 3.3v pad.
    3. or both the above to be really sure

Double check that that you have it correct by checking wth a multimeter on the EX8874 before you connect it to the ES32:

- There should be an open circuit between the IOREF pin and the GND pin on the I2C pins
- There should be an open circuit between the other `5v` pin (beside the two GND pins) and the `Vdd` pin on the I²C pins
- There should be a closed circuit between the `3.3v` pin and the Vdd pin on the I2C pins

![EX8874 IOREF](/_static/images/esp32/esp32-keyestudio-bent-pin.png){ width=25% align=right }

## Option B - bend and jumper (Acceptable solution)

This option does not require soldering.

- Locate the IOREF pin. (and many clone board it will be labed `5V`) and bend the corresponding pin on the EX8874 is bent ou
- Jumper to `3V3` pin to the `IOREF` pin on the EX8874.


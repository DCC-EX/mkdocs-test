# Hardware
  
## What you need for EX-FastClock

- An EX-CommandStation running version 5.0.0 or later
- An Arduino Uno microcontroller
- An MCUFRIEND type plug-in shield TFT touchscreen
- A suitable power supply
- Dupont type wires to connect the components, male to female or female to female as required
- A USB cable to connect the Arduino to a PC to load the software

The software for the  EX-FastClock can be found in the  EX-FastClock repository in the DCC-EX GitHub.  The code can be configured to run a clock which will communicate to the Command Station by either Serial or I2C.  The options are chosen from the file config.h.  Instructions are contained in the README.md file.  Which option you choose will depend upon weather you have serial throttles connected to the serial ports in which case I2C might be the better option.  Alternatively if you already have lots of I2C devices then it might be better to run the Serial option.

Given that the MCUFRIEND style shield is a shield and uses the A4 pin as LCD_RST it is necessary to make a modification to enable the I2C communication.  This involces cutting the A4 pin and soldering a jumper from LCD_RST on the back of the TFT board to the pin that aligns with the UNO RST pin.  However if one is intending to configure the clock as a serial device then this modification is not required.

![Modified LCD Sheild](/_static/images/ex-fastclock/Modification.png)

This modification allow the A4 & A5 to operate correctly as I2C and was suggested by David Prentice who wrote the MCUFRIEND_kbv library that this project uses.  A discussion on this modification can be found on the [Arduino forum here](https://forum.arduino.cc/t/mcufriend-kbv-library-for-uno-2-4-2-8-3-5-3-6-3-95-inch-mcufriend-shields/353100/100).

If using Serial communication no modification is required. Pins 0 & 1 (TX/RX) are unused on the LCD PCB therefore wires may be soldered to the Arduino PCB to run to Serial connections on the CS.

Now that you know what you need, click the "next" button see how you use  EX-FastClock.

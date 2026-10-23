# EX-SensorCAM

![EX-SensorCAM Light Logo](../../_static/images/logos/product-logo-ex-sensorcam-only-light.png){ .only-light width=400px align=right }
![EX-SensorCAM Dark Logo](../../_static/images/logos/product-logo-ex-sensorcam-only-dark.png){ .only-dark width=400px align=right }

EX-SensorCAM is a video based multi-channel position sensing camera.

## Introduction

This single camera is capable of replacing up to 80 detectors/sensors on a model railroad/railway along with their extensive wiring. As it is a cheap device, on large railroads/railways, several cameras can be used for adequate coverage. It can detect, and be used to control, train movements without any trackside sensors at all.

Used in conjunction with an I2C bus to a **DCC-EX EX-CommandStation**, the options through **EXRAIL** automation seem unlimited.

It does not, however, include loco or rolling stock identification.

## Hardware

### Base Processor Module

The Camera may be a standard ESP32-CAM with an ESP32-CAM-MB (CH-340G based) to add USB capability, OR a preferred ESP32-WROVER CAM with a 38P/V4/Expansion board and regulator.  In its simplest form, a PCA9515A or LTC4311 I2C interface module is needed to connect the sensorCAM to i2c bus, some limited soldering is required to connect the PCA9515A (5 wires) to the USB MB on the CAM.

An isolated power supply, and indicator LEDs complete the system.  For longer reach, Sparkfun Endpoints may be used, for long I2C buffering (up to 30metres).  A cheap commercial aerial may be added in marginal WiFi situations.


### Camera Module

The **EX-sensorCAM** uses the 32bit ESP32-S microcontroller with an **OV2640** camera module.  
It requires a 4Mbyte PSRAM for image storage and a built in WiFi aerial.  It also has 3Mb of available program storage, EPROM memory for parameters, and 327kbytes of dynamic memory.

## Software requirements

The Arduino IDE or VSC/PIO is recommended for the sensorCAM and, if used, the connected **EX-CommandStation** DCC-EX-CS software (5.4.16+) with **EXRAIL**.
The ESP32-CAM has an Arduino library of software that is needed to enable the camera image manipulation and the WiFi imaging of the railroad/railway.
In addition, the **Processing 4** application is highly desired to enable railroad/railway images to be captured and sensor positions to be located and seen, as the Arduino or VSC/PIO IDE cannot give visual feedback.

You can download Processing from [the website](https://processing.org/)

The webserver WiFi images are not a substitute for the Processing 4 utility, as sensorCAM cannot "sense" in webserver mode.
Specific SensorCAM files are provided for each of the above apps.

NOTE: For enhanced versions, rather than "main/master" branch, use a recent "devel" version of **EX-CommandStation** (5.5.40+) and "devel" branch of sensorCAM (0.3.20+)

## Documentation

The sensorCAM is a complex device needing some in depth understanding to achieve its full potential.
A 30 page manual is provided to assist with this process.

If you want clarification or wish to discuss the implementation please contact the developer on Discord (@Barryd) or at bcdaniel2@optusnet.com.au and he will attempt to address your issues. All feedback is welcome.

## Outline of install process

1. Acquire ESP32-CAM and MB or ESP32-WROVER-CAM and 38P/v4 expander board with OV2640.
2. install Arduino IDE or VSC/PIO with the ESP32 libraries (includes a WiFi CAM example)
3. Load the CAM with the WiFi (webCAM) example and test.
4. Install the sensorCAM.ino software and configure.
5. Test the basic sensorCAM functions to confirm functional install.
6. Load Processing 4 app. and sensorCAM.pde code.
7. Use the Processing 4 app to replace the Arduino Monitor.  Familiarise and test.
8. Create test sensors and test detection with moving targets.
9. Setup the CAM viewing the model railroad/railway and test a virtual sensor with moving rolling stock.
10. Optimise parameters for best performance.
11. Connect CAM to an i2c interface (e.g. PCA9515A, LTC4311 or better).
12. Integrate **EX-sensorCAM** into Command Station using appropriate code.

For a detailed 12 step guide refer to the [Installation Guide](/products/ex-sensorcam/installation-guide.md).

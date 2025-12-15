# EX-SensorCAM Abridged Manual

## CONTENTS

1. Overview 1

2. ESP32-CAM 3

3. Physical Installation 5

4. Notation& Help commands 7

5. Configuration 8

6. PROCESSING4 monitor/console 11

7. Wiring Requirements 13

8. Communication and Host Operation 14

## Appendix

A. ESP32 sensorCAM Command Summary 17

B. Check List for Optimising Sensor Resonse 19

C. Filtered/parsed DCC EX-CS commands 20

E. Tabulation of Recommended DCC-EX-CS id's for sensorCAM 23

F. Hardware Interface Notes.(including PCA9515A & SF Endpoints) 24

H. Notes on use of EX-Rail with SensorCAM 29

J. ESP32-CAM pinout (v1.6) and WROVER-CAM notes 31

Addenda 32

## 1. Overview

The sensorCAM is a video camera replacement for physical proximity sensors/detectors on a model railroad. It can replace up to 80 detectors and their associated power and signal wiring using artificial vision alone. It offers the flexibility of sensor placement or relocation instantly by software command with no physical layout modification.The railroad can be automated using artificial vision of train activity. Each virtual sensor can produce a logical state of 1 (occupied) or 0 (unoccupied) and is readable over an i2c cable. SensorCAM originally used the ESP32-CAM module. However, the ESP32-WROVER-DEV CAM (v1.6) is the preferred substitute with potentially simpler setup.

The sensorCAM takes 10 frames per second in RGB565 format at QVGA resolution of 240 x 320. Each sensor consists of a square group of 16 pixels which equates to approximately 20x20mm square with the standard lens at 1500mm. The software decodes and saves only the 80 sensor images (1280 pixels) and then compares each sensor image with a reference image prerecorded either at startup, on request, or by a "recent" automatic update. If the images do not match the references well, then the sensor is "tripped" or "occupied" & status '1' is registered. A good match results in '0' output. The state of virtual sensors can be manually monitored on the USB monitor, or polled by microcontroller over the i2c interface cable.  
**Note:** The sensorCAM is sensing only when the Flash LED is pulsing at 10Hz (for each new frame).

![ESP32 CAM with MB](/_static/images/ex-sensorcam/esp32-cam-with-mb.png)

2PCS ESP32-CAM-MB, ESP32-CAM Board, Micro USB to Serial Port CH-340G with OV2640 2MP Camera Module 4MB PSRAM

![ESP32 Wrover CAM](/_static/images/ex-sensorcam/esp32-wrover-cam.png)

**Note:** While the full manual primarily talks about the ESP32-CAM-MB, the focus here is the alternative in the newer **ESP32 WROVER-CAM** single board option. For some further preliminary details refer to Section 7 Wiring, **Figure 6**.  The software is identical for both CAMs.

Dealing with video images involves complexities not normally associated with model railroading sensors. The sensorCAM is a complex device with a number of commands explicitly for setup and evaluation. In addition to these, several “output” commands can be used by a host to interrogate the “virtual sensor” output states. The initial setup can be somewhat involved and requires familiarity with many of the 25 commands discussed below.

The sensorCAM has two ***mutually exclusive modes*** of operation; the sensorCAM mode and the webCAM mode. The webCAM mode is essentially as described in the on-line tutorials. Use that mode only for education and alignment. Invoke webCAM video mode by issuing the **v1** (or **v2**) sensorCAM command to get a webCAM URL (e.g.192.168.0.64)

The WROVER-CAM has USB integrated.  The WROVER or MB is far simpler to use than a separate FTDI used in the videos.

The ESPRESSIF guide will show how to install the Arduino-ESP32 support.

[Installing Arduino-ESP32 2.0.6 documentation (readthedocs-hosted.com)](https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/installing.html#installing-using-arduino-ide)

A tutorial on setting up the ESP32 on Arduino IDE is available on YouTube called [ESP32 CAM-10 Dollar Camera for IoT Projects](https://www.bing.com/videos/search?q=ESP32+CAM+-+10+Dollar+Camera+for+loT+Projects+-+YouTube&view=detail&mid=77BF6363644D71DF685B77BF6363644D71DF685B&FORM=VIRE)

[Introduction to ESP32- Getting Started](https://www.youtube.com/watch?v=xPINTk3VLQ)

The sensorCAM software is uploaded to the ESP32-CAM using the Arduino IDE. The sensorCAM has been programmed with two modes of operation; a webCAM mode (as in the on-line tutorial) and a sensorCAM mode. The limited power of an ESP32 prevents both functioning at the same time. Consequently, to see an image of the railway while sensorCAM is operational requires a third application (Processing 4.3) to retrieve a still image from the CAM over the USB cable to a computer. The Processing 4 _sensorCAM.pde_ app replaces the Arduino IDE and IDE monitor retaining the sensorCAM command set and offering a (slow) image capture capability over USB cable. Processing 4 allows virtual sensors to be placed interactively on an image of the railway with a simple mouse click.

In addition to the USB interface, you are likely to need a daughter board “carrier” or prototyping board to connect to the real world (power, indicators, control wires, and i2c.) Further details are given below. However to test the sensorCAM functions, one only needs the CAM and a USB interface, with power from the PC's USB port.

To control a railway, the railway needs a microcontroller based management system. This typically could be an Arduino Mega (or CSB1) based system running software such as the DCC-EX CommandStation and EX-RAIL automation application. The EX Command Station(CS) includes a sensorCAM specific driver as detailed later.

## 2. ESP32/WROVER-CAM

The heart of the sensorCAM is the ESP32 CAM module with an ov2640 camera sensor and a 32bit ESP32-S microprocessor. The sensorCAM software/sketch is loaded into the ESP32 using the Arduino IDE over a USB port with settings newline/115200 baud. Follow the above guidelines and run the camera example first, to get a demo webserver and CAM operational with a simple coloured test image. Experiment with settings to "get a feel" for the parameter effects. The CAM has a considerable number of video related on-screen settings. The standard ov2640 can see some Infra Red light which may be utilised to see a bright IR LED as a beam-break sensor.

![ESP32 CAM Example Sketch](/_static/images/ex-sensorcam/esp32-cam-example-sketch.png)

**Figure 1. &nbsp; webCAM mode**

**Figure 1.** is an example of the standard webCAM browser presentation. It is a very useful mode for alignment and as a training aid in investigating the effects of the many video adjustments possible, but does not allow placement of sensors as sensorCAM mode can't be simultaneously enabled.

The sensorCAM uses QVGA but VGA is better in webCAM mode. These settings can be changed after the CAM images are stable, but the default values should be adequate.

If you “Start Stream”, parameter changes will seem almost immediate. But with “stills”, after changing a variable, you may have to click “Get Still” 3 times to clear the pipeline and get a changed image. In Stream mode, close observation will reveal changing whole image brightness/colour for several seconds after image disturbance (e.g. a hand in front of CAM) as the auto adjustments “correct” the image. These types of changes can trip the sensorCAM even if the obstruction does not block the virtual sensor. Consequently after power-up, the sensorCAM may stabilize and then turn off some auto adjustments in the first 15 seconds. Changing environment lighting may result in a need to use a “re-reference” command, for example perhaps after sunset or turning on extra lighting.

Due to the slowness of the ESP32 & wifi, the "live stream" is slow and a webCAM delay in response will be observed.  The delay is inevitable in webCAM WiFi mode.

![ESP32 CAM Example Capture Sample](/_static/images/ex-sensorcam/esp32-cam-example-capture-sample.png)

**Figure 2 &nbsp; Initiall sensorCAM settings**

After the sensorCAM has booted up, it reads frames for 9 seconds before automatically doing a reference grab for all defined sensors (the **r00** command). 

The ESP32-CAM has an Infra-Red(IR) filter to enhance colour response. The sensorCAM relies on strong colour contrast(saturation) to detect changes. Low lighting levels and poor contrast degrades performance.  Some IR penetrates, so the CAM may use an IR LED for reliable beam-break sensing.

To run the sensorCAM.ino, it will be necessary to configure the Arduino IDE for the ESP32 as covered in the above you-tube tutorial links. Load and run the demonstration. For the sensorCAM, you will require new files as described in the sensorCAM installation Guide. 

The ESP32-CAM can take rgb565 frames at 13/second. However it is a 3 step process; image sensing, processing and storing. It will then take further cycles to assess the state of the 80 virtual sensors in the frame(another two cycles) A total of 5 cycles places a significant limit on the sensorCAM speed of response time (up to 0.5 seconds at 10 frames/second). A fast HO loco can travel 160mm @ 100kph, so this latency might need to be accommodated in planning virtual sensor locations.

## 3. Physical Installation

For testing purposes you will need a computer with a spare USB port and the Arduino IDE software installed. The PROCESSING 4 software is also advisable as it gives a more reliable and convenient image for setup. A long powered USB cable (5m?) may be an advantage as the sensorCAM may be some distance from the PC. For a final installation the sensorCAM would be connected via a cat5/6 cable carrying power and a differential i2c bus (of up to 30m) to a Command Station or similar. Some different practical wiring solutions are explored in **Appendix F**.

For a test hookup between a USB powered sensorCAM and a Command Station(mega) with a short existing i2c bus, provided the total length is under say 3 meters, a simple, cheap arrangement could be tried using a PCA9515A as both buffer and level shifter if needed. The CAM on i2c bus is best used theoretically with the USB computer running on battery power alone (unplugged) to absolutely avoid ground loops and associated electrical noise, but will probably function OK anyway.

![ESP32 CAM with PCA9515A and LTC4311](/_static/images/ex-sensorcam/esp32-cam-pca9515a-ltc4311.png)

**Figure 3 &nbsp; CAM with 3.3 to 5V i2c interface and optional LTC4311 “terminator” for greater reach**

 The sensorCAM is preferably placed above and square-on to a section of layout at a height of 1 to 1.8m above the surface. 1.2m gives a max. coverage of approximately 1.2x0.9m with the standard lens. Tilting the CAM by up to 30 degrees can increase the layout coverage by up to 50%.  

Lighting is critical for reliable operation. The lighting should be steady. Both LED flood and Fluorescent lighting might degrade results due to the flickering levels of illumination at 100/120 Hz. Use quality LED lights. The light fittings should not be visible in the camera's field of view. A uniform level of lighting is the objective, with a minimum influence from fluctuating daylight, fans or direct sun and cloud shadows through windows. Some experimentation may be needed to avoid local “glare”.  Bright lighting is desirable (good quality LEDS) to enhance colour differentiation. Check your lighting for flicker by taking a “slo-mo” test video on a cell phone. Fluoro's are bad!

The CAM mount needs to be rigid to avoid vibration which may trip sensors due to small image movements. It also needs to have a suitable route for a (cat5) cable for its own power supply and the necessary i2c communications. The length of this cable needs to be considered if the railway's i2c network is otherwise long. The quick connection above (using PCA9515A) is for short lengths only (i2c under 3m). Up to 7m may be achieved using 2k pull-up resistance and one LTC4311 “terminator” to enhance signal rise time.  The recommended alternative for longer cables is the Sparkfun differential Endpoint system.  Power should be regulated near the remote sensorCAM if not using a short USB cable.

Most reliable results may be obtained with light grey coloured ballast and darker sleepers. If results are inadequate, light green (grass?) or yellow "reflectors" between the rails may relieve any problem (recommended in fiddle yards). If lighting throws shadows beside targeted rolling stock, the shadows may be used advantageously by good sensor placement.

For initial configuration, access to the sensorCAM's USB port is important. Loading computer code over a long USB cable is problematic, but monitoring and tweaking settings may be done with a reduced BAUD rate or a (5m?) buffered USB cable at 115200 BAUD.

With regards lighting, fluoroescent or LED lighting normally flickers at twice mains frequency so it pulses at 100 or 120Hz. Tolerable to humans, but it can be seen in a sensorCAM image on a uniformly white test panel as below (**Figure 5**). In 100mSec there could be up to 10 bands in one image.  the faint bands will drift across the sensors and potentially trip them in the worst case scenario. Set the threshold high enough to avoid such trips or (better) change lighting. **Figure 4** shows an example of bad 100Hz banding.

![Test Image with Light Banding](/_static/images/ex-sensorcam/test-image-light-banding.png)

**Figure 4 &nbsp; Test image showing fluorescent or LED light banding**

## 4. Notation

The notation used in all sensorCAM reference material uses symbols according to the following convention:

**%**&nbsp; &nbsp; &nbsp; used to designate a digit as part of a bank/sensor designator in bsNo style. i.e. 0/2, b/s or %/% or %%  
**\#** &nbsp; &nbsp; &nbsp; used to designate a digit as part of a decimal number as in ### for a 3 digit decimal number.  
**$** &nbsp; &nbsp; &nbsp; used to designate a single alphanumeric character(0-9 or A-Z) depending on context.  
**S** &nbsp; &nbsp; &nbsp; Capital S may be used to refer to a specific sensor such as S02 for example. Designation format: S%%  
**[ ]** &nbsp; &nbsp;&nbsp; Square brackets may be used to indicate optional command arguments(don't include[ ] in command).

Sensor "bsNo." number consists of two digits preferably written separated by a '/' as in 1/2 but in commands this is reduced to 12 as in command **i12**. Command 'i' has the form **i%%** indicating it requires a 2-digit bsNo. As 49 is an invalid bsNo.(s range is 0-7), i49 is invalid. Some commands require a DECIMAL number and are expressed as having form **t##** for example. **t49** is therefore a valid command. The '**m**' command takes the form **m$,##** requiring a single digit and a 2-digit decimal number. For more details on commands see **APPENDIX A**.

Where bsNo.'s are printed, they can take several equivalent forms depending on context. Where possible they are printed as %/% e.g. 2/3. However an equivalent form is 023. Any printed sensor number starting with a '0' can be treated as equivalent to the '/' form so 023 == 2/3 == bank 2 sensor 3. The 0%% form is in fact the "OCTAL" format of bsNo. (Note: 087 and 097 are invalid. Keeping usage to banks ranging from 0 to 7 avoids any confusion).

Some diagnostic output (e.g. **f%%**) may resort to another numbering system  (i.e.HEXADECIMAL) for compactness, but for normal usage this notation can generally be avoided. Just be aware of the context in which numbers are being used.

Where words are in *italics*, these are the actual names used in the C++ programs for sensorCAM. Consequently they may seem cryptic, but their function is hopefully clear. 

## 5. Configuration

### 5.1 Plan a grand sensor numbering strategy

The first step is to decide a sensor distribution strategy & numbering strategy (not set in stone) . A sensorCAM has 10 banks (0-9) of eight (0-7) individual sensors available (total 80). Each **bank** can be tested as a whole to see if ANY sensors tripped or NO sensors tripped. Also placing a string of sensors in a row, for example along a platform, can indicate train position with the binary bank value increasing as the train approaches a signal as it crosses sensors 0 through 7. (see **Figure 5** for examples) Sensors are generally referred to with a two digit bank/sensor designation (their bsNo.) e.g. Sensor 68 and 69 are therefore invalid bs numbers, 97 is valid. Use one bank for a platform (set of 8 sensors). Sensor **S00** is reserved as a brightness reference sensor. Sensor **S06** is also RESERVED for now. It is suggested that user's Sensors start with bank 1, i.e. S10, S11 & upwards, with related sensors in their own bank. They do NOT need to be sequential (Follow the installation Guide for full details). **With the recommended definitions set up, the user does not need to remember or refer to vPins for sensorCAM sensors at all - just use the S%% identifier.**

For an EX-Command Station (CS), the 80 sensors will have vPin numbers ranging from #00 to #79 (DECIMAL) and mapped to 80 b/s id's(S00 to S97). Users can use, for example, **AT(CAM 0%%)** in EXRAIL commands where a vPin ID is called for.  For the technically minded, CS invisibly calculates vPin=BasePin+b*8+s. 

### 5.2 Preset the wifi SSID and password

Before uploading the software into CAM, check that it has the appropriate WiFi definitions for your railway _WIFI_SSID_ & _WIFI_PWD_, and perhaps for your test area _ALTWIFI_SSID_ & _ALTWIFI_PWD_ are in your **_configCAM.h_** file.

### 5.3  Adjust other configCAM.h settings

 &nbsp; &nbsp; a) If i2c address 0x11 is in use, change to 0x12 (or 0x13) i.e. _I2C_DEV_ADDR 0x11_ in your _configCAM.h_  
 &nbsp; &nbsp; b) If you want to use “larger” sensors, Place _#define SEN_SIZE 2_ (0-7) in your _configCAM.h_ (ver319+)  

### 5.4 Load sensorCAM software 

Follow you-tube to pre-configure the Arduino IDE for ESP32.  Using this IDE, load the software into sensorCAM with it unmounted. Then mount the CAM in a suitable place for tests. A long USB cable is problematical.

### 5.5 Establish a monitor screen to sensorCAM

Establish a USB connected monitor (e.g. Arduino IDE monitor, or PROCESSING4 monitor, preferably at 115200 baud. The PROCESSING 4 monitor coded for the sensorCAM has the advantage of displaying the CAM's railroad image (or selected part thereof), all-be-it rather slowly!). Because of the many changeable CAM parameters, the WiFi link (webCAM) is not a reliable indicator of the sensorCAM image quality. It may be better or worse. The PC (using Arduino IDE) is only able to show images via WiFi, but because the sensorCAM runs on RGB565 format it cannot send WiFi (jpeg) images without rebooting into WiFi/jpg webCAM mode (under which it cannot read sensors!). The reboot/display/reboot cycle for WiFi webCAM is also tediously time consuming.

The sensorCAM takes some time to boot and establish sensing mode. The flash LED starts flashing on every frame after about 10 seconds and data flows to the USB terminal. A period of averaging ensues with “good” sensing by about 30 seconds. This flow of data (and sensing) can be suspended with the ‘**w**’ (wait) monitor command. Some commands (including a blank line entry) will subsequently restart the sensing camera and sensor output. The CAM may crash if it is left waiting for input for over 30 minutes. Reference images would also be long out of date.  
**Note: t1** toggles output srolling data without stopping flashing/sensing.

### 5.6 Verify wifi webCAM operation

The CAM can be switched to webCAM WiFi video mode with the '**v1**' command. '**v2**' can select your alternate WiFi network. ('**v**' will give sensorCAM software version). '**v1**' (or '**v2**') will reboot and load webCAM mode connecting to the network selected, and providing a URL e.g. http://192.168.0.xx that can be used to connect with a browser. An image, like **Figure 1** above, should be seen with controls for experimenting with Brightness etc. This image is educational and useful for camera alignment, but not necessarily a good indication of the sensorCAM (sensor mode) image because of the unpredictable parameter effects. To see a more reliable image run the PROCESSING 4 *SensorCAM.pde* monitor instead of Arduino IDE monitor (refer **Section 6.**). To exit video mode, try the monitor command '**R**' (or '**F**'). If this software reset fails, try manually rebooting the sensorCAM (power OFF/ON or via the on-board RST push-button using a non-metallic tool!).

### 5.7 Familiarise with sensorCAM command set.

Review the sections below (**5.8 etc.**), before mounting the camera over the railroad, as it is advisable to be familiar with the sensorCAM command set. The setup commands will have to be repeated accurately once the CAM is mounted in its final location (Step 5. Installation Guide).

### 5.8 Sensor placement

Setting up the CAM first requires locating sensors. When deciding on sensor location, be aware that the sensor response is slow compared to conventional sensors. Allowing for 500mSec delay, which at 100kph equates to 150mm of travel (in HO), may influence sensor placement. Best performance is obtained if the sensors are not within 20 rows/columns of an image edge. Remember to save to EPROM with the ‘e’ command once satisfied. Virtual sensor location can be set up in several ways. Option d. is preferred.

**a.** &nbsp; Automatic loading from EPROM on bootup. This is only applicable after an initial sensor set has been established and command '**e**' used to save them to EPROM.

**b.** &nbsp; The bright LED method: Place a bright LED at the required location and reduce room lighting if needed.  Issue an '**s%%**' command (e.g. S00 for an off-track reference sensor) and wait for the CAM to scan and locate the LED and setup sensor coordinates. Remove the LED, restore lighting, and perform an ‘**r%%**’ for new reference images.

**c.** &nbsp; Issue a ‘**k%%,rrr,xxx**’ command to place sensor %% at CAM pixel position rrr(row) and xxx(column). This method is most useful for "tweaking" coordinates if you want to adjust the result of the LED method. The CAM has 240 rows/lines of 320 pixels each, numbered from 0. Use the ‘**i%%**’ command for info. on sensor. NOTE: Use ‘**k**' to set up test sensors initially, but delay setting final positions until Processing 4 installed and enhanced ‘**k**’ and ‘**a**’ available. The ‘**a**’ command does 3 commands in one (i.e. **k**, **a**(enable) & **r**).

**d.** &nbsp; Running Processing 4, an image can be downloaded, a bsNo. nominated by typing **k%%** (or **a%%**) and the mouse click on the image appends coordinates to **k%%**. Press Enter if the command is complete and correct. Similarly, the long version of '**a%%**' sets position, enables, and records a reference all in one command.

### 5.9 Sensor status and save

Once a sensor has been located, the '**p$**' command can show/tabulate all defined positions up to bank$. To enable a sensor use the '**a%%**' command. This will enable AND record a new reference image for the sensor. It will then be included in the screen “data dump”. Only “enable” sensors when UN-occupied, or do an **r%%** later when the sensor is empty. Also, remember to do an '**e**' command when you want to save positions in EPROM for next time.

### 5.10 Set a Sensor Threshold

A threshold needs to be set to define the level of difference in image required to register a sensor trip or “Occupation”. This typically ranges from 40 to 60. Try ‘**t45**’ for starters. Some fluctuating lighting and electrical “noise” needs to be tolerated, but a higher threshold reduces sensor sensitivity for dark-on-dark contrast in particular. If there are “noise” trips, adjust the threshold or min2trip a little higher. See **APPENDIX B** for more.  

### 5.11 Limit printout to manageable range

It is desirable to set (using '**m**') a *maxSensors* parameter (e.g. 030) to limit diagnostic printouts to a manageable screen width, and especially important to set the *min2flip* parameter which helps filter out noise trips. However *min2flip* slows the response to valid trips by 100mSec (frame rate) per extra count. Suggest settings of 2(default) or 3. e.g.'**m3,30**' say. Note: *maxSensors* (pulled from EPROM) limits the following....

**a.** the data stream for console/monitor, limited to enabled sensors below _maxSensors_ (and above _minSensors_)

**b.** histogram printout, to enabled sensors below _maxSensors_ (see statistics command ‘**&**’)

**c.** the _boxlt()_ sensor boxes seen on Processing 4 images, for enabled sensors below _maxSensors_

**d.** i2c buffer data for 't' record, to bsn's below _maxSensors_ (and above _minSensors_)(sent to Command Station) The cmd '**t**' acts as a flag to prepare a packet of i2c data that the CS can reconstitute as per the USB ASCII data stream/scroll.

### 5.12 LED bank trip indicator & EPROM

If you want a LED bank occupancy indicator on the CAM, use the '**n$**' command to cause a bank occupied LED to show (default Bank 2). *nLED, min2flip, maxSensors* and *threshold* can be saved to EPROM, along with sensor positions and twins (see **5.15** below) with the '**e**' command. *minSensors* (**n10,%%**) is not currently saved in EPROM.  You will of course have to add a resistor and LED to the physical CAM (GPIO14 or GPIO32).

### 5.13 Sensor reference image refreshing

Although sensor enabling (**a**) causes an immediate reference capture, it may be necessary to occasionally do a fresh reference capture for all sensors (make sure they are unoccupied!) by using the '**r00**' command. Individual sensor references can be refreshed using ‘**r%%**’. The results of a refresh can be seen in the scrolling “data dumps” of enabled sensors, their “difference scores” (32-99), and their perceived occupancy state. The sensor **S00** is constantly averaged and refreshed every 6.4 seconds. Furthermore, there is an automatic refresh process that cycles through enabled sensors and regularly averages 32 consecutive sample images.  
If the sensor remains unoccupied, it updates the reference, compensating for slowly drifting lighting changes. 

### 5.14 Scrolling data interpretation

The scrolling data dump displays “SUS” (suspend) if auto updates are off. It also displays *threshold*(T), *min2trip*(M), the bank assigned to the on-board _nLED_(N), S00 reference diff. score, as well as the S00 reference brightness(R) and its current actual brightness(A), a brightness scale factor(B) and other enabled sensors. ‘A’ is the Actual latest sum of the 48 bytes of a sensor image (max 3024) and should be between 1200 and 2500 ideally. Following a reference refresh (**r**), for an unoccupied image, the (noisy) diff. scores should be 32-37. If references are being updated, a note will appear at the right hand side of the data dump in the form of “**Ref 0%%**” to indicate that a new reference for an UNOCCUPIED sensor has occurred. This dump allows for performance monitoring during commissioning.  
:**oo46##** indicates tripped sensor (## = **occupied**) sensor are shown by default with a central diff score.  
:**?-46-?** indicate an above threshold image **potentially occupied**** (waiting for *min2trip*).  
:**oo47?T** indicates **suspected occupied** but no confirmation from Twin (see **5.15**).

## 6 PROCESSING4 monitor/console

![Processing4 Console with Image](/_static/images/ex-sensorcam/processing4-console-image.png)

**Figure 5 &nbsp; Processing 4 Console and image window**  
 &nbsp; Note: Sub-optimum 'c' settings caused green tint.

The Processing application displays the image using sensorCAM settings, and also shows colour coded sensors. As previously stated, the PROCESSING4 application is a crude USB monitor that enables the user to control and configure the sensorCAM with the additional benefit of being able to invoke a display of the image. All the sensorCAM commands can be used. At 115200 baud, a full RGB565 image takes 13 seconds, but it is often convenient to reduce this by prescribing a smaller image segment of limited rows and/or columns (e.g. **Y120** for lower half of a 240 row screen).  
The Processing 4 application can be [downloaded from here](https://processing.org)

The SensorCAM.pde code assumes the USB port for the sensorCAM is the lowest (_comNo=0;_) on the list displayed on startup. Should this not be the case, for example if another USB is being used to simultaneously run an IDE to a Command Station, then the *int&nbsp;comNo=0;* code line (line 15?) of the sensorCAM.pde will need to be increased to, for example, *int&nbsp;comNo=1;*  
You may also increase the image display window size factor by editing the next *final&nbsp;&nbsp;int&nbsp;&nbsp;SF=2;* line to *=3;* or *=4;* on high res. screens.

The sensorCAM Processing 4 monitor accepts commands **W, X, Y** & **Z** which allow one to nominate a “strip” or subsection to image. e.g. **Z80 X240 Y** will update the last quarter image(columns 240-319) of the 240x320 pixels in 4 seconds. This shortcut method enables, for example, comparison of quarter images under different lighting conditions by using different **X** values. Similarly **W60 Y120**  will produce a quarter image from row 120 to 179. Each part image is pasted over previous images. Each new image appears more quickly if only a subsection is specified this way. The next image can be flipped Vertically(y) and Horizontally(x) by using **V** &/or **H** before capture. The **Figure 5** image used  **V H Y60**  The values for V, H, W, X & Z are remembered for subsequent '**Yrrr**' commands so need not be repeated.  
**NOTE: Do not flip image before creating new sensors as cursor coordinates don't flip!**

The image will have enabled sensors (b/s) boxed and identified by a (resistor) colour code. Left bar is bank# and right bar is sensor#. Combined, they give the bsNo. If two sensors have the same coordinates, the colour code will be for the highest bsNo.  
**Note:** Only sensors below _maxSensors_ will appear boxed. **N.B.** the ‘**H**’ command will REVERSE the coding from b/s to s/b.  
**(The resistor colour code is 0:black 1=brown 2=red 3=orange 4=yellow 5=green 6=blue 7=violet 8=grey 9=white)**

#### PROCESSING4 command summary:

**W###** &nbsp; will limit the image to\#\#\# rows wide/high(1-240) (default 240)

**X###** &nbsp; will start the image from column ###(0-319) (default 0) -uses the sensorCAM 'x' command.

**Y###** &nbsp; will initiate an image download starting at row ### (0-239) (default 0) -uses the sensorCAM 'y' cmd.

**Z###** &nbsp; will limit the image to ### columns (1-320) (default 320) -uses the sensorCAM 'z' command.

**H** &nbsp; will flip/mirror subsequent images horizontally. **Note:** reverses bsNo sensor colour code to sb!

**V** &nbsp; will flip/mirror subsequent images vertically. (V + H effectively rotates image 180 degrees)

**R** &nbsp; will cause a firmware reset of the sensorCAM via the DTR line via. the USB interface. CAM will enter a wait mode for confirmation.  Reset can be aborted with command 'aw'(Abort&Wait). **Ctrl-R** Resets CAM instantly.

> **NOTE**

1. The above commands ARE CASE SENSITIVE. They are recognized by Processing 4 as non-sensorCAM commands and processed in the monitor/PC. Commands **X, Y** & **Z** in turn automatically issue related sensorCAM commands **x, y** & **z** respectively, with appropriate parameters.  The '**Y**' command suspends sensorCAM immaging, holding a single “frozen” frame until a terminating command is received. 

2. If you use **H** to mirror, the colour coding for boxed sensor number (bsNo.) has to be read right to left.  Do NOT click on image to create sensors if image has been flipped.

3. **Ctrl-E** and **Ctrl-N** enable/disable echo of commands as typed, to the monitor/log file. It can replace the user's focus on the CAM image Cmd: window. **YO** should toggle the verbose mode. The command **Y** images from row 0 by default.

## 7 Wiring Requirements

Refer to **Figure 6** and **Appendix F** for alternate solutions for connecting sensorCAM to an i2c bus for remote control. For initial testing from a PC, the basic ESP32-CAM-MB or Wrover-CAM (**CH340** based USB interface) could be sufficient via. USB.  With i2c, take care to use level shifting (PCA9515A or endpoints) if using a 5V Mega CS. 

The recommended hardware interface to a CS is currently the **Sparkfun Endpoint** system (**Figure 6.** & **APPENDIX&nbsp;F**) which permits the i2c bus to be run over long standard Cat5 twisted pair cable.  It can also carry the required raw power supply. The Sparkfun Endpoints are used **in pairs** and can cater for voltage shifting between 5V Command Stations  (e.g. Mega) and 3.3V sensorCAM as required. For the very simplest off-the-shelf arrangement, an ESP32-WROVER-DEV CAM with a cheap ESP32 breakout board (including regulator) can be linked to an Endpoint with 4 Dupont wires for a working CAM system on the end of a cat5 cable of considerable length as indicated in **Figure 6** & **APPENDIX&nbsp;F**, needing only a remote, preferably electrically isolated(floating), 7-10Vdc 0.5A power supply and a matching endpoint on a Command Station.  For a cheaper solution, use the PCA9515A with dupont jumpers for a limited (2m?) reach with either esp32-CAM or Wrover-CAM powered via USB.  
**Note:** The Sparkfun Endpoint may also need a jumper cut or joined for i2c bus voltage level matching to the Command Station.  

The ESP32-WROVER-DEV board is a good alternative to the original ESP32-CAM-MB. The slightly bigger CAM will be a little more convenient with the ESP32S 38P Expansion board. This 38 pin expansion board with 5V regulator is described in the video below **BUT IGNORE PRESENTERS DESCRIPTION OF HIS FAULTY 5V REGULATOR AT THE END**

https://www.youtube.com/watch?v=AP_CX-SFPAQ

The SensorCAM software has been almost exclusively tested on the ESP32-CAM-MB as seen in **Figure 7**. The original prototype was fitted with some enhancements that may not be needed for the user's application.  However, at least one “super bright” LED (the "programmable nLED") is recommended for convenience to visually indicate when a sensor is “tripped”, connected between 3.3V via a resistor (~470R) to GPIO14.

The ESP32-CAM reset button, remotely mounted on CAM, may be difficult to access. To reset the device, two options need to be available. These can be via software command, either from the attached USB monitor, or i2c connected Command Station, or via a power supply induced reboot. A switch at the (“wall-wart”) 9V supply is recommended independent of the CS supply. The USB connection is needed to set up the sensors initially and view images, but should be able to be disconnected once setup testing is complete.  Some esp32's may need a 1uF on the reset pin for reliable reset.

**Note:** Care is needed as the WROVER CAM has 40 pins (not 38) but the spare end Gnd and Vcc can remain disconnected (cut off?).

![ESP32 Wrover CAM with Sparkfun Endpoint](/_static/images/ex-sensorcam/esp32-wrover-sparkfun-endpoint.png)

**Figure 6 &nbsp; ESP32 WROVER-CAM& interface**

![ESP32 CAM MB with PCA9515A](/_static/images/ex-sensorcam/esp32-cam-mb-pca9515a.png)

**Figure 7 &nbsp; PCA9515A 3.3V to 5V i2c interface improvisation compared to a full feature prototype solution**  
 &nbsp; Note: for 3.3V microprocessors (e.g. CSB1) ensure Vcc1 is connected to 3.3V (Vcc0) not 5V.

## 8 Host Communication

### 8.1 Introduction

The operation of the railway depends on a Control Station that polls the sensorCAM for sensor states. This might be a dedicated Arduino Mega 2560 for example. It might be a Command Station running DCC-EX and EXRAIL software, or your own personal device & code. If the sensorCAM is powered up with default settings (from EPROM), or adjusted by the user at the start, the program need only talk to sensorCAM over an i2c bus using the commands a,b,i,l & o for example, or it may be more sophisticated, providing a command channel from a Control Station console/monitor to the sensorCAM to enable most configuration commands via the i2c bus.

The i2c bus is running at 100kHz on the prototype software. It has not been tested at any higher speed yet. It is running fine over a 20m long i2c bus to the master microcontroller (CSB1 or Mega).

### 8.2   DCC-EX Command Station

Setting up a DCC-EX Command Station, should you have one, requires configuration details placed in files _config.h_ and _mySetup.h_ along with a driver _IO_EXSensorCAM.h_ and _myAutomation.h_. These must go in the directory containing file CommandStation-EX.ino. Refer to **APPENDIX H** for installation details.  _EXSensorCAM.h_ code mirrors the sensorCAM command set with a few exceptions.  Imaging and graphic placement is not available.  Functionality was added using the DCC-EX sensorCAM native command <N\> format. 

### 8.4 Monitor Lighting

Stable good lighting is needed.  Gross Lighting changes will have two effects, namely cause trips of most sensors and stop automatic reference refreshes, it may be wise to include monitoring for this eventuality by detecting and setting an “alarm” state. The reference sensor (S00) is automatically re-referenced every 6.4 seconds so will indicate a fault-trip for a maximum of 6.4 seconds. All other sensors will continue to indicate a trip until the user resets the references with an r00 (having checked all unoccupied). See full manual for creating a fault LED indicator.  PLED uses GPIO14 and QLED uses GPIO32 (Wrover).

## APPENDIX A

### ESP32 sensorCAM Command Summary

rev 1DEC25

#### Introduction

Up to 10 banks (0-9) of sensors. Each bank can have up to 8 enabled sensors (0-7). Bank/sensor (%%) up to '97'.  Array _Sensor\[n]_ holds coordinates(rx) of sensor n.  Sensors are grouped into banks(b) of sensors(s). e.g. bsNo 6/7 identifies bank 6, sensor 7 (n=8x6+7=55=067). Sensors are undefined if coordinates(rx) are set to 00. They are disabled if _SensorActive\[n\]_ is set to false.  
If a sensor detects differences, then any output LED (e.g. _pLED qLED_) assigned to the associated Bank of sensors should turn ON.  
On reset (power-up), reference grabs are taken for all defined (in EEPROM) sensors, and then enables them.
To define a sensor, use '**a**' command,  Processing4, or (outdated method) a bright LED on the desired spot and dim lighting with a "scan" (**s%%**). Save in EEPROM (**e**). SensorCAM uses RGB565 image format which is incompatible with JPG, so auto reboots between SensorCAM or webCAM modes occurs.

#### Serial Command USB format  

**a%%[, rr, xx]** **enAble** _Sensor[%%]_ & refresh _Sensor_ref[%%]_, _cRatios_ etc. 4x4 from image in latest frame. **(Note 20.)**

**b#\[,$]**&nbsp; &nbsp; **Bank** # sensors. Show which sensors OCCUPIED(in bits 7-0).(1=occ.)(**b#,$** sets _brightSF_ to $)

**c$$$$**&nbsp; &nbsp; **reCalibrate** camera CCD occasionally and grab new references for all enabled sensors(Beware of doing this while any sensors are occupied) **N.B.** Obstructed sensors will later need an **r%%**. Check all bank LEDS are off AND check all sensors are unoccupied before recalibrate. Can set AWB AEC AGC CB through $$$$ e.g. c0110  
Also able to change default setting for Brightness, Contrast & Saturation with extra digits e.g. c$$$$012

**d%%[#]**&nbsp; **\*Difference** score in colour& brightness between Ref & actual image. Show # grabs.

**e**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **EPROM** save of any new Sensor offset positions, pvtThresholds, new twins and 5 default parameter settings.

**f%%**&nbsp; &nbsp; &nbsp; **\*Frame** buffer sample display. Print latest bytes in _Sensor_ref[%%]_ & Sensor S[%%] positions.

**g**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **\*Get** Camera Status. Displays most current settings available in webcam window (both sensor & video mode).

**h$[,\#]** &nbsp; &nbsp; **\*Help(debug)** output.  **h9**  to turn all OFF,  **h0**  turn ON detailed USB output. '**h7,#**' "Waits" scroll on a bank# trip.

**i%%[,$$]** &nbsp;**Info.** on S%%.  Status(enabled/occupied), position(r,x), any twin(S$$), pvtThreshold & brightness

**j$#** &nbsp; &nbsp; &nbsp; &nbsp; **\*adJust** camera setting $ to value # and display most settings(as for '**g**'). '**j**' alone lists the options for $#

**k%%,rrr,xxx** \*set **coordinates** of Sensor S$$ to row: rrr & column: xxx. Follow with  **r%%**. Verify values with **p$** 

 **l%%** &nbsp; &nbsp; &nbsp; (Lima) **Latch** sensor S%% to on(1 = occupied(LED lit) & also set _SensorActive[%%]_ false to disable sensing.

**m$[,%%]** **\*Minimum** $(2) sequential frames over _Threshold_ to trigger/trip sensor. Shows list of parameters. **(Note 14)**

 **n#[,%%]** &nbsp; **nLED** bank Number assigned to the programmable status nLED. Optional  **n10,%%**  to set *minSensors*.

**o%%**  (Oscar) force **Off** sensor%% (0=UN-occupied(LED off) Also set _SensorActive[##]_ false to disable updating.

**p$**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **\*Position Pointe**r table info for banks 0 to  $\$  giving DEFINED sensor r/ x\) positions.  p%% shorter.

**q$**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **\*Query** bank$, to show which sensors ENABLED(in bits 7-0). 1=enabled. **q9** gives ALL banks

**r%%[,0]** &nbsp;**Refresh** Average _Sensor_Ref[##]_ (if defined), enable & calc. cRatios etc. **r%%,0** refreshes block  S%0  to  S%% 

**r00** &nbsp; &nbsp; &nbsp; &nbsp; **Refresh** Average Refs etc. for ALL defined sensors. Ignores enable[]. Sensor[00] reserved for brightness ref.

**s%%** &nbsp; &nbsp; &nbsp; **\*Scan** for new location for sensor  S%%(00-97). If found, records location in _Sensor[0%%]_. Note 12

**t##[,%%]** **Threshold** level##(31-98 only) set as default. **t\#\#,%%** sets the pvtThreshold for sensor %%. (**t0,%%** to clear)

**t##** &nbsp; &nbsp; &nbsp; &nbsp; **Tabulates** \#\#(2-30 only) rows of scroll data (continuous scroll toggled off) **Note:** **t1** alone toggles scroll on/off.

**t1,%%**  &nbsp; &nbsp; clear 1 entire bank of _pvtThresholds_. Use **t1,99** to clear ALL banks (0-9). **Note:** **t99** lists all _pvtThresholds_

 **u%%** &nbsp; &nbsp; &nbsp; **\*Un-define**/remove sensor %%  (Sensor S%%=0 & set DISABLED) **u99** for ALL. Cmd '**e**' will erase from EPROM.

**v[1|2]**&nbsp; &nbsp; &nbsp; **Video** mode. Causes reboot as a webserver. "**v2**" will connect to  2nd (alt.) router ssid.(**v** or **v0** for version)

**w**&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **\*Wait** for new command line (\\n) before resuming sensing (handy to freeze display data scroll - see **t1** toggle)

**x###** &nbsp; &nbsp; &nbsp; \*selects first pixel column(0-319) & **z###** selects image width (### columns(1-320)) for imaging.

**y###** &nbsp; &nbsp; &nbsp; \*selects first row for image and initiates a binary data dump for that row (header + #*2 bytes) using rgb565.  
  &nbsp; &nbsp; &nbsp; &nbsp; This command starts a process that must, after a series of 'y' commands, end with a terminator of 'yy'.

**R** & **F**&nbsp; &nbsp; &nbsp; ***Reset** commands- will Reset CAM and initiate the Sensor mode. Both will Finish the WebServer('**v**') mode.

**\\%,#,$** &nbsp; &nbsp;  Convert bank to linear sensor starting with  S$$  and using r,x step sizes of **#,$**(0-31) Slope is "down-right".

**/%,#,$** &nbsp; &nbsp;  Convert bank to linear sensor starting with S$$ as for '\\' but line will slope "down-left" (-deltaX).

**&** &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;  **statistics** histogram on trips and potential trips since last '**&**', then reset counters and start another sample process. The table gives number of single highs, double highs etc. and totals for No. of frames/run time

**@##** &nbsp; &nbsp; &nbsp;  \*set the "occupied" symbol in the scroll to ASCII character\##. Default is 35('#') Arduino IDE **@12** is bolder!

**+\#,$** &nbsp; &nbsp; &nbsp; *add offset(\# pixels) in $ direction to re-centre sensors after physical drift in CAM alignment. $(0-7) for N-NW

 &nbsp; &nbsp; &nbsp; * These commands typically for diagnostic/setup use only. They wait for a line feed or command to resume.

```Note: The value of"bs"(80 sensors 0-79dec) is printed in several formats. For data entry, bsNo format ( %% e.g. 47) is bank/sensor, so bsn=8*4+7=39dec.(vpin). S47 may be printed as(char) 47, 4/7, (octal) 047,(or hex 0x27) depending on context. Debug output likely uses OCT(or HEX). Note: OCT 0107=8/7, 0117=9/7.```

### Startup Notes:

1. Normal power up reset will initiate Sensor mode, as will the'R' command, and uses EPROM data settings.  
2. Sensor mode startup flashes white LED at 10Hz after \~10 seconds, and exhibits a "flicker" at ~20 seconds.  
3. Requested (v1) WebServer mode reset will flash LED at  ~3seconds and again (brighter) at ~8 seconds.  
4. After the 8 second flash the Webserver will be operational at web address 192.168.0.xx (xx from display).  
5. If the OV2640 camera or WiFi fails to initialize, the CAM resets and may restart/revert into Sensor mode.  
6. If USB FTDI/MB is removed or not connected to PC, then WebServer may fail/reboot. Power issue?  

### I2C command Notes:

**(EX-CS may exhibit small variations & reduced cmd functionality refer APPENDIX C)**

**1.** The same commands are valid from an I2C Master Arduino, but there are some variations.  
**2.** The commands with asterisks normally pause CAM execution so the operator can read USB output on a monitor screen. The same commands from I2C DO NOT wait for a new line, with the exception of'w'.  
**3.** Commands b,d,i,m,p,q&t can return data to the I2C master Arduino(Mega). This data is delivered if the master calls a _Wire.requestFrom(addr,#)_; following the command, from the slave CAM address 17(0x11).  
**4.** The I2C data returned(after header byte) is in binary bytes and in a format depending on the last command.  
**5.** Header byte[0] is the ASCII command character (b,d.i,m,p,q,or t) or an error code(OxFE) if no valid data.  
**6.** If the error code is generated, it is followed by the last received (inappropriate) command string.  
**7.** b$ cmd returns$+1 sensor status bytes for bank$,$-1 etc. down to bank 0. 'b' defaults to 'b9'(all).  
**8.** d%% cmd returns 4 data bytes with binary values for bsn, maxDiff+bright, maxDiff \& bright in that order.  
**9.** i%% cmd returns 2 data bytes: byte[1]= bsn and byte[2]=0 if unoccupied or 1(true) if occupied.(+ more)  
**10.** p$ cmd returns Byte[0] header + count +3 data bytes per enabled (bank$) sensor+ parity (max 27 bytes).  
**11.** q$ cmd returns$+1 bank sensor enabled status bytes for bank$,$-1 etc. down to bank 0. 'q' defaults to 'q1'  
**12.** s%% Scan looks for a bright LED on a dimmer background. The LED should be placed on the desired sensor position. This old method of placing sensors is not recommended. The Scan command may be be deprecated.  
**13.** t##[,%%] cmd. initially sends CS the old threshold value (i.e. BEFORE change in the case of t##). Also returns sensor scores(bpd) in 2-byte pairs with MSB set so: bsn(+0x80 if undecided) & bpd(+0x80 if OCCUPIED). Byte[0]header;[1]threshold;[2]S00bpd;[3]bsn;[4]bpd;[5]bsn;[6]bpd etc. Ends with bsn=80 (max 15 enabled)  
**14.** m$,%% sets maxSensors to %% (USB or i2c) (as can h%% (%%<98)). m0,1%% sets minSensors. Data sent to screen is bound between min and maxSensors. Extra parameter status bytes added to i2c bus for display.  
**15.** The ‘‘ character is just a null cmd. Used before R, d & t to prevent BCD Mega itself pre-interpreting them.  
**16.** N.B.: The ESP32-CAM uses old ESP32 which has I2C limitations. It has a “pipeline” for returning data which results in a delay in response. i.e. the first request after a command will return OLD data. A SECOND request should return the desired data described above. A third or fourth request may return updated data.  
**17.** Some commands take time to complete, as command processing can only happen once per 100mSeconds (i.e. the frame rate of the CAM). The I2C master should allow for latency in response where necessary.  
**18.** Data requested over i2c may have a parity byte appended, and a check byte in byte[31].  
**19.** NOTE Automatic updating of ref image of unoccupied sensors now starts after last SUS (suspend) indicator.  
**20.** **a%%,rrr,xxx** performs extended 'create sensor' equivalent to  **k%%,rrr,xxx + a%% + r%%** for new sensor %%  
**21.** Connection to DCC-EX Command Station has cmd. variations. See APPENDIX C for revised command detail.

## APPENDIX B

### Check List for Optimising Sensor Response

In the situation where sensors may be tripping undesirably, there is a range of adjustments that can be made to find a satisfactory operating point. Some have disadvantages that need to be considered and compromises may be necessary.

**1.** First step is to refresh the sensor reference image. Try Cmd: **r00**, or **r%%** for a single sensor. This may be necessary after any disturbance to the environment such as changed lighting.

**2.** Check the "Diff" scores on the scrolling display. After a refresh they should be in the range 32-37 for normal operation. If occasional trips occur, one remedy is to increase the threshold with Cmd: **t46** say. Increasing the threshold reduces the sensitivity to low contrast objects (e.g. black over brown) If unoccupied Diff scores are consistently 32-35, reduce threshold for greater sensitivity.

**3.** Is the lighting adequate? **Steady** muted daylight is ideal. Beware of rotating fans and other moving shadows (clouds?) (Note: may need to consider extreme case of mains induced ripple from 50/60Hz LED/fluoro lighting-to be discussed later) Brighter stable lighting means reduced "noise".

**4.** Sensitivity to electrical "noise" can be reduced by increasing the "_min2trip_" parameter to 3 consecutive frames using Cmd: **m3** (default is m2). However this increases response time by 100mS.

**5.** You can create a "Twin" sensor for a "second opinion" by placing a Second Sensor S$$ on the track adjacent to the primary sensor S%% (3-4 pixels away) by using the Cmd: **a$$,123,234** selecting the position from that of the primary sensor (obtained from Cmd: **i%%**) To avoid increasing response time, use a twin bsNo LOWER than the primary sensor (possibly in a “reserved” bank, perhaps a matching bsNo in that bank). This twin S$$ can be assigned to the primary sensor S%% with the Cmd: **i%%,$$** The primary sensor will not trip unless the twin agrees. This suppresses pixel noise spikes.

**6.** Check that there isn't anything elsewhere in the field of view that is moving and could trigger the auto exposure in the camera. e.g. spectators near the edge of the field of view.(It is possible to change camera ov2640 module settings with '**j**' and '**c**' commands, but this can be a frustrating experience and needs considerable practice as some settings interact and can be order dependent)

**7.** Make sure you do a refresh/record reference (**r**) after any changes or the benefit will be obscured.

**8.** Is the camera steady? No vibration or movement since the last reference images (**r**)?

**9.** There is a 2-frame (experimental) averaging applied to low bank sensors (currently 0-2) This can be extended to cover all banks, if desired by increasing CAM parameter _TWOIMAGE_MAXBS_ above 3/0

**10.** There has been poorer behavior observed with sensors placed near the edge of the frame. They seem to experience more electrical noise than mid-frame sensors and may need extra attention.

**11.** A statistics function can be obtained to see how bad spurious tripping is. The '**&**' cmd gives a table of stats accumulated since the previous '**&**' command. May be useful. HINT: You can compare two or more sensors with different settings on the same spot. Accumulate data with no genuine trips.

**12.** Consider whether a pixel may be faulty or unduly noisy. Try another nearby sensor position.

**13.** If necessary, enhance the brightness of the Sensor location with light colour or a small reflector.

**14.** It is possible to set private thresholds on individual sensors if other solutions inadequate. (**t##,%%**)

**15.** Consider adjusting _brightSF_($) if colour contrast is generally poor (**b#,$**) default 3, try 1-5.

**16.** In some situations, repositioning sensor slightly to include loco shadow will give extra sensitivity.

**17.** Consider repositioning CAM for better oblique view angle giving more contrast for better detection, catching sides of coaches/wagons, shadows and some trackside references.

**18** Consider a beam break enhancement by placing an IR led between rails at the sensor position (power from DCC track?)

## APPENDIX C

### Parsed DCC EX-CS sensorCAM commands

The file _CamParser.cpp_ has been added to the CS specifically tailored to provide a mechanism for the CS to send commands more easily than by using the clumsy diagnostic command style **\<D&nbsp; ANOUT&nbsp;vpin&nbsp;parm1&nbsp;parm2\>**. The CS Native CAM command format is **<N&nbsp;c&nbsp;[parm1]&nbsp;[parm2]\>** where command character '**c**' can be any of those listed below. Generally, to effect changes in sensorCAM, the CAM must be in the run mode (flashing).

The base vpin address defaults to 700 but one can use the _#define SENSORCAM_VPIN ###_ for another value (in _config.h_). With 2 to 4 CAM's, use **<N&nbsp;C&nbsp;vpin0\>** when a switch is needed. The CAM# may also be placed, if defined in _config.h_, prefixing the sensor bsNo.  
e.g. **<Ni 2%%\> <Nr&nbsp;2%%\>** also **<Nm 200\> <Nf 212\> <Nt 243\>**

### User commands

| Command | Example | Equivalent| sensorCAM command & action (some commands only return "ACK OK" to CS) |
| --- | --- | --- | --- |
| **<N\>** | <N\> | n/a | Lists current& alt. defined CAM baseVpins.    |
| **<N C vpin\>** | <NC 600\> |Set base | **CAM** vpin for following commands. <NC #\> selects CAM # (1-4)     | 
| **<N a %%\>**  | <Na 12\> | a12 | **enAble** sensor S%% (bsNo) |
| **<N&nbsp;a%%&nbsp;row&nbsp;col\>** | <Na&nbsp;12&nbsp;32&nbsp;43\> | a12,32,43 | **enAble** & also set new coordinates for sensor bsNo & refresh | 
| **<N b bank#\>** | <Nb 1\> | b1  | **Bank** sensor states(all 8).(used by IFGTE() ATLT() e.g. to locate loco) |
| **<N e\>**     | <Ne\>     | e   |**EPROM** write any changed settings to sensorCAM EPROM.|
| **<N f %%\>**   | <Nf 12\> | f12 | **Frame image** pixel data for Sensor_ref[] and sensor666[] (RGB bytes) |
| **<N F\>**     | <NF\>    | F   | **Forced reboot**, restoring sensorCAM sensor mode& EPROM defaults |
| **<N g\>**     | <Ng\>    | g   | **Get** status ov2640 camera module settings(on sensorCAM monitor) |
| **<N h %%\>**    | <Nh 30\>    | h30 | set _maxSensors_ to limit display to below sensor S%%. Also **Help** (0-9) |
| **<N i [%%]\>** | <Ni 12\> | i12 | **Information** on sensor bsNo state, position & twin (0=No twin)
| **<N i %%[ $$]\>** | <Ni 12\> | i12,02 | **Info.** & sets new twin sensor(S$$) for "second-opinion" on S%%. | 
| **<N j $ #\>**  | <Nj B 2\> | jB2 | **adJust** ov2640 parameters($)(Brightness, Contrast etc)(values 0-2 only) |
| **<N l %%\>**   | <Nl 12\>  | l12 | (lima) **Latch** output state of sensor bsNo to 1 & disable |
| **<N m $ [%%]\>** | <Nm 3 20\> | m3,20 | **Min/max** _min2trip_(1-4) frames [_maxSensors_] Show parameter status data |
| **<N n$ [%%]\>** | <Nn 1 10\> | n1,10 | set **nLED**= bank $ [and _minSensors_=%% to limit display range] $<Nn v\> verifies |
| **<N o %%\>**   | <No 12\> | o12 | (oscar) **Zero** output state of sensor bsNo. Reset to 0& disable. |
| **<N p %%\>**   | <Np 1\>  | p1  | **Positions**(r,x) of all enabled sensors in bank are listed. |
| **<N q #\>**    | <Nq 1\>   | q1  | **Query bank**# enabled states of sensors[0 indicates sensor disabled] |
| **<N r [%%]\>**  | <Nr 12\> | r12 | **Refresh Reference** image for sensor S%%(bsNo)(default ALL=r00). |
| **<N s %%\>**    | <Ns 12\>  | s12 | **Scan** image for brightest spot and set bsNo to center that pixel. |
| **<N t ## [%%]\>** | <N t 43 12\> | t43,12 | **Threshold** displayed, sets global threshold (32-98), [sets a _pvtThreshold_] |
| **<N t ##\>**    | <N t 10\> | t10 | Tabulate ## (2-31) rows of scroll data similar to CAM scroll
| **<N t # [%%]\>** |  <Nt 1\>   | t1 | Trash pvtThresholds. **<Nt 0 %%\>** individually, **<Nt 1 %%\>** for bank, **<Nt&nbsp;99\>** trashes ALL pvtThresholds,  **<Nt&nbsp;1\>** toggles scroll on/off. |
| **<N u %%\>**  | <Nu 12\>  | u12 | **Undefine** and disable sensor bsNo(erase coordinates). **<Nu 99\>** for ALL |
| **<N v [#]\>** | <N v 1\> | v1  |  **Video** mode(1-2) invoke webCAM, or alt webCAM with v 2. **v** for **version** |
| **<N&nbsp;w\>**     | <Nw\>    | w   | **Wait**. Stop/start CAM imaging (flash), status sensing & streaming. |
| **x &nbsp; y &nbsp; z** |    |     | Reserved for binary export for Processing 4 images |
| **<N ### ## ##\>** | <N&nbsp;711&nbsp;75&nbsp;85\> | a13,75,85 | Note: This uses the **vpin** for a sensor, NOT id/bsNo.(ref. **Appendix E**). |

> **Notes:** The'i' cmd prints bsNo(bsn) where bsn/vPin offsets range from(7)00 to(7)79(e.g. baseVpin address 700).  
> Some commands return previous(old) values then update sensorCAM. Use <Nm\> to confirm change.  
> Space after <N is optional, as is capitalization of command. e.g.<N t 42\>=<NT 42\>,<N r 00\>=<NR\>
> Multiple CAM selections can be achieved by config.h entry and use of a prefix on param1 e.g.<N i 212\> for CAM 2
> For commands to work fully, need latest _CamParser.cpp_, CS driver(_IO-EXSensorCAM.h_) & _sensorCAM.ino_

## APPENDIX E

### Tabulated DCC-EX-CS ID's for sensorCAM

**Table B** below shows the colour code used to identify sensors on the Processing 4 track image.  
For example, sensor S12 has a bsNo 1/2 for which the colours are Brown/Red (seen on sensor box edges).  
For CAM number 1, the full CS sensor S12 ID is 112 when used in CS native <N\> commands such as **<N i 112\>** 
The use of the CAM # can be optional.  If only one CAM is installed (or selected), **<Ni 12\>** is sufficient.
For EXRAIL it can be tested so: **AT(CAM 012)** where the vpin is invisibly calculated as (700+012).
**N.B.** The use of the '0' after CAM is essential in EXRAIL.  
The colour code is the standard resistor value colour code for 0-9.

Under normal circumstances if the CS has been configured as per the installation instructions, there is no need to refer to the vpin of any Sensor.  They are all relative to the baseVpin of the CAM.

The full ID consists of CAM number #-bank-sensor or #bs. Each bank(0-9) contains 8 sensors(0-7)  
vPin is the (CAM number # baseVpin) + 0bs,  bsNo skips id's ending in 8 or 9.  (e.g. 700 + 012 = 710)
vPin is the base/first vPin number (e.g. 700) + DEC(bsn)number in the conversion table below.
 
![Sensor Code Conversions](/_static/images/ex-sensorcam/sensor-code-conversions.png)

**Table E &nbsp; &nbsp; Reference Sensor ID to colour code conversion table**

## APPENDIX F

### Hardware Interface (PCA9515A & Endpoints)

> **Note:** This Appendix originally focused on the **ESP32-CAM-MB** implementation, but for that information now refer to the full sensorCAM Manual.
> The information below pertains mostly to the newer WROVER-CAM, as mentioned in **Section 7**, **Figure 6** for a simpler implementation.

The ESP32 CAM drives GPIO pins with 3.3V logic. This may well be incompatible with the master l2C signals at 5V. It is essential that appropriate voltage level shifting and buffering is used where necessary. Unbuffered I2C is limited in range but a Sparkfun differential i2c driver/endpoint may also be used to achieve long lengths and voltage shifting (3.5v to 5v) if needed. 

The sensorCAM can be Reset remotely by software or by cycling the power supply. The CAM MUST be rigidly mounted as it's response to any image vibration can trip sensors. It is best not moved after sensor location programming as precise realignment could be tedious. It is, however, advisable to make guides or jig arrangement to at least be able to remove (for maintenance) and return with minimal misalignment to cover the same field of view. The LED method of placing/positioning sensors may be necessary if a long USB cable is impractical. A 5m buffered USB cable might be advantageous. Even so, programming or imaging over a long USB cable may not be satisfactory.

The PCA9515A based module offers a simpler, but limited, interface to an i2c bus the use of will act as a level changer (3.3V to 5V) and can connect to a SHORT i2c bus (max 2-3m). If the i2c length is near or just over the limit, an optional LTC4311 extender can be attached to boost the signal. As indicated, this option relies on 5V USB power so needs a dedicated (permanent) USB cable connection.  A local 5v buck converter can be used beside the CAM for a better supply.  This is included on the Wrover breakout board. You could also extend a cable between the PCA9515 buffer and CAM (1m).

A programmable nLED and 330ohm resistor may be attached between 3.3V VCC to GPIO14 to aid testing.


The Sparkfun endpoint is perhaps the best overall solution at this stage for driving one (or more) sensorCAMs. It provides greater lengths of cable without extending the Command Station i2c local bus. The endpoints are used in pairs, connected by a long (<100m) differential pair cat5 cable providing power and communications. It can provide buffering, level shifting and power, but care is needed at the CS end to avoid over-voltage damage. It is suggested, with a 5V CS, that the Endpoint pullup 0-1 jumpers at the CS end be cut for safety. The sensorCAM Endpoint default pullups are needed for the 3.3V CAM i2c bus. The CS Endpoint requires 3.3V power(from the CS) and a separate (7 to 9V) DC supply for the Regulator & CAM.

Typical device applications (with BUCK 5V inverters):

![Typical Mega with ESP32 CAM](/_static/images/ex-sensorcam/typical-mega-esp32-cam.png)

Sparkfun endpoints(requires a matching sparkfun endpoint at CS)

![ESP32 Wrover CAM with Sparkfun Endpoint](/_static/images/ex-sensorcam/esp32-wrover-sparkfun-endpoint.png)

Recommended CAM wiring is with Endpoints and 5V dedicated regulator with power over GRN-GRNW(Vin) (CAT 5) with Vin(7-9V) from an ungrounded 0.5A DC supply (wall-wart/plug pack).

There are two basic variations below for connecting the Endpoints to the CS. The choice depends on the current system being extended. Options A applies to a 5V CS(Mega) with or without other existing I2C accessory connections, while Option C is the simplest connection to a 3.3Volt CS (e.g. CSB1) i2c bus.  The i2c bus should be "tuned" to include the CAM load before the CAM is attached.  The Endpoint has a pair of 4k7 pullups that may be disconnected by jumper cuts.  Refer to Tinkerers Guide to Tuning documentation on i2c.

The 2x Endpoints require about  10mA  each from the 3.3V PS. All options can be adapted for use with a mux if necessary. 

**Option A:** CUT CAM endpoint jumper 0-1 and supply 5V and 3.3V from the CS. Option A connections results in a 5V i2c interface to 3.3V differential cable for 5V microprocessor based CS (e.g. Mega).

**Option C:** used with newer (32bit) MPU's (e.g. CSB1) & uses 3V3 throughout. No Endpoint jumpers need to be cut. Whichever option is used, the user should consider if the I2C bus needs to be tuned differently. For very short extra cable length to the Endpoint and only one extra device count on an I2C bus under 1m in length, tuning may be unnecessary. In marginal conditions consider returning as per DCC-EX recommendations.

#### A FOR 3.3V Differential drive 5V CS I2C BUS

![Differential Drive 5V CS](/_static/images/ex-sensorcam/differential-drive-5v-cs.png)

#### C FOR 3.3V Differential drive 3.3V CS I2C BUS

![Differential Drive 3.3V Only CS](/_static/images/ex-sensorcam/differential-drive-3v3-only-cs.png)

## APPENDIX H

### Notes on use of EX-RAIL with sensorCAM

### 1. Sensor/vpin Numbering

The numbering of sensors can be consecutive by vPin, which is the common practice with multi-pin peripherals (e.g. PCA9685 16-channel Servo driver and MCP23017 16-channel GPIO Expander). Sequential vPin numbers within a device is hardware enforced, but this loses some of the advantages available by a more meaningful ID notation. Such ID's are available for jmri use and so can also be used for sensorCAM. Use of IDs, as suggested below, can remove any need to program with vPin numbers.

For any peripheral device, the vPin is needed for commands (e.g.700+5), but, if predefined (e.g. in config.h), alphanumeric names such as CAM or CAM2 or ESSEX can be used in place of the base vPin to identify the camera. Then commands for CAM pin 5 become: e.g. AT(CAM 05) or AT(ESSEX 05)

```c++
 e.g.  
 #define SENSORCAM_VPIN 700    //place in config.h or myAutomation.h or mysetup.h  
 #define CAM  SENSORCAM_VPIN+  //in config.h or myAutomation.h or mysetup.h  

 Valid EXRAIL commands: AFTER(CAM 5)  AT(SENSORCAM_VPIN+7)  IFGTE(CAM 010, 2)  

 To avoid frequent “CAM” in scripts, an alias can be assigned e.g. ALIAS(ESSEX_P1, CAM+0x10)
```

With each sensorCAM having up to 80 sensors, it is desirable to test groups of (1 to 8) sensors with a single EXRAIL test using the **IFGTE()** or **IFLE()** commands. To do this, the sensors are logically arranged in “banks” of (consecutive) vpins. The logical grouping available can be written in the form “bs” or b/s where b can have bank values of 0-9 (10 banks) and s values 0-7 (8 sensors). **IFGTE** and **IFLT** read a whole bank "value". Native CAM commands can also be issued e.g. **PARSE("<N b 4\>")** for bank 4.

EXRAIL can accept “b/s” numbering (e.g. 047) if we add the leading 0. e.g. vpin= **SENSORCAM_VPIN+ 047** e.g. **IFGTE(CAM 047,1)** provided values are defined for **SENSORCAM_VPIN** & **CAM**(as above).

**(N.B. “CAM” includes the ‘+’)** Using this method there is no need to remember assigned vPin values!

**Example 1:** For the approach to a signal, several sensors may be deployed (say S13 to S17) with S17 last at the signal. As a train approaches the signal, the (bank) “value” of the tripping sensors will increase. This can be used to control the loco speed for a smooth and precise stop at a platform for example.  
Commands **IFGTE(CAM 013,8) SPEED(40)**... **IFGTE(CAM 013,16)** **SPEED(30)** etc. can be used to control the loco approach speed with some precision.  
Finally, at the signal(S17), **IFGTE(CAM 013,128) STOP**

 Aliases could also be defined and used for station/bank or line sensors. e.g.IFGTE(TRENTHAM, 0x80)

**Example 2:** The CAM can have up to 10 occupation/line detectors. If two "linear" line sensors are needed, and we have bank 1 allocated (S10-S17), the following 16 vPins could be assigned to 2 banks of linear sensors. We can use (bs#) ID of 20 to 27 for first linear sensor (bank2) and 30-37 of bank3. The Command Station can easily handle banks of 8, using an ID based format of (CAM 020) and (CAM 030). The "bank" or b/s notation requires the leading ‘0’ on the bsNo. for automatic vpin calculation. The linear segments at S21 to S27 may also be tested individually and a common bank threshold can be set if needed. e.g. **IFGTE(CAM 020,1)**...// bank occupied, or **IFGTE(CAM 024,16)** &nbsp; //2nd half occupied.

Note: With ‘0%%’ notation, unless you understand the issue, avoid using bank 8 & 9 as mistakes may arise. (08# must be expressed as 010# and 09# as 011# for correct outcome)

### 2. Multiple Cams

Multiple sensorCAMs can be easily handled if CAM2, CAM3 etc are defined along the lines of CAM above, so **IF(CAM2 012)** tests a different sensor to **IF(CAM3 012)**, provided **SENSORCAM2_ VPIN** etc. are defined. Using CS native commands, e.g. **<Ni 212>** and **<Ni 312>**, can also access **S12** on different CAMs. **The #define SENSORCAM_VPIN ###** is essential for cam1. Do NOT insert a 1 in to **SENSORCAM_VPIN**. You may use **SENSORCAM2_VPIN** and **SENSORCAM3_VPIN** with **CAM2** and **CAM3** in _config.h_

## APPENDIX J

### WROVER-CAM notes.

### 1 Note on i2c clock frequency

The newer sensorCAM drivers default to an i2c bus frequency of 100,000 Hz. With caution, this may be increased somewhat (e.g. 200000) if the i2c bus is well tuned and all attached devices can handle higher frequencies. To set a higher frequency, for example, place the following in mySetup.h or myHal.cpp I2Cmanager.forceClock(200000); //place after void halSetup()

### 2. Notes on 40-pin WROVER CAM and 38-pin breakout board

Potentially simplest commercially available hookup for 40 pin WROVER-CAM:

Software configuration: add #define CAMERA_MODEL_WROVER_KIT to bottom of configCAM.h

2x“Spare” (USB end) Vcc and GND pins not used with the 38 pin breakout board shown. (remove?)

Adding 1.0uF capacitor between reset (EN) pin and gnd ensures more reliable power-on reset.

Add a super-bright green LED and 330R from 3.3V to GPIO14 for programmable LED indicator.

There is no white “flash” LED but, in sensorCAM mode, the on-board blue LED flashes instead. (GPIO2)

The breakout board USB connectors are for an optional 5V power source ONLY. No comm's.

Limit Vin barrel jack to 7-10V max to avoid destruction of the 1117C 5V regulator. (Vne= 16V)

For a limited reach, perhaps using a LTC4311 terminator/buffer at the CS to boost signal rise times and range, the cheaper PCA9515A may be used with the Wrover-CAM connected as below.  The wires from PCA9515A to the CAM can be up to 2m long (with extra pullups) using twisted pairs (cat5?).

![ESP32 Wrover CAM with PCA9515A](/_static/images/ex-sensorcam/esp32-wrover-pca9515a.png)


### ADDITIONAL RANDOM NOTES:

ALL FOLLOWING IMAGES ARE FOR GENERAL INFORMATION ONLY& NOT DIRECTLY REFERENCED IN THE FULL MANUAL ABOVE

![ESP32 CAM MB v1.6 vs v1.9](/_static/images/ex-sensorcam/esp32-cam-mb-16-19.png)

![ESP32 CAM Closeup 1](/_static/images/ex-sensorcam/esp32-cam-closeup-1.png)

![ESP32 CAM Closeup 2](/_static/images/ex-sensorcam/esp32-cam-closeup-2.png)

![ESP32 CAM Closeup 3](/_static/images/ex-sensorcam/esp32-cam-closeup-3.png)

![ESP32 CAM Closeup 4](/_static/images/ex-sensorcam/esp32-cam-closeup-4.png)


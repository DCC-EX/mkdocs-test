# Installing Command Station Software

This assumes you have read and done the EX-Installer installation, know how to execute it and have done the [CLI download and optional ESP32 steps](first-run.md) to make sure you have the necessary build processor and run time libraries for your Command Station.

To proceed, click the Select your device button.

## Device Selection

![device selection](/_static/images/ex-installer/select-device.png)

A scan for devices will start automatically. Usually the installer is able to work out the details automatically.

If you see No devices found it means that you either

- have not connected the device to the computer, connect it now then click the Scan for Devices button again
- the device was not recognised by the computer, this may be a bad USB cable or a missing USB driver. Refer to the Diagnosing Basic Problems page for assistance.

Next select the USB port (if several) and the type of device you wish to load the EX‑CommandStation software onto. EX‑Installer will attempt to work out both of these for you, but it may need assistance.

**NOTE:** For the EX‑CSB1 select ‘DCC-EX EX-CSB1’ from the drop-down list.

Now press the Select Product To Install button and click on the EX‑CommandStation logo to proceed.

## Version Selection

![select version](/_static/images/ex-installer/select-version.png)

Select which version of the EX‑CommandStation software to load onto your hardware. If you are unsure, or unless you have been otherwise directed by the support team, we recommend you select Latest Production.

## Configuration

![config](/_static/images/ex-installer/config.png)

When loading for the first time, you should use Configure Options. Alternatively you may [reuse your previous files](#stored-configuration-files).

On this screen you can select some of the flexible and optional features of the EX‑CommandStation:

### Motor Driver Type

You must select the motor shield that you have installed. The installer can’t detect this. Selecting the wrong board will not work and may damage the hardware by compromising the short-circuit protection.

- For the EX‑CSB1 alone select ‘EX-CSB1’ or ‘EXCSB1_WITH_EX8874’ as appropriate.

![motor_driver](/_static/images/ex-installer/motor-driver.png)

## Other options

You should select "Disable EEPROM support" for most cases. 

### Optional LCD or OLED display

The EX‑CSB1 will generally be supplied with an OLED 128 X 64

If you have installed and optional OLED or LED display, enable [I have a display] option, which will present you with a drop-down list to select the type of display you have.

![display-option](/_static/images/ex-installer/display-option.png)

### Optional Wi-fi

If you are using a CSB1 or other board with integrated Wi-Fi, or have installed and optional Wi-Fi board you need to enable the `I have WiFi`.
This enables the "Wi-fi Options" button where you can configure the Wi-Fi.

### WiFi Access Point mode

![wifi AP](/_static/images/ex-installer/wifi-ap.png)

In Access Point mode, you command station runs a completely isolated Wi-Fi Network. This is most useful if your layout is away from the house, or you transport your layout frequently, or do not want to give guests access to your home WiFi. WiFi phones or tablets will need to connect their WiFi to the Access Point and will lose access to your home WiFi. 
Wi-Fi Password is optional.
If this field is left blank the password will default to ‘PASS_xxxxxx’ where ‘xxxxxx’ will be the same as the SSID name that will be automatically configured.
If possible, choose a channel that is unused (or least used) by other Wi-Fi networks around your location.
There are numerous phone apps that can help you determine which channels are being used by other networks. For Android, ‘Wifi Analyzer’ is one that works. For iOS ‘Netspot’ is suitable (you don’t need to purchase WiPry device they mention).

Wi-Fi Channel can be any value from 1-11.

#### WiFi Station mode

![wifi station](/_static/images/ex-installer/wifi-station.png)

In Station mode, the CommandStation connects to your existing home Wi-Fi Network or other router.
Phone and Tablet throttles on your home network can find the CommandStation easily.

Wi-Fi SSID is the name of your home network.

Wi-Fi Password is the password for your home network.

Additionally, if you choose, you may customise the Wi-Fi hostname, or leave it as the default “dccex” which is easily found by throttles. 

### Optional Ethernet

If you have installed and Ethernet board, select this option.

Note that it is not possible to have both Wi-Fi and Ethernet enabled at the same time.

### Start With Power On

![power-on](/_static/images/ex-installer/power-on.png)

The EX‑CSB1 will generally be supplied with this enabled.

If you don’t enable this, you will need to turn the track power with your controller, or with TrackManger automations.

### Override Current Limit (Advanced)

Do not select without Engineer level knowledge.

### Set Track Modes (Advanced)

![track manager](/_static/images/ex-installer/track-manager.png)

The default has Track A and DCC MAIN  and Track B as a PROG track.
This is an advanced option and should only be used do not need to alter this unless you are running multiple motor shields or wish to operate only in DC.

### Advanced Configuration (Optional)

Skip this page when you first start. You will need it later once you start adding accessories or automations.  

Note there is an additional option Create myAutomation.h that allows a blank myAutomation.h file to be created, which you can edit on the following Advanced Config screen. Leaving this option disabled means a myAutomation.h file will not be generated if it is not required, which saves memory on your EX‑CommandStation device.

## Compile and Load

![load](/_static/images/ex-installer/load.png)

This proceeds to compile your configuration in with the base code and load it into the Command Station Arduino processor.

There may be errors compiling (usually due to a mistake in the advanced configuration or myAutomation.h) and this will prevent the load stage from taking place.

![loaded](/_static/images/ex-installer/loaded.png)

Errors during the load stage are almost invariably caused by problems communicating with the Arduino, possibly by incorrect selection of the type or by having another program, such as JMRI or EX-Webthrottle still using the USB connection.

## Backup

After loading the software onto your device, you can optionally copy the generated configuration files to a folder of your choice as a backup by clicking the Backup config files button.
You will be prompted to select a folder, and if the chosen folder already contains config files, you can overwrite these, or you can select an alternative location.

## Device Monitor

Once you have selected a device in EX‑Installer on the “Select your device” screen, or after successfully loading software onto your device, a View device monitor button will be available.

When clicking this button, the EX-Installer Device Monitor window will open, allowing you to interact with your device by sending commands and viewing the serial console output.

![device monitor](/_static/images/ex-installer/device-monitor.png)
For further details on using EX-Installer Device Monitor, continue on to the next page with the ‘Next’ button, or go straight to Using the EX-Installer Device Monitor.

Next Steps - Test your setup

**IMPORTANT**

The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.

See the Testing your installation page or click the ‘Next’ button to learn how to test and use your EX‑CommandStation.

## Stored Configuration Files

Click the Browse button and navigate through your computer’s folders and files to select any file in the folder containing your existing configuration.

On this screen you can edit the configuration files. If you have more than two files to edit, they will be separated into tabs as shown in the second figure above.

**NOTE:** If you did not enable any options requiring myAutomation.h, and did not enable Create myAutomation.h, you will only be able to edit config.h on this screen.

![stored_files](/_static/images/ex-installer/stored-files.png)
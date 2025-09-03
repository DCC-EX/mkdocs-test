# Nucleo - STLink Firmware

## Upgrade the debugger firmware

- All Nucleos come with a built-in debugger interface, which is the portion of the PCB at the top near the USB connector. This is of great advantage during development as it helps us track down issues more readily. It does however mean that device drivers are needed for Windows (7, 10 and 11 supported), and that the debugger firmware may need upgrading. See notes below.

- During testing, it was noted with certain USB chipsets on Windows 11 that serial responses via the USB debugger port would stop being received by the Serial Monitor, even though the device continued to operate normally. The recommendation to resolve this issue is to upgrade the debugger firmware.

- We recommend you upgrade the debugger firmware regardless if you experience this issue or not, and regardless of whether you use Windows, Linux or MacOS. Instructions for Linux and MacOS can be found on the web but rely on using the Java app in the AllPlatforms folder.

- You need to ensure your NUCLEO device is plugged in to a USB port prior to commencing the upgrade.

- [Download stsw-link007-v3-16-9.zip or later from st.com ](https://www.st.com/en/development-tools/stsw-link007.html)

- You will need to navigate through the “en.stsw-link007_v3-16-9” folder down to the “Windows” folder, which contains an executable “ST-LinkUpgrade.exe” to upgrade the firmware on the NUCLEO devices.  
  ![download and extracted folders](/_static/images/nucleo/stlink-driver-install.png){width=40%}

- Double click this file to run it, which should present the upgrade window.  
  ![download and extracted folders](/_static/images/nucleo/stlink-driver-install2.png){width=40%}

- Clicking the “Device Connect” button will attempt to connect to your NUCLEO device and display the currently installed firmware version, along with the version it will attempt to upgrade to.  
  ![download and extracted folders](/_static/images/nucleo/stlink-driver-install2.png){width=40%}

- Providing your NUCLEO device has been detected and is running an older version of the firmware, click “Yes >>>>” to proceed with the upgrade.

- Hopefully you will see the “Upgrade is successful” pop up appear when complete.  
  ![download and extracted folders](/_static/images/nucleo/stlink-driver-install3.png){width=40%}

- At this point, after clicking “OK” the software should display the new version of the firmware that has been applied to your device.

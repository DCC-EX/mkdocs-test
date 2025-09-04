# Nucleo - USB Drivers

# Required for Windows

When using any of the NUCLEO series microcontrollers with Microsoft Windows, you will need to install their STLink USB drivers in order to be able to upload software to them and use the Serial Monitor in either PlatformIO or the Arduino IDE.

!!! note "Note"

    You should install these drivers before plugging your NUCLEO device in for the first time.  
    Linux and MacOS users don’t need the drivers installed.

- [Download stsw-link009.zip from st.com ](https://www.st.com/en/development-tools/stsw-link009.html)

- Once you download and extract this zip file, you will need to install the STLink drivers located in the “stsw-link009” folder.

- Right click the “stlink_winusb_install.bat” file and select “Run as administrator”. You will need to click “Yes” to allow it to make changes to your computer.  
  ![USB driver install](/_static/images/nucleo/usb-driver-install1.png){width=40%}

- Click ‘Next’ to install the drivers, and you should see this summary screen to confirm the drivers installed successfully:  
  ![USB driver install](/_static/images/nucleo/usb-driver-install2.png){width=40%}

- You can now plug your NUCLEO device in and proceed with upgrading the debugger firmware (highly recommended).

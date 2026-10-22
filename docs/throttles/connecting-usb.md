# Connecting a USB Throttle to your EX-CommandStation

Other than some purpose built devices, currently we are only aware of three options for using a throttle by connecting a PC or smart device(phone) directly to an **EX-CommandStation** via USB

- [**EX-WebThrottle](../products/ex-webthrottle/)
- [JMRI](https://jmri.org)
- [Engine Driver](../throttles/engine-driver.md) Android App, using USB On-The-Go (OTG)

!!! important "Only one USB connection at a time"

    Only one app or device can connect to the **EX-CommandStation** at at one time.  
    So it it important that **EX-Installer** is closed before use **EX-WebThrottle** or **JMRI**.  Similarly, **EX-WebThrottle** or **JMRI** must be closed before using **EX-Installer**.

!!! Note "Microcontroller Power supply"

    The USB port will provide power to Arduino Mega microcontroller so the second Power supply is not needed, but not a problem if you leave it connected.

    The **EX-CBS1** power supply or the power supply to any separate Motor Drivers ***is still needed*** to power the track.

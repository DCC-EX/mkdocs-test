# The EX-Installer

With the exception of a Command Station Booster1 Express [CSB1](?CSB1) used solely as shipped with no accessories or options, you will need to download and install software to your Command Station or other DCC-EX products.

This is managed by EX-Installer which is responsible for obtaining the relevant software and libraries, merging your custom configurations and mind-bending automations, locating the USB connection to your device,  compiling and downloading the result and showing the serial log from your device if required.

Since every layout is essentially a prototype, and there are a huge variety of hardware build combinations, it is not possible to download a pre-built firmware package from the web.

## Warning Antivirus Software

You may need to turn off your antivirus software before you try to install, or you may be prompted to trust this executable.

Sometimes our software gets blocked by antivirus applications. If you see any errors on the installation screen, this is usually the issue.

## Installing EX-Installer

[Windows x64](92-download-win.md){ .md-button }
[macOS](91-download-mac.md){ .md-button }
[Linux x64](90-download-linux.md){ .md-button }

**NOTE:** There is no support for EX-Installer on Windows 7, nor 32 bit operating systems such as Windows x32 or RaspberryPi OS.

## Alternatives to the EX-Installer

Experienced programmers or those wishing to develop new features or products will generally find [VSCode/PlatformIO](05-platformio.md) a more powerful and familiar option.

Methods involving downloading zip files have caused  support issues in the past, are troublesome and not recommended.

Use of the Arduino IDE is discouraged and not covered in this documentation as it has far less functionality than VSCode and has limitations with respect to compiler and library options.

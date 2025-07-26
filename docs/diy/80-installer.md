# Installing Command Station firmware

Your command station cannot operate without the appropriate firmware which must be configured in advance to suit the hardware target. Since every layout is essentially a prototype, and there are a huge variety of hardware build combinations, it is not possible to download a pre-built firmware package from the web.

Note: Only the CSB1 comes pre-installed but this too must be reconfigured and reinstalled to utilise layout-specific features.

Once your initial Command Station build is operating, you will almost certainly wish to make use of additional features such as defining turnouts, rosters, signals, routes, animations and other varied accessories. In each case, we make it as simple as possible but you do need to use the appropriate tools to re-install the firmware to incorporate your changes.

There are essentially two ways to handle this:

- Use the [EX-Installer](81-installer.md) which guides you through the process with menus and dialogs. This is appropriate for all users.
- Use VSCode/PlatformIO which is a fully featured programmers IDE (Integrated Development Environment) which will be familiar to programmers and definitely more suited to those wishing to explore the open C++ source and potentially contribute code to our project.

Methods involving downloading zip files, or use of the Arduino IDE are generally slow,  troublesome and not recommended.

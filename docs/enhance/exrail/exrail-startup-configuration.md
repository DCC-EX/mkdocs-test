# Startup Configuration - Native/Serial Commands

Sometimes, you may want to configure your **EX‑CommandStation** with settings which are not otherwise saved by the Command Station when restarted, and are not included in the normal **EXRAIL** commands. For example the ``ACK min`` for the Hornby R7150 Decoder (which seems to need its minimum ACK pulse duration limit set to 2600µS to be recognised).

To automatically run [native/serial commands](../../reference/serial-commands/index.md) at start up using the ``PARSE()`` command in your ``myAutomation.h``.

!!! NOTE "PARSE() supersedes SETUP()"
    The old method of creating a ``mySetup.h`` file and using ``SETUP()`` commands still works, but is no longer recommended.

How you method you use will depend on how you load the **EX‑CommandStation** software onto your Arduino.

- By using [EX‑Installer](#if-you-are-using-ex-installer)
- By using the [Visual Studio Code (VSC)](#if-you-are-using-visual-studio-code-vsc)
- By using the [Arduino IDE](#if-you-are-using-the-arduino-ide-not-recommended) - ***Not recommended***

----

## If you are using EX-Installer

==TODO== MEDIUM - Adding to your myAutomation.h in EX-Installer

----

## If you are using Visual Studio Code (VSC)

==TODO== MEDIUM - Adding to your myAutomation.h in VSC

----

## If you are using the Arduino IDE (Not Recommended)

This will need to be done in the Install using the Arduino IDE, so first make sure you have followed these steps to load up the Arduino IDE.

!!! IMPORTANT "Arduino IDE is not recommended"
    A word of caution on using the Arduino IDE to install the software:  
    While it is possible install the software using the Arduino IDE, we seriously ***DO NOT RECOMMEND IT*** for a novice users. It is an order of magnitude more complex, much slower, and with a very high probability of getting something wrong unless you really know what you are doing.  
    The **EX‑Installer** will meet 100% of the needs of a most users with considerably less effort.

==TODO== MEDIUM - Adding to your myAutomation.h in the Arduino IDE

----

## Adding in the startup commands

Within the new file that has been created, you can add in the commands that you wish the Command Station to run at startup. For example, if you need to run the following command each time your Command Station starts up:

```c++
<D ACK MIN 2600>
```

Then you would need to enter into the myAutomation.h file:

```c++
PARSE("<D ACK MIN 2600>");
```

Note the upper case word ``PARSE`` at the start.

Adding in more than one startup command
If you need to have multiple commands run at start up, you will need to enter each additional command on a new line, so a longer myAutomation.h file could look like:

```c++
PARSE("<D ACK MAX 9200>"); // Set ACK detection to allow pulses up to 9200uS
PARSE("<D ACK LIMIT 60>"); // 60mA is the default
PARSE("<0>"); // tracks off at startup
PARSE("<D CMD 0>"); // can be set to ON for testing in the serial monitor
```

Here you can add comments on each line, these can be added by using two forward slash characters ``//`` and then your comments. This makes it easier to remember why you added these start up commands.

## Upload the new version of the software

Finally, upload the code to the Arduino as you would do during the standard Arduino IDE Setup. Restart the Command Station and these commands will have run at start up.

## Examples

Automatically Turning Track Power on at Startup
Adding this line to mySetup.h will cause the track power to turn on automatically when the **EX‑CommandStation** powers up.

```c++
PARSE("<1>");  // Turn track power on at startup
```



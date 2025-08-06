# What is EXRAIL?

EXRAIL is an “EXtended Railroad Automation Instruction Language” used to:

- Describe your turnouts, signals etc.
- Configure your Command Station to understand the hardware and accessories you have attached.
- Handle what to do when things happen (e.g. a button is pressed)
- Create automated route settings through your layout
- Move things, make sounds, flash lights
- Drive trains under automatic control
- Implement mimic panels and control panels
- Display status information or platform announcements on OLED screens.
  
## You DON’T need

- JMRI, or any additional utilities
- Engine Driver, wiThrottle, or any other WiThrottle app
- A separate computer living under your layout
- Knowledge of C++ or Python/Jython programming

Although EXRAIL has more than 100 individual commands available, it is generally easier to work from the how-to cookbook examples rather than attempt to understand every feature. It's important to understand a few principles first.

## Important Background Information

- EXRAIL scripts are written into a file called myAutomation.h which you can edit with any suitable text editor. You don't need any extra tools installed on your PC that you don't already have in VSCode or the EX-Installer.
- When you upload the command station with the DCC-EX code, myAutomation.h is used by the compiler to configure the software and embed any sequences so that the command station can run without further assistance from your PC. If you change myAutomation.h then you must upload again.
- EXRAIL can run multiple sequences simultaneously so it's great for annoying Arduino programmers who find that extremely complex to do in C++.

## Basic building blocks

There are a few basic building blocks that will appear in the examples:

- ```SEQUENCE``` - Simply a list of things to be done in order. These things might be to actually drive a train around, or merely to set some turnouts or flash some scene or panel lights. Actions can be made to wait for conditions to be met, like a sensor detecting a train, a button being pushed, or a period of time elapsing.
e.g.

```cpp
  SEQUENCE(27) // Close crossing gates
    BLINK(100,500,500) // start flasher
    DELAY(4000)
    SERVO(200,30,Slow) // move barrier
    DONE   // sequence completed
```

- ```ROUTE``` - A special type of SEQUENCE that is made visible to a throttle with a readable name so the user can press a button to get the sequence executed. This might be best used to set a series of turnouts and signals to create a route through the layout. For example

```cpp
  ROUTE(1,"Platform A to mainline")
    THROW(27) // set turnouts
    CLOSE(6)
    GREEN(101) // change departure signal
    DONE 
```

- ```AUTOMATION``` - A special type of SEQUENCE that is made visible to a throttle so that a user can hand over a loco and let EXRAIL drive the train away, following each step listed in the sequence. For example, a user could manually drive a train into a station and press a handoff button in the throttle to run an AUTOMATION to take it on a journey around the layout.

```cpp
  AUTOMATION(17,"Depart to Byeckaslike")
    FWD(20) // start slowly
    AT(167) // when we reach sensor 167
    SPEED(55)
    AT(168) // approaching station
    SPEED(10) // slow down
    AT(169) // at the terminus
    ESTOP // stop dead
    DONE
```

- ON-handler - a sequence that is automatically started when some event happens. For example when a button is pressed (ONBUTTON) or a turnout is changed (ONTHROW / ONCLOSE) so you can intercept turnout/point changes to automatically adjust signals or other turnouts.

```cpp
ONBUTTON(167)
  RED(108)
  THROW(6)
  GREEN(112)
  DONE
```

## A users story

I have used C++ on Arduino’s and Python/Jython on JMRI software to build Automation sequences. I now use EXRAIL instead because:

- It’s significantly easier and more flexible than the other two options.

- I reduce the number of Uno and Nano accessory boards needed to do the same tasks on the layout by using the DCC-EX Command Station and embedded EXRAIL instead.

- I can create Automations, Routes, & Sequence scripts With EXRAIL on the Command Station and still access them from JMRI PanelPro and DecoderPro GUI buttons with a simple sendDCCmessage.py script pointer that passes them to the EXRAIL scripts on the Command Station, so I don’t have to rewrite the script in Jython/Python.

- EXRAIL is ten times easier to learn and use and is more flexible then the other methods.

# Engine Driver


![Android](../_static/images/os/icon_android.png){: width="50px"} ![Engine Driver](../_static/images/engine-driver/engine_driver_logo.png){: width="50px"}

**Engine Driver** (ED) is an Android App that uses the *WiThrottle Protocol* *or* the *DCC-EX Native Commands* to connect directly to the **EX-CommandStation** via WiFi. It can also connect to the JMRI WiThrottle Server via WiFi using the *WiThrottle Protocol*.

If you wish to connect **Engine Driver** directly to **EX-CommandStation**, you need to add a WiFi option to your **EX-CommandStation**.

If you wish to connect **Engine Driver** to **JMRI**, you need to start the *WiThrottle Server* and (optionally [^1]) the Web Server in JMRI on the computer running **JMRI**. The **JMRI** computer must be connected to the **EX-CommandStation** using a USB cable.

[^1]: The JMRI Web server is required if you want to show the Loco images in Engine Driver from JMRI.

## Platforms

![Android](../_static/images/os/icon_android.png){width="50px"}

* You can Get 'Engine Driver Throttle' from the [Google Play Store](https://play.google.com/store/apps/details?id=jmri.enginedriver) <br />or

* Visit the Engine Driver Website: [https://enginedriver.mstevetodd.com/](https://enginedriver.mstevetodd.com/) for more information.

Extensive help is available at the [Engine Driver Home](https://flash62au.github.io/EngineDriver_Home/index.html) site.

## Standard Features (all WiThrottle servers)

* Control one to six locomotives or consists
* Speed and direction control
* Up to 29 DCC functions
* Create and edit consists (software-defined)
* Control layout power, turnouts, routes, and access JMRI web panels and windows
* 'Discover Server' Detect, Select & Connect to WiFi enabled Command Stations
* 'Roster Server' download Engine ID's & function keys from the Command Station
* 'Virtual Engine Sounds' {Bell, Horn, Short Horn, Mute} for motor only decoders, on first two throttles
* Able to use inexpensive Bluetooth gamepads for tactile control
* Multiple theme, colours and throttle layout options 

## EX-CommandStation Specific or Advantageous Features

* DCC-EX EXRAIL Automation {Handoff}, Route {Set} and EXRAIL Command function buttons
* Able to select local images for roster locos
* New 'Request Loco ID' & 'Drive Away' feature from a Program track onto Mainline track with **EX-CommandStation**

## EX-CommandStation Specific Features - when using the DCC-EX Native Protocol

* Read and write DCC addresses on the Programming Track
* Read and write CVs of decoders on the Programming Track
* Write CVs of decoders on the Main Track
* Issue Native commands to the **EX-CommandStation**
* TrackManager control - able to change the type and state of each Track/Channel (e.g DCC and DC)

See the [Engine Driver - Features when using the Native Protocol](engine-driver-native-protocol_not_in_nav.md) page for more information.

## Screenshots

![Engine Driver Main Screen](../_static/images/engine-driver/ed1.png){width="150px"} ![Engine Driver 2](../_static/images/engine-driver/ed2.png){width="150px"} ![Engine Driver 3](../_static/images/engine-driver/ed3.png){width="150px"} ![Engine Driver 4](../_static/images/engine-driver/ed4.png){width="150px"}

## Operation

See [https://enginedriver.mstevetodd.com/operation/getting_started.html](https://enginedriver.mstevetodd.com/operation/getting_started.html)

and [https://enginedriver.mstevetodd.com/videos/index.html](https://enginedriver.mstevetodd.com/videos/index.html)

----

## Using a Bluetooth Gamepad Controller

Here is one of a number of Bluetooth controllers that provides extra function buttons and you can hold by placing your finger in the ring and using the buttons and DPAD.

![Ring Shape Hand Controller](../_static/images/engine-driver/bt_controller2.png){: align="center" width="150px"}
  
Examples: [Walmart](https://www.walmart.com/ip/Gamepad-Ring-Shape-Wireless-VR-Joystick-Rechargeable-Bluetooth-compatible-V4-0-Game-Controller/443871148?wmlspartner=wlpa&selectedSellerId=101036302) :
[AliExpress](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20220515220821&isPremium=y&SearchText=%22r1%22+bluetooth+game+controller&spm=a2g0o.productlist.1000002.0>)

Notes *From Steve:*

<div style="padding-left: 30px;" markdown="1">

I set speedsteps to 10, change amount to 1, repeat delay to 9999, horizontal switching layout, throttle web view. <br />
I acquire loco/consist using my phone, then dim & lock and put phone in my holster. <br />
Then I can "bump" the joystick up and down 3,2,1,0,-1,-2,-3, easily keeping track of the current "notch". 1 is coupling speed, 2 is switching/yard speed, 3 is mainline. <br />
If I'm at home, I put the Conductor view in the web and I have my work for each location.

</div>

![Engine Driver Conductor View](../_static/images/engine-driver/ed_conductor_view1.png){: width="200px"}

More information is available on the [Engine Driver](https://enginedriver.mstevetodd.com/operation/gamepads.html#example-gamepads&gsc.tab=0l) site.

## Adding a Physical Dial (Knob)

It is possible to easily add a rotary dial (knob) to **Engine Driver**.  see [Adding a Physical Dial/Knob to Engine Driver](engine-driver-physical-knobs_not_in_nav.md) for more information.

## Recording a log file in EngineDriver

If you are having difficulties with Engine Driver connecting to an **EX-CommandStation** it is very helpful if you can provide the support team with a log file of when the problem occurs.

To record a log file in EngineDriver:

1. Start ED.
1. From the menu, select ``View Log``
1. Click :guilabel:`Start recording to a file`
1. Click :guilabel:`Close`
1. Attempt whatever is causing the problem a few times
1. Exit ED
1. Connect a USB cable to your phone and PC 
1. Allow access if the phone asks.
1. In some versions of Android you may also need to change the connection type on the phone from 'charging' to 'file transfer'
1. Open a file manager and find the connected phone
1. Browse down to the folder ``...\Internal shared storage\Android\data\jmri.enginedriver\files``
1. Find the most resent file that looks like ``logcatxxxxxxxxxxxxx.txt``     e.g. logcat1699833098998.txt
1. Attach that file to a message here in discord using the paperclip button on the toolbar above the message content

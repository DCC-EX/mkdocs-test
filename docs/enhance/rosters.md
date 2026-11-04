---
tags:
  - _▪J▪_▪R▪_▫locoid▫_▫name▫_▫functionMap▫
  - _▪J▪_▪R▪_▪SAVE▪
  - _▪J▪_▪R▪_▫id▫_▪DELETE▪
---

# Roster

The Roster is a list of loco DCC addresses, with names for convenience and a list of named/labelled function keys that are supported by each loco decoder.

## How to create a Roster

There are three ways to create or manipulate a roster

* [In a Web Browser](#roster-editing-with-a-web-browser)
* [In EXRAIL](#roster-in-exrail-as-per-previous-versions)
* [With Serial Commands](#roster-serial-commands)

----

## Roster Editing with a Web Browser

!!! note "Version 6.0 only"

    {{new_in_v(6.0)}} This capability is available to the **EX-CSB1** and DIY **EX-CommandStations** using ESP32 and NUCLEO microprocessors, running version 6.0, or later, **EX-CommandStation** software.  It is not available on the Arduino Mega.

When using a web browser dialog on the command station, the Config.. Roster Editor menu will show a roster editing dialog. This edits and saves roster entries in RAM.

Enter the IP address of the **EX-CommandStation** into the address bar of you browser. e.g. That will be ``192.168.1.4`` if you are using the default [Access Point](../prepare-to-use/installer/config-wifi-esp32.md#the-wifi-different-modes) mode.
Or use the Web Page in Engine Driver, after you have connected to the **EX-CommandStation**.

To find the IP address:

* If you have an OLED screen, it will tell you the IP address of the **EX-CommandStation**
* The Engine Driver app (and most other throttle apps) will tell you the IP address of the **EX-CommandStation** on the connection screen

![Engine driver](../_static/images/web-server/engine-driver-web1.png){ width=200px }

### Instructions

#### Accessing the Web Server

==TODO== VERY HIGH! - needs detailed instructions for Roster Editing with a Web Browser.

Using a PC Web Browser:

* Connect to the same SSID (WiFi network) that the **EX-CommandStation** is using.
* Open your web browser (Chrome, Firefox, Edge, Safari, etc.) and enter the IP address of the server (see the previous section) e.g. In will be ``192.168.1.4`` if you are using the default Access Point (AP) mode.

    Note: it is not normally necessary but you may need to prefix the IP address with ``http://``.  e.g. ``http://192.168.1.4``  
    Normally the web browser will automatically add this

    Note: the web browser may warn you that the connection is not secure. This is normal. Just tell it to proceed.

The initial web page should open:

![web browser](../_static/images/web-server/web-server1.png){ width=400px }

Using Engine Driver's Web page:

* Connect to the same SSID (WiFi network) that the **EX-CommandStation** is using.
* Connect to the **EX-CommandStation** from the list
* From the overflow menu (``≡`` or ``⋮``), select ``Web``

![Engine driver](../_static/images/web-server/engine-driver-web2.png){ width=200px }  ![Engine driver](../_static/images/web-server/engine-driver-web3.png){ width=200px }

The initial web page should open:

![web browser](../_static/images/web-server/web-server1.png){ width=400px }

#### Editing the Roster

* Click ``Configs`` then select ``Roster Editor``

![web browser](../_static/images/web-server/web-server2.png){ width=500px }

#### To add a New Roster Entry

* ???

#### Edit an Existing Roster Entry

* To edit an existing roster entry select the loco from the drop list
* ???

![web browser](../_static/images/web-server/web-server-roster1.png){ width=500px }

#### Changing the Function labels

* ???

![web browser](../_static/images/web-server/web-server-roster2.png){ width=500px }

#### Deleting a Roster Entry

* To delete a roster entry first select it from the drop list
* Click the ``Delete`` button.
* ???

![web browser](../_static/images/web-server/web-server-roster3.png){ width=500px }

#### Saving Your Changes

* To save the roster entries to ???...
* ???

----

### Roster in EXRAIL (as per previous versions)

Roster entries in EXRAIL are compiled into the command station and therefore are backward compatible with previous versions. On startup the **EXRAIL** ROSTER entries are loaded into RAM before any locally saved roster entries are loaded from non-volatile storage on the command station.

See the [EXRAIL Rosters](../enhance/exrail/exrail-objects-introduction.md#adding-a-roster) page for more information.

----

## Roster Serial Commands

!!! note ""

    {{new_in_v(6.0)}} Available in version 5.9.13 and above of **EX-CommandStation** only.

There are a selection of roster commands which are normally used by throttles to extract roster information from the command station.

`<JR>` returns a list of the DCC loco addresses in the roster, e.g.
`<jR 3 5 100>`

`<JR 100>` Returns details for DCC address 100 e.g.
`<jR 100 "Thomas" "Lights/*Whistle/Squeal">`
The functions are separated by '/' and a '*' prefix indicates that the function is momentary rather than toggled.
A request for a roster that does not exist (eg `<JR 999>`) is returned as `<jR 999 X>`

New Roster commands for v5.9.13 and above:

`<JR id "name" "functions">`  adds or replaces a roster in RAM.

`<JR id DELETE>`  removes a roster entry from ram.

`<JR SAVE>`  saves the current rosters in ram. They will be reloaded again at startup.

See the [Roster Serial Commands](../reference/serial-commands/serial-command-jj-rr_not_in_nav.md) reference page for more information.

See the [using a serial monitor](../reference/tools/serial-monitor.md) page for information and options on how and where to enter serial commands.

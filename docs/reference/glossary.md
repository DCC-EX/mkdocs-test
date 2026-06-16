---
search:
  exclude: true
---

# Glossary of Terms

These are common terms used throughout our documentation.

If you wish to see where a term is used, click the term name to search for it.

## Access Point (AP) Mode

[Search for Acccess Point Mode](?access point mode)

In Access Point (AP) mode, the tiny ESP-WiFi chip acts as a very basic WiFi server and provides a small IP network for your throttle or for your computer running JMRI with the WiThrottle Server enabled. It acts much like your router does to let things connect directly to it (currently up to four connections).
Using the Command Station in AP mode allows you to have a separate network so you can keep your layout network separate from your home network.

## Base Station, Command Station, DCC Command Station, DCC Base Station

See [https://dccwiki.com/Command_Station](https://dccwiki.com/Command_Station)

## Consist[^1], Multiple Unit[^2]

Multiple locos hauling a single train. See [https://dccwiki.com/Multiple_Unit_Consisting](https://dccwiki.com/Multiple_Unit_Consisting)

## DCC++ Commands, ``<DCC++>``, DCC++ Protocol, DCC++ API

Old name for the DCC-EX Serial Command / DCC-EX Native Commands / DCC-EX Native Protocol.
Some references to this still remain for backward compatibility. i.e. JMRI still refers to DCC++.

## DCC-EX Serial Commands, DCC-EX Native Commands, DCC-EX Native Protocol, DCC-EX Native API

New name for the DCC++ Commands/Protocol/API.
Refer to [DCC-EX Serial Command List](serial-command-list.md) for details.

## Pullup

[Search for pullup](?pullup)

The term pullup within the context of DCC-EX is commonly used when discussing inputs or sensors along with other topics such as I2C cabling. This is an electronics focused term, typically referring to the use of a resistor to ensure an input/sensor or I2C line is pulled up or held to a specific voltage (typically 3.3V or 5V).

## Pulldown

[Search for pulldown](?pulldown)

The term pulldown within the context of DCC-EX is commonly used when discussing inputs or sensors along with other topics such as I2C cabling. This is an electronics focused term, typically referring to the use of a resistor to ensure an input/sensor or I2C line is pulled down or held to ground or 0V.

You will also see search results for using a pulldown menu, but that is a different context!

## Roster

[Search for roster](?roster)

A roster is a list of locomotives that are known in advance by the command station so that DCC addresses, name, and functions can be used by throttles to configure buttons etc.  

## SSID

[Search for SSID](?ssid)

An SSID (Service Set Identifier) is the technical term for your WiFi network's name. It is the identifier your router broadcasts so nearby devices (like phones and laptops) can find and connect to the right network.

## Station (STA) Mode

[Search for Station Mode](?station mode)

Station Mode allows you to connect the Command Station to your existing home network.
The Command Station becomes a Station or Client rather than an Access Point.
That means instead of being a host that manages the IP of the smartphone that runs your Throttle, it becomes a station that connects to your existing network just like any of the other computers or devices connected to your network. The Throttle then connects to the Command Station by finding its IP address on the network.

## Turnout[^1] (Point[^2]/Switch)

[Search for turnout](?turnout)

In a prototypical railway, a turnout/point allows a train to diverge from one track to another. In DCC-EX terms, this term also denotes a software object that can control a physical turnout/point on your layout. A turnout/point can also be referred to as a point or a switch.

Depending on your region, turnouts/points are also commonly referred to as points or switches.

## VPIN

[Search for VPIN](?VPIN)

A VPIN is an Arduino pin number that has been extended to include pins on external devices or expanders. Once the mapping of VPIN numbers to devices has been done, the commands that set or test pins do not have to care how the electronics works.

## WiThrottle

1. Trademark owned by Brett Hoffman
2. Proprietary iOS app developed by Brett Hoffman.

## WiThrottle Protocol

A proprietary protocol developed by Brett Hoffman

## WiThrottle Server

A piece of software that listens and acts on WiThrottle commands
EX‑CommandStation contains a WiThrottle Server, as does JMRI

----

[^1]: Term primariarly used in North American railroading.
[^2]: Term used in most of the English speaking world other than North America. (British/United Kingdom origin)
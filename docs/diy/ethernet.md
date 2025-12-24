# Optionally install Ethernet

The standard Ethernet shields must be first in the stack as they use pins that are not passed through the headers of the motor shield. Look underneath the shield and this will become obvious. The shields also cause issues with their height, shields above may not sit level (but will still work) unless you introduce an extra row of header extenders.

<div style="clear: both;"></div>

## Arduino Network Shield 2

![Arduino Shield](/_static/images/ethernet/arduino_ethernet_shield_2.png){ align=right }
There have been different revisions for the Arduino Network Shields, the main difference is the version of the Wiznet chip on the board. The “2” board uses the Wiznet W5500, other versions used the older W5100 chip. The only supported chip currently is the W5500, but the other boards may work as well. The W5500 can handle 8 simultaneous socket connections while the W5100 can only handle 4.

This board also has an SDCard capability but it can't be used in the  EX‑CommandStation due to timing limitations.

<div style="clear: both;"></div>

## Wiznet WIZ850IO

![Wiznet](/_static/images/ethernet/WIZ850IO.png){ align=right }
This is a micro Ethernet board no bigger than the RJ45 connector it is attached to. You have to wire this with jumpers or solder it to a prototyping PCB.

<div style="clear: both;"></div>

## Sunfounder Ethernet Shield

![Sunfounder](/_static/images/ethernet/sunfounder_ethernet_shield.png){ align=right }
This board is tested and works. It is less expensive than the Arduino brand-name board and based on the Wiznet W5100 instead of the W5500.


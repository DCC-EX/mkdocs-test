---
tags:
    - _9D9_9ACK9_9MAX9_value_9MS9
    - _9D9_9ACK9_9MAX9_value
    - _9D9_9ACK9_9MIN9_value_9MS9
    - _9D9_9ACK9_9MIN9_value
    - _9D9_9ACK9_9OFF9
    - _9D9_9ACK9_9ON9
---
# Programming Tips

==TODO== Fill this page out. Also move the references from the old site

## *Hints and Tips*

### **Hornby HM7000 decoders**

The HM7000's DCC implementation has a bug in that the ACK response to a DCC CV read from the decoder on the programming track is far, far too long. So much so, the **DCC-EX** developers added a feature to cater specifically for the HM7000.

* Make sure the loco is on the PROG output which is typically channel B on the EX-CommandStation.
* Bring up a serial console to the EX-CommandStation, or use the command entry features in EX-Toolbox, EX-WebThrottle or Engine Driver.
* Type and send ``<1 PROG>`` to force the PROG track to power up early.
* Type and send ``<D ACK MAX 20000>``
* Then try reading the decoder. <br/>Either from the console with <R>, <br/>or with the appropriate buttons in EX-Toolbox, EX-WebThrottle or Engine Driver, <br/>to watch for a response.
* If this isn't working, then also add ``<D ACK MIN 150>``

If this isn't working, then ``<D ACK ON>`` will enable diagnostic output from the **EX-CSB1** to show what the <R> is doing.

You can also refer to the [RailSnail -DCC-EX and Hornby TTS Decoders – (No ACK!)](https://railsnail.uk/dcc-ex-and-hornby-tts-decoders-no-ack/?cn-reloaded=1) article for more information.

--8<-- "snippets/abbr.md"

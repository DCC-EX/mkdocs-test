---
search:
    boost: 2
tags:
    - _9D9_9ACK9_9MAX9_value_9MS9
    - _9D9_9ACK9_9MAX9_value
    - _9D9_9ACK9_9MIN9_value_9MS9
    - _9D9_9ACK9_9MIN9_value
    - _9D9_9ACK9_onoff
---
# CV Programming Tips

==TODO== LOW - Fill this page out.

## *Hints and Tips*

### General Programming Best Practices

1. **Use a Dedicated Programming Track (PROG):**
   Always test new or unknown decoders on the dedicated `PROG` track output of your EX-CommandStation rather than the main track (`MAIN`) to prevent unintended programming of other locomotives.

2. **Verify Acknowledgement (ACK):**
   Decoder CV reading relies on current-sensing pulses (ACK). If CV reading fails or returns `-1` / errors, check physical track contact and wheel cleanliness.

3. **Resetting to Factory Defaults:**
   Most, but not all, DCC decoders (including Hornby) can be reset to factory default settings by writing `8` to **CV8**. Power cycle the track after issuing a reset command.  
   Refer to your decoder manual to confirm that this is to correct way to reset it.

----

### Hornby HM7000 decoders

The HM7000's DCC implementation has a bug in that the ACK response to a DCC CV read from the decoder on the programming track is far, far too long. So much so, the **DCC-EX** developers added a feature to cater specifically for the HM7000.

!!! note "Dual-Mode Operation"
    Hornby HM7000 decoders can operate in both **Bluetooth (BLE)** mode via the Hornby HM | DCC app and standard **DCC mode**. When connected active to Bluetooth, DCC programming commands from your EX-CommandStation may be ignored or rejected.

* **Unlink/Disconnect Bluetooth for DCC Programming:**  
    To reliably read or write CVs over the DCC programming track (PROG) or main track (POM) with EX-CommandStation, ensure the decoder is not actively connected to the Hornby HM | DCC app on your mobile device. Close the app or disconnect the locomotive in the app before attempting DCC CV programming.
* Make sure the loco is on the `PROG` output which is typically channel B on the **EX-CommandStation**.
* Bring up a serial console to the EX-CommandStation, or use the command entry features in EX-Toolbox, EX-WebThrottle or Engine Driver.
* Type and send ``<1 PROG>`` to force the PROG track to power up early.
* Type and send ``<D ACK MAX 20000>``
* Then try reading the decoder. <br/>Either from the console with <R>, <br/>or with the appropriate buttons in EX-Toolbox, EX-WebThrottle or Engine Driver, <br/>to watch for a response.
* If this isn't working, then also add ``<D ACK MIN 150>``

If this isn't working, then ``<D ACK ON>`` will enable diagnostic output from the **EX-CSB1** to show what the <R> is doing.

#### Additional Notes

* **Power Cycle After Programming:**

    After updating CVs on an HM7000 decoder via DCC, perform a full power cycle (turn track power off and back on via your throttle or `EX-WebThrottle`) to ensure the decoder reloads and applies the new CV settings properly.

* **ACK / Current Pulse Sensing:**
  
    HM7000 sound decoders can draw higher current bursts during startup or acknowledgment pulses. If you experience `ACK` read timeouts during PROG track operations:

    * Ensure the programming track rails and locomotive wheels are clean.
    * Verify that track power limits on your EX-CommandStation motor shield are configured correctly for standard DCC acknowledgment pulses.

* You can also refer to the [RailSnail -DCC-EX and Hornby TTS Decoders – (No ACK!)](https://railsnail.uk/dcc-ex-and-hornby-tts-decoders-no-ack/?cn-reloaded=1) article for more information.

!!! tip "Hornby Bluetooth Firmware Updates"
    Always use the official **Hornby HM | DCC app** via Bluetooth to update the HM7000 decoder firmware to the latest release before configuring custom DCC CV settings.

#### Making the changes permanent

If you expect to be needing this often, you can add whatever commands you found worked for you, to your `myAutomation.h`.  e.g.

```c++
AUTOSTART
  PARSE("<D ACK MAX 20000>")
  PARSE("<D ACK MIN 150>")
DONE
```

--8<-- "snippets/abbr.md"

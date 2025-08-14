# Easy build - Arduino Mega

The instructions below detail the steps required to use an EX8874 motor shield.

**DO NOT USE ANY OTHER SHIELD TYPE WITHOUT FIRST CHECKING OUR DETAILED INSTRUCTIONS FOR THAT SHIELD.**

## What you need

To build a basic DIY Command Station in easy steps you will need:

- A PC or laptop (Not a Raspberry Pi) running a reasonably recent versions of Windows, Linux or macOS
- an Arduino Mega microprocessor or Elegoo clone.
- USB cable to your PC for the processor.
- an [EX-MotorShield8874](/products/ex-motorshield8874/ex-motorshield8874.md) to power the track.
- A double-insulated DC [power supply](/diy/10-power.md) with a voltage suitable for your layout/locos.
- (Optional) [EX-WiFiShield8266](/products/ex-wifishield8266/ex-wifishield8266.md) to use Wi-Fi throttles.

## Step-by-Step Build

### Prepare your Mega

1. Use sticky tape or similar to cover up the barrel connector on the Mega. (Power to the processor will be provided by the EX8874 shield and you don't want accidents.)

2. Use sticky tape or similar to cover the top of the USB connector on the mega. This prevents any accidental contact with the underside of the motor shield. ![connectors](/_static/images/mega/mega1.png)

3. Mount your Mega on 3d printed tray, a piece of plastic card or wood to make sure that the underside solder points are insulated. Placing your Command Station down on a tool, coin or even your track can short the pins and, in some cases, damage the board.

### Mount the EX8874 shield

**DO NOT USE ANY OTHER SHIELD TYPE WITHOUT FIRST CHECKING OUR DETAILED INSTRUCTIONS FOR THAT SHIELD.**

1. Make sure the pins are straight.
2. Line up the shield with the connectors at the same end as the mega and carefully insert the pins. This is easiest if you insert one side slightly first. Don’t force anything, there will be a visible gap  between the bottom of the motor board and the top of the headers.

Check your work. Look under and through where the boards connect, make sure no pins missed the holes and got bent so that they run along the outside of the headers.

![Mounted EX8874](/_static/images/mega/mega2.png)
![Mounted EX8874](/_static/images/mega/mega3.png)

### Optionally Install WiFiShield

1. Prepare your EX-WiFiShield8266 by removing the two jumpers, see picture. ![Wifi Jumpers](/_static/images/mega/mega4.png)
2. Mount the Wi-Fi shield on the EX8874 noting the correct orientation in the pictures and there will be 2 pins on either side which are deliberately missing.![Wifi shield](/_static/images/mega/mega5.png)
3. Use a male-female Dupont wire (normally supplied with the shield) to connect to any one of the row of Tx pins on the Wi-Fi Board, and connect the other end to the Rx1 pin on the mega (pin 19). See photo below.
4. Take a second jumper wire and connect it to any one of the row of Rx pins on the Wi-Fi Board and connect the other end to Tx1 on the mega (pin 18).![txrx](/_static/images/mega/mega6.png)
5. Use a small piece of sticky tape or similar to keep the Dupont wires firmly in place in the mega header sockets. They are easily knocked out.  

### Connect your power supply

We recommend you label the power supply so that it does not get confused with others of different voltages you may use later. Plug in to the barrel connector on the EX8874 shield (NOT the Mega).

### Connect to your PC

Using a suitable USB cable (must carry Data and Power, not all cables do this!) connect the Mega USB to your PC.

### Connect your track

The EX8874 track connectors unplug for easy access.
    If you only have one piece of track for testing, wire it to the PROG track plug.

 1. Your PROG track is wired to the green socket closest to the power barrel connector.
 2. The MAIN track is wired to the far connector.

![CONNECTIONS](/_static/images/mega/mega7.png)

### Load the software

Congratulations, you have built a DIY command station the easy way. But you still have to load the software.

For simplicity, software loading is best done with the [EX-Installer](80-installer.md)

# Selecting a power supply

You will require a power supply unit to provide track power and to run the **EX-CommandStation** processor.

## Volts and Amps

The volt and current requirements for your track vary according to the scale of your locos and the number you expect to run simultaneously.

These recommendations are generalised, and you must check to make sure they don't exceed your loco and DCC decoder manufacturer's recommendations.

| **Scale**     | **Recommended Voltage (DC)** | **Minimum Current (Amps)**  | **Notes**                                                                 |
|---------------|------------------------------|-----------------------------|---------------------------------------------------------------------------|
| Z (1:220)     | 10–12V                       | 2A                          | Lower voltage protects tiny motors; avoid exceeding 12V.                  |
| N (1:160)     | 12V                          | 3A                          | Most decoders rated for ~14V max; higher voltages increase brush wear.    |
| TT (1:120)    | 12–14V                       | 3–4A                        | Slightly more headroom than N scale.                                      |
| HO (1:87)     | 14–15V                       | 4–5A                        | Common sweet spot for DCC; 15V is typical for DCC-EX setups.              |
| OO (1:76)     | 15V                          | 4–5A                        | Similar to HO; check decoder specs.                                       |
| S (1:64)      | 15–16V                       | 5A                          | Larger motors can handle more voltage.                                    |
| O (1:48)      | 16–18V                       | 5–6A                        | Ensure decoder supports higher voltage; some cap at 18V.                  |
| G (1:22.5)    | 18–22V                       | 6A+                         | Outdoor locos often need more torque and current.                         |

## Track Voltage VS Power Supply Voltage

Not all Motor Drivers are equal!

For the **EX-CSB1** and the **EX-8874** the DC voltage of the power supply that you use, will be very close to the quasi-AC voltage that will be provided to the track.

For the Arduino Motor Shield, the DEEK Motor Shield and most others, the quasi-AC voltage on the track will be 1.5-2v *less than* the voltage of the power supply. So for those motor drivers, it is necessary to use a power supply about 2vDC greater than you want on the track.

## Using an EX8874 or EX-CSB1

The EX8874 (which is also built into the EX-CSB1) provides power for both the track and the **EX-CommandStation**. There is almost zero voltage drop between the power supply and the track.

We strongly advise purchasing a suitable power supply at the same time as the CSB or EX8874 from a vendor who understands your requirements.

## Other motor shields

Should you choose a motor-shield other than the **EX-8874**:

- You must allow for the voltage drop within your chosen shield. (see [above](#track-voltage-vs-power-supply-voltage))
- You must provide separate power for the **EX-CommandStation** microcontroller:
    - Most easily this is done via the USB socket. A standard phone charger, or a connection to a computer, will be adequate. Note that if you are powering other devices connected directly to the GPIOs (including a WiFi shield), the USB socket may not provide adequate power.
    - If you power the microcontroller through its barrel connector, you need to use a 7-9vDC power supply, not the 5v you might expect. Do not exceed 9vDC as this can cause electrical interference.
- Note: You may not be protected from reverse-polarity mistakes.

## What to look for

![Power brick](/_static/images/power/powerbrick.png){ align=right }

Typically, retired or replacement laptop power supply bricks are suitable and readily available. You need to check their markings:

- Volts and Amps suitable for your trains and layout (see above)
- Double square safety markings.
- Plug polarity indicator, center positive.

<div style="clear: both;"></div>

## SAFETY WARNING

![DANGEROUS](/_static/images/power/dangerous.png){ align=right }

A Command Station is NOT a typical consumer electronics device where the user is never in contact with any bare wire of any voltage.  Your track is effectively a large bare wire that will be touched frequently.

You MUST use a suitable, double insulated, power supply where it is not possible for a loose wire or stray flexi-track clipping from your model building to fall in and bridge the gap between mains voltage and the output.

Should this happen, it could melt your electronics, locos or children.

--8<-- "snippets/abbr.md"

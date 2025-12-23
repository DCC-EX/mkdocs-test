# Selecting a power supply

You will require a power supply unit to provide track power and to run the Command Station processor.

## Volts and Amps

The volt and current requirements for your track vary according to the scale of your locos and the number you expect to run simultaneously.

These recommendations are generalised, and you must check to make sure they don't exceed your loco and DCC decoder manufacturer's recommendations.

| **Scale**     | **Recommended Voltage (DC)** | **Minimum Current (Amps)** | **Notes**                                                                 |
|---------------|------------------------------|-----------------------------|---------------------------------------------------------------------------|
| Z (1:220)     | 10–12V                       | 2A                          | Lower voltage protects tiny motors; avoid exceeding 12V.                  |
| N (1:160)     | 12V                          | 3A                          | Most decoders rated for 12V max; higher voltages increase brush wear.     |
| TT (1:120)    | 12–14V                       | 3–4A                        | Slightly more headroom than N scale.                                      |
| HO (1:87)     | 14–15V                       | 4–5A                        | Common sweet spot for DCC; 15V is typical for DCC-EX setups.              |
| OO (1:76)     | 15V                          | 4–5A                        | Similar to HO; check decoder specs.                                       |
| S (1:64)      | 15–16V                       | 5A                          | Larger motors can handle more voltage.                                    |
| O (1:48)      | 16–18V                       | 5–6A                        | Ensure decoder supports higher voltage; some cap at 18V.                  |
| G (1:22.5)    | 18–22V                       | 6A+                         | Outdoor locos often need more torque and current.                         |

## Using an EX8874 or CSB1

The EX8874 (which is also built in to the CSB1) provides power for both the track and the Command Station. There is almost zero voltage drop between the power supply and the track.

We strongly advise purchasing a suitable power supply at the same time as the CSB or EX8874 from a vendor who understands your requirements.

## Other motor shields

Should you have the temerity to choose a motor-shield other than the EX8874:

- you must allow for the voltage drop within your chosen shield.
- you must provide separate power for the Command Station processor, most easily via the USB socket. A standard phone charger, or a connection to a computer, will be adequate. Other options are significantly more complex.
- you may not be protected from reverse-polarity mistakes.

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

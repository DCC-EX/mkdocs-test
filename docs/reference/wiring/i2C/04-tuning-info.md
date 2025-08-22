# I2C Tuning Summary

This is an introductory guide for tinkerers, which may help many to quickly get an overview of the main points and hopefully can be followed by most with a few minutes effort.

# Guide to tuning a standard mode (100kHz) I2C bus:

1. The two signal lines (SCL & SDA) EACH require a resistor to pull them to a logic high voltage and a device output pin to pull them low.  
    All devices on an I2C bus segment must use the correct voltage level.  
    i.e. 5V (or 3.3V) supply voltage to all pull-up resistors (typically 10k ohms included on each I2C device).

2. Do NOT mix incompatible 3.3V and 5V devices on a segment (without a passive level-shifter).  
    The segment (or sub-bus) is the full wire length from extremities, passing through some devices - end-to-end (e.g. PCA9685), but NOT through a multiplexer (mux) or bus buffers. (A mux or level shifter can interface different sub-buses/segments).

3. Connected devices may, or may not, have a (weak) pullup resistor (pair) on them, typically 10k ohms.  
    We need to add up the number of 10k (pairs) of resistors to see if we need to add/remove some.  (Alternatively, see NOTE below about measuring this in situ.)

4. The pull-up has to be neither too strong (output pins can't pull it down) nor too weak (resistor can't pull
it up fast enough).

5. The MAXIMUM number (of 10k ohm pullups) that the (SCL or SDA) output pin can pull down is about 6 (9 on a 3.3V bus), so we MAY have to disconnect some pullups (jumpers?) or use a mux.

6. Some devices may not have any pullups, and other devices may EFFECTIVELY have 2 or 3 (4.7k Endpoint = 2x10k)

7. The load the resistors have to drive depends on the NUMBER OF DEVICES and the total LENGTH of the segment
wire/cable (passing through some devices) between bus segment ends.

8. The required minimum NUMBER(P) of 10k pullups on SCL must not be less than (number of devices(D) on bus +
length(L feet) divided by 3. i.e. P = (D + L)/3   This ensures the signal can rise quickly to a good high level.

9. Inversely, allowable max LENGTH(ft) = number of pullups(P) x 3 - number of devices(D) i.e. L = Px3 - D.  
    The practical length varies somewhat with cable type (twisted pair, ribbon, dupont, etc.) so limit your
segment length, say 2/3 of max., to avoid errors and timeouts.

10. If number of available pullups is too low, extra pullups (max 6 @10cents each)(or a LTC4311, $10) may be
added for length, BUT if number of pullups is TOO HIGH the only quick fix is to remove/cut jumpers/unsolder some pullups.  
    &nbsp;  
    NOTE:  If unsure of the effective number of active pullup resistors(10k), it is possible, after ALL POWER OFF
    FOR SEVERAL MINUTES, to use an ohm meter to measure the net resistance between the SCL line (or SDA) to the
    pullup supply rail (Vcc).  Divide 10k by the resistance for the effective number of pullups.  
    (e.g. if it measures 2500 ohms, there are effectively 4 pullups in the circuit)  
    (Do not use any diode test function or continuity test function on the meter, just basic resistance range.)

## EXAMPLES:

    [for length(L), pullup count(P) & device count(D)]

A. Mega bus:   3 Devices: Mega(10k), 1x MCP23017(10k) and one sparkfun Endpoint (with jumpers cut; no pullups)  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 2x3-3 = 3ft (safe 2ft)

B. Mega bus:   7 Devices: Mega(10k), 3x MCP23017(10k), 2x PCA9685(10k) & Endpoint(4k7)  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Pullups P = 8 (8x10k) too high!  Can cut Endpoint jumpers to remove 2. Then...  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 6x3-7 = 11ft (safe 7ft)

C. MUX sub-bus:4 Devices: Mux (no 10k) and 3x MCP23017(10k each)  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 3x3-4 = 5ft (safe 3.5ft)

D. MUX sub-bus:2 Devices: Mux (no 10k) and a single PCA9685(10k)  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 1x3-2 = 1ft (safe 8inch)

E. Remote bus: 3 Devices: Endpoint (4k7=2x10k) and 2x esp32 slaves(no k)  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 2x3-3 = 3ft (safe 2ft)

F. Remote bus: 3 Devices+extras: Endpoint (4k7=2x10k), 2x esp32 and EXTRA 4k7(2x10k)  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 4x3-3 = 9ft (safe 6ft)

G. To achieve 400kHz fast-mode use Px1.5 e.g. example F. (with 4 effective pullups)  
         &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 1.5 - D = 4x1.5 - 3 = 3ft (safe 2ft)

- In all cases, to increase workable length or speed, add pullups towards the max. number, or add one LTC4311 I2C Accelerator, provided P is not over the max. allowed pullup count.  

- LTC4311 detects a rising edge and injects a strong, current-limited pull-up current to quickly charge the bus capacitance. This actively accelerates the rise time, producing a cleaner, faster signal without compromising the signal's ability to be pulled low.

- **Note:** LTC4311 to be placed at the head of the chain, not the tail.

- If you decide you need extra pullups for length, it is a good idea to be generous and add "spare" pullups (i.e. use a lower value resistor) while keeping within the max count(6/9), as this will give extra safety margins and noise immunity at no extra cost.

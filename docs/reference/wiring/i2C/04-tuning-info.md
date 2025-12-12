
# Tuning an I2C Bus for the Engineer

## Guiding Principles

1. **The two signal lines (SCL & SDA) EACH require a resistor to pull them to a logic high voltage and a device output pin to pull them low.**  
  All devices on an i2c bus segment should use the same voltage level. (exception: passive level-shifers)  
  i.e. 5V (or 3.3V) supply voltage to all pull-up resistors (typically 10k ohms each).

2. **Do NOT mix incompatible 3.3V and 5V devices on a segment (without a passive level-shifter).**  
  The segment(or sub-bus) is the full wire length  from extremities passing through some devices end-to-end (e.g. PCA9685) but NOT through a multiplexer(mux) or bus  buffers (A mux or level shifter can interface different sub-buses/segments).

3. **We need to add up the number of 10k (pairs) of resistors to see if we need to add/remove some.**  
  Connected devices may, or may not, have a (weak) pullup resistor (pair) on them, typically 10k ohms.  
  (alternatively, see NOTE below about measuring this number in situ)

4. **The pull-up has to be neither too strong (output pins can't pull it down) nor too weak.**  
  (resistor can't pull it up enough)

5. **The MAXIMUM number (of 10k ohm) that the (SCL or SDA) output pin can pull down is about 6 (5V bus)**  
  (max 9 on a 3.3V bus) so we MAY have to disconnect some pullups (jumpers?) or use a MUX.

6. **Some devices may not have any pullups, and other devices may EFFECTIVELY have 2&nbsp;or&nbsp;3.**  
  (e.g 4.7k Endpoint pullup = 2x10k)

7. **The load the resistors have to drive depends on the NUMBER OF DEVICES and the total segment LENGTH.**  
  (The full segment wire/cable length, passing through some devices, between the bus segment extremities.)

8. **The MINIMUM required NUMBER\(P\) of 10k pullups on SCL must not be less than...**  
  (number of devices(D) on bus + length(L feet)) all divided by 3.  
  &nbsp; &nbsp; i.e.&nbsp;**min.&nbsp;P&nbsp;=&nbsp;(D&nbsp;+&nbsp;L)/3**  
  This ensures the signal can rise quickly to a good high level.  
  Adding spare pullups, up to max.(6/9), is recommended and gives better length & noise margins.

9. **Inversely, MAXIMUM LENGTH(L ft) must not exceed..**  
  number of pullups\(P\) x 3 - number of devices(D)  
  &nbsp; &nbsp; i.e.&nbsp;**max.&nbsp;L&nbsp;=&nbsp;Px3&nbsp;-&nbsp;D**  
  The practical length varies somewhat with cable type (twisted pair, ribbon, dupont, etc.) so limit your segment length below 2/3 of max., to avoid errors and timeouts.

10. **If number of available pullups is too low, extra pullups (max 6 @10cents each)(or a LTC4311, $10) may be added for length & noise margins, up to the limit, BUT..**  
  if number of pullups is TOO HIGH the only quick fix is to remove/cut jumpers/unsolder some pullups.

## Measurement in situ

**Note:  If unsure of the effective number of active pullup resistors(10k), it is possible, after ALL POWER OFF FOR SEVERAL MINUTES, to use an ohm meter to measure the net resistance between the SCL line (or SDA) to the pullup supply rail (Vcc).**  
**Divide 10k (10000) by the resistance for the effective number of pullups.**  
&nbsp; (e.g. if measure 2500ohm then effectively 4 pullups currently on the bus)  
&nbsp; (Do not use any diode test function or continuity test function on the meter, just basic resistance range.)

## Examples

**A. Mega bus**   4 Devices: Mega(10k), display(10k), PCA9685(10k) and a sparkfun Endpoint(4k7=2x10k)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 5x3 - 4 = 11ft (safe 7ft)

**B. Mega bus:**   7 Devices: Mega(10k), 2x PCA9685(10k), 3x MCP23017(10k), & Endpoint(4k7=2x10k)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Pullup count P = 8 (8x10k) too high!  Can cut Endpoint jumpers to remove 2. Then...  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 6x3 - 7 = 11ft (safe 7ft)

**C. MUX sub-bus:** 2 Devices: Mux (no P) and a single PCA9685(10k)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 1x3 - 2 = 1ft (safe 0.66ft) (use extra pullup for more length)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 2x3 - 2 = 4ft (safe 2.7ft)  (includes an extra 1x10k(pair) on end)

**D. MUX sub-bus:** 5 Devices: Mux (no P) 2xPCA9685(10k) & 2xMCP23017(10k)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 4x3 - 5 = 7ft (safe 4ft)    (add 1 or 2 extra P for 5ft)

**E. Remote bus:** 3 Devices: 1x Endpoint(4k7=2x10k), 1x MCP23017(10k) & 1x PCA9685(10k)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 4x3 - 3 = 9ft (safe 6ft)

**F. Remote bus:** 3 Devices+extras: Endpoint (4k7=2x10k), 2xESP32(no P) with EXTRA 4k7(=2x10k)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 3 - D = 4x3 - 3 = 9ft (safe 6ft)

**G. To achieve 400kHz fast-mode** use Px1.5 e.g. example F. (with 4 effective pullups)  
    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; max length L = P x 1.5 - D = 4x1.5 - 3 = 3ft (safe 2ft)

**In all cases, to increase workable length, noise margin or speed, add pullups towards the max. number, OR add one LTC4311 I2C active pullup at the CS end, provided P is not over the max. allowed pullup count.**  With an LTC4311, max pullups(6/9) are NOT recommended.  A limit of 3P is advised, especially with MCP23017's.

![I2C Examples](/_static/images/i2c-devices/i2c-devices-example01.png)

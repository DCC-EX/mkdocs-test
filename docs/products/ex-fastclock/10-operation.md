# Operation

At startup the clock will calculate a start time based on either a) a coded start time (currently 6:00 a.m.) or b) a run time stored in the EEPROM (see item 2) below.

The clock will start in a paused state and will display the speed rate factor (default = x 4).  Once any adjustments have been made the clock can be started.  The usage of the six buttons are as below:

1. **Start** - Pressing this button will start the clock and the button text will change to **Pause**.  
2. **Save** - Pressing this button will pause the clock and save the current time and Speed Factor to the EEPROM.  These figures will be used to initialise the clock on next startup.
3. **Reset** - Pressing this button will pause the clock and set the time to 06:00 with a speed factor of 4.
4. **T+** - Pressing this key will pause the clock and add 15 minutes to the time.
5. **T-** - Pressing this key will pause the clock and deduct 15 minutes from the time.
6. **Rate** - Pressing this key will increase the speed factor to the next level.  The speed factor will cycle around the seven speed settings of 1, 2, 4, 6,, 8, 12 & 30.

In Serial Mode, at startup the initial clock time will be sent to the Command Station but when in a paused state no further time commands are sent until the START button is pressed.

In I2C mode the Command Station polls the FastClock at intervals.

# Grouped DCC-EX EXRAIL Command Reference

Reference guide for EXRAIL commands used by **EX-CommandStations**, shown in functional groups.

!!! warning "This list may not be complete"

    This list of commands is manually created and may lag behind the latest developments.  Refer to the [Full Command List](../exrail-command-reference.md) for the up-to-date list of commands.

!!! warning "Deprecated Commands"
    Commands marked with ⚠️ are deprecated and may be removed in future versions. Use the recommended alternatives where available.

--8<-- "snippets/exrail/exrail-intro.md"

<style>
.md-typeset table:not([class]) {
    width: 100% !important;
    display: table;
    table-layout: fixed;
}

.md-typeset table:not([class]) tr th:first-child,
.md-typeset table:not([class]) tr td:first-child {
  width:30% !important;
}

.md-typeset table:not([class]) tr th:nth-child(2),
.md-typeset table:not([class]) tr td:nth-child(2) {
  width:30%  !important;
}
.md-typeset table:not([class]) tr th:nth-child(3),
.md-typeset table:not([class]) tr td:nth-child(3) {
  width:25%  !important;
}
.md-typeset table:not([class]) tr th:nth-child(4),
.md-typeset table:not([class]) tr td:nth-child(4) {
  width:15%  !important;
}
</style>

## General

| Command | Description |
| ------- | ----------- |
| [ALIAS( name \[, value\])](?ALIAS) | Assigns name to a value. `value` is optional. If omitted, a large negative value is created automatically |

----

## Flow Control

| Command | Description |
| ------- | ----------- |
| [AUTOSTART](?AUTOSTART) | Automatically start sequence at this point during EX-CommandStation startup |
| [AUTOMATION( id, "description" )](?AUTOMATION) | Define an automation, advertised to throttles/clients |
| [ROUTE( id, "description" )](?ROUTE) | Define a route, advertised to throttles/clients |
| [SEQUENCE( id )](?SEQUENCE) | A general purpose sequence, not advertised to throttles/clients |
| [DONE](?DONE) | Completes a Sequence/Route/Animation/Event, or any other automation |
| [ENDTASK](?ENDTASK) | Completes a Sequence/Route/Animation/Event, or any other automation |
| [CALL( id )](?CALL) | Branch to a separate sequence, which will need to RETURN when complete. The current sequence is paused until the called sequence has completed. |
| [RETURN](?RETURN) | Return to the calling sequence when completed |
| [FOLLOW( sequence_id )](?FOLLOW) | Branch or Follow a specified sequence.  The current sequence ends and control is passed to the specified sequence. |
| [PAUSE](?PAUSE) | E-STOP all locos and PAUSE all other EXRAIL tasks |
| [RESUME](?RESUME) | Resume all paused tasks, including loco movement |
| [START( id )](?START) | Execute a route or sequence |
| [START_SEND( id )](?START_SEND) | Execute a route or sequence and send the current loco |
| [START_SHARED( id )](?START_SHARED) | Execute a route or sequence and pass the current loco |
| [SENDLOCO( loco, route )](?SENDLOCO) | Start route/sequence with a specified loco |
| [DELAY( delay )](?DELAY) | Delay the sequence a number of milliseconds |
| [DELAYMS( delay )](?DELAYMS) | Delay the sequence a number of milliseconds |
| [DELAYMINS( delay )](?DELAYMINS) | Delay the sequence a number of minutes |
| [DELAYRANDOM( min_delay, max_delay )](?DELAYRANDOM) | Delay a random period of time |
| [RANDWAIT( ??? )](?RANDWAIT) | TBA |
| [IFRANDOM( percent )](?IFRANDOM) | Run commands a random percentage of the time |
| [ROUTE_CAPTION( route_id, "caption" )](?ROUTE_CAPTION) | Change the label of the Route button |
| [ROUTE_ACTIVE( route_id )](?ROUTE_ACTIVE) | Activate a Route |
| [ROUTE_INACTIVE( route_id )](?ROUTE_INACTIVE) | Deactivate a Route |
| [ROUTE_HIDDEN( route_id )](?ROUTE_HIDDEN) | Hide a Route from display |
| [ROUTE_DISABLED( route_id )](?ROUTE_DISABLED) | disable a Route |
| [STASH( stash_id )](?STASH) | Stashes the current loco/invert |
| [CLEAR_STASH( stash_id )](?CLEAR_STASH) | Zeroes the specified stash |
| [CLEAR_ALL_STASH](?CLEAR_ALL_STASH) | Zeroes all stashes |
| [PICKUP_STASH( stash_id )](?PICKUP_STASH) | Retrieves and sets the loco/invert from the specified stash |

----

<br/>

----

## Objects: Definition and Control

### Create and manage HAL device objects

| Command | Description |
| ------- | ----------- |
| [HAL( device, parameters )](?HAL) | Create a HAL device in myAutomation.h |
| [HAL_IGNORE_DEFAULTS](?HAL_IGNORE_DEFAULTS) | Disable default MCP23017 and PCA9685 HAL devices |

----

### Signal Objects: Definition and Control

| Command | Description |
| ------- | ----------- |
| [SIGNAL( red_pin, amber_pin, green_pin )](?SIGNAL) | Define a pin based signal |
| [SIGNALH( red_pin, amber_pin, green_pin )](?SIGNALH) | Define a pin based signal with active high pins |
| [SERVO_SIGNAL( vpin, red_pos, amber_pos, green_pos )](?SERVO_SIGNAL) | Define a servo based signal |
| [DCC_SIGNAL( id, addr, sub_addr )](?DCC_SIGNAL) | Define a DCC accessory signal |
| [DCCX_SIGNAL( Address, redAspect, amberAspect, greenAspect )](?DCCX_SIGNAL) | Defines a signal (with id as dcc address) |
| [VIRTUAL_SIGNAL( id )](?VIRTUAL_SIGNAL) | Define a virtual signal |
| [IFRED( signal_id )](?IFRED) | Test if signal is red |
| [IFAMBER( signal_id )](?IFAMBER) | Test if signal is amber |
| [IFGREEN( signal_id )](?IFGREEN) | Test if signal is green |
| [GREEN( signal_id )](?GREEN) | Set a defined signal to GREEN |
| [AMBER( signal_id )](?AMBER) | Set a defined signal to Amber |
| [RED( signal_id )](?RED) | Set defined signal to Red |
| [ASPECT( address, aspect )](?ASPECT) | Command for DCC Extended Accessories |
| [ONGREEN( signal_id)](?ONGREEN) | Define event handler for when a signal is set to the green |
| [ONAMBER( signal_id)](?ONAMBER) | Define event handler for when a signal is set to the amber |
| [ONRED( signal_id)](?ONRED) | Define event handler for when a signal is set to the red aspect |

----

### Turnout/Point Objects: Definition and Control

| Command | Description |
| ------- | ----------- |
| [TURNOUT( turnout_id, addr, sub_addr \[, "description"\]\|HIDDEN )](?TURNOUT) | Define a DCC accessory turnout/point |
| [TURNOUTL( turnout_id, addr \[, "description"\]\|HIDDEN )](?TURNOUTL) | Define a DCC accessory turnout/point |
| [PIN_TURNOUT( turnout_id, pin \[, "description"\]\|HIDDEN )](?PIN_TURNOUT) | Define a pin operated turnout |
| [SERVO_TURNOUT( turnout_id, pin, active_angle, inactive_angle, profile [, "description"]\|HIDDEN )](?SERVO_TURNOUT) | Define a servo turnout/point |
| [VIRTUAL_TURNOUT( turnout_id [, "description"]\|HIDDEN )](?VIRTUAL_TURNOUT) | Define a virtual turnout, which is backed by another automation sequence |
| [IFCLOSED( turnout_id )](?IFCLOSED) | Test if a turnout/point is closed |
| [IFTHROWN( turnout_id )](?IFTHROWN) | Test if a turnout/point is thrown |
| [ONCLOSE( turnout_id )](?ONCLOSE) | Event handler for when a turnout/point is closed |
| [ONTHROW( turnout_id )](?ONTHROW) | Event handler for when a turnout/point is thrown |
| [CLOSE( turnout_id )](?CLOSE) | Close a turnout/point |
| [THROW( turnout_id )](?THROW) | Throw a turnout/point |
| [TOGGLE_TURNOUT( turnout_id )](?TOGGLE_TURNOUT) | Toggle a defined turnout/point between CLOSE/THROW |

*Parameters:*  

- **turnout_id** - unique Id for the turnout/point servo  
- **pin** - vpin to which the servo is attached  
- **active_angle** - the PWM value corresponding to the servo position for THROWN state, normally in the range 102 to 490  
- **inactive_angle** - the PWM value corresponding to the servo position for CLOSED state, normally in the range 102 to 490  
- **profile** - one of  
    - `Instant` = Instant,  
    - `Fast` = Fast (0.5 sec),  
    - `Medium` = Medium (1 sec),  
    - `Slow` = Slow (2 sec) and  
    - `Bounce` = Bounce (subject to revision)  
- **description** - The description that will be assigned to the turnout/point, or  
- *HIDDEN* - keyword - if used instead of the "description" the Turnout/point will not appear in the lists sent to throttle/controllers

----

### Turntable/Traverser Objects: Definition and Control

| Command | Description |
| ------- | ----------- |
| [MOVETT( id, steps, activity )](?MOVETT) | Move a EX‑Turntable to a step position and perform an activity |
| [IFRE ( vpin, value )](?IFRE) | Test if a rotary encoder has been set to a value |
| [ONCHANGE( vpin )](?ONCHANGE) | Detects a rotary encoder has changed position |
| [Turntable features](?Turntable) | |
| [DCC_TURNTABLE( id, home_angle, [, "description"] )](?DCC_TURNTABLE) | Define a DCC accessory turntable/traverser |
| [EXTT_TURNTABLE( id, vpin, home_angle, [, "description"] )](?EXTT_TURNTABLE) | Define an EX-Turntable turntable/traverser |
| [TT_ADDPOSITION( id, position_id, value, angle [, "description"] )](?TT_ADDPOSITION) | Add a turntable position |
| [IFTTPOSITION( id, position )](?IFTTPOSITION) | Test if turntable/traverser is at a position |
| [ONROTATE( id )](?ONROTATE) | Event handler for when a turntable/traverser is rotated |
| [ROTATE( id, position, activity )](?ROTATE) | Rotate an EX-Turntable turntable/traverser |
| [ROTATE_DCC( id, position )](?ROTATE_DCC) | Rotate a DCC accessory turntable/traverser |
| [WAITFORTT( id )](?WAITFORTT) | Wait for EX-Turntable turntable/traverser to complete a rotation |

----

### Sensors/Inputs: Reading and Responding

| Command | Description |
| ------- | ----------- |
| [JMRI_SENSOR(vpin [,count])](?JMRI_SENSOR) | Creates <S> type sensors visible to JMRI |
| [AT( vpin )](?AT) | Causes a sequence to wait until a sensor is active/triggered |
| [AFTER( vpin )](?AFTER) | Causes a sequence to wait until after a sensor has been triggered |
| [ATTIMEOUT( vpin, timeout_ms )](?ATTIMEOUT) | Causes a sequence to wait until either a sensor is active/triggered, or if the timer runs out |
| [IF( vpin )](?IF) | If sensor activated or latched, continue |
| [IFNOT( vpin )](?IFNOT) | If sensor NOT activated and NOT latched, continue |
| [IFTIMEOUT](?IFTIMEOUT) | Tests if “timed out” flag has been set by an ATTIMEOUT() sensor reading attempt |
| [ATGTE( vpin, value )](?ATGTE) | Waits for an analog pin to reach a value |
| [ATLT ( vpin, value )](?ATLT) | Waits for an analog pin to go below a value |
| [IFGTE( vpin, value )](?IFGTE) | Test if analog pin reading is greater than or equal to value |
| [IFLT( vpin, value )](?IFLT) | Test if analog pin reading is less than value |
| [ATTIMOUT1 ( vpin, value )](?ATTIMOUT1) | TBA |
| [ATTIMOUT2 ( vpin, value )](?ATTIMOUT2) | TBA |
| [DRIVE ( vpin )](?DRIVE) | TBA |
| [LATCH( vpin )](?LATCH) | Latches a sensor on |
| [UNLATCH( vpin )](?UNLATCH) | Remove LATCH on sensor |
| [ONBUTTON( vpin )](?ONBUTTON) | Event handler for debounced button presses |
| [ONSENSOR( vpin )](?ONSENSOR) | Event handler for sensors |

*Parameters:*

- `vpin` - The VPin the encoder is connected to. <br/>A negative value for a vpin can be used for an active high sensor.|BR| > value - value to test

----

### Output and LED control

| Command | Description |
| ------- | ----------- |
| [SET( vpin [,count] )](?SET) | Set an output pin HIGH |
| [RESET( vpin [,count] )](?RESET) | Reset output pin |
| [FADE( vpin, value, ms )](?FADE) | Fade an LED |
| [BLINK( vpin, onMs, offMs )](?BLINK) | Blink an output pin |
| [LCN( "msg" )](?LCN) | Send message to LCN Accessory Network |
| [CONFIGURE_SERVO(vpin, pos1, pos2, profile)](?CONFIGURE_SERVO) | Define LED’s connected to PCA9685 boards |
| [NEOPIXEL( vpin, red, green, blue [,count] )](?NEOPIXEL) | Controls the colour of attached Neopixel LEDs |
| [NEOPIXEL_SIGNAL( signalid, red, green, blue )](?NEOPIXEL_SIGNAL) | Controls the colour of attached Neopixel LED |
| [ANOUT( vpin, value, param1, param2)](?ANOUT) | Writes to the HAL analog output interface of a device driver |
| [PLAYSOUND( vpin, fileNumber, volume )](?PLAYSOUND) | Play mp3 files from a Micro-SD card |

----

### Servo Control

| Command | Description |
| ------- | ----------- |
| [SERVO( id, position, profile )](?SERVO) | Move an animation servo |
| [SERVO2( id, position, duration )](?SERVO2) | Move an animation servo taking duration |
| [WAITFOR( pin )](?WAITFOR) | Wait for a servo motion to complete prior to continuing |

*Parameters:*  

- **id** - id of the servo to move  
- **position** - position to move to  
- **profile** - one of  
    - **Instant** = Instant,  
    - **Fast** = Fast (0.5 sec),  
    - **Medium** = Medium (1 sec),  
    - **Slow** = Slow (2 sec) and  
    - **Bounce** = Bounce (subject to revision)

----

### DCC Accessory Decoder Control

| Command | Description |
| ------- | ----------- |
| [ONACTIVATE( addr, sub_addr )](?ONACTIVATE) | Event handler for 2 part DCC accessory packet value 1 |
| [ONACTIVATEL( linear )](?ONACTIVATEL) | Event handler for linear DCC accessory packet value 1 |
| [ONDEACTIVATE( addr, sub_addr )](?ONDEACTIVATE) | Event handler for 2 part DCC accessory packet value 0 |
| [ONDEACTIVATEL( linear )](?ONDEACTIVATEL) | Event handler for linear DCC accessory packet value 0 |
| [ACTIVATE( addr, sub_addr )](?ACTIVATE) | Sends a DCC accessory packet with value 1 |
| [ACTIVATEL( linear )](?ACTIVATEL) | Sends a DCC accessory packet with value 1 to a linear address |
| [DEACTIVATE( addr, sub_addr )](?DEACTIVATE) | Sends a DCC accessory packet with value 0 |
| [DEACTIVATEL( addr )](?DEACTIVATEL) | Sends a DCC accessory packet with value 0 to a linear address |
| [DCCACTIVATE( addr, sub_addr )](?DCCACTIVATE) | TBA |

----

### EX-FastClock Event Handlers

| Command | Description |
| ------- | ----------- |
| [ONTIME( value )](?ONTIME) | Event handler for when the specified time is reached |
| [ONCLOCKTIME( hours, mins )](?ONCLOCKTIME) | Event handler for when the specified clock time is reached |
| [ONCLOCKMINS( mins )](?ONCLOCKMINS) | Event handler to be repeated the same time every hour |

----

<br/>

----

## Locos and Tracks

| Command | Description |
| ------- | ----------- |
| [ESTOP](?ESTOP) | Emergency stops all locomotives |
| [SETLOCO( loco )](?SETLOCO) | Set the loco address for this task |
| [READ_LOCO](?READ_LOCO) | Read loco ID from prog track |
| [FWD( speed )](?FWD) | Drive loco forward at DCC speed |
| [REV( speed )](?REV) | Drive loco in reverse at DCC speed |
| [SPEED( speed )](?SPEED) | Drive loco in current direction at DCC speed |
| [STOP](?STOP) | Set loco speed to 0 |
| [MOMENTUM( accel [,decel])](?MOMENTUM) | Set loco momentum |
| [FON( func )](?FON) | Turn on loco function |
| [FOFF( func )](?FOFF) | Turn off loco function |
| [FTOGGLE( func )](?FTOGGLE) | Toggle the state of a loco’s function |
| [INVERT_DIRECTION](?INVERT_DIRECTION) | Switches FWD/REV meaning for loco |
| [ROSTER( loco, "name", "func_map" )](?ROSTER) | Provide roster info for a specified loco |
| [POM( cv, value )](?POM) | Program CV value on main |
| [IFLOCO( loco )](?IFLOCO) | perform commands if the specified loco ID is defined for this sequence |
| [XFWD( loco, speed )](?XFWD) | Sends DCC speed to a loco in forward direction |
| [XREV( loco, speed )](?XREV) | Sends DCC speed to a loco in reverse direction |
| [XFON( loco, func )`](?XFON) | Send DCC function ON to specific cab |
| [XFOFF( loco, func )](?XFOFF) | Send DCC function OFF to specific cab |
| [XFTOGGLE( loco, func )](?XFTOGGLE) | Toggle DCC function on specific loco |
| [XPOM( loco, cv, value )](?XPOM) | Write CV value to specified loco on main |
| [XSAVE_SPEED( loco )](?XSAVE_SPEED) | Saves the current speed of a loco |
| [XRESTORE_SPEED( loco )](?XRESTORE_SPEED) | Restores the saved speed of a loco |
| [FORGET](?FORGET) | Forget the loco in the running automation/sequence |

*Parameters:*  

- **speed** - DCC speed (0-127)  
    - 2-127 = speed 1-126  
    - 0 = stop  
    - 1 = Estop

- **loco** - DCC address of your loco \> **name** - the name of this loco that will appear in the throttle apps. Enclosed in quotes (")
- **funct_map** - the names that you want to see for the functions specific to this loco separated by forward slashes (/). All enclosed in quotes (")

    Note that if the function is ‘momentary’ rather than ‘latching’ (On/Off) then start the function label with a asterisk (\*). The most common example of this is the Horn/Whistle which is commonly on F2.

- **func** - Function number (0-31)
- **cv** - cv to change
- **value** - value to write

----

### Locos: Definition and Control

| Command | Description |
| ------- | ----------- |
| [SET_TRACK( track, mode )](?SET_TRACK) | Configures the mode of a track |
| [SET_POWER( track, ON/OFF )](?SET_POWER) | Enable/Disable power on a track |
| [SETFREQ( frequency )](?SETFREQ) | Enable a specific frequency |

----

### TrackManager Control

| Command | Description |
| ------- | ----------- |
| [SET_TRACK( track, mode )](?SET_TRACK) | Configures the mode of a track |
| [SET_POWER( track, ON/OFF )](?SET_POWER) | Enable/Disable power on a track |
| [SETFREQ( frequency )](?SETFREQ) | Enable a specific frequency |

*Parameters:*

- **track** - - The track to configure, valid options are A to H
- **mode** - - The mode to set the track to.
    - valid options for DCC are:  
        - `MAIN`
        - `MAIN_INV`
        - `MAIN_AUTO`
        - `PROG`
    - valid options for DC are:  
        - `DC`
        - `DC_INV`
        - `DCX` (same as DC_INV)
    - If a track is unused, it can be set to:
        - `NONE`
    - If the **EX‑CommandStation** is configured as a Booster (ESP32 Microcontrollers only), it can be set to:  
        - `BOOST`
        - `BOOST_INV`
        - `BOOST_AUTO`

!!! note "DC"

    When setting at track mode to either DC or DC_INV / DCX, you must use the SETLOCO( loco ) command first to specify the loco ID that will be used for the DC track then SET_TRACK()

----

### Controlling Overload/Shorts

| Command | Description |
| ------- | ----------- |
| [ONOVERLOAD( track )](?ONOVERLOAD) | Event handler for when an Overload occurs |
| [AFTEROVERLOAD( track )](?AFTEROVERLOAD) | Event handler for when an Overload clears |

----

### Virtual Block Control

| Command | Description |
| ------- | ----------- |
| [RESERVE( block_id )](?RESERVE) | Reserve a block |
| [FREE( block_id )](?FREE) | Free block |
| [IFRESERVE( block_id )](?IFRESERVE) | Execute commands if block is NOT reserved |

----

<br/>

----

## System

### Communication and Display Functions

| Command | Description |
| ------- | ----------- |
| [LCD( row, "msg" )](?LCD) | Write message on LCD/OLED |
| [SCREEN( display, row, "msg" )](?SCREEN) | Writes a message to a display |
| [BROADCAST( "msg" )](?BROADCAST) | Broadcast to all throttles/JMRI on serial and WiFi |
| [PRINT( "msg" )](?PRINT) | Print diagnostic message to Serial Monitor |
| [SERIAL( "msg" )](?SERIAL) | Writes direct to Serial |
| [SERIAL1( "msg" )](?SERIAL1) | Writes direct to Serial1 |
| [SERIAL2( "msg" )](?SERIAL2) | Writes direct to Serial2 |
| [SERIAL3( "msg" )](?SERIAL3) | Writes direct to Serial3 |
| [SERIAL4( "msg" )](?SERIAL4) | Writes direct to Serial4 |
| [SERIAL5( "msg" )](?SERIAL5) | Writes direct to Serial5 |
| [SERIAL6( "msg" )](?SERIAL6) | Writes direct to Serial6 |
| [WITHROTTLE( "msg" )](?WITHROTTLE) | Writes a message to WiThrottle clients |
| [MESSAGE( "msg" )](?MESSAGE) | Writes a message to all clients |

----

### EX-CommandStation Functions

| Command | Description |
| ------- | ----------- |
| [POWERON](?POWERON) | Power on track and UNJOIN |
| [POWEROFF](?POWEROFF) | Power off track |
| [JOIN](?JOIN) | Join PROG and MAIN track outputs |
| [UNJOIN](?UNJOIN) | Disconnect prog track from main |
| [ENDEXRAIL](?ENDEXRAIL) | ⚠️ Deprecated - Do not use |
| [EXRAIL](?EXRAIL) | ⚠️ Deprecated - Do not use |
| [KILLALL](?KILLALL) | Kills all running EXRAIL activities |
| [PARSE( "msg" )](?PARSE) | Allows parsing of a DCC-EX API command via myAutomation.h |
| [DISABLE_PROG](?DISABLE_PROG) | Disable programming to save RAM/Flash |
| [IO_NO_HAL](?IO_NO_HAL) | Reduce FLASH footprint when HAL features not required |

----

### Layout Command Control (LCC)

| Command | Description |
| ------- | ----------- |
| [ONLCC(sender, eventid)](?ONLCC) | Start task here when LCC event arrives from sender |
| [LCC(eventid)](?LCC) | Issue event to LCC |
| [LCCX(senderid,eventid)](?LCCX) | Issue LCC event while impersonating another sender |
| [ACON(eventid)](?ACON) | TBA |
| [ACOF(eventid)](?ACOF) | TBA |
| [ONACON(eventid)](?ONACON) | TBA |
| [ONACOF(eventid)](?ONACOF) | TBA |

----

<br/>

----

## Advanced

| Command | Description |
| ------- | ----------- |
| [STEALTH( code )](?STEALTH) | include some C++ code in a ROUTE/SEQUENCE |
| [STEALTH_GLOBAL( code )](?STEALTH_GLOBAL) | Inserts code such as static variables and functions that may be utilized by multiple STEALTH operations |

Please use this option with great care. If in doubt ask for assistance.

For example:

```c++
// run a routine to free any LATCHES that are left on.
SEQUENCE(999)
      STEALTH(  //RESET ANY LATCHES WE TURNED ON
      for (int i = 1; i <= 255; i++) {
        if (getFlag(i,LATCH_FLAG)) {    //IF LATCH ON
        setFlag(i,0,LATCH_FLAG);      //RESET LATCH
          }
        }
      )
RETURN
```

then ``CALL(999)`` inside your onthrow/onclose sections.

--8<-- "snippets/abbr.md"

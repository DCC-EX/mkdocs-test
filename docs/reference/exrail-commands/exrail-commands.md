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

## Flow Control

| Command | Description |
| ------- | ----------- |
| AUTOSTART | Automatically start sequence at this point during EX-CommandStation startup |
| AUTOMATION( id, "description" ) | Define an automation, advertised to throttles/clients |
| ROUTE( id, "description" ) | Define a route, advertised to throttles/clients |
| SEQUENCE( id ) | A general purpose sequence, not advertised to throttles/clients |
| DONE | Completes a Sequence/Route/Animation/Event, or any other automation |
| ENDTASK | Completes a Sequence/Route/Animation/Event, or any other automation |
| CALL( id ) | Branch to a separate sequence |
| RETURN | Return to the calling sequence when completed |
| FOLLOW( sequence_id ) | Branch or Follow a specified sequence |
| PAUSE | E-STOP all locos and PAUSE all other EXRAIL tasks |
| RESUME | Resume all paused tasks, including loco movement |
| START( id ) | Execute a route or sequence |
| START_SEND( id ) | Execute a route or sequence and send the current loco |
| START_SHARED( id ) | Execute a route or sequence and pass the current loco |
| SENDLOCO( loco, route ) | Start route/sequence with a specified loco |
| DELAY( delay ) | Delay the sequence a number of milliseconds |
| DELAYMS( delay ) | Delay the sequence a number of milliseconds |
| DELAYMINS( delay ) | Delay the sequence a number of minutes |
| DELAYRANDOM( min_delay, max_delay ) | Delay a random period of time |
| RANDWAIT( ??? ) | TBA |
| IFRANDOM( percent ) | Run commands a random percentage of the time |
| ROUTE_CAPTION( route_id, "caption" ) | Change the label of the Route button |
| ROUTE_ACTIVE( route_id ) | Activate a Route |
| ROUTE_INACTIVE( route_id ) | Deactivate a Route |
| ROUTE_HIDDEN( route_id ) | Hide a Route from display |
| ROUTE_DISABLED( route_id ) | disable a Route |
| STASH( stash_id ) | Stashes the current loco/invert |
| CLEAR_STASH( stash_id ) | Zeroes the specified stash |
| CLEAR_ALL_STASH | Zeroes all stashes |
| PICKUP_STASH( stash_id ) | Retrieves and sets the loco/invert from the specified stash |

## Objects: Definition and Control

### Create and manage HAL device objects

| Command | Description |
| ------- | ----------- |
| HAL( device, parameters ) | Create a HAL device in myAutomation.h |
| HAL_IGNORE_DEFAULTS | Disable default MCP23017 and PCA9685 HAL devices |

### Signal Objects: Definition and Control

| Command | Description |
| ------- | ----------- |
| SIGNAL( red_pin, amber_pin, green_pin ) | Define a pin based signal |
| SIGNALH( red_pin, amber_pin, green_pin ) | Define a pin based signal with active high pins |
| SERVO_SIGNAL( vpin, red_pos, amber_pos, green_pos ) | Define a servo based signal |
| DCC_SIGNAL( id, addr, sub_addr ) | Define a DCC accessory signal |
| DCCX_SIGNAL( Address, redAspect, amberAspect, greenAspect ) | Defines a signal (with id as dcc address) |
| VIRTUAL_SIGNAL( id ) | Define a virtual signal |
| IFRED( signal_id ) | Test if signal is red |
| IFAMBER( signal_id ) | Test if signal is amber |
| IFGREEN( signal_id ) | Test if signal is green |
| GREEN( signal_id ) | Set a defined signal to GREEN |
| AMBER( signal_id ) | Set a defined signal to Amber |
| RED( signal_id ) | Set defined signal to Red |
| ASPECT( address, aspect ) | Command for DCC Extended Accessories |
| ONGREEN( signal_id) | Define event handler for when a signal is set to the green |
| ONAMBER( signal_id) | Define event handler for when a signal is set to the amber |
| ONRED( signal_id) | Define event handler for when a signal is set to the red aspect |

### Turnout/Point Objects: Definition and Control

| Command | Description |
| ------- | ----------- |
| TURNOUT( turnout_id, addr, sub_addr [, "description"]\|HIDDEN ) | Define a DCC accessory turnout/point |
| TURNOUTL( turnout_id, addr [, "description"]\|HIDDEN ) | Define a DCC accessory turnout/point |
| PIN_TURNOUT( turnout_id, pin [, "description"]\|HIDDEN ) | Define a pin operated turnout |
| SERVO_TURNOUT( turnout_id, pin, active_angle, inactive_angle, profile [, "description"]|HIDDEN ) | Define a servo turnout/point |
| VIRTUAL_TURNOUT( turnout_id [, "description"]\|HIDDEN ) | Define a virtual turnout, which is backed by another automation sequence |
| IFCLOSED( turnout_id ) | Test if a turnout/point is closed |
| IFTHROWN( turnout_id ) | Test if a turnout/point is thrown |
| ONCLOSE( turnout_id ) | Event handler for when a turnout/point is closed |
| ONTHROW( turnout_id ) | Event handler for when a turnout/point is thrown |
| CLOSE( turnout_id ) | Close a turnout/point |
| THROW( turnout_id ) | Throw a turnout/point |
| TOGGLE_TURNOUT( turnout_id ) | Toggle a defined turnout/point between CLOSE/THROW |

### Turntable/Traverser Objects: Definition and Control

| Command | Description |
| ------- | ----------- |
| MOVETT( id, steps, activity ) | Move a EX‑Turntable to a step position and perform an activity |
| IFRE ( vpin, value ) | Test if a rotary encoder has been set to a value |
| ONCHANGE( vpin ) | Detects a rotary encoder has changed position |
| Turntable features | |
| DCC_TURNTABLE( id, home_angle, [, "description"] ) | Define a DCC accessory turntable/traverser |
| EXTT_TURNTABLE( id, vpin, home_angle, [, "description"] ) | Define an EX-Turntable turntable/traverser |
| TT_ADDPOSITION( id, position_id, value, angle [, "description"] ) | Add a turntable position |
| IFTTPOSITION( id, position ) | Test if turntable/traverser is at a position |
| ONROTATE( id ) | Event handler for when a turntable/traverser is rotated |
| ROTATE( id, position, activity ) | Rotate an EX-Turntable turntable/traverser |
| ROTATE_DCC( id, position ) | Rotate a DCC accessory turntable/traverser |
| WAITFORTT( id ) | Wait for EX-Turntable turntable/traverser to complete a rotation |

### Sensors/Inputs: Reading and Responding

| Command | Description |
| ------- | ----------- |
| JMRI_SENSOR(vpin [,count]) | Creates <S> type sensors visible to JMRI |
| AT( vpin ) | Causes a sequence to wait until a sensor is active/triggered |
| AFTER( vpin ) | Causes a sequence to wait until after a sensor has been triggered |
| ATTIMEOUT( vpin, timeout_ms ) | Causes a sequence to wait until either a sensor is active/triggered, or if the timer runs out |
| IF( vpin ) | If sensor activated or latched, continue |
| IFNOT( vpin ) | If sensor NOT activated and NOT latched, continue |
| IFTIMEOUT | Tests if “timed out” flag has been set by an ATTIMEOUT() sensor reading attempt |
| ATGTE( vpin, value ) | Waits for an analog pin to reach a value |
| ATLT ( vpin, value ) | Waits for an analog pin to go below a value |
| IFGTE( vpin, value ) | Test if analog pin reading is greater than or equal to value |
| IFLT( vpin, value ) | Test if analog pin reading is less than value |
| ATTIMOUT1 ( vpin, value ) | TBA |
| ATTIMOUT2 ( vpin, value ) | TBA |
| DRIVE ( vpin ) | TBA |
| LATCH( vpin ) | Latches a sensor on |
| UNLATCH( vpin ) | Remove LATCH on sensor |
| ONBUTTON( vpin ) | Event handler for debounced button presses |
| ONSENSOR( vpin ) | Event handler for sensors |

### Output and LED control

| Command | Description |
| ------- | ----------- |
| SET( vpin [,count] ) | Set an output pin HIGH |
| RESET( vpin [,count] ) | Reset output pin |
| FADE( vpin, value, ms ) | Fade an LED |
| BLINK( vpin, onMs, offMs ) | Blink an output pin |
| LCN( "msg" ) | Send message to LCN Accessory Network |
| CONFIGURE_SERVO(vpin, pos1, pos2, profile) | Define LED’s connected to PCA9685 boards |
| NEOPIXEL( vpin, red, green, blue [,count] ) | Controls the colour of attached Neopixel LEDs |
| NEOPIXEL_SIGNAL( signalid, red, green, blue ) | Controls the colour of attached Neopixel LED |
| ANOUT( vpin, value, param1, param2) | Writes to the HAL analog output interface of a device driver |
| PLAYSOUND( vpin, fileNumber, volume ) | Play mp3 files from a Micro-SD card |

### Servo Control

| Command | Description |
| ------- | ----------- |
| SERVO( id, position, profile ) | Move an animation servo |
| SERVO2( id, position, duration ) | Move an animation servo taking duration |
| WAITFOR( pin ) | Wait for a servo motion to complete prior to continuing |

### DCC Accessory Decoder Control

| Command | Description |
| ------- | ----------- |
| ONACTIVATE( addr, sub_addr ) | Event handler for 2 part DCC accessory packet value 1 |
| ONACTIVATEL( linear ) | Event handler for linear DCC accessory packet value 1 |
| ONDEACTIVATE( addr, sub_addr ) | Event handler for 2 part DCC accessory packet value 0 |
| ONDEACTIVATEL( linear ) | Event handler for linear DCC accessory packet value 0 |
| ACTIVATE( addr, sub_addr ) | Sends a DCC accessory packet with value 1 |
| ACTIVATEL( linear ) | Sends a DCC accessory packet with value 1 to a linear address |
| DEACTIVATE( addr, sub_addr ) | Sends a DCC accessory packet with value 0 |
| DEACTIVATEL( addr ) | Sends a DCC accessory packet with value 0 to a linear address |
| DCCACTIVATE( addr, sub_addr ) | TBA |

### EX-FastClock Event Handlers

| Command | Description |
| ------- | ----------- |
| ONTIME( value ) | Event handler for when the specified time is reached |
| ONCLOCKTIME( hours, mins ) | Event handler for when the specified clock time is reached |
| ONCLOCKMINS( mins ) | Event handler to be repeated the same time every hour |

## Locos and Tracks

| Command | Description |
| ------- | ----------- |
| ESTOP | Emergency stops all locomotives |
| SETLOCO( loco ) | Set the loco address for this task |
| READ_LOCO | Read loco ID from prog track |
| FWD( speed ) | Drive loco forward at DCC speed |
| REV( speed ) | Drive loco in reverse at DCC speed |
| SPEED( speed ) | Drive loco in current direction at DCC speed |
| STOP | Set loco speed to 0 |
| MOMENTUM( accel [,decel]) | Set loco momentum |
| FON( func ) | Turn on loco function |
| FOFF( func ) | Turn off loco function |
| FTOGGLE( func ) | Toggle the state of a loco’s function |
| INVERT_DIRECTION | Switches FWD/REV meaning for loco |
| ROSTER( loco, "name", "func_map" ) | Provide roster info for a specified loco |
| POM( cv, value ) | Program CV value on main |
| IFLOCO( loco ) | perform commands if the specified loco ID is defined for this sequence |
| XFWD( loco, speed ) | Sends DCC speed to a loco in forward direction |
| XREV( loco, speed ) | Sends DCC speed to a loco in reverse direction |
| XFON( cab, func )` | Send DCC function ON to specific cab |
| XFOFF( cab, func ) | Send DCC function OFF to specific cab |
| XFTOGGLE( loco, func ) | Toggle DCC function on specific loco |
| XPOM( loco, cv, value ) | Write CV value to specified loco on main |
| XSAVE_SPEED( loco ) | Saves the current speed of a loco |
| XRESTORE_SPEED( loco ) | Restores the saved speed of a loco |
| FORGET | Forget the loco in the running automation/sequence |

### Locos: Definition and Control

| Command | Description |
| ------- | ----------- |
| SET_TRACK( track, mode ) | Configures the mode of a track |
| SET_POWER( track, ON/OFF ) | Enable/Disable power on a track |
| SETFREQ( frequency ) | Enable a specific frequency |

### TrackManager Control

| Command | Description |
| ------- | ----------- |
| SET_TRACK( track, mode ) | Configures the mode of a track |
| SET_POWER( track, ON/OFF ) | Enable/Disable power on a track |
| SETFREQ( frequency ) | Enable a specific frequency |

### Controlling Overload/Shorts

| Command | Description |
| ------- | ----------- |
| ONOVERLOAD( track ) | Event handler for when an Overload occurs |
| AFTEROVERLOAD( track ) | Event handler for when an Overload clears |

### Virtual Block Control

| Command | Description |
| ------- | ----------- |
| RESERVE( block_id ) | Reserve a block |
| FREE( block_id ) | Free block |
| IFRESERVE( block_id ) | Execute commands if block is NOT reserved |

## System

### Communication and Display Functions

| Command | Description |
| ------- | ----------- |
| LCD( row, "msg" ) | Write message on LCD/OLED |
| SCREEN( display, row, "msg" ) | Writes a message to a display |
| BROADCAST( "msg" ) | Broadcast to all throttles/JMRI on serial and WiFi |
| PRINT( "msg" ) | Print diagnostic message to Serial Monitor |
| SERIAL( "msg" ) | Writes direct to Serial |
| SERIAL1( "msg" ) | Writes direct to Serial1 |
| SERIAL2( "msg" ) | Writes direct to Serial2 |
| SERIAL3( "msg" ) | Writes direct to Serial3 |
| SERIAL4( "msg" ) | Writes direct to Serial4 |
| SERIAL5( "msg" ) | Writes direct to Serial5 |
| SERIAL6( "msg" ) | Writes direct to Serial6 |
| WITHROTTLE( "msg" ) | Writes a message to WiThrottle clients |
| MESSAGE( "msg" ) | Writes a message to all clients |

### EX-CommandStation Functions

| Command | Description |
| ------- | ----------- |
| POWERON | Power on track and UNJOIN |
| POWEROFF | Power off track |
| JOIN | Join PROG and MAIN track outputs |
| UNJOIN | Disconnect prog track from main |
| ENDEXRAIL | ⚠️ Deprecated - Do not use |
| EXRAIL | ⚠️ Deprecated - Do not use |
| KILLALL | Kills all running EXRAIL activities |
| PARSE( "msg" ) | Allows parsing of a DCC-EX API command via myAutomation.h |
| DISABLE_PROG | Disable programming to save RAM/Flash |
| IO_NO_HAL | Reduce FLASH footprint when HAL features not required |

### Layout Command Control (LCC)

| Command | Description |
| ------- | ----------- |
| ONLCC(sender, eventid) | Start task here when LCC event arrives from sender |
| LCC(eventid) | Issue event to LCC |
| LCCX(senderid,eventid) | Issue LCC event while impersonating another sender |
| ACON(eventid) | TBA |
| ACOF(eventid) | TBA |
| ONACON(eventid) | TBA |
| ONACOF(eventid) | TBA |

## Advanced

| Command | Description |
| ------- | ----------- |
| STEALTH( code ) | include some C++ code in a ROUTE/SEQUENCE |
| STEALTH_GLOBAL( code ) | Inserts code such as static variables and functions that may be utilized by multiple STEALTH operations |

--8<-- "snippets/abbr.md"


```cpp
ACTIVATE(addr,subaddr)
```

Send DCC Accessory Activate packet (gate on then off)

- addr DCC short address of accessory
- subaddr DCC sub address

```cpp
ACTIVATEL(linearaddr)
```

Send DCC Accessory Activate packet (gate on then off)

- linearaddr DCC linear address of accessory

```cpp
AFTER(vpin,timer...)
```

Wait for sensor activated, then decativated for given time

- vpin Virtual Pin number of sensor
- timer... optional wait in mS, default 500

```cpp
AFTEROVERLOAD(track_id)
```

Wait for overload to be resolved

- track_id A..H

```cpp
ALIAS(name,value...)
```

defines a named numeric value.

- name c++ variable name that can be used throughout the script
- value...  if omitted, a large negative value is created automatically

```cpp
AMBER(signal_id)
```

Sets a signal to amber state

see ONAMBER


```cpp
ANOUT(vpin,value,param1,param2)
```

Writes to the HAL analog output interface of a device driver.

- vpin Virtual pin number of device 
- value basic analog value
- param1 device dependent 
- param2 device dependent

```cpp
AT(vpin)
```

Wait until a sensor becomes active

- vpin Virtual pin of sensor. Use negative value for sensors that are HIGH when activated

```cpp
ASPECT(address,value)
```

Sends a DCC aspect value to an accessory address. May also change status of a signal defined using this aspect.

- address Linear DCC address of device 
- value Aspect value (Device dependent)

```cpp
ATGTE(vpin,value)
```

Wait for analog sensor to be greater than given value

- vpin Analog pin number 
- value integer value to compare against

```cpp
ATLT(vpin,value) 
```

Wait for analog sensor value to be less than given value

- vpin Analog pin number 
- value integer value to compare against

```cpp
ATTIMEOUT(vpin,timeout_ms)
```

Wait for sensor active, with timeout. Use IFTIMEOUT to determine whether the AT was satisfied.

see IFTIMEOUT  

- vpin Sensor pin number 
- timeout_ms Millseconds to wait before timeout

```cpp
AUTOMATION(sequence_id,description)
```

Defines starting point of a sequence that will be shown as an Automation by 

the throttles. Automations are started by the throttle handing over a loco id to be driven.

- sequence_id Unique sequence id value
- description (Quoted text) will be shown on throttle button

```cpp
AUTOSTART
```

A new task will be created starting from this point at Command Station startup


```cpp
BLINK(vpin,onDuty,offDuty)
```

Starts a blinking process for a vpin (typically a LED). Stop blink with SET or RESET.

- vpin Pin to blink
- onDuty Milliseconds with LED ON
- offDuty Milliseconds with LED off

```cpp
BROADCAST(msg)
```

Send raw message text to all throttles using the DCC-EX protocol

see WITHROTTLE

- msg  Quoted message

```cpp
CALL(sequence_id)
```

transfer control to another sequence with expectation to return

see RETURN

- sequence_id SEQUENCE to jump processing to, must terminate or RETURN

```cpp
CLEAR_STASH(stash_id)
```

Clears loco value stored in stash  

- stash_id which stash to clear.

```cpp
CLEAR_ALL_STASH
```

Clears all stashed loco values


```cpp
CLEAR_ANY_STASH
```

Clears loco value from all stash entries


```cpp
CLOSE(turnout_id)
```

Close turnout by id

see THROW


```cpp
CONFIGURE_SERVO(vpin,pos1,pos2,profile)
```

setup servo movement parameters for non-turnout

- vpin must refer to a servo capable pin
- pos1 SET position of servo
- pos2 RESET position of servo
- profile Movement profile (Instant, Fast, Medium, Slow, Bounce)

```cpp
DCC_SIGNAL(signal_id,addr,subaddr)
```

Define a DCC accessory signal with short address

- signal_id Id used for all signal manipulation commands
- addr DCC address
- subaddr DCC subaddress

```cpp
DCCX_SIGNAL(signal_id,redAspect,amberAspect,greenAspect)
```

Dfeine advanced DCC accessory signal with aspects

- signal_id DCC Linear address AND Id used for all signal manipulation commands

```cpp
DCC_TURNTABLE(turntable_id,home,description...)
```

defines a Turntable device 

- homeAngle the angle of the home position, valid angles are 0 - 3600
- description... Quoted text description of turntable

```cpp
DEACTIVATE(addr,subaddr)
```

Sends DCC Deactivate packet (gate on, gate off) 

- addr DCC accessory address
- subaddr DCC accessory subaddress

```cpp
DEACTIVATEL(addr)
```

Sends DCC Deactivate packet (gate on, gate off) 

- addr DCC Linear accessory address

```cpp
DELAY(delay_ms)
```

Waits for given milliseconds delay (This is not blocking) 

- delay_mS Delay time in milliseconds

```cpp
DELAYMINS(delay_minutes)
```

Waits for given minutes delay (This is not blocking)


```cpp
DELAYRANDOM(mindelay,maxdelay)
```

Waits for random delay between min and max milliseconds (This is not blocking)

- mindelay minumum delay in mS
- maxdelay maximum delay in mS

```cpp
DONE
```

Stops task loco (if any) and terminates current task


```cpp
DRIVE(analogpin)
```

RESERVED do not use


```cpp
ELSE
```

introduces alternate processing path after any kind of IF

see IF


```cpp
ENDEXRAIL
```

obsolete.. no longer needed. Does nothing.


```cpp
ENDIF  
```

determines end of IF(any type)  block.

IF something ENDIF, or    

IF something ELSE something ENDIF

see IF


```cpp
ENDTASK
```

same as DONE

see DONE


```cpp
ESTOP
```

Performs emergency stop on current task loco


```cpp
ESTOPALL
```

Performs emergency stop on all locos


```cpp
EXRAIL
```

obsolete.. no longer needed. Does nothing.


```cpp
EXTT_TURNTABLE(id,vpin,home,description...)
```

This statement will create the EXΓÇæTurntable turntable/traverser object only, so you will need a separate HAL() statement for an EXΓÇæTurntable device driver.

- homeAngle  the angle of the home position, valid angles are 0 - 3600
- quoted description...

```cpp
FADE(vpin,value,ms)
```

Modifies analog value slowly taking a given time

- vpin Servo virtual pin number 
- value new target value
- ms time to reach value

```cpp
FOFF(func)
```

Turns off current loco function

see FON


```cpp
FOLLOW(sequence_id)
```

Task processing follows given route or sequence (Effectively a GoTo)


```cpp
FON(func)
```

Turn on current loco function

see FOFF


```cpp
FORGET
```

Removes current loco from task and DCC reminders table.


```cpp
FREE(token_id)
```

Frees logical token 

see RESERVE

- token_id 0..255

```cpp
FREEALL
```

Frees all logical tokens 

see RESERVE


```cpp
FTOGGLE(func)
```

Toggles function for current loco


```cpp
FWD(speed)
```

Instructs current loco to set DCC speed

- speed 0..127   (1=ESTOP)

```cpp
GREEN(signal_id)
```

Sets signal to green state 


```cpp
HAL(haltype,params...)
```

Defines VPIN mapping for specific hardware drivers

- haltype driver name, normally device type
- params... depend on driver.

```cpp
HAL_IGNORE_DEFAULTS
```

System will ignore default HAL device mappings


```cpp
IF(vpin)
```

Checks sensor state, If false jumps to matching nested ELSE or ENDIF

- vpin  VPIN of sensor. Negative VPIN will invert sensor state.

```cpp
IFAMBER(signal_id)
```

Checks if signal is in AMBER state. 

see IF


```cpp
IFCLOSED(turnout_id)
```

Checks if given turnout is in close state

see IF


```cpp
IFGREEN(signal_id)
```

Checks if given signal is in GREEN state

see IF


```cpp
IFGTE(vpin,value)
```

Checks if analog vpin sensor >= value

see IF


```cpp
IFLOCO(loco_id)
```

Checks if current task loco = loco_id

see IF


```cpp
IFLT(vpin,value)
```

Checks if analog sensor < value

see IF

- vpin  Analog vpin of sensor 

```cpp
IFNOT(vpin)
```

Inverse of IF

see IF


```cpp
IFRANDOM(percent)
```

randomly satisfield IF at given percent probability

see IF


```cpp
IFRED(signal_id)
```

Checks if given signal is in RED state

see IF


```cpp
IFSTASH(stash_id)
```

Checks if given stash entry has a non zero value

see IF


```cpp
IFSTASHED_HERE(stash_id)
```

Checks if given stash entry has the current loco

see IF


```cpp
IFTHROWN(turnout_id)
```

Checks if given turnout is in THROWN state

see IF


```cpp
IFRESERVE(token_id)
```

Attempts to reserve token and if satisfiled the token remains reserved. 

see IF RESERVE FREE


```cpp
IFTIMEOUT
```

Checks TIMEOUT state after an AT/AFTER request with timeout value.

see IF AT AFTER


```cpp
IFTTPOSITION(turntable_id,position)
```

Checks if Turntable is in given position

see IF


```cpp
IFRE(vpin,value)
```

Checks external rotary encoder value 

- vpin of device driver for rotary encoder  

```cpp
IFBITMAP_ALL(vpin,mask)
```

briaf Checks if (vpin pseudo-analog value & mask) == mask.

see IF

- mask Binary mask applied to vpin value

```cpp
IFBITMAP_ANY(vpin,mask)
```

briaf Checks if vpin pseudo-analog value & mask is non zero

see IF

- mask Binary mask applied to vpin value

```cpp
IFROUTE_ACTIVE(sequence_id)
```

briaf Checks if route is active

see IF


```cpp
IFROUTE_INACTIVE(sequence_id)
```

briaf Checks if route is inactive

see IF


```cpp
IFROUTE_HIDDEN(sequence_id)
```

briaf Checks if route is hidden

see IF


```cpp
IFROUTE_DISABLED(sequence_id)
```

briaf Checks if route is disabled

see IF


```cpp
INVERT_DIRECTION
```

Marks current task so that FWD and REV commands are inverted.


```cpp
JMRI_SENSOR(vpin,count...)
```

Defines multiple JMRI `<s>` type sensor feedback definitions each with id matching vpin and INPUT_PULLUP

- vpin first vpin number
- count... Number of consecutine VPINS for which to create JMRI sensor feedbacks. Default 1.

```cpp
JMRI_SENSOR_NOPULLUP(vpin,count...)
```

Defines multiple JMRI `<s>` type sensor feedback definitions each with id matching vpin

- vpin first vpin number
- count... Number of consecutine VPINS for which to create JMRI sensor feedbacks. Default 1.

```cpp
JOIN
```

Switches PROG track to receive MAIN track DCC packets. (Drive on PROG track)


```cpp
KILLALL
```

Tertminates all running EXRAIL tasks


```cpp
LATCH(vpin)
```

Make all AT/AFTER/IF see vpin as HIGH without checking hardware

- vpin Must only be for VPINS 0..255

```cpp
LCC(eventid)
```

Issue event to LCC 


```cpp
LCCX(senderid,eventid)
```

Issue LCC event while impersonating another sender 


```cpp
LCD(row,msg)
```

Write message on row of default configured LCD/OLED

see SCREEN 

- msg Quoted text

```cpp
MOMENTUM(accel,decel...)
```

sets momentum in mS per DCC 127 step for curent loco. 

- accel Acceleration momentum  
- decel... Braking momantum. (=Acceleration if not given)

```cpp
SCREEN(display,row,msg)
```

Send message to external display hadlers 

- display number, 0=local display, others are handled by external
displays which may have different display numbers on different devices. 

- msg Quoted text

```cpp
LCN(msg)
```

Reserved for LCN communication. Refer to their documentation.


```cpp
MESSAGE(msg)
```

Send a human readable message to all throttle users

- msg Quoted text

```cpp
MOVETT(turntable_id,steps,activity)
```

Move Turntable to specific position

see ROTATE

- steps position to move to 
- activity see ROTATE

```cpp
NEOPIXEL(vpin,r,g,b,count...)
```

Set a NEOPIXEL vpin to a given red/green/blue colour

- vpin VPIN of a pixel
- r red component 0-255 
- g green component 0-255
- b blue component 0-255
- count... Number of consecutive pixels to set, Default 1.

```cpp
NEOPIXEL_SIGNAL(vpin,redcolour,ambercolour,greencolour)
```

Define a signal that uses a single multi colour pixel

see NEORGB 

- vpin unique signal_id 
- redcolour  RGB colour use NEORGB(red,green,blue) to create values.

```cpp
ACON(eventid)
```

Send MERG CBUS ACON to Adapter


```cpp
ACOF(eventid)
```

Send MERG CBUS ACOF to Adapter


```cpp
ONACON(eventid)
```

Start task here when ACON for event receied from MERG CBUS


```cpp
ONACOF(eventid)
```

Start task here when ACOF for event receied from MERG CBUS


```cpp
ONACTIVATE(addr,subaddr)
```

Start task here when DCC Activate sent for short address


```cpp
ONACTIVATEL(linear)
```

Start task here when DCC Activate sent for linear address


```cpp
ONAMBER(signal_id)
```

Start task here when signal set to AMBER state


```cpp
ONBLOCKENTER(block_id)
```

Start task here when a loco enters a railcom block

- block_id vpin associated to block by HAL(I2CRailcom..)

```cpp
ONBLOCKEXIT(block_id)
```

Start task here when a loco leaves a railcom block

- block_id vpin associated to block by HAL(I2CRailcom..)

```cpp
ONTIME(minute_in_day)
```

Start task here when fastclock matches

- minute_in_day (0..1439)

```cpp
ONCLOCKTIME(hours,mins)
```

Start task here when fastclock matches time


```cpp
ONCLOCKMINS(mins)
```

Start task here hourly when fastclock minutes matches 


```cpp
ONOVERLOAD(track_id)
```

Start task here when given track goes into overload

- track_id A..H

```cpp
ONRAILSYNCON
```

Start task here when the railsync (booster) input port get a valid DCC signal


```cpp
ONRAILSYNCOFF
```

Start task here when the railsync (booster) input port does not get a valid DCC signal any more


```cpp
ONDEACTIVATE(addr,subaddr)
```

Start task here when DCC deactivate packet sent


```cpp
ONDEACTIVATEL(linear) 
```

Start task here when DCC deactivate sent to linear address


```cpp
ONCLOSE(turnout_id)
```

Start task here when turnout closed


```cpp
ONLCC(sender,event)
```

Start task here when LCC event arrives from sender


```cpp
ONGREEN(signal_id)
```

Start task here when signal set to GREEN state 


```cpp
ONRED(signal_id)
```

Start task here when signal set to RED state 


```cpp
ONROTATE(turntable_id)
```

Start task here when turntable is rotated


```cpp
ONTHROW(turnout_id)
```

Start task here when turnout is Thrown


```cpp
ONCHANGE(vpin)
```

Rotary encoder change starts task here (This is obscurely different from ONSENSOR which will be merged in a later release.) 


```cpp
ONSENSOR(vpin)
```

Start task here when sensor changes state (debounced)


```cpp
ONBITMAP(vpin)
```

Start task here when bitmap sensor changes state (debounced)


```cpp
ONBUTTON(vpin)
```

Start task here when sensor changes HIGH to LOW. 


```cpp
PAUSE
```

Pauses all EXRAIL tasks except the curremnt one.

Other tasks ESTOP their locos until RESUME issued


```cpp
PIN_TURNOUT(id,vpin,description...)
```

Defines a turnout which operates on a signle pin

- description... Quoted text (shown to throttles) or HIDDEN

```cpp
PRINT(msg)
```

prints diagnostic message on USB serial 

- msg Quoted text

```cpp
PARSE(msg)
```

Executes `<>` command as if entered from serial

- msg Quoted text, preferably including `<>`

```cpp
PICKUP_STASH(stash_id)
```

see STASH

Loads stashed value into current task loco

- stash_id position in stash where a loco id was previously saved.

```cpp
POM(cv,value)
```

Write value to cv on current tasks loco (Program on Main) 


```cpp
POWEROFF
```

Powers off all tracks


```cpp
POWERON
```

Powers ON all tracks


```cpp
RANDOM_CALL(sequence_id...)
```

CALL to another sequence randomly chosen from list

see CALL

- sequence_id.. list of SEQUENCE that may be called, each must terminate or RETURN

```cpp
RANDOM_FOLLOW(sequence_id...)
```

jump to another sequence randomly chosen from list

see FOLLOW

- sequence_id.. list of SEQUENCE that may be followed

```cpp
READ_LOCO
```

Reads loco Id from prog track and sets currenmt task loco id.


```cpp
RED(signal_id)
```

sets signal to RED state 


```cpp
RESERVE(token_id)
```

Waits for token for block. If not available immediately, current task loco is stopped.


```cpp
RESET(vpin,count...)
```

Sets output pin LOW

see SET

- count... Number of consecutive pins, default 1

```cpp
RESTORE_SPEED
```

Resumes locos saved speed 

see SAVE_SPEED


```cpp
RESUME
```

Resumes PAUSEd tasks 

see PAUSE


```cpp
RETURN
```

Returns to CALL 

see CALL


```cpp
REV(speed)
```

Issues DCC speed packet for current loco in reverse.

see FWD

- speed  (0..127, 1=ESTOP)

```cpp
ROTATE(turntable_id,position,activity)
```

Rotates an EX-Turntable to a given position

- activity .. One of:
- **Turn**: Rotate turntable, maintain phase

- **Turn_PInvert**: Rotate turntable, invert phase

- **Home**: Initiate homing

- **Calibrate**: Initiate calibration sequence

- **LED_On**: Turn LED on

- **LED_Slow**: Set LED to a slow blink

- **LED_Fast**: Set LED to a fast blink

- **LED_Off**: Turn LED off

- **Acc_On**: Turn accessory pin on

- **Acc_Off**: Turn accessory pin off


```cpp
ROTATE_DCC(turntable_id,position_id)
```

Rotates turntable to a given position using DCC commands


```cpp
ROSTER(cab,name,funcmap...)
```

Describes a loco roster entry visible to throttles

- cab loco DCC address or 0 for default entry
- name Quoted text
- funcmap... Quoted text, optional list of function names separated by / character with momentary function names prefixed with an *.

```cpp
ROUTE(sequence_id,description)
```

DEfines starting point of a sequence that will appear as a route on throttle buttons.

- description Quoted text, throttle button capotion.

```cpp
ROUTE_ACTIVE(sequence_id)
```

Tells throttle to display the route button as active

- sequence_id of ROUTE/AUTOMATION

```cpp
ROUTE_INACTIVE(sequence_id)
```

Tells throttle to display the route button as inactive

- sequence_id of ROUTE/AUTOMATION

```cpp
ROUTE_HIDDEN(sequence_id)
```

Tells throttle to hide the route button

- sequence_id of ROUTE/AUTOMATION

```cpp
ROUTE_DISABLED(sequence_id)
```

Tells throttle to display the route button as disabled

- sequence_id of ROUTE/AUTOMATION

```cpp
ROUTE_CAPTION(sequence_id,caption)
```

Tells throttle to change thr route button caption

- sequence_id of ROUTE/AUTOMATION 

```cpp
SAVE_SPEED
```

Resumes locos saved speed 

see RESTORE_SPEED


```cpp
SENDLOCO(cab,sequence_id)
```

Start a new task to drive the loco 

- cab loco to be driven 
- route sequence_id of route, automation or sequence to drive

```cpp
SEQUENCE(sequence_id)
```

Provides a unique label than can be used to call, follow or start. 

see CALL

see FOLLOW

see START


```cpp
SERIAL(msg)
```

Write direct to Serial output

- msg Quoted text

```cpp
SERIAL1(msg)
```

Write direct to Serial1 output

- msg Quoted text

```cpp
SERIAL2(msg)
```

Write direct to Serial2 output

- msg Quoted text

```cpp
SERIAL3(msg)
```

Write direct to Serial3 output

- msg Quoted text

```cpp
SERIAL4(msg)
```

Write direct to Serial4 output

- msg Quoted text

```cpp
SERIAL5(msg)
```

Write direct to Serial5 output

- msg Quoted text

```cpp
SERIAL6(msg)
```

Write direct to Serial6 output

- msg Quoted text

```cpp
SERVO(vpin,position,profile)
```

Move servo to given position

- vpin of servo
- position  servo position (values are hardware dependent) 
- profile movement profile (Instant, Fast, Medium, Slow, Bounce)

```cpp
SERVO2(vpin,position,duration)
```

Move servo to given position taking time 

- vpin of servo
- position  servo position (values are hardware dependent) 
- duration mS

```cpp
SERVO_SIGNAL(vpin,redpos,amberpos,greenpos)
```

Dedfine a servo based signal with 3 servo positions

- vpin of servo, acts as signal_id
- redpos servo position (values are hardware dependent) 
- amberpos servo position (values are hardware dependent)
- greenpos servo position (values are hardware dependent)

```cpp
SERVO_TURNOUT(turnout_id,vpin,activeAngle,inactiveAngle,profile,description...)
```

Define a servo driven turnout

- turnout_id used by THROW/CLOSE 
- vpin for servo
- activeAngle servo position (values are hardware dependent)
- inactiveAngle servo position (values are hardware dependent)
- profile movement profile (Instant, Fast, Medium, Slow, Bounce)
- description... Quoted text shown to throttles or HIDDEN keyword to hide turnout button

```cpp
SET(vpin,count...)
```

Set pin HIGH

see RESET  

- count...  Number of sequential vpins to set. Default 1.

```cpp
SET_TRACK(track,mode)
```

Set output track type

- track A..H
- mode NONE, MAIN, PROG, DC, EXT, BOOST, BOOST_INV, BOOST_AUTO, MAIN_INV, MAIN_AUTO, DC_INV, DCX

```cpp
SET_POWER(track,onoff)
```

Set track power mode

- track A..H
- onoff ON or OFF

```cpp
SETLOCO(loco)
```

Sets the loco being handled by the current task


```cpp
SETFREQ(freq)
```

Sets the DC track PWM frequency 

- freq Frequency is default 0, or 1..3

```cpp
SIGNAL(redpin,amberpin,greenpin)
```

Define a Signal with LOW=on leds 

see SIGNALH  

- redpin vpin for RED state, also acts as signal_id

```cpp
SIGNALH(redpin,amberpin,greenpin)
```

define a signal with HIGH=ON leds 

- redpin vpin for RED state, also acts as signal_id

```cpp
SPEED(speed)
```

Changes current tasks loco speed without changing direction

- speed 0..127 (1=ESTOP)

```cpp
START(sequence_id)
```

Starts a new task at the given route/animation/sequence


```cpp
START_SHARED(sequence_id)
```

Starts a new task at the given route/animation/sequence an share current loco with it


```cpp
START_SEND(sequence_id)
```

Starts a new task at the given route/animation/sequence an send current loco to it. Remove loco from current task.


```cpp
STASH(stash_id)
```

saves cuttent tasks loco id in the stash array

- stash_id  position in stash array to save loco id

```cpp
STEALTH(code...)
```

Allows for embedding raw C++ code in context of current task.

- code... c++ code to be executed. This requires intimate understanding of the product acrhitecture.

```cpp
STEALTH_GLOBAL(code...)
```

Allows for embedding raw c++ code out of context.

- code...  c++ code to be defined. This requires intimate understanding of the product acrhitecture.

```cpp
STOP
```

Same as SPEED(0)


```cpp
THROW(turnout_id)
```

Throws given turnout

see CLOSE


```cpp
TOGGLE_TURNOUT(turnout_id)
```

Toggles given turnout


```cpp
TT_ADDPOSITION(turntable_id,position_id,value,angle,description...)
```

Defines a turntable track position

- position_id each position is given an id
- address DCC accessory address 
- angle Used only for throttles that may draw a visual representation of the turntable
- description... quoted text or HIDDEN

```cpp
TURNOUT(turnout_id,addr,subaddr,description...)
```

Defines a DCC accessory turnout with legacy address

- turnout_id to be used in THROW/CLOSE etc  
- addr DCC accessory address
- subaddr DCC accessory subaddress
- description... Quoted text or HIDDEN, appears on throttle buttons

```cpp
TURNOUTL(tirnout_id,addr,description...)
```

Defines a DCC accessory turnout with inear address

see TURNOUT

- turnout_id to be used in THROW/CLOSE etc  
- addr DCC accessory linear address
- description... Quoted text or HIDDEN, appears on throttle buttons

```cpp
UNJOIN
```

Disconnects PROG track from MAIN

see JOIN


```cpp
UNLATCH(vpin)
```

removes latched on flag

see LATCH 

- vpin (limited to 0..255)

```cpp
VIRTUAL_SIGNAL(signal_id)
```

Defines a virtual (no hardware) signal, use ONhandlers to simulate hardware

see SIGNAL ONRED ONAMBER ONGREEN


```cpp
VIRTUAL_TURNOUT(id,description...)
```

Defines a virtual (no hardware) turnout, use ONhandlers to simulate hardware

see TURNOUT ONCLOSE ONTHROW

- description... quoted text or HIDDEN

```cpp
BITMAP_AND(vpin1,mask)
```

Performs a bitwise AND operation on the given vpin analog value and mask.

- mask Binary mask to be ANDed with vpin1 value

```cpp
BITMAP_INC(vpin)
```

Increments poesudo analog value by 1


```cpp
BITMAP_DEC(vpin)
```

Decrements poesudo analog value by 1  (to zero)


```cpp
BITMAP_OR(vpin1,mask)
```

Performs a bitwise OR operation on the given vpin analog value and mask.

- mask Binary mask to be ORed with vpin1 value

```cpp
BITMAP_XOR(vpin1,mask)
```

Performs a bitwise XOR operation on the given vpin analog value and mask.

- mask Binary mask to be XORed with vpin1 value

```cpp
WAITFOR(pin)
```

Waits for completion of servo movement


```cpp
WAITFORTT(turntable_id)
```

waits for completion of turntable movement


```cpp
VIRTUAL_SIGNAL(signal_id)
```

Defines a virtual (no hardware) signal, use ONhandlers to simulate hardware

see SIGNAL


```cpp
WAIT_WHILE_RED(signal_id)
```

Keeps loco at speed 0 while signal is RED


```cpp
WITHROTTLE(msg)
```

Broadcasts a string in Withrottle protocol format to all throttles using this protocol. 

- msg quoted string

```cpp
XFOFF(cab,func)
```

Turns function off for given loco 

- func function number

```cpp
XFON(cab,func)
```

Turns function ON for given loco


```cpp
XFTOGGLE(cab,func)
```

Toggles function state for given loco


```cpp
XFWD(cab,speed)
```

Sends DCC speed to loco in forward direction

- speed (0..127, 1=ESTOP)

```cpp
XREV(cab,speed)
```

Sends DCC speed to loco in reverse direction

- speed (0..127, 1=ESTOP)

```cpp
XPOM(cab,cv,value)
```

Sends DCC speed to loco in reverse direction

- cab loco id
- cv  to be updated
- value to be written to cv

```cpp
XRESTORE_SPEED(cab)
```

Resumes locos saved speed 

- cab loco id
see XSAVE_SPEED


```cpp
XSAVE_SPEED(cab)
```

Resumes locos saved speed 

- cab loco id
see XRESTORE_SPEED


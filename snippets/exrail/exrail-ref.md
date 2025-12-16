
## ACTIVATE(addr,subaddr)

Send DCC Accessory Activate packet (gate on then off)

- addr DCC short address of accessory
- subaddr DCC sub address

## ACTIVATEL(linearaddr)

Send DCC Accessory Activate packet (gate on then off)

- linearaddr DCC linear address of accessory

## AFTER(vpin,timer...)

Wait for sensor activated, then deactivated for given time

- vpin Virtual Pin number of sensor
- timer... optional wait in ms, default 500

## AFTEROVERLOAD(track_id)

Wait for overload to be resolved

- track_id A..H

## ALIAS(name,value...)

defines a named numeric value.

- name c++ variable name that can be used throughout the script
- value...  if omitted, a large negative value is created automatically

## AMBER(signal_id)

Sets a signal to amber state

see ONAMBER


## ANOUT(vpin,value,param1,param2)

Writes to the HAL analog output interface of a device driver.

- vpin Virtual pin number of device
- value basic analog value
- param1 device dependent
- param2 device dependent

## AT(vpin)

Wait until a sensor becomes active

- vpin Virtual pin of sensor. Use negative value for sensors that are HIGH when activated

## ASPECT(address,value)

Sends a DCC aspect value to an accessory address. May also change status of a signal defined using this aspect.

- address Linear DCC address of device
- value Aspect value (Device dependent)

## ATGTE(vpin,value)

Wait for analog sensor to be greater than given value

- vpin Analog pin number
- value integer value to compare against

## ATLT(vpin,value)

Wait for analog sensor value to be less than given value

- vpin Analog pin number
- value integer value to compare against

## ATTIMEOUT(vpin,timeout_ms)

Wait for sensor active, with timeout. Use IFTIMEOUT to determine whether the AT was satisfied.

see IFTIMEOUT

- vpin Sensor pin number
- timeout_ms Milliseconds to wait before timeout

## AUTOMATION(sequence_id,description)

Defines starting point of a sequence that will be shown as an Automation by

the throttles. Automations are started by the throttle handing over a loco id to be driven.

- sequence_id Unique sequence id value
- description (Quoted text) will be shown on throttle button

## AUTOSTART

A new task will be created starting from this point at Command Station startup


## BLINK(vpin,onDuty,offDuty)

Starts a blinking process for a vpin (typically a LED). Stop blink with SET or RESET.

- vpin Pin to blink
- onDuty Milliseconds with LED ON
- offDuty Milliseconds with LED off

## BROADCAST(msg)

Send raw message text to all throttles using the DCC-EX protocol

see WITHROTTLE

- msg  Quoted message

## BUILD_CONSIST(loco_id)

Adds a loco to follow the current loco in a consist

- loco_id may be negative to indicate loco facing backwards

## BREAK_CONSIST

Breaks up any consist involving the current loco


## CALL(sequence_id)

transfer control to another sequence with expectation to return

see RETURN

- sequence_id SEQUENCE to jump processing to, must terminate or RETURN

## CLEAR_STASH(stash_id)

Clears loco value stored in stash

- stash_id which stash to clear.

## CLEAR_ALL_STASH

Clears all stashed loco values


## CLEAR_ANY_STASH

Clears loco value from all stash entries


## CLOSE(turnout_id)

Close turnout by id

see THROW


## CONFIGURE_SERVO(vpin,pos1,pos2,profile)

Set up servo movement parameters for non-turnout

- vpin must refer to a servo capable pin
- pos1 SET position of servo
- pos2 RESET position of servo
- profile Movement profile (Instant, Fast, Medium, Slow, Bounce)

## DCC_SIGNAL(signal_id,addr,subaddr)

Define a DCC accessory signal with short address

- signal_id Id used for all signal manipulation commands
- addr DCC address
- subaddr DCC subaddress

## DCCX_SIGNAL(signal_id,redAspect,amberAspect,greenAspect)

Define advanced DCC accessory signal with aspects

- signal_id DCC Linear address AND Id used for all signal manipulation commands

## DCC_TURNTABLE(turntable_id,home,description...)

defines a Turntable device

- homeAngle the angle of the home position, valid angles are 0 - 3600
- description... Quoted text description of turntable

## DEACTIVATE(addr,subaddr)

Sends DCC Deactivate packet (gate on, gate off)

- addr DCC accessory address
- subaddr DCC accessory subaddress

## DEACTIVATEL(addr)

Sends DCC Deactivate packet (gate on, gate off)

- addr DCC Linear accessory address

## DELAY(delay_ms)

Waits for given milliseconds delay (This is not blocking)

- delay_mS Delay time in milliseconds

## DELAYMINS(delay_minutes)

Waits for given minutes delay (This is not blocking)


## DELAYRANDOM(mindelay,maxdelay)

Waits for random delay between min and max milliseconds (This is not blocking)

- mindelay minimum delay in ms
- maxdelay maximum delay in ms

## DONE

Stops task loco (if any) and terminates current task


## DRIVE(analogpin)

RESERVED do not use


## ELSE

introduces alternate processing path after any kind of IF

see IF


## ENDEXRAIL

obsolete.. no longer needed. Does nothing.


## ENDIF

determines end of IF(any type)  block.

IF something ENDIF, or

IF something ELSE something ENDIF

see IF


## ENDTASK

same as DONE

see DONE


## ESTOP

Performs emergency stop on current task loco


## ESTOPALL

Performs emergency stop on all locos


## EXRAIL

obsolete.. no longer needed. Does nothing.


## EXTT_TURNTABLE(id,vpin,home,description...)

Defines the EXΓÇæTurntable turntable/traverser object only, so you will need a separate HAL() statement for an EXΓÇæTurntable device driver.

- homeAngle  the angle of the home position, valid angles are 0 - 3600
- quoted description...

## FADE(vpin,value,ms)

Modifies analog value slowly taking a given time

- vpin Servo virtual pin number
- value new target value
- ms time to reach value

## FOFF(func)

Turns off current loco function

see FON


## FOLLOW(sequence_id)

Task processing follows given route or sequence (Effectively a GoTo)


## FON(func)

Turn on current loco function

see FOFF


## FORGET

Removes current loco from task and DCC reminders table.


## FREE(token_id)

Frees logical token

see RESERVE

- token_id 0..255

## FREEALL

Frees all logical tokens

see RESERVE


## FTOGGLE(func)

Toggles function for current loco


## FWD(speed)

Instructs current loco to set DCC speed

- speed 0..127   (1=ESTOP)

## GREEN(signal_id)

Sets signal to green state


## HAL(haltype,params...)

Defines VPIN mapping for specific hardware drivers

- haltype driver name, normally device type
- params... depend on driver.

## HAL_IGNORE_DEFAULTS

System will ignore default HAL device mappings


## IF(vpin)

Checks sensor state, If false jumps to matching nested ELSE or ENDIF

- vpin  VPIN of sensor. Negative VPIN will invert sensor state.

## IFAMBER(signal_id)

Checks if signal is in AMBER state.

see IF


## IFCLOSED(turnout_id)

Checks if given turnout is in close state

see IF


## IFGREEN(signal_id)

Checks if given signal is in GREEN state

see IF


## IFGTE(vpin,value)

Checks if analog vpin sensor >= value

see IF


## IFLOCO(loco_id)

Checks if current task loco = loco_id

see IF


## IFLT(vpin,value)

Checks if analog sensor < value

see IF

- vpin  Analog vpin of sensor

## IFNOT(vpin)

Inverse of IF

see IF


## IFRANDOM(percent)

randomly satisfied IF at given percent probability

see IF


## IFRED(signal_id)

Checks if given signal is in RED state

see IF


## IFSTASH(stash_id)

Checks if given stash entry has a non-zero value

see IF


## IFSTASHED_HERE(stash_id)

Checks if given stash entry has the current loco

see IF


## IFTHROWN(turnout_id)

Checks if given turnout is in THROWN state

see IF


## IFRESERVE(token_id)

Attempts to reserve token and if satisfiled the token remains reserved.

see IF RESERVE FREE


## IFTIMEOUT

Checks TIMEOUT state after an AT/AFTER request with timeout value.

see IF AT AFTER


## IFTTPOSITION(turntable_id,position)

Checks if Turntable is in given position

see IF


## IFRE(vpin,value)

Checks external rotary encoder value

- vpin of device driver for rotary encoder

## IFBITMAP_ALL(vpin,mask)

Checks if (vpin pseudo-analog value & mask) == mask.

see IF

- mask Binary mask applied to vpin value

## IFBITMAP_ANY(vpin,mask)

Checks if vpin pseudo-analog value & mask is non-zero

see IF

- mask Binary mask applied to vpin value

## IFROUTE_ACTIVE(sequence_id)

Checks if route is active

see IF


## IFROUTE_INACTIVE(sequence_id)

Checks if route is inactive

see IF


## IFROUTE_HIDDEN(sequence_id)

Checks if route is hidden

see IF


## IFROUTE_DISABLED(sequence_id)

Checks if route is disabled

see IF


## INVERT_DIRECTION

Marks current task so that FWD and REV commands are inverted.


## JMRI_SENSOR(vpin,count...)

Defines multiple JMRI `<s>` type sensor feedback definitions each with id matching vpin and INPUT_PULLUP

- vpin first vpin number
- count... Number of consecutive VPINS for which to create JMRI sensor feedbacks. Default 1.

## JMRI_SENSOR_NOPULLUP(vpin,count...)

Defines multiple JMRI `<s>` type sensor feedback definitions each with id matching vpin

- vpin first vpin number
- count... Number of consecutive VPINS for which to create JMRI sensor feedbacks. Default 1.

## JOIN

Switches PROG track to receive MAIN track DCC packets. (Drive on PROG track)


## KILLALL

Terminates all running EXRAIL tasks


## LATCH(vpin)

Make all AT/AFTER/IF see vpin as HIGH without checking hardware

- vpin Must only be for VPINS 0..255

## LCC(eventid)

Issue event to LCC


## LCCX(senderid,eventid)

Issue LCC event while impersonating another sender


## LCD(row,msg)

Write message on row of default configured LCD/OLED

see SCREEN

- msg Quoted text

## MOMENTUM(accel,decel...)

sets momentum in ms per DCC 127 step for current loco.

- accel Acceleration momentum
- decel... Braking momentum. (=Acceleration if not given)

## SCREEN(display,row,msg)

Send message to external display handlers

- display number, 0=local display, others are handled by external
displays which may have different display numbers on different devices.

- msg Quoted text

## LCN(msg)

Reserved for LCN communication. Refer to their documentation.


## MESSAGE(msg)

Send a human readable message to all throttle users

- msg Quoted text

## MOVETT(turntable_id,steps,activity)

Move Turntable to specific position

see ROTATE

- steps position to move to
- activity see ROTATE

## NEOPIXEL(vpin,r,g,b,count...)

Set a NEOPIXEL vpin to a given red/green/blue colour

- vpin VPIN of a pixel
- r red component 0-255
- g green component 0-255
- b blue component 0-255
- count... Number of consecutive pixels to set, Default 1.

## NEOPIXEL_SIGNAL(vpin,redcolour,ambercolour,greencolour)

Define a signal that uses a single multi colour pixel

see NEORGB

- vpin unique signal_id
- redcolour  RGB colour use NEORGB(red,green,blue) to create values.

## ACON(eventid)

Send MERG CBUS ACON to Adapter


## ACOF(eventid)

Send MERG CBUS ACOF to Adapter


## ONACON(eventid)

Start task here when ACON for event received from MERG CBUS


## ONACOF(eventid)

Start task here when ACOF for event received from MERG CBUS


## ONACTIVATE(addr,subaddr)

Start task here when DCC Activate sent for short address


## ONACTIVATEL(linear)

Start task here when DCC Activate sent for linear address


## ONAMBER(signal_id)

Start task here when signal set to AMBER state


## ONBLOCKENTER(block_id)

Start task here when a loco enters a railcom block

- block_id vpin associated to block by HAL(I2CRailcom..)

## ONBLOCKEXIT(block_id)

Start task here when a loco leaves a railcom block

- block_id vpin associated to block by HAL(I2CRailcom..)

## ONTIME(minute_in_day)

Start task here when fastclock matches

- minute_in_day (0..1439)

## ONCLOCKTIME(hours,mins)

Start task here when fastclock matches time


## ONCLOCKMINS(mins)

Start task here hourly when fastclock minutes matches


## ONOVERLOAD(track_id)

Start task here when given track goes into overload

- track_id A..H

## ONRAILSYNCON

Start task here when the railsync (booster) input port get a valid DCC signal


## ONRAILSYNCOFF

Start task here when the railsync (booster) input port does not get a valid DCC signal any more


## ONDEACTIVATE(addr,subaddr)

Start task here when DCC deactivate packet sent


## ONDEACTIVATEL(linear)

Start task here when DCC deactivate sent to linear address


## ONCLOSE(turnout_id)

Start task here when turnout closed


## ONLCC(sender,event)

Start task here when LCC event arrives from sender


## ONGREEN(signal_id)

Start task here when signal set to GREEN state


## ONRED(signal_id)

Start task here when signal set to RED state


## ONROTATE(turntable_id)

Start task here when turntable is rotated


## ONTHROW(turnout_id)

Start task here when turnout is Thrown


## ONCHANGE(vpin)

Rotary encoder change starts task here (This is obscurely different from ONSENSOR which will be merged in a later release.)


## ONSENSOR(vpin)

Start task here when sensor changes state (debounced)


## ONBITMAP(vpin)

Start task here when bitmap sensor changes state (debounced)


## ONBUTTON(vpin)

Start task here when sensor changes HIGH to LOW.


## PAUSE

Pauses all EXRAIL tasks except the current one.

Other tasks ESTOP their locos until RESUME issued


## PIN_TURNOUT(id,vpin,description...)

Defines a turnout which operates on a single pin

- description... Quoted text (shown to throttles) or HIDDEN

## PRINT(msg)

prints diagnostic message on USB serial

- msg Quoted text

## PARSE(msg)

Executes `<>` command as if entered from serial

- msg Quoted text, preferably including `<>`

## PICKUP_STASH(stash_id)

see STASH

Loads stashed value into current task loco

- stash_id position in stash where a loco id was previously saved.

## POM(cv,value)

Write value to cv on current tasks loco (Program on Main)


## POWEROFF

Powers off all tracks


## POWERON

Powers ON all tracks


## RANDOM_CALL(sequence_id...)

CALL to another sequence randomly chosen from list

see CALL

- sequence_id.. list of SEQUENCE that may be called, each must terminate or RETURN

## RANDOM_FOLLOW(sequence_id...)

jump to another sequence randomly chosen from list

see FOLLOW

- sequence_id.. list of SEQUENCE that may be followed

## READ_LOCO

Reads loco Id from prog track and sets currenmt task loco id.


## RED(signal_id)

sets signal to RED state


## RESERVE(token_id)

Waits for token for block. If not available immediately, current task loco is stopped.


## RESET(vpin,count...)

Sets output pin LOW

see SET

- count... Number of consecutive pins, default 1

## RESTORE_SPEED

Resumes locos saved speed

see SAVE_SPEED


## RESUME

Resumes PAUSEd tasks

see PAUSE


## RETURN

Returns to CALL

see CALL


## REV(speed)

Issues DCC speed packet for current loco in reverse.

see FWD

- speed  (0..127, 1=ESTOP)

## ROTATE(turntable_id,position,activity)

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


## ROTATE_DCC(turntable_id,position_id)

Rotates turntable to a given position using DCC commands


## ROSTER(cab,name,funcmap...)

Describes a loco roster entry visible to throttles

- cab loco DCC address or 0 for default entry
- name Quoted text
- funcmap... Quoted text, optional list of function names separated by / character with momentary function names prefixed with an *.

## ROUTE(sequence_id,description)

Defines starting point of a sequence that will appear as a route on throttle buttons.

- description Quoted text, throttle button caption.

## ROUTE_ACTIVE(sequence_id)

Tells throttle to display the route button as active

- sequence_id of ROUTE/AUTOMATION

## ROUTE_INACTIVE(sequence_id)

Tells throttle to display the route button as inactive

- sequence_id of ROUTE/AUTOMATION

## ROUTE_HIDDEN(sequence_id)

Tells throttle to hide the route button

- sequence_id of ROUTE/AUTOMATION

## ROUTE_DISABLED(sequence_id)

Tells throttle to display the route button as disabled

- sequence_id of ROUTE/AUTOMATION

## ROUTE_CAPTION(sequence_id,caption)

Tells throttle to change thr route button caption

- sequence_id of ROUTE/AUTOMATION

## SAVE_SPEED

Resumes locos saved speed

see RESTORE_SPEED


## SENDLOCO(cab,sequence_id)

Start a new task to drive the loco

- cab loco to be driven
- route sequence_id of route, automation or sequence to drive

## SEQUENCE(sequence_id)

Provides a unique label that can be used to call, follow or start.

see CALL

see FOLLOW

see START


## SERIAL(msg)

Write direct to Serial output

- msg Quoted text

## SERIAL1(msg)

Write direct to Serial1 output

- msg Quoted text

## SERIAL2(msg)

Write direct to Serial2 output

- msg Quoted text

## SERIAL3(msg)

Write direct to Serial3 output

- msg Quoted text

## SERIAL4(msg)

Write direct to Serial4 output

- msg Quoted text

## SERIAL5(msg)

Write direct to Serial5 output

- msg Quoted text

## SERIAL6(msg)

Write direct to Serial6 output

- msg Quoted text

## SERVO(vpin,position,profile)

Move servo to given position

- vpin of servo
- position  servo position (values are hardware dependent)
- profile movement profile (Instant, Fast, Medium, Slow, Bounce)

## SERVO2(vpin,position,duration)

Move servo to given position taking time

- vpin of servo
- position  servo position (values are hardware dependent)
- duration mS

## SERVO_SIGNAL(vpin,redpos,amberpos,greenpos)

Dedfine a servo based signal with 3 servo positions

- vpin of servo, acts as signal_id
- redpos servo position (values are hardware dependent)
- amberpos servo position (values are hardware dependent)
- greenpos servo position (values are hardware dependent)

## SERVO_TURNOUT(turnout_id,vpin,activeAngle,inactiveAngle,profile,description...)

Define a servo driven turnout

- turnout_id used by THROW/CLOSE
- vpin for servo
- activeAngle servo position (values are hardware dependent)
- inactiveAngle servo position (values are hardware dependent)
- profile movement profile (Instant, Fast, Medium, Slow, Bounce)
- description... Quoted text shown to throttles or HIDDEN keyword to hide turnout button

## SET(vpin,count...)

Set pin HIGH

see RESET

- count...  Number of sequential vpins to set. Default 1.

## SET_TRACK(track,mode)

Set output track type

- track A..H
- mode NONE, MAIN, PROG, DC, EXT, BOOST, BOOST_INV, BOOST_AUTO, MAIN_INV, MAIN_AUTO, DC_INV, DCX

## SET_POWER(track,onoff)

Set track power mode

- track A..H
- onoff ON or OFF

## SETLOCO(loco)

Sets the loco being handled by the current task


## SETFREQ(freq)

Sets the DC track PWM frequency

- freq Frequency is default 0, or 1..3

## SIGNAL(redpin,amberpin,greenpin)

Define a Signal with LOW=on leds

see SIGNALH

- redpin vpin for RED state, also acts as signal_id

## SIGNALH(redpin,amberpin,greenpin)

define a signal with HIGH=ON leds

- redpin vpin for RED state, also acts as signal_id

## SPEED(speed)

Changes current tasks loco speed without changing direction

- speed 0..127 (1=ESTOP)

## START(sequence_id)

Starts a new task at the given route/animation/sequence


## START_SHARED(sequence_id)

Starts a new task at the given route/animation/sequence and share current loco with it


## START_SEND(sequence_id)

Starts a new task at the given route/animation/sequence and send current loco to it. Remove loco from current task.


## STASH(stash_id)

saves current task's loco id in the stash array

- stash_id  position in stash array to save loco id

## STEALTH(code...)

Allows for embedding raw C++ code in context of current task.

- code... c++ code to be executed. This requires intimate understanding of the product architecture.

## STEALTH_GLOBAL(code...)

Allows for embedding raw c++ code out of context.

- code...  c++ code to be defined. This requires intimate understanding of the product architecture.

## STOP

Same as SPEED(0)


## THROW(turnout_id)

Throws given turnout

see CLOSE


## TOGGLE_TURNOUT(turnout_id)

Toggles given turnout


## TT_ADDPOSITION(turntable_id,position_id,value,angle,description...)

Defines a turntable track position

- position_id each position is given an id
- address DCC accessory address
- angle Used only for throttles that may draw a visual representation of the turntable
- description... quoted text or HIDDEN

## TURNOUT(turnout_id,addr,subaddr,description...)

Defines a DCC accessory turnout with legacy address

- turnout_id to be used in THROW/CLOSE etc
- addr DCC accessory address
- subaddr DCC accessory subaddress
- description... Quoted text or HIDDEN, appears on throttle buttons

## TURNOUTL(turnout_id,addr,description...)

Defines a DCC accessory turnout with linear address

see TURNOUT

- turnout_id to be used in THROW/CLOSE etc
- addr DCC accessory linear address
- description... Quoted text or HIDDEN, appears on throttle buttons

## UNJOIN

Disconnects PROG track from MAIN

see JOIN


## UNLATCH(vpin)

removes latched on flag

see LATCH

- vpin (limited to 0..255)

## VIRTUAL_SIGNAL(signal_id)

Defines a virtual (no hardware) signal, use ONhandlers to simulate hardware

see SIGNAL ONRED ONAMBER ONGREEN


## VIRTUAL_TURNOUT(id,description...)

Defines a virtual (no hardware) turnout, use ONhandlers to simulate hardware

see TURNOUT ONCLOSE ONTHROW

- description... quoted text or HIDDEN

## BITMAP_AND(vpin1,mask)

Performs a bitwise AND operation on the given vpin analog value and mask.

- mask Binary mask to be ANDed with vpin1 value

## BITMAP_INC(vpin)

Increments pseudo analog value by 1


## BITMAP_DEC(vpin)

Decrements pseudo analog value by 1  (to zero)


## BITMAP_OR(vpin1,mask)

Performs a bitwise OR operation on the given vpin analog value and mask.

- mask Binary mask to be ORed with vpin1 value

## BITMAP_XOR(vpin1,mask)

Performs a bitwise XOR operation on the given vpin analog value and mask.

- mask Binary mask to be XORed with vpin1 value

## WAITFOR(pin)

Waits for completion of servo movement


## WAITFORTT(turntable_id)

waits for completion of turntable movement


## VIRTUAL_SIGNAL(signal_id)

Defines a virtual (no hardware) signal, use ONhandlers to simulate hardware

see SIGNAL


## WAIT_WHILE_RED(signal_id)

Keeps loco at speed 0 while signal is RED


## WITHROTTLE(msg)

Broadcasts a string in Withrottle protocol format to all throttles using this protocol.

- msg quoted string

## XFOFF(cab,func)

Turns function off for given loco

- func function number

## XFON(cab,func)

Turns function ON for given loco


## XFTOGGLE(cab,func)

Toggles function state for given loco


## XFWD(cab,speed)

Sends DCC speed to loco in forward direction

- speed (0..127, 1=ESTOP)

## XREV(cab,speed)

Sends DCC speed to loco in reverse direction

- speed (0..127, 1=ESTOP)

## XPOM(cab,cv,value)

Sends DCC speed to loco in reverse direction

- cab loco id
- cv  to be updated
- value to be written to cv

## XRESTORE_SPEED(cab)

Resumes locos saved speed

- cab loco id
see XSAVE_SPEED


## XSAVE_SPEED(cab)

Resumes locos saved speed

- cab loco id
see XRESTORE_SPEED


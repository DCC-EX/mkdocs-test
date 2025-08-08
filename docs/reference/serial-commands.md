# Serial Commands

```<#>```

Request number of simultaneously supported locos

```<!>```

Emergency stop all locos

```<t loco>```

Request loco status

```<t loco tspeed direction>```

Set throttle speed(0..127) and direction (0=reverse, 1=fwd)

```<t ignore loco tspeed direction>```

(Deprecated) Set throttle speed and direction

```<f loco byte1>```

(Deprecated use F) Set loco function group

```<f loco group byte2>```

(Deprecated use F) Set loco function group

```<T>```

List all turnouts

```<T id>```

Delete turnout

```<T id X>```

List turnout details

```<T id T>```

Throw Turnout

```<T id C>```

Close turnout#

```<T id value>```

Close (value=0) ot Throw turnout

```<T id SERVO vpin closedValue thrownValue>```

Create Servo turnout  

```<T id VPIN vpin>```

Create pin turnout

```<T id DCC addr subadd>```

Create DCC turnout

```<T id DCC linearAddr>```

Create DCC turnout

```<T id addr subadd>```

Create DCC turnout

```<T id vpin closedValue thrownValue>```

Create SERVO turnout

```<S id vpin pullup>```

Create Sensor

```<S id>```

Delete sensor

```<S>```

List sensors

```<J M>```

List stash values

```<J M stash_id>```

get stash value

```<J M CLEAR ALL>```

Clear all stash values

```<J M CLEAR stash_id>```

Clear given stash

```<J M stashId locoId>```

Set stash value


```<J M CLEAR ANY locoId>```

Clear all stash entries that contain locoId


```<J C>```

get fastclock time


```<J C mmmm nn>```

Set fastclock time


```<J G>```

FReport gauge limits 


```<J I>```

Report currents 


```<J A>```

List Routes


```<J R>```

List Roster


```<J R id>```

Get roster for loco


```<J T>```

Get turnout list 


```<J T id>```

Get turnout state and description


```<z vpin>```

Set pin. HIGH iv vpin positive, LOW if vpin negative  


```<z vpin analog profile duration>```

Change analog value over duration (Fade or servo move)


```<z vpin analog profile>```

Write analog device using profile number (Fade or servo movement)


```<z vpin analog>```

Write analog device value


```<I>```

List all turntables


```<I id>```

Broadcast turntable type and current position    


```<I id position>```

Rotate a DCC turntable


```<I id DCC home>```

Create DCC turntable


```<I id position activity>```

Rotate an EXTT turntable


```<I id EXTT vpin home>```

Create an EXTT turntable


```<I id ADD position value angle>```

Add turntable position


```<Q>```

List all sensors 


```<s>```

Command station status


```<E>```

STORE EPROM


```<e>```

CLEAR EPROM


```<Z>```

List Output definitions 


```<Z id pin iflag>```

Create Output


```<Z id active>```

Set output 


```<Z id>```

Delete output


```<D ACK ON>```

Enable PROG track diagnostics


```<D ACK OFF>```

Disable PROG track diagnostics


```<D CABS>```

Diagnostic display loco state table


```<D RAM>```

Diagnostic display free RAM


```<D CMD ON>```

Enable command input diagnostics


```<D CMD OFF>```

Disable command input diagnostics


```<D RAILCOM ON>```

Enable Railcom diagnostics


```<D RAILCOM OFF>```

DIsable Railcom diagnostics


```<D WIFI ON>```

Enable Wifi diagnostics


```<D WIFI OFF>```

Disable Wifi diagnostics


```<D ETHERNET ON>```

Enable Ethernet diagnostics


```<D ETHERNET OFF>```

Disabel Ethernet diagnostics 


```<D WIT ON>```

Enable Withrottle diagnostics


```<D WIT OFF>```

Disable Withrottle diagnostics 


```<D LCN ON>```

Enable LCN Diagnostics


```<D LCN OFF>```

Disabel LCN diagnostics


```<D WEBSOCKET ON>```

Enable Websocket diagnostics 


```<D WEBSOCKET OFF>```

Disable wensocket diagnostics 


```<D EEPROM numentries>```

Dump EEPROM contents


```<D ANOUT vpin position>```

see <z vpin position>


```<D ANOUT vpin position profile>```

see <z vpin position profile>


```<D SERVO vpin position>```

Test servo


```<D SERVO vpin position profile>```

Test servo


```<D ANIN vpin>```

Display analogue input value


```<D HAL SHOW>```

Show HAL devices table


```<D HAL RESET>```

Reset all HAL devices


```<D TT vpin steps>```

Test turntable


```<D TT vpin steps activity>```

Test turntable


```<C PROGBOOST>```

Configute PROG track boost


```<C RESET>```

Reset and restart command station


```<C SPEED28>```

Set all DCC speed commands as 28 step to old decoders


```<C SPEED128>```

Set all DCC speed commands to 128 step (default)


```<C RAILCOM ON>```

Enable Railcom cutout 


```<C RAILCOM OFF>```

Disable Railcom cutout


```<C RAILCOM DEBUG>```

Enable Railcom cutout for easy scope reading test


```<D ACK LIMIT value>```

Set ACK detection limit mA


```<D ACK MIN value MS>```

Set ACK minimum duration mS


```<D ACK MIN value>```

Set ACK minimum duration uS


```<D ACK MAX value MS>```

Set ACK maximum duration mS


```<D ACK MAX value>```

Set ACK maximum duration uS


```<D ACK RETRY value>```

Set ACK retry count


```<C WIFI "ssid" "password">```

reconfigure stored wifi credentials 


```<o vpin>```

Set neopixel on(vpin>0) or off(vpin<0)


```<o vpin count>```

Set multiple neopixels on(vpin>0) or off(vpin<0)


```<o vpin r g b>```

Set neopixel colour


```<o vpin r g b count>```

Set multiple neopixels colour 


```<1>```

Power ON all tracks


```<1 MAIN>```

Power on MAIN track


```<1 PROG>```

Power on PROG track


```<1 JOIN>```

JOIN prog track to MAIN and power


```<1 track>```

Power on given track


```<0>```

Power off all tracks


```<0 MAIN>```

Power off MAIN track


```<0 PROG>```

Power off PROG track


```<0 track>```

Power off given track


```<c>```

Report main track currect (Deprecated)


```<a address subaddress activate>```

Send DCC accessory command


```<a address subaddress activate onoff>```

Send DCC accessory command with onoff control (==TODO==.. numbers) 


```<a linearaddress activate>```

send dcc accessory command      


```<A address value>```

Send DCC extended accessory (Aspect) command


```<w loco cv value>```

POM write cv on main track


```<r loco cv>```

POM read cv on main track


```<b loco cv bit bitvalue>```

POM write cv bit on main track


```<m LINEAR>```

Set Momentum algorithm to linear acceleration


```<m POWER>```

Set momentum algortithm to very based on difference between current speed and throttle seting


```<m loco momentum>```

set momentum for loco (accel and braking)


```<m loco accelerating braking>```

set momentum for loco


```<W cv value ignore1 ignore2>```

(Deprecated) Write cv value on PROG track


```<W loco>```

Write loco address on PROG track


```<W CONSIST loco REVERSE>```

Write consist address and reverse flag on PROG track 


```<W CONSIST loco>```

write consist address on PROG track       


```<W cv value>```

Write cv value on PROG track


```<W cv bitvalue bit>```

Write cv bit on prog track


```<V cv value>```

Fast read cv with expected value


```<V cv bit bitvalue>```

Fast read bit with expected value


```<B cv bit bitvalue>```

Write cv bit


```<R cv ignore1 ignore2>```

(Deprecated) read cv value on PROG track


```<R cv>```

Read cv


```<R>```

Read driveable loco id (may be long, short or consist)


```<->```

Clear loco state and reminder table


```<- loco>```

remove loco state amnd reminders


```<F loco DCCFREQ freqvalue>```

Set DC frequencey for loco   


```<F loco function onoff>```

Set loco function ON/OFF


```<M ignore d0 d1 d2 d3 d4 d5>```

Send up to 5 byte DCC packet on MAIN track (all d values in hex)


```<P ignore d0 d1 d2 d3 d4 d5>```

Send up to 5 byte DCC packet on PROG track (all d values in hex)


```<J O>```

List turntable IDs


```<J O id>```

List turntable state


```<J P id>```

list turntable positions


```<=>```

list track manager states


```<= track MAIN>```

Set track to MAIN


```<= track MAIN_INV>```

Set track to MAIN inverted polatity


```<= track MAIN_AUTO>```

Set track to MAIN with auto reversing


```<= track PROG>```

Set track to PROG


```<= track OFF>```

Set track power OFF


```<= track NONE>```

Set track no output


```<= track EXT>```

Set track to use external sync


```<= track AUTO>```

Update track to auto reverse


```<= track INV>```

Update track to inverse polarity


```<= track DC loco>```

Set track to DC


```<= track DC_INV loco>```

Set track to DC with inverted polarity


```<= track DCX loco>```

Set track to DC with inverted polarity

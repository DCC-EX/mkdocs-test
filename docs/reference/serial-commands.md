# DCC Command Station Protocol

==TODO== Review tables and commands

Complete reference guide for serial commands used with DCC command stations.

## System Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `<#>` | Request number of simultaneously supported locos | None |
| `<!>` | Emergency stop all locos | None |
| `<s>` | Command station status | None |
| `<E>` | Store EEPROM | None |
| `<e>` | Clear EEPROM | None |

## Power Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<1>` | Power ON all tracks | None |
| `<1 MAIN>` | Power on MAIN track | None |
| `<1 PROG>` | Power on PROG track | None |
| `<1 JOIN>` | JOIN prog track to MAIN and power | None |
| `<1 track>` | Power on given track | `track`: Track identifier |
| `<0>` | Power off all tracks | None |
| `<0 MAIN>` | Power off MAIN track | None |
| `<0 PROG>` | Power off PROG track | None |
| `<0 track>` | Power off given track | `track`: Track identifier |

## Locomotive Control

| Command | Description | Parameters | Status |
|---------|-------------|------------|--------|
| `<t loco>` | Request loco status | `loco`: Locomotive ID | Active |
| `<t loco tspeed direction>` | Set throttle speed and direction | `loco`: ID, `tspeed`: 0-127, `direction`: 0/1 | Active |
| `<t ignore loco tspeed direction>` | Set throttle speed and direction | Legacy format | ⚠️ Deprecated |
| `<- loco>` | Remove loco state and reminders | `loco`: Locomotive ID | Active |
| `<->` | Clear loco state and reminder table | None | Active |

## Function Control

| Command | Description | Parameters | Status |
|---------|-------------|------------|--------|
| `<F loco function onoff>` | Set loco function ON/OFF | `loco`: ID, `function`: Function number, `onoff`: 0/1 | Active |
| `<F loco DCCFREQ freqvalue>` | Set DC frequency for loco | `loco`: ID, `freqvalue`: Frequency value | Active |
| `<f loco byte1>` | Set loco function group | `loco`: ID, `byte1`: Function byte | ⚠️ Deprecated |
| `<f loco group byte2>` | Set loco function group | `loco`: ID, `group`: Group ID, `byte2`: Function byte | ⚠️ Deprecated |

## Turnout Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<T>` | List all turnouts | None |
| `<T id>` | Delete turnout | `id`: Turnout ID |
| `<T id X>` | List turnout details | `id`: Turnout ID |
| `<T id T>` | Throw turnout | `id`: Turnout ID |
| `<T id C>` | Close turnout | `id`: Turnout ID |
| `<T id value>` | Close (value=0) or Throw turnout | `id`: Turnout ID, `value`: 0/1 |
| `<T id SERVO vpin closedValue thrownValue>` | Create servo turnout | `id`: ID, `vpin`: Pin, values for positions |
| `<T id VPIN vpin>` | Create pin turnout | `id`: ID, `vpin`: Pin number |
| `<T id DCC addr subadd>` | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address |
| `<T id DCC linearAddr>` | Create DCC turnout | `id`: ID, `linearAddr`: Linear address |
| `<T id addr subadd>` | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address |
| `<T id vpin closedValue thrownValue>` | Create SERVO turnout | `id`: ID, `vpin`: Pin, position values |

## Sensor Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<S id vpin pullup>` | Create sensor | `id`: Sensor ID, `vpin`: Pin, `pullup`: Pull-up setting |
| `<S id>` | Delete sensor | `id`: Sensor ID |
| `<S>` | List sensors | None |
| `<Q>` | List all sensors | None |

## CV Programming

| Command | Description | Parameters | Status |
|---------|-------------|------------|--------|
| `<W cv value>` | Write CV value on PROG track | `cv`: CV number, `value`: Value | Active |
| `<W loco>` | Write loco address on PROG track | `loco`: Address | Active |
| `<W CONSIST loco>` | Write consist address on PROG track | `loco`: Address | Active |
| `<W CONSIST loco REVERSE>` | Write consist address and reverse flag | `loco`: Address | Active |
| `<W cv bitvalue bit>` | Write CV bit on prog track | `cv`: CV, `bitvalue`: Bit value, `bit`: Bit position | Active |
| `<W cv value ignore1 ignore2>` | Write CV value on PROG track | Legacy format | ⚠️ Deprecated |
| `<R cv>` | Read CV | `cv`: CV number | Active |
| `<R>` | Read driveable loco ID | None | Active |
| `<R cv ignore1 ignore2>` | Read CV value on PROG track | Legacy format | ⚠️ Deprecated |
| `<V cv value>` | Fast read CV with expected value | `cv`: CV number, `value`: Expected value | Active |
| `<V cv bit bitvalue>` | Fast read bit with expected value | `cv`: CV, `bit`: Bit position, `bitvalue`: Expected | Active |
| `<B cv bit bitvalue>` | Write CV bit | `cv`: CV number, `bit`: Bit position, `bitvalue`: Value | Active |
| `<w loco cv value>` | POM write CV on main track | `loco`: ID, `cv`: CV number, `value`: Value | Active |
| `<r loco cv>` | POM read CV on main track | `loco`: ID, `cv`: CV number | Active |
| `<b loco cv bit bitvalue>` | POM write CV bit on main track | `loco`: ID, `cv`: CV, `bit`: Position, `bitvalue`: Value | Active |

## DCC Accessory Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `<a address subaddress activate>` | Send DCC accessory command | `address`: Address, `subaddress`: Sub-address, `activate`: 0/1 |
| `<a address subaddress activate onoff>` | Send DCC accessory command with on/off | `address`: Address, `subaddress`: Sub, `activate`: 0/1, `onoff`: 0/1 |
| `<a linearaddress activate>` | Send DCC accessory command | `linearaddress`: Linear address, `activate`: 0/1 |
| `<A address value>` | Send DCC extended accessory (Aspect) command | `address`: Address, `value`: Aspect value |

## Momentum Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<m LINEAR>` | Set momentum algorithm to linear acceleration | None |
| `<m POWER>` | Set momentum algorithm based on speed difference | None |
| `<m loco momentum>` | Set momentum for loco (accel and braking) | `loco`: ID, `momentum`: Value |
| `<m loco accelerating braking>` | Set momentum for loco | `loco`: ID, `accelerating`: Value, `braking`: Value |

## Output Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<Z>` | List output definitions | None |
| `<Z id pin iflag>` | Create output | `id`: Output ID, `pin`: Pin number, `iflag`: Invert flag |
| `<Z id active>` | Set output | `id`: Output ID, `active`: 0/1 |
| `<Z id>` | Delete output | `id`: Output ID |

## Pin Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<z vpin>` | Set pin HIGH if vpin positive, LOW if negative | `vpin`: Pin number (signed) |
| `<z vpin analog>` | Write analog device value | `vpin`: Pin, `analog`: Value |
| `<z vpin analog profile>` | Write analog device using profile | `vpin`: Pin, `analog`: Value, `profile`: Profile ID |
| `<z vpin analog profile duration>` | Change analog value over duration | `vpin`: Pin, `analog`: Value, `profile`: Profile, `duration`: Time |

## NeoPixel Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<o vpin>` | Set neopixel on (vpin>0) or off (vpin<0) | `vpin`: Pin number (signed) |
| `<o vpin count>` | Set multiple neopixels on/off | `vpin`: Pin, `count`: Number of pixels |
| `<o vpin r g b>` | Set neopixel colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue |
| `<o vpin r g b count>` | Set multiple neopixels colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue, `count`: Count |

## Turntable Control

| Command | Description | Parameters |
|---------|-------------|------------|
| `<I>` | List all turntables | None |
| `<I id>` | Broadcast turntable type and current position | `id`: Turntable ID |
| `<I id position>` | Rotate a DCC turntable | `id`: ID, `position`: Position |
| `<I id DCC home>` | Create DCC turntable | `id`: ID, `home`: Home position |
| `<I id position activity>` | Rotate an EXTT turntable | `id`: ID, `position`: Position, `activity`: Activity |
| `<I id EXTT vpin home>` | Create an EXTT turntable | `id`: ID, `vpin`: Pin, `home`: Home position |
| `<I id ADD position value angle>` | Add turntable position | `id`: ID, `position`: Position, `value`: Value, `angle`: Angle |

## JSON Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `<J M>` | List stash values | None |
| `<J M stash_id>` | Get stash value | `stash_id`: Stash identifier |
| `<J M CLEAR ALL>` | Clear all stash values | None |
| `<J M CLEAR stash_id>` | Clear given stash | `stash_id`: Stash identifier |
| `<J M stashId locoId>` | Set stash value | `stashId`: Stash ID, `locoId`: Loco ID |
| `<J M CLEAR ANY locoId>` | Clear all stash entries containing locoId | `locoId`: Locomotive ID |
| `<J C>` | Get fastclock time | None |
| `<J C mmmm nn>` | Set fastclock time | `mmmm`: Minutes, `nn`: Rate |
| `<J G>` | Report gauge limits | None |
| `<J I>` | Report currents | None |
| `<J A>` | List routes | None |
| `<J R>` | List roster | None |
| `<J R id>` | Get roster for loco | `id`: Locomotive ID |
| `<J T>` | Get turnout list | None |
| `<J T id>` | Get turnout state and description | `id`: Turnout ID |
| `<J O>` | List turntable IDs | None |
| `<J O id>` | List turntable state | `id`: Turntable ID |
| `<J P id>` | List turntable positions | `id`: Turntable ID |

## Track Manager

| Command | Description | Parameters |
|---------|-------------|------------|
| `<=>` | List track manager states | None |
| `<= track MAIN>` | Set track to MAIN | `track`: Track identifier |
| `<= track MAIN_INV>` | Set track to MAIN inverted polarity | `track`: Track identifier |
| `<= track MAIN_AUTO>` | Set track to MAIN with auto reversing | `track`: Track identifier |
| `<= track PROG>` | Set track to PROG | `track`: Track identifier |
| `<= track OFF>` | Set track power OFF | `track`: Track identifier |
| `<= track NONE>` | Set track no output | `track`: Track identifier |
| `<= track EXT>` | Set track to use external sync | `track`: Track identifier |
| `<= track AUTO>` | Update track to auto reverse | `track`: Track identifier |
| `<= track INV>` | Update track to inverse polarity | `track`: Track identifier |
| `<= track DC loco>` | Set track to DC | `track`: Track ID, `loco`: Loco ID |
| `<= track DC_INV loco>` | Set track to DC with inverted polarity | `track`: Track ID, `loco`: Loco ID |
| `<= track DCX loco>` | Set track to DC with inverted polarity | `track`: Track ID, `loco`: Loco ID |

## Configuration Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `<C PROGBOOST>` | Configure PROG track boost | None |
| `<C RESET>` | Reset and restart command station | None |
| `<C SPEED28>` | Set all DCC speed commands as 28 step | None |
| `<C SPEED128>` | Set all DCC speed commands to 128 step (default) | None |
| `<C RAILCOM ON>` | Enable Railcom cutout | None |
| `<C RAILCOM OFF>` | Disable Railcom cutout | None |
| `<C RAILCOM DEBUG>` | Enable Railcom cutout for scope testing | None |
| `<C WIFI "ssid" "password">` | Reconfigure stored WiFi credentials | `ssid`: Network name, `password`: Password |

## Diagnostic Commands

| Command | Description | Parameters |
|---------|-------------|------------|
| `<D ACK ON>` | Enable PROG track diagnostics | None |
| `<D ACK OFF>` | Disable PROG track diagnostics | None |
| `<D ACK LIMIT value>` | Set ACK detection limit mA | `value`: Current limit in mA |
| `<D ACK MIN value MS>` | Set ACK minimum duration mS | `value`: Duration in milliseconds |
| `<D ACK MIN value>` | Set ACK minimum duration µS | `value`: Duration in microseconds |
| `<D ACK MAX value MS>` | Set ACK maximum duration mS | `value`: Duration in milliseconds |
| `<D ACK MAX value>` | Set ACK maximum duration µS | `value`: Duration in microseconds |
| `<D ACK RETRY value>` | Set ACK retry count | `value`: Retry count |
| `<D CABS>` | Diagnostic display loco state table | None |
| `<D RAM>` | Diagnostic display free RAM | None |
| `<D CMD ON>` | Enable command input diagnostics | None |
| `<D CMD OFF>` | Disable command input diagnostics | None |
| `<D RAILCOM ON>` | Enable Railcom diagnostics | None |
| `<D RAILCOM OFF>` | Disable Railcom diagnostics | None |
| `<D WIFI ON>` | Enable WiFi diagnostics | None |
| `<D WIFI OFF>` | Disable WiFi diagnostics | None |
| `<D ETHERNET ON>` | Enable Ethernet diagnostics | None |
| `<D ETHERNET OFF>` | Disable Ethernet diagnostics | None |
| `<D WIT ON>` | Enable Withrottle diagnostics | None |
| `<D WIT OFF>` | Disable Withrottle diagnostics | None |
| `<D LCN ON>` | Enable LCN diagnostics | None |
| `<D LCN OFF>` | Disable LCN diagnostics | None |
| `<D WEBSOCKET ON>` | Enable Websocket diagnostics | None |
| `<D WEBSOCKET OFF>` | Disable Websocket diagnostics | None |
| `<D EEPROM numentries>` | Dump EEPROM contents | `numentries`: Number of entries |
| `<D ANOUT vpin position>` | Test analog output | `vpin`: Pin, `position`: Position |
| `<D ANOUT vpin position profile>` | Test analog output with profile | `vpin`: Pin, `position`: Position, `profile`: Profile |
| `<D SERVO vpin position>` | Test servo | `vpin`: Pin, `position`: Position |
| `<D SERVO vpin position profile>` | Test servo with profile | `vpin`: Pin, `position`: Position, `profile`: Profile |
| `<D ANIN vpin>` | Display analogue input value | `vpin`: Pin number |
| `<D HAL SHOW>` | Show HAL devices table | None |
| `<D HAL RESET>` | Reset all HAL devices | None |
| `<D TT vpin steps>` | Test turntable | `vpin`: Pin, `steps`: Step count |
| `<D TT vpin steps activity>` | Test turntable with activity | `vpin`: Pin, `steps`: Steps, `activity`: Activity |

## Raw DCC Packets

| Command | Description | Parameters | Status |
|---------|-------------|------------|--------|
| `<M ignore d0 d1 d2 d3 d4 d5>` | Send up to 5 byte DCC packet on MAIN track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| `<P ignore d0 d1 d2 d3 d4 d5>` | Send up to 5 byte DCC packet on PROG track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| `<c>` | Report main track current | None | ⚠️ Deprecated |

!!! info "Speed Values"
    - **0**: Stop
    - **1-127**: Variable speed (1=slowest, 127=fastest)

!!! info "Direction Values"
    - **0**: Reverse
    - **1**: Forward

!!! warning "Deprecated Commands"
    Commands marked with ⚠️ are deprecated and may be removed in future versions. Use the recommended alternatives where available.
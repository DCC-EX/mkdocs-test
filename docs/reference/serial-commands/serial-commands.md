# Grouped DCC-EX Serial Command Reference

Reference guide for serial commands used by **EX-CommandStations**, shown in functional groups.

!!! warning "This list may not be complete"

    This list of commands is manually created and may lag behind the latest developments.  Refer to the [Full Command List](./serial-command-list.md) for the up-to-date list of commands.

## Common Elements / Parameters

How to understand the syntax:

- The first symbol after the `<` character is the opcode. It's case sensitive so `<F` is not the same as `<f`.
- parameters in UPPER CASE (eg ``LIMIT``) are keywords and form part of the command. Keywords are not case sensitive.
- parameters in lower case (eg ``tSpeed``) are values you must supply
- parameters in ``[square brackets]`` are optional (e.g. ``[volume]``). Do not include the brackets in your command.

See the [Overview](./index.md) for more information on these and other common elements.

----

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

## System Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<#>`](?_:h:) | Request number of simultaneously supported locos | None | Active |
| [`<!>`](?_!) | Emergency stop all locos | None | Active |
| [`<!P>`](?_!) | Emergency stop and PAUSE loco movement | None | Active |
| [`<!R>`](?_!) | Resume after `<!P>` | None | Active |
| [`<s>`](?_s) | Command station status | None | Active |
| [`<E>`](?_9E9) | Store EEPROM | None | Active |
| [`<e>`](?_e) | Clear EEPROM | None | Active |

## Power Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<1>` | Power ON all tracks | None | Active |
| `<1 MAIN>` | Power on MAIN track | None | Active |
| `<1 PROG>` | Power on PROG track | None | Active |
| `<1 JOIN>` | JOIN prog track to MAIN and power | None | Active |
| `<1 track>` | Power on given track | `track`: Track identifier | Active |
| `<0>` | Power off all tracks | None | Active |
| `<0 MAIN>` | Power off MAIN track | None | Active |
| `<0 PROG>` | Power off PROG track | None | Active |
| `<0 track>` | Power off given track | `track`: Track identifier | Active |

## Locomotive Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<t loco>` | Request loco status | `loco`: Locomotive ID | Active |
| `<t loco tSpeed direction>` | Set throttle speed and direction | `loco`: ID, `tSpeed`: 0-127, `direction`: 0/1 | Active |
| `<t ignore loco tSpeed direction>` | Set throttle speed and direction | Legacy format | ⚠️ Deprecated |
| `<- loco>` | Remove loco state and reminders | `loco`: Locomotive ID | Active |
| `<->` | Clear loco state and reminder table | None | Active |

## Function Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<F loco function onoff>` | Set loco function ON/OFF | `loco`: ID, `function`: Function number, `onoff`: 0/1 | Active |
| `<F loco DCCFREQ freqvalue>` | Set DC frequency for loco | `loco`: ID, `freqvalue`: Frequency value | Active |
| `<f loco byte1>` | Set loco function group | `loco`: ID, `byte1`: Function byte | ⚠️ Deprecated |
| `<f loco group byte2>` | Set loco function group | `loco`: ID, `group`: Group ID, `byte2`: Function byte | ⚠️ Deprecated |

## Consist Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<^>` | Show all consists | none | Active |
| `<^ loco1 loco2 ... >` | Create Consist | `loco`: ID, negative for reversed loco | Active |
| `<^ loco1>` | Deletes consist | `loco1`: ID | Active |

## Turnout/Point Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<T>` | List all turnouts/points | None | Active |
| `<T id>` | Delete turnout/point | `id`: Turnout ID | Active |
| `<T id X>` | List turnout/point details | `id`: Turnout ID | Active |
| `<T id T>` | Throw turnout/point | `id`: Turnout ID | Active |
| `<T id C>` | Close turnout/point | `id`: Turnout ID | Active |
| `<T id value>` | Close (value=0) or Throw turnout | `id`: Turnout ID, `value`: 0/1 | Active |
| `<T id SERVO vpin closedValue thrownValue>` | Create servo turnout | `id`: ID, `vpin`: Pin, values for positions | Active |
| `<T id VPIN vpin>` | Create pin turnout | `id`: ID, `vpin`: Pin number | Active |
| `<T id DCC addr subadd>` | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address | Active |
| `<T id DCC linearAddr>` | Create DCC turnout | `id`: ID, `linearAddr`: Linear address | Active |
| `<T id addr subadd>` | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address | Active |
| `<T id vpin closedValue thrownValue>` | Create SERVO turnout | `id`: ID, `vpin`: Pin, position values | Active |

## Sensor Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<S id vpin pullup>` | Create sensor | `id`: Sensor ID, `vpin`: Pin, `pullup`: Pull-up setting | Active |
| `<S id>` | Delete sensor | `id`: Sensor ID | Active |
| `<S>` | List sensors | None | Active |
| `<Q>` | List all sensors | None | Active |

## CV Programming

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<W cv value>` | Write CV value on PROG track | `cv`: CV number, `value`: Value | Active |
| `<W loco>` | Write loco address on PROG track | `loco`: Address | Active |
| `<W CONSIST loco>` | Write consist address on PROG track | `loco`: Address | Active |
| `<W CONSIST loco REVERSE>` | Write consist address and reverse flag | `loco`: Address | Active |
| `<W cv bitvalue bit>` | Write CV bit on prog track | `cv`: CV, `bitvalue`: Bit value, `bit`: Bit position | Active |
| `<W cv value ignore1 ignore2>` | Write CV value on PROG track | Legacy format | ⚠️ Deprecated |
| `<R cv>` | Read CV | `cv`: CV number | Active |
| `<R>` | Read driveable loco ID | None | Active |
| `<R LOCOID>` | Read loco ID (ignoring consist) | None | Active |
| `<R CONSIST>` | Read consist ID | None | Active |
| `<R cv ignore1 ignore2>` | Read CV value on PROG track | Legacy format | ⚠️ Deprecated |
| `<V cv value>` | Fast read CV with expected value | `cv`: CV number, `value`: Expected value | Active |
| `<V cv bit bitvalue>` | Fast read bit with expected value | `cv`: CV, `bit`: Bit position, `bitvalue`: Expected | Active |
| `<B cv bit bitvalue>` | Write CV bit | `cv`: CV number, `bit`: Bit position, `bitvalue`: Value | Active |
| `<w loco cv value>` | POM write CV on main track | `loco`: ID, `cv`: CV number, `value`: Value | Active |
| `<r loco cv>` | POM read CV on main track | `loco`: ID, `cv`: CV number | Railcom dependent |
| `<b loco cv bit bitvalue>` | POM write CV bit on main track | `loco`: ID, `cv`: CV, `bit`: Position, `bitvalue`: Value | Active |

## DCC Accessory Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<a address subaddress activate>` | Send DCC accessory command | `address`: Address, `subaddress`: Sub-address, `activate`: 0/1 | Active |
| `<a address subaddress activate onoff>` | Send DCC accessory command with on/off | `address`: Address, `subaddress`: Sub, `activate`: 0/1, `onoff`: 0/1 | Active |
| `<a linearaddress activate>` | Send DCC accessory command | `linearaddress`: Linear address, `activate`: 0/1 | Active |
| `<A address value>` | Send DCC extended accessory (Aspect) command | `address`: Address, `value`: Aspect value | Active |

## Momentum Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<m LINEAR>` | Set momentum algorithm to linear acceleration | None | Active |
| `<m POWER>` | Set momentum algorithm based on speed difference | None | Active |
| `<m loco momentum>` | Set momentum for loco (accel and braking) | `loco`: ID, `momentum`: Value | Active |
| `<m loco accelerating braking>` | Set momentum for loco | `loco`: ID, `accelerating`: Value, `braking`: Value | Active |

## Output Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<Z>` | List output definitions | None | Active |
| `<Z id pin iflag>` | Create output | `id`: Output ID, `pin`: Pin number, `iflag`: Invert flag | Active |
| `<Z id active>` | Set output | `id`: Output ID, `active`: 0/1 | Active |
| `<Z id>` | Delete output | `id`: Output ID | Active |

## Pin Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<z vpin>` | Set pin HIGH if vpin positive, LOW if negative | `vpin`: Pin number (signed) | Active |
| `<z vpin analog>` | Write analog device value | `vpin`: Pin, `analog`: Value | Active |
| `<z vpin analog profile>` | Write analog device using profile | `vpin`: Pin, `analog`: Value, `profile`: Profile ID | Active |
| `<z vpin analog profile duration>` | Change analog value over duration | `vpin`: Pin, `analog`: Value, `profile`: Profile, `duration`: Time | Active |

## NeoPixel Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<o vpin>` | Set neopixel on (vpin>0) or off (vpin<0) | `vpin`: Pin number (signed) | Active |
| `<o vpin count>` | Set multiple neopixels on/off | `vpin`: Pin, `count`: Number of pixels | Active |
| `<o vpin r g b>` | Set neopixel colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue | Active |
| `<o vpin r g b count>` | Set multiple neopixels colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue, `count`: Count | Active |

## Turntable Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<I>` | List all turntables | None | Active |
| `<I id>` | Broadcast turntable type and current position | `id`: Turntable ID | Active |
| `<I id position>` | Rotate a DCC turntable | `id`: ID, `position`: Position | Active |
| `<I id DCC home>` | Create DCC turntable | `id`: ID, `home`: Home position | Active |
| `<I id position activity>` | Rotate an EXTT turntable | `id`: ID, `position`: Position, `activity`: Activity | Active |
| `<I id EXTT vpin home>` | Create an EXTT turntable | `id`: ID, `vpin`: Pin, `home`: Home position | Active |
| `<I id ADD position value angle>` | Add turntable position | `id`: ID, `position`: Position, `value`: Value, `angle`: Angle | Active |

## Sound Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<y vpin PLAY track [volume]>` | Play track | Active |
| `<y vpin REPEAT track [volume]>` | Play track repeat | Active |
| `<y vpin STOP>` | Stop playing | Active |
| `<y vpin PAUSE>` | Pause playing | Active |
| `<y vpin RESUME>` | Resume playing | Active |
| `<y vpin FOLDER folder>` | Set folder to play from | Active |
| `<y vpin VOLUME vol>` | Set default volume 0..30 | Active |
| `<y vpin EQ type>` | Set EQ type NORMAL, POP, ROCK, JAZZ, CLASSCS, BASS | Active |
| `<y vpin RESET>` | Reset player | Active |

## Throttle Information Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<J M>` | List stash values | None | Active |
| `<J M stash_id>` | Get stash value | `stash_id`: Stash identifier | Active |
| `<J M CLEAR ALL>` | Clear all stash values | None | Active |
| `<J M CLEAR stash_id>` | Clear given stash | `stash_id`: Stash identifier | Active |
| `<J M stashId locoId>` | Set stash value | `stashId`: Stash ID, `locoId`: Loco ID | Active |
| `<J M CLEAR ANY locoId>` | Clear all stash entries containing locoId | `locoId`: Locomotive ID | Active |
| `<J C>` | Get fastclock time | None | Active |
| `<J C mmmm nn>` | Set fastclock time | `mmmm`: Minutes, `nn`: Rate | Active |
| `<J G>` | Report gauge limits | None | Active |
| `<J I>` | Report currents | None | Active |
| `<J A>` | List routes | None | Active |
| `<J R>` | List roster | None | Active |
| `<J R id>` | Get roster for loco | `id`: Locomotive ID | Active |
| `<J T>` | Get turnout/point list | None | Active |
| `<J T id>` | Get turnout state and description | `id`: Turnout ID | Active |
| `<J O>` | List turntable IDs | None | Active |
| `<J O id>` | List turntable state | `id`: Turntable ID | Active |
| `<J P id>` | List turntable positions | `id`: Turntable ID | Active |

## Track Manager

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<=>` | List track manager states | None | Active |
| `<= track MAIN>` | Set track to MAIN | `track`: Track identifier | Active |
| `<= track MAIN_INV>` | Set track to MAIN inverted polarity | `track`: Track identifier | Active |
| `<= track MAIN_AUTO>` | Set track to MAIN with auto reversing | `track`: Track identifier | Active |
| `<= track PROG>` | Set track to PROG | `track`: Track identifier | Active |
| `<= track OFF>` | Set track power OFF | `track`: Track identifier | Active |
| `<= track NONE>` | Set track no output | `track`: Track identifier | Active |
| `<= track EXT>` | Set track to use external sync | `track`: Track identifier | Active |
| `<= track AUTO>` | Update track to auto reverse | `track`: Track identifier | Active |
| `<= track INV>` | Update track to inverse polarity | `track`: Track identifier | Active |
| `<= track DC loco>` | Set track to DC | `track`: Track ID, `loco`: Loco ID | Active |
| `<= track DC_INV loco>` | Set track to DC with inverted polarity | `track`: Track ID, `loco`: Loco ID | Active |
| `<= track DCX loco>` | Set track to DC with inverted polarity | `track`: Track ID, `loco`: Loco ID | Active |

## Configuration Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<C PROGBOOST>` | Configure PROG track boost | None | Active |
| `<C RESET>` | Reset and restart **EX-CommandStation** | None | Active |
| `<C SPEED28>` | Set all DCC speed commands as 28 step | None | Active |
| `<C SPEED128>` | Set all DCC speed commands to 128 step (default) | None | Active |
| `<C RAILCOM ON>` | Enable Railcom cutout | None | Active |
| `<C RAILCOM OFF>` | Disable Railcom cutout | None | Active |
| `<C RAILCOM DEBUG>` | Enable Railcom cutout for scope testing | None | Active |
| `<C WIFI "ssid" "password">` | Reconfigure stored STA WiFi credentials | `ssid`: Network name, `password`: Password | Active |
| `<C WIFI AP "ssid" "password" [channel]>` | Reconfigure stored WiFi AP | `ssid`: Network name, `password`: Password | Active |
| `<C WIFI HIDDENAP "ssid" "password" [channel]>` | Reconfigure stored WiFi AP | `ssid`: Network name, `password`: Password | Active |
| `<C WIFI DEFAULT>` | Set WiFi to default | None | Active |
| `<C WIFI ON/OFF>` | Set WiFi on/off name | None | Active |

## Diagnostic Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<D ACK ON>` | Enable PROG track diagnostics | None | Active |
| `<D ACK OFF>` | Disable PROG track diagnostics | None | Active |
| `<D ACK LIMIT value>` | Set ACK detection limit mA | `value`: Current limit in mA | Active |
| `<D ACK MIN value MS>` | Set ACK minimum duration mS | `value`: Duration in milliseconds | Active |
| `<D ACK MIN value>` | Set ACK minimum duration µS | `value`: Duration in microseconds | Active |
| `<D ACK MAX value MS>` | Set ACK maximum duration mS | `value`: Duration in milliseconds | Active |
| `<D ACK MAX value>` | Set ACK maximum duration µS | `value`: Duration in microseconds | Active |
| `<D ACK RETRY value>` | Set ACK retry count | `value`: Retry count | Active |
| `<D CABS>` | Diagnostic display loco state table | None | Active |
| `<D RAM>` | Diagnostic display free RAM | None | Active |
| `<D CMD ON>` | Enable command input diagnostics | None | Active |
| `<D CMD OFF>` | Disable command input diagnostics | None | Active |
| `<D RAILCOM ON>` | Enable Railcom diagnostics | None | Active |
| `<D RAILCOM OFF>` | Disable Railcom diagnostics | None | Active |
| `<D WIFI ON>` | Enable WiFi diagnostics | None | Active |
| `<D WIFI OFF>` | Disable WiFi diagnostics | None | Active |
| `<D WIFI SHOW>` | Shows WiFi settings | None | Active |
| `<D ETHERNET ON>` | Enable Ethernet diagnostics | None | Active |
| `<D ETHERNET OFF>` | Disable Ethernet diagnostics | None | Active |
| `<D WIT ON>` | Enable Withrottle diagnostics | None | Active |
| `<D WIT OFF>` | Disable Withrottle diagnostics | None | Active |
| `<D LCN ON>` | Enable LCN diagnostics | None | Active |
| `<D LCN OFF>` | Disable LCN diagnostics | None | Active |
| `<D WEBSOCKET ON>` | Enable Websocket diagnostics | None | Active |
| `<D WEBSOCKET OFF>` | Disable Websocket diagnostics | None | Active |
| `<D EEPROM numentries>` | Dump EEPROM contents | `numentries`: Number of entries | Active |
| `<D ANOUT vpin position>` | Test analog output | `vpin`: Pin, `position`: Position | Active |
| `<D ANOUT vpin position profile>` | Test analog output with profile | `vpin`: Pin, `position`: Position, `profile`: Profile | Active |
| `<D SERVO vpin position>` | Test servo | `vpin`: Pin, `position`: Position | Active |
| `<D SERVO vpin position profile>` | Test servo with profile | `vpin`: Pin, `position`: Position, `profile`: Profile | Active |
| `<D ANIN vpin>` | Display analogue input value | `vpin`: Pin number | Active |
| `<D HAL SHOW>` | Show HAL devices table | None | Active |
| `<D HAL RESET>` | Reset all HAL devices | None | Active |
| `<D TT vpin steps>` | Test turntable | `vpin`: Pin, `steps`: Step count | Active |
| `<D TT vpin steps activity>` | Test turntable with activity | `vpin`: Pin, `steps`: Steps, `activity`: Activity | Active |

## Raw DCC Packets

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| `<M ignore d0 d1 d2 d3 d4 d5>` | Send up to 5 byte DCC packet on MAIN track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| `<P ignore d0 d1 d2 d3 d4 d5>` | Send up to 5 byte DCC packet on PROG track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| `<c>` | Report main track current | None | ⚠️ Deprecated |

!!! info "tSpeed Values"
    - **0**: Stop
    - **1-127**: Variable speed (1=slowest, 127=fastest)
    - **-1**: Emergency stop

!!! info "Direction Values"
    - **0**: Reverse
    - **1**: Forward

!!! warning "Deprecated Commands"
    Commands marked with ⚠️ are deprecated and may be removed in future versions. Use the recommended alternatives where available.

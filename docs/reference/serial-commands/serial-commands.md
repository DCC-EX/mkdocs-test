# Grouped DCC-EX Serial Command Reference

Reference guide for serial commands used by **EX-CommandStations**, shown in functional groups.

!!! warning "This list may not be complete"

    This list of commands is manually created and may lag behind the latest developments.  Refer to the [Full Command List](./serial-command-list.md) for the up-to-date list of commands.

!!! warning "Deprecated Commands"
    Commands marked with ⚠️ are deprecated and may be removed in future versions. Use the recommended alternatives where available.

--8<-- "snippets/serial-commands/conventions.md"

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
| [`<#>`](?_8hash8) | Request number of simultaneously supported locos | None | Active |
| [`<!>`](?_!) | Emergency stop all locos | None | Active |
| [`<!P>`](?_!) | Emergency stop and PAUSE loco movement | None | Active |
| [`<!R>`](?_!) | Resume after `<!P>` | None | Active |
| [`<s>`](?_s) | Command station status | None | Active |
| [`<E>`](?_9E9) | Store EEPROM | None | Active |
| [`<e>`](?_e) | Clear EEPROM | None | Active |

## Power Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<1>`](?_1) | Power ON all tracks | None | Active |
| [`<1 MAIN>`](?_1_9MAIN9) | Power on MAIN track | None | Active |
| [`<1 PROG>`](?_1_9PROG9) | Power on PROG track | None | Active |
| [`<1 JOIN>`](?_1_9JOIN9) | JOIN prog track to MAIN and power | None | Active |
| [`<1 track>`](?_1_track) | Power on given track | `track`: Track identifier | Active |
| [`<0>`](?_0) | Power off all tracks | None | Active |
| [`<0 MAIN>`](?_0_9MAIN9) | Power off MAIN track | None | Active |
| [`<0 PROG>`](?_0_9PROG9) | Power off PROG track | None | Active |
| [`<0 track>`](?_0_track) | Power off given track | `track`: Track identifier | Active |

## Locomotive Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<t loco>`](?_t_loco) | Request loco status | `loco`: Locomotive ID | Active |
| [`<t loco tSpeed direction>`](?_t_loco_tSpeed_direction) | Set throttle speed and direction | `loco`: ID, `tSpeed`: 0-127, `direction`: 0/1 | Active |
| `<t ignore loco tSpeed direction>` | Set throttle speed and direction | Legacy format | ⚠️ Deprecated |
| [`<- loco>`](?_8equals8_loco) | Remove loco state and reminders | `loco`: Locomotive ID | Active |
| [`<->`](?_8equals8) | Clear loco state and reminder table | None | Active |

## Function Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<F loco function onoff>`](?_9F9_loco_function_onoff) | Set loco function ON/OFF | `loco`: ID, `function`: Function number, `onoff`: 0/1 | Active |
| [`<F loco DCCFREQ freqvalue>`](?_9F9_loco_9DCCFREQ9_freqValue) | Set DC frequency for loco | `loco`: ID, `freqvalue`: Frequency value | Active |
| [`<f loco byte1>`](?_f_loco_byte1) | Set loco function group | `loco`: ID, `byte1`: Function byte | ⚠️ Deprecated |
| [`<f loco group byte2>`](?_f_loco_group_byte2) | Set loco function group | `loco`: ID, `group`: Group ID, `byte2`: Function byte | ⚠️ Deprecated |

## Consist Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<^>`](?_8caret8) | Show all consists | none | Active |
| [`<^ leadLoco follower [ follower2..7]>`](?_8caret8_ leadLoco_follower [_follower2..7]) | Create Consist | `loco`: ID, negative for reversed loco | Active |
| [`<^ loco>`](?_8caret8_loco) | Deletes consist | `loco1`: ID | Active |

## Turnout/Point Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<T>`](?_9t9) | List all turnouts/points | None | Active |
| [`<T id>`](?_9t9_id) | Delete turnout/point | `id`: Turnout ID | Active |
| [`<T id X>`](?_9t9_id_9X9) | List turnout/point details | `id`: Turnout ID | Active |
| [`<T id T>`](?_9t9_id_9T9) | Throw turnout/point | `id`: Turnout ID | Active |
| [`<T id C>`](?_9t9_id_9C9) | Close turnout/point | `id`: Turnout ID | Active |
| [`<T id value>`](?_9t9_id_value) | Close (value=0) or Throw turnout | `id`: Turnout ID, `value`: 0/1 | Active |
| [`<T id SERVO vpin closedValue thrownValue>`](?_9t9_id_9SERVO9_vpin_closedValue_thrownValue) | Create servo turnout | `id`: ID, `vpin`: Pin, values for positions | Active |
| [`<T id VPIN vpin>`](?_9t9_id) | Create pin turnout | `id`: ID, `vpin`: Pin number | Active |
| [`<T id DCC addr subAddr>`](?_9t9_id_9DCC9_addr_subAaddr) | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address | Active |
| [`<T id DCC linearAddr>`](?_9t9_id_9DCC9_linearAddr) | Create DCC turnout | `id`: ID, `linearAddr`: Linear address | Active |
| [`<T id addr subadd>`](?_9t9_id_addr_aubaddr) | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address | Active |
| [`<T id vpin closedValue thrownValue>`](?_9t9_id_vpin_closedValue_thrownValue) | Create SERVO turnout | `id`: ID, `vpin`: Pin, position values | Active |

## Sensor Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<S id vpin pullup>`](?_9S9_id_vpin_pullup) | Create sensor | `id`: Sensor ID, `vpin`: Pin, `pullup`: Pull-up setting | Active |
| [`<S id>`](?_9S9_id) | Delete sensor | `id`: Sensor ID | Active |
| [`<S>`](?_9S9) | List sensors | None | Active |
| [`<Q>`](?_9Q9) | List all sensors | None | Active |

## CV Programming

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<W cv value>`](?_9W9_cv_value) | Write CV value on PROG track | `cv`: CV number, `value`: Value | Active |
| [`<W loco>`](?_9W9_loco) | Write loco address on PROG track | `loco`: Address | Active |
| [`<W CONSIST loco>`](?_9W9_9CONSIST9_loco) | Write consist address on PROG track | `loco`: Address | Active |
| [`<W CONSIST loco REVERSE>`](?_9W9_9CONSIST9_loco_9REVERSE]) | Write consist address and reverse flag | `loco`: Address | Active |
| [`<W cv bitvalue bit>`](?_9W9_cv_bitvalue_bit) | Write CV bit on prog track | `cv`: CV, `bitvalue`: Bit value, `bit`: Bit position | Active |
| [`<W cv value ignore1 ignore2>`](?_9W9_cv_bitvalue_bit)ignore1 ignore2) | Write CV value on PROG track | Legacy format | ⚠️ Deprecated |
| [`<R cv>`](?_9R9_cv) | Read CV | `cv`: CV number | Active |
| [`<R>`](?_9R9) | Read driveable loco ID | None | Active |
| [`<R LOCOID>`](?_9R9_9LOCOID9) | Read loco ID (ignoring consist) | None | Active |
| [`<R CONSIST>`](?_9R9_9CONSIST9) | Read consist ID | None | Active |
| [`<R cv ignore1 ignore2>`](?_9R9_cv_ignore1_ignore2) | Read CV value on PROG track | Legacy format | ⚠️ Deprecated |
| [`<V cv value>`](?_9V9_value) | Fast read CV with expected value | `cv`: CV number, `value`: Expected value | Active |
| [`<V cv bit bitvalue>`](?_9V9_cv_bit_bitvalue) | Fast read bit with expected value | `cv`: CV, `bit`: Bit position, `bitvalue`: Expected | Active |
| [`<B cv bit bitvalue>`](?_9B9_cv_bit_bitvalue) | Write CV bit | `cv`: CV number, `bit`: Bit position, `bitvalue`: Value | Active |
| [`<w loco cv value>`](?_w_loco_cv_value) | POM write CV on main track | `loco`: ID, `cv`: CV number, `value`: Value | Active |
| [`<r loco cv>`](?_r_loco_cv) | POM read CV on main track | `loco`: ID, `cv`: CV number | Railcom dependent |
| [`<b loco cv bit bitvalue>`](?_w_loco_cv_bit_bitvalue) | POM write CV bit on main track | `loco`: ID, `cv`: CV, `bit`: Position, `bitvalue`: Value | Active |

## DCC Accessory Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<a address subaddress activate>`](?_a_address_subaddress_activate) | Send DCC accessory command | `address`: Address, `subaddress`: Sub-address, `activate`: 0/1 | Active |
| [`<a address subaddress activate onoff>`](?_a_address_subaddress_activate_onoff) | Send DCC accessory command with on/off | `address`: Address, `subaddress`: Sub, `activate`: 0/1, `onoff`: 0/1 | Active |
| [`<a linearaddress activate>`](?_a_linearaddress_activate) | Send DCC accessory command | `linearaddress`: Linear address, `activate`: 0/1 | Active |
| [`<A address value>`](?_9A9_address_value) | Send DCC extended accessory (Aspect) command | `address`: Address, `value`: Aspect value | Active |

## Momentum Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<m LINEAR>`](?_m_9LINEAR9) | Set momentum algorithm to linear acceleration | None | Active |
| [`<m POWER>`](?_m_9POWER9) | Set momentum algorithm based on speed difference | None | Active |
| [`<m loco momentum>`](?_m_loco_momentum) | Set momentum for loco (accel and braking) | `loco`: ID, `momentum`: Value | Active |
| [`<m loco accelerating braking>`](?_m_loco_accelerating_braking) | Set momentum for loco | `loco`: ID, `accelerating`: Value, `braking`: Value | Active |

## Output Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<Z>`](?_9Z9) | List output definitions | None | Active |
| [`<Z id pin iflag>`](?_9Z9_id_pin_iflag) | Create output | `id`: Output ID, `pin`: Pin number, `iflag`: Invert flag | Active |
| [`<Z id active>`](?_9Z9_id_active) | Set output | `id`: Output ID, `active`: 0/1 | Active |
| [`<Z id>`](?_9Z9_id) | Delete output | `id`: Output ID | Active |

## Pin Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<z vpin>`](?_z_vpin) | Set pin HIGH if vpin positive, LOW if negative | `vpin`: Pin number (signed) | Active |
| [`<z vpin analog>`](?_z_vpin_analog) | Write analog device value | `vpin`: Pin, `analog`: Value | Active |
| [`<z vpin analog profile>`](?_z_vpin_analog_profile) | Write analog device using profile | `vpin`: Pin, `analog`: Value, `profile`: Profile ID | Active |
| [`<z vpin analog profile duration>`](?_z_vpin_analog_profile_duration) | Change analog value over duration | `vpin`: Pin, `analog`: Value, `profile`: Profile, `duration`: Time | Active |

## NeoPixel Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<o vpin>`](?_o_vpin) | Set neopixel on (vpin>0) or off (vpin<0) | `vpin`: Pin number (signed) | Active |
| [`<o vpin count>`](?_o_vpin_count) | Set multiple neopixels on/off | `vpin`: Pin, `count`: Number of pixels | Active |
| [`<o vpin r g b>`](?_o_vpin_r_g_b) | Set neopixel colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue | Active |
| [`<o vpin r g b count>`](?_o_vpin_r_g_b_count) | Set multiple neopixels colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue, `count`: Count | Active |

## Turntable Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<I>`](?_9I9) | List all turntables | None | Active |
| [`<I id>`](?_9I9_id) | Broadcast turntable type and current position | `id`: Turntable ID | Active |
| [`<I id position>`](?_9I9_id_position) | Rotate a DCC turntable | `id`: ID, `position`: Position | Active |
| [`<I id DCC home>`](?_9I9_id_9DCC9_home) | Create DCC turntable | `id`: ID, `home`: Home position | Active |
| [`<I id position activity>`](?_9I9_id_position_activity) | Rotate an EXTT turntable | `id`: ID, `position`: Position, `activity`: Activity | Active |
| [`<I id EXTT vpin home>`](?_9I9_id_9EXTT9_vpin_home) | Create an EXTT turntable | `id`: ID, `vpin`: Pin, `home`: Home position | Active |
| [`<I id ADD position value angle>`](?_9I9_id_9ADD9_position_value_angle) | Add turntable position | `id`: ID, `position`: Position, `value`: Value, `angle`: Angle | Active |

## Sound Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<y vpin PLAY track [volume]>`](?_y_vpin_9PLAY9_track_volume) | Play track | Active |
| [`<y vpin REPEAT track [volume]>`](?_y_vpin_9REPEAT9_track_volume) | Play track repeat | Active |
| [`<y vpin STOP>`](?_y_vpin_9STOP9) | Stop playing | Active |
| [`<y vpin PAUSE>`](?_y_vpin_9PAUSE9) | Pause playing | Active |
| [`<y vpin RESUME>`](?_y_vpin_9RESUME9) | Resume playing | Active |
| [`<y vpin FOLDER folder>`](?_y_vpin_9FOLDER9_folder) | Set folder to play from | Active |
| [`<y vpin VOLUME vol>`](?_y_vpin_9VOLUME9_vol) | Set default volume 0..30 | Active |
| [`<y vpin EQ type>`](?_y_vpin_9EQ9_type) | Set EQ type NORMAL, POP, ROCK, JAZZ, CLASSCS, BASS | Active |
| [`<y vpin RESET>`](?_y_vpin_9RESET9) | Reset player | Active |

## Throttle Information Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<J M>`](?_9J9_9M9) | List stash values | None | Active |
| [`<J M stashId>`](?_9J9_9M9_stashid) | Get stash value | `stash_id`: Stash identifier | Active |
| [`<J M CLEAR ALL>`](?_9J9_9M9_9CLEAR9_9ALL9) | Clear all stash values | None | Active |
| [`<J M CLEAR stashId>`](?_9J9_9M9_9CLEAR9_stashid) | Clear given stash | `stash_id`: Stash identifier | Active |
| [`<J M stashId locoId>`](?_9J9_9M9_stashid_locoid) | Set stash value | `stashId`: Stash ID, `locoId`: Loco ID | Active |
| [`<J M CLEAR ANY locoId>`](?_9J9_9M9_9CLEAR9_9ANY9_locoid) | Clear all stash entries containing locoId | `locoId`: Locomotive ID | Active |
| [`<J C>`](?_9J9_9C9) | Get fastclock time | None | Active |
| [`<J C mmmm nn>`](?_9J9_9C9_mmm_nn) | Set fastclock time | `mmmm`: Minutes, `nn`: Rate | Active |
| [`<J G>`](?_9J9_9G9) | Report gauge limits | None | Active |
| [`<J I>`](?_9J9_9I9) | Report currents | None | Active |
| [`<J A>`](?_9J9_9A9) | List routes | None | Active |
| [`<J R>`](?_9J9_9R9) | List roster | None | Active |
| [`<J R id>`](?_9J9_9R9_id) | Get roster for loco | `id`: Locomotive ID | Active |
| [`<J T>`](?_9J9_9T9) | Get turnout/point list | None | Active |
| [`<J T id>`](?_9J9_9T9_id) | Get turnout state and description | `id`: Turnout ID | Active |
| [`<J O>`](?_9J9_9O9) | List turntable IDs | None | Active |
| [`<J O id>`](?_9J9_9O9_id) | List turntable state | `id`: Turntable ID | Active |
| [`<J P id>`](?_9J9_9P9_id) | List turntable positions | `id`: Turntable ID | Active |

## Track Manager

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<=>`](?_8equals8) | List track manager states | None | Active |
| [`<= track MAIN>`](?_8equals8_track_9MAIN9) | Set track to MAIN | `track`: Track identifier | Active |
| [`<= track MAIN_INV>`](?_8equals8_track_9MAIN_INV9) | Set track to MAIN inverted polarity | `track`: Track identifier | Active |
| [`<= track MAIN_AUTO>`](?_8equals8_track_9MAIN_AUTO9) | Set track to MAIN with auto reversing | `track`: Track identifier | Active |
| [`<= track PROG>`](?_8equals8_track_9PROG9) | Set track to PROG | `track`: Track identifier | Active |
| [`<= track OFF>`](?_8equals8_track_9OFF9) | Set track power OFF | `track`: Track identifier | Active |
| [`<= track NONE>`](?_8equals8_track_9NONE9) | Set track no output | `track`: Track identifier | Active |
| [`<= track EXT>](?_8equals8_track_9EXT9)` | Set track to use external sync | `track`: Track identifier | Active |
| [`<= track AUTO>`](?_8equals8_track_9AUTO9) | Update track to auto reverse | `track`: Track identifier | Active |
| [`<= track INV>`](?_8equals8_track_9INV9) | Update track to inverse polarity | `track`: Track identifier | Active |
| [`<= track DC loco>`](?_8equals8_track_9DC9_loco) | Set track to DC | `track`: Track ID, `loco`: Loco ID | Active |
| [`<= track DC_INV loco>`](?_8equals8_track_9DC_INV9_loco) | Set track to DC with inverted polarity | `track`: Track ID, `loco`: Loco ID | Active |
| [`<= track DCX loco>`](?_8equals8_track_9DCX9_loco) | Set track to DC with inverted polarity. Same as DC_INV | `track`: Track ID, `loco`: Loco ID | Active |

## Configuration Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<C PROGBOOST>`](?_9PROGBOOST9) | Configure PROG track boost | None | Active |
| [`<C RESET>`](?_9RESET9) | Reset and restart **EX-CommandStation** | None | Active |
| [`<C SPEED28>`](?_9SPEED289) | Set all DCC speed commands as 28 step | None | Active |
| [`<C SPEED128>`](?_9SPEED1289) | Set all DCC speed commands to 128 step (default) | None | Active |
| [`<C RAILCOM onOff>`](?_9RAILCOM9_onoff) | Enable/Disable Railcom cutout | None | Active |
| [`<C RAILCOM DEBUG>`](?_9RRAILCOM9_9DEBUG9) | Enable Railcom cutout for scope testing | None | Active |
| [`<C WIFI "ssid" "password">`](?_9WIFI9_ssid_password) | Reconfigure stored STA WiFi credentials | `ssid`: Network name, `password`: Password | Active |
| [`<C WIFI AP "ssid" "password" [channel]>`](?_9WIFI9_9AP9_ssid_password_channel) | Reconfigure stored WiFi AP | `ssid`: Network name, `password`: Password | Active |
| [`<C WIFI HIDDENAP "ssid" "password" [channel]>`](?_9WIFI9_9HIDDENAP9_ssid_password_channel) | Reconfigure stored WiFi AP | `ssid`: Network name, `password`: Password | Active |
| [`<C WIFI DEFAULT>`](?_9WIFI9_9DEFAULT9) | Set WiFi to default | None | Active |
| [`<C WIFI onOff>`](?_9WIFI9_onoff) | Set WiFi on/off name | None | Active |

## Diagnostic Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<D ACK onoff>`](?_9D9_9ACK9_onoff) | Enable/Disable PROG track diagnostics | None | Active |
| [`<D ACK LIMIT value>`](?_9D9_9ACK9_9LIMIT9_value) | Set ACK detection limit mA | `value`: Current limit in mA | Active |
| [`<D ACK MIN value MS>`](?_9D9_9ACK9_9MIN9_value_9MS9) | Set ACK minimum duration mS | `value`: Duration in milliseconds | Active |
| [`<D ACK MIN value>`](?_9D9_9ACK9_9MIN9_value) | Set ACK minimum duration µS | `value`: Duration in microseconds | Active |
| [`<D ACK MAX value MS>`](?_9D9_9ACK9_9MAX9_value_9MS9) | Set ACK maximum duration mS | `value`: Duration in milliseconds | Active |
| [`<D ACK MAX value>`](?_9D9_9ACK9_9MAX9_value) | Set ACK maximum duration µS | `value`: Duration in microseconds | Active |
| [`<D ACK RETRY value>`](?_9D9_9ACK9_9RETRY9_value) | Set ACK retry count | `value`: Retry count | Active |
| [`<D CABS>`](?_9D9_9CABS9) | Diagnostic display loco state table | None | Active |
| [`<D RAM>`](?_9D9_9RAM9) | Diagnostic display free RAM | None | Active |
| [`<D CMD onOff>`](?_9D9_9CMD9_onoff) | Enable/Disable command input diagnostics | None | Active |
| [`<D RAILCOM onOff>`](?_9D9_9RAILCOM9_onoff) | Enable/Disable Railcom diagnostics | None | Active |
| [`<D WIFI onOff>`](?_9D9_9WIFI9_onoff) | Enable/Disable WiFi diagnostics | None | Active |
| [`<D WIFI SHOW>`](?_9D9_9WIFI9_9SHOW9) | Shows WiFi settings | None | Active |
| [`<D ETHERNET onOff>`](?_9D9_9ETHERNET9_onoff) | Enable/Disable Ethernet diagnostics | None | Active |
| [`<D WIT onOff>`](?_9D9_9WIT9_onoff) | Enable/Disable Withrottle diagnostics | None | Active |
| [`<D LCN onOff>`](?_9D9_9LCN9_onoff) | Enable/Disable LCN diagnostics | None | Active |
| [`<D WEBSOCKET onOff>`](?_9D9_9WEBSOCKET9_onoff) | Enable/Disable Websocket diagnostics | None | Active |
| [`<D EEPROM numentries>`](?_9D9_9EEPROM9_numentries) | Dump EEPROM contents | `numentries`: Number of entries | Active |
| [`<D ANOUT vpin position>`](?_9D9_9ANOUT9_vpin_position) | Test analog output ⚠️ Deprecated - use `<z vpin position>` | `vpin`: Pin, `position`: Position | Active |
| [`<D ANOUT vpin position profile>`](?_9D9_9ANOUT9_vpin_position_profile) | Test analog output with profile ⚠️ Deprecated - use `<z vpin position profile>` | `vpin`: Pin, `position`: Position, `profile`: Profile | Active |
| [`<D SERVO vpin position>`](?_9D9_9SERVO9_vpin_position) | Test servo | `vpin`: Pin, `position`: Position | Active |
| [`<D SERVO vpin position profile>`](?_9D9_9SERVO9_vpin_position_profile) | Test servo with profile | `vpin`: Pin, `position`: Position, `profile`: Profile | Active |
| [`<D ANIN vpin>`](?_9D9_9ANIN9_vpin) | Display analogue input value | `vpin`: Pin number | Active |
| [`<D HAL SHOW>`](?_9D9_9HAL9_9SHOW9) | Show HAL devices table | None | Active |
| [`<D HAL RESET>`](?_9D9_9HAL9_9RESET9) | Reset all HAL devices | None | Active |
| [`<D TT vpin steps>`](?_9D9_9TT9_vpin_steps) | Test turntable | `vpin`: Pin, `steps`: Step count | Active |
| [`<D TT vpin steps activity>`](?_9D9_9TT9_vpin_steps_activity) | Test turntable with activity | `vpin`: Pin, `steps`: Steps, `activity`: Activity | Active |

## Raw DCC Packets

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<M ignore d0 d1 d2 d3 d4 d5>`](?_9M9_ignore_d0_d1_[d2_d3_d4_d5]) | Send up to 5 byte DCC packet on MAIN track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| [`<P ignore d0 d1 d2 d3 d4 d5>`](?_9P9_ignore_d0_d1[_d2_d3_d4_d5]) | Send up to 5 byte DCC packet on PROG track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| [`<c>`](?_c) | Report main track current | None | ⚠️ Deprecated |



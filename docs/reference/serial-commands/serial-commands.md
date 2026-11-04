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
| [`<#>`](?_▫hash▫) | Request number of simultaneously supported locos | None | Active |
| [`<!>`](?_▫!▫) | Emergency stop all locos | None | Active |
| [`<!P>`](?_▫!) | Emergency stop and PAUSE loco movement | None | Active |
| [`<!R>`](?_▫!▫) | Resume after `<!P>` | None | Active |
| [`<s>`](?_▫s▫) | Command station status | None | Active |
| [`<E>`](?_▪E▪) | Store EEPROM | None | Active |
| [`<e>`](?_▫e▫) | Clear EEPROM | None | Active |

## Power Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<1>`](?_▫1▫) | Power ON all tracks | None | Active |
| [`<1 MAIN>`](?_▫1▫_▪MAIN▪) | Power on MAIN track | None | Active |
| [`<1 PROG>`](?_▫1▫_▪PROG▪) | Power on PROG track | None | Active |
| [`<1 JOIN>`](?_▫1▫_▪JOIN▪) | JOIN prog track to MAIN and power | None | Active |
| [`<1 track>`](?_▫1▫_▫track▫) | Power on given track | `track`: Track identifier | Active |
| [`<0>`](?_▫0▫) | Power off all tracks | None | Active |
| [`<0 MAIN>`](?_▫0▫_▪MAIN▪) | Power off MAIN track | None | Active |
| [`<0 PROG>`](?_▫0▫_▪PROG▪) | Power off PROG track | None | Active |
| [`<0 track>`](?_▫0▫_track) | Power off given track | `track`: Track identifier | Active |

## Locomotive Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<t loco>`](?_▫t▫_▫loco▫) | Request loco status | `loco`: Locomotive ID | Active |
| [`<t loco tSpeed direction>`](?_▫t▫_▫loco▫_▫tSpeed▫_▫direction▫) | Set throttle speed and direction | `loco`: ID, `tSpeed`: 0-127, `direction`: 0/1 | Active |
| `<t ignore loco tSpeed direction>` | Set throttle speed and direction | Legacy format | ⚠️ Deprecated |
| [`<- loco>`](?_▫equals▫_loco) | Remove loco state and reminders | `loco`: Locomotive ID | Active |
| [`<->`](?_▫equals▫) | Clear loco state and reminder table | None | Active |

## Function Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<F loco function onoff>`](?_▪F▪_▫loco▫_▫function▫_▫onoff▫) | Set loco function ON/OFF | `loco`: ID, `function`: Function number, `onoff`: 0/1 | Active |
| [`<F loco DCCFREQ freqvalue>`](?_▪F▪_▫loco▫_▪DCCFREQ▪_▫freqValue▫) | Set DC frequency for loco | `loco`: ID, `freqvalue`: Frequency value | Active |
| [`<f loco byte1>`](?_▫f▫_▫loco▫_▫byte1▫) | Set loco function group | `loco`: ID, `byte1`: Function byte | ⚠️ Deprecated |
| [`<f loco group byte2>`](?_▫f▫_▫loco▫_▫group▫_▫byte2▫) | Set loco function group | `loco`: ID, `group`: Group ID, `byte2`: Function byte | ⚠️ Deprecated |

## Consist Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<^>`](?_▫caret▫) | Show all consists | none | Active |
| [`<^ leadLoco follower [ follower2..7]>`](?_▫caret▫_▫leadLoco▫_▫follower▫ [▫_▫follower2..7]▫) | Create Consist | `loco`: ID, negative for reversed loco | Active |
| [`<^ loco>`](?_▫caret▫_▫loco▫) | Deletes consist | `loco1`: ID | Active |

## Turnout/Point Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<T>`](?_▪T▪) | List all turnouts/points | None | Active |
| [`<T id>`](?_▪T▪_▫id▫) | Delete turnout/point | `id`: Turnout ID | Active |
| [`<T id X>`](?_▪T▪_▫id▫_▪X▪) | List turnout/point details | `id`: Turnout ID | Active |
| [`<T id T>`](?_▪T▪_▫id▫_▪T▪) | Throw turnout/point | `id`: Turnout ID | Active |
| [`<T id C>`](?_▪T▪_▫id▫_▪C▪) | Close turnout/point | `id`: Turnout ID | Active |
| [`<T id value>`](?_▪T▪_▫id▫_▫value▫) | Close (value=0) or Throw turnout | `id`: Turnout ID, `value`: 0/1 | Active |
| [`<T id SERVO vpin closedValue thrownValue>`](?_▪T▪_▫id▫_▪SERVO▪_▫vpin▫_▫closedValue▫_▫thrownValue▫) | Create servo turnout | `id`: ID, `vpin`: Pin, values for positions | Active |
| [`<T id VPIN vpin>`](?_▪T▪_▫id▫) | Create pin turnout | `id`: ID, `vpin`: Pin number | Active |
| [`<T id DCC addr subAddr>`](?_▪T▪_▫id▫_▪DCC▪_▫addr▫_▫subAaddr▫) | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address | Active |
| [`<T id DCC linearAddr>`](?_▪tT▪_▫id▫_▪DCC▪_▫linearAddr▫) | Create DCC turnout | `id`: ID, `linearAddr`: Linear address | Active |
| [`<T id addr subadd>`](?_▪T▪_▫id▫_▫addr▫_▫subaddr▫) | Create DCC turnout | `id`: ID, `addr`: Address, `subadd`: Sub-address | Active |
| [`<T id vpin closedValue thrownValue>`](?_▪T▪_▫id▫_▫vpin▫_▫closedValue▫_▫thrownValue▫) | Create SERVO turnout | `id`: ID, `vpin`: Pin, position values | Active |

## Sensor Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<S id vpin pullup>`](?_▪S▪_▫id▫_▫vpin▫_▫pullup▫) | Create sensor | `id`: Sensor ID, `vpin`: Pin, `pullup`: Pull-up setting | Active |
| [`<S id>`](?_▪S▪_▫id▫) | Delete sensor | `id`: Sensor ID | Active |
| [`<S>`](?_▪S▪) | List sensors | None | Active |
| [`<Q>`](?_▪Q▪) | List all sensors | None | Active |

## CV Programming

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<W cv value>`](?_▪W▪_▫cv▫_▫value▫) | Write CV value on PROG track | `cv`: CV number, `value`: Value | Active |
| [`<W loco>`](?_▪W▪_▫loco▫) | Write loco address on PROG track | `loco`: Address | Active |
| [`<W CONSIST loco>`](?_▪W▪_▪CONSIST▪_▫loco▫) | Write consist address on PROG track | `loco`: Address | Active |
| [`<W CONSIST loco REVERSE>`](?_▪W▪_▪CONSIST▪_▫loco▫_▪REVERSE▪]) | Write consist address and reverse flag | `loco`: Address | Active |
| [`<W cv bitvalue bit>`](?_▪W▪_▫cv▫_▫bitvalue▫_▫bit▫) | Write CV bit on prog track | `cv`: CV, `bitvalue`: Bit value, `bit`: Bit position | Active |
| [`<W cv value ignore1 ignore2>`](?_▪W▪_▫cv▫_▫bitvalue▫_▫bit▫)ignore1 ignore2) | Write CV value on PROG track | Legacy format | ⚠️ Deprecated |
| [`<R cv>`](?_▪R▪_▫cv▫) | Read CV | `cv`: CV number | Active |
| [`<R>`](?_▪R▪) | Read driveable loco ID | None | Active |
| [`<R LOCOID>`](?_▪R▪_▪LOCOID▪) | Read loco ID (ignoring consist) | None | Active |
| [`<R CONSIST>`](?_▪R▪_▪CONSIST▪) | Read consist ID | None | Active |
| [`<R cv ignore1 ignore2>`](?_▪R▪_▫cv▫_▫ignore1▫_▫ignore2▫) | Read CV value on PROG track | Legacy format | ⚠️ Deprecated |
| [`<V cv value>`](?_▪V▪_▫value▫) | Fast read CV with expected value | `cv`: CV number, `value`: Expected value | Active |
| [`<V cv bit bitvalue>`](?_▪V▪_▫cv▫_▫bit▫_▫bitvalue▫) | Fast read bit with expected value | `cv`: CV, `bit`: Bit position, `bitvalue`: Expected | Active |
| [`<B cv bit bitvalue>`](?_▪B▪_▫cv▫_▫bit▫_▫bitvalue▫) | Write CV bit | `cv`: CV number, `bit`: Bit position, `bitvalue`: Value | Active |
| [`<w loco cv value>`](?_▫w▫_▫loco▫_▫cv▫_▫value▫) | POM write CV on main track | `loco`: ID, `cv`: CV number, `value`: Value | Active |
| [`<r loco cv>`](?_▫r▫_▫loco▫_▫cv▫) | POM read CV on main track | `loco`: ID, `cv`: CV number | Railcom dependent |
| [`<b loco cv bit bitvalue>`](?_▫w▫_▫loco▫_▫cv▫_▫bit▫_▫bitvalue▫) | POM write CV bit on main track | `loco`: ID, `cv`: CV, `bit`: Position, `bitvalue`: Value | Active |

## DCC Accessory Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<a address subaddress activate>`](?_▫a▫_▫address▫_▫subaddress▫_▫activate▫) | Send DCC accessory command | `address`: Address, `subaddress`: Sub-address, `activate`: 0/1 | Active |
| [`<a address subaddress activate onoff>`](?_▫a▫_▫address▫_▫subaddress▫_▫activate▫_▫onoff▫) | Send DCC accessory command with on/off | `address`: Address, `subaddress`: Sub, `activate`: 0/1, `onoff`: 0/1 | Active |
| [`<a linearaddress activate>`](?_▫a▫_▫linearaddress▫_▫activate▫) | Send DCC accessory command | `linearaddress`: Linear address, `activate`: 0/1 | Active |
| [`<A address value>`](?_▪A▪_▫address▫_▫value▫) | Send DCC extended accessory (Aspect) command | `address`: Address, `value`: Aspect value | Active |

## Momentum Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<m LINEAR>`](?_▫m▫_▪LINEAR▪) | Set momentum algorithm to linear acceleration | None | Active |
| [`<m POWER>`](?_▫m▫_▪POWER▪) | Set momentum algorithm based on speed difference | None | Active |
| [`<m loco momentum>`](?_▫m▫_▫loco▫_▫momentum▫) | Set momentum for loco (accel and braking) | `loco`: ID, `momentum`: Value | Active |
| [`<m loco accelerating braking>`](?_▫m▫_▫loco▫_▫accelerating▫_▫braking▫) | Set momentum for loco | `loco`: ID, `accelerating`: Value, `braking`: Value | Active |

## Output Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<Z>`](?_▪Z▪) | List output definitions | None | Active |
| [`<Z id pin iflag>`](?_▪Z▪_▫id▫_▫pin▫_▫iflag▫) | Create output | `id`: Output ID, `pin`: Pin number, `iflag`: Invert flag | Active |
| [`<Z id active>`](?_▪Z▪_▫id▫_▫active▫) | Set output | `id`: Output ID, `active`: 0/1 | Active |
| [`<Z id>`](?_▪Z▪_▫id▫) | Delete output | `id`: Output ID | Active |

## Pin Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<z vpin>`](?_▫z▫_▫vpin▫) | Set pin HIGH if vpin positive, LOW if negative | `vpin`: Pin number (signed) | Active |
| [`<z vpin analog>`](?_▫z▫_▫vpin▫_▫analog▫) | Write analog device value | `vpin`: Pin, `analog`: Value | Active |
| [`<z vpin analog profile>`](?_▫z▫_▫vpin▫_▫analog▫_▫profile▫) | Write analog device using profile | `vpin`: Pin, `analog`: Value, `profile`: Profile ID | Active |
| [`<z vpin analog profile duration>`](?_▫z▫_▫vpin▫_▫analog▫_▫profile▫_▫duration) | Change analog value over duration | `vpin`: Pin, `analog`: Value, `profile`: Profile, `duration`: Time | Active |

## NeoPixel Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<o vpin>`](?_▫o▫_▫vpin▫) | Set neopixel on (vpin>0) or off (vpin<0) | `vpin`: Pin number (signed) | Active |
| [`<o vpin count>`](?_▫o▫_▫vpin▫_▫count▫) | Set multiple neopixels on/off | `vpin`: Pin, `count`: Number of pixels | Active |
| [`<o vpin r g b>`](?_▫o▫_▫vpin▫_▫r▫_▫g▫_▫b▫) | Set neopixel colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue | Active |
| [`<o vpin r g b count>`](?_▫o▫_▫vpin▫_▫r▫_▫g▫_▫b▫_▫count▫) | Set multiple neopixels colour | `vpin`: Pin, `r`: Red, `g`: Green, `b`: Blue, `count`: Count | Active |

## Turntable Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<I>`](?_▪I▪) | List all turntables | None | Active |
| [`<I id>`](?_▪I▪_▫id▫) | Broadcast turntable type and current position | `id`: Turntable ID | Active |
| [`<I id position>`](?_▪I▪_▫id▫_▫position▫) | Rotate a DCC turntable | `id`: ID, `position`: Position | Active |
| [`<I id DCC home>`](?_▪I▪_▫id▫_▪DCC▪_▫home▫) | Create DCC turntable | `id`: ID, `home`: Home position | Active |
| [`<I id position activity>`](?_▪I▪_▫id▫_▫position▫_▫activity▫) | Rotate an EXTT turntable | `id`: ID, `position`: Position, `activity`: Activity | Active |
| [`<I id EXTT vpin home>`](?_▪I▪_▫id▫_▪EXTT▪_▫vpin▫_▫home▫) | Create an EXTT turntable | `id`: ID, `vpin`: Pin, `home`: Home position | Active |
| [`<I id ADD position value angle>`](?_▪I▪_▫id▫_▪ADD▪_▫position▫_▫value▫_▫angle▫) | Add turntable position | `id`: ID, `position`: Position, `value`: Value, `angle`: Angle | Active |

## Sound Control

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<y vpin PLAY track [volume]>`](?_▫y▫_▫vpin▫_▪PLAY▪_▫track▫_▫volume▫) | Play track | Active |
| [`<y vpin REPEAT track [volume]>`](?_▫y▫_▫vpin▫_▪REPEAT▪_▫track▫_▫volume▫) | Play track repeat | Active |
| [`<y vpin STOP>`](?_▫y▫_▫vpin▫_▪STOP▪) | Stop playing | Active |
| [`<y vpin PAUSE>`](?_▫y▫_▫vpin▫_▪PAUSE▪) | Pause playing | Active |
| [`<y vpin RESUME>`](?_▫y▫_▫vpin▫_▪RESUME▪) | Resume playing | Active |
| [`<y vpin FOLDER folder>`](?_▫y▫_▫vpin▫_▪FOLDER▪_▫folder▫) | Set folder to play from | Active |
| [`<y vpin VOLUME vol>`](?_▫y▫_▫vpin▫_▪VOLUME▪_▫vol▫) | Set default volume 0..30 | Active |
| [`<y vpin EQ type>`](?_▫y▫_▫vpin▫_▪EQ▪_▫type▫) | Set EQ type NORMAL, POP, ROCK, JAZZ, CLASSCS, BASS | Active |
| [`<y vpin RESET>`](?_▫y▫_▫vpin▫_▪RESET▪) | Reset player | Active |

## Throttle Information Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<J M>`](?_▪J▪_▪M▪) | List stash values | None | Active |
| [`<J M stashId>`](?_▪J▪_▪M▪_▫stashid▫) | Get stash value | `stash_id`: Stash identifier | Active |
| [`<J M CLEAR ALL>`](?_▪J▪_▪M▪_▪CLEAR▪_▪ALL▪) | Clear all stash values | None | Active |
| [`<J M CLEAR stashId>`](?_▪J▪_▪M▪_▪CLEAR▪_▫stashid▫) | Clear given stash | `stash_id`: Stash identifier | Active |
| [`<J M stashId locoId>`](?_▪J▪_▪M▪_stashid_▫locoid▫) | Set stash value | `stashId`: Stash ID, `locoId`: Loco ID | Active |
| [`<J M CLEAR ANY locoId>`](?_▪J▪_▪M▪_▪CLEAR▪_▪ANY▪_▫locoid▫) | Clear all stash entries containing locoId | `locoId`: Locomotive ID | Active |
| [`<J C>`](?_▪J▪_▪C▪) | Get fastclock time | None | Active |
| [`<J C mmmm nn>`](?_▪J▪_▪C▪_▫mmm▫_▫nn▫) | Set fastclock time | `mmmm`: Minutes, `nn`: Rate | Active |
| [`<J G>`](?_▪J▪_▪G▪) | Report gauge limits | None | Active |
| [`<J I>`](?_▪J▪_▪I▪) | Report currents | None | Active |
| [`<J A>`](?_▪J▪_▪A▪) | List routes | None | Active |
| [`<J R>`](?_▪J▪_▪R▪) | List roster | None | Active |
| [`<J R id>`](?_▪J▪_▪R▪_▫id▫) | Get roster for loco | `id`: Locomotive ID | Active |
| [`<J T>`](?_▪J▪_▪T▪) | Get turnout/point list | None | Active |
| [`<J T id>`](?_▪J▪_▪T▪_▫id▫) | Get turnout state and description | `id`: Turnout ID | Active |
| [`<J O>`](?_▪J▪_▪O▪) | List turntable IDs | None | Active |
| [`<J O id>`](?_▪J▪_▪O▪_▫id▫) | List turntable state | `id`: Turntable ID | Active |
| [`<J P id>`](?_▪J▪_▪P▪_▫id▫) | List turntable positions | `id`: Turntable ID | Active |

## Track Manager

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<=>`](?_▫equals▫) | List track manager states | None | Active |
| [`<= track MAIN>`](?_▫equals▫_▫track▫_▪MAIN▪) | Set track to MAIN | `track`: Track identifier | Active |
| [`<= track MAIN_INV>`](?_▫equals▫_▫track▫_▪MAIN_INV▪) | Set track to MAIN inverted polarity | `track`: Track identifier | Active |
| [`<= track MAIN_AUTO>`](?_▫equals▫_▫track▫_▪MAIN_AUTO▪) | Set track to MAIN with auto reversing | `track`: Track identifier | Active |
| [`<= track PROG>`](?_▫equals▫_▫track▫_▪PROG▪) | Set track to PROG | `track`: Track identifier | Active |
| [`<= track OFF>`](?_▫equals▫_▫track▫_▪OFF▪) | Set track power OFF | `track`: Track identifier | Active |
| [`<= track NONE>`](?_▫equals▫_▫track▫_▪NONE▪) | Set track no output | `track`: Track identifier | Active |
| [`<= track EXT>](?_▫equals▫_▫track▫_▪EXT▪)` | Set track to use external sync | `track`: Track identifier | Active |
| [`<= track AUTO>`](?_▫equals▫_▫track▫_▪AUTO▪) | Update track to auto reverse | `track`: Track identifier | Active |
| [`<= track INV>`](?_▫equals▫_▫track▫_▪INV▪) | Update track to inverse polarity | `track`: Track identifier | Active |
| [`<= track DC loco>`](?_▫equals▫_▫track▫_▪DC▪_▫loco▫) | Set track to DC | `track`: Track ID, `loco`: Loco ID | Active |
| [`<= track DC_INV loco>`](?_▫equals▫_▫track▫_▪DC_INV▪_▫loco▫) | Set track to DC with inverted polarity | `track`: Track ID, `loco`: Loco ID | Active |
| [`<= track DCX loco>`](?_▫equals▫_▫track▫_▪DCX▪_▫loco▫) | Set track to DC with inverted polarity. Same as DC_INV | `track`: Track ID, `loco`: Loco ID | Active |

## Configuration Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<C PROGBOOST>`](?_▪PROGBOOST▪) | Configure PROG track boost | None | Active |
| [`<C RESET>`](?_▪RESET▪) | Reset and restart **EX-CommandStation** | None | Active |
| [`<C SPEED28>`](?_▪SPEED28▪) | Set all DCC speed commands as 28 step | None | Active |
| [`<C SPEED128>`](?_▪SPEED128▪) | Set all DCC speed commands to 128 step (default) | None | Active |
| [`<C RAILCOM onOff>`](?_▪RAILCOM▪_▫onoff▫) | Enable/Disable Railcom cutout | None | Active |
| [`<C RAILCOM DEBUG>`](?_▪RRAILCOM▪_▪DEBUG▪) | Enable Railcom cutout for scope testing | None | Active |
| [`<C WIFI "ssid" "password">`](?_▪WIFI▪_▫ssid▫_▫password▫) | Reconfigure stored STA WiFi credentials | `ssid`: Network name, `password`: Password | Active |
| [`<C WIFI AP "ssid" "password" [channel]>`](?_▪WIFI▪_▪AP▪_▫ssid▫_▫password▫_▫channel▫) | Reconfigure stored WiFi AP | `ssid`: Network name, `password`: Password | Active |
| [`<C WIFI HIDDENAP "ssid" "password" [channel]>`](?_▪WIFI▪_▪HIDDENAP▪_▫ssid▫_▫password▫_▫channel▫) | Reconfigure stored WiFi AP | `ssid`: Network name, `password`: Password | Active |
| [`<C WIFI DEFAULT>`](?_▪WIFI▪_▪DEFAULT▪) | Set WiFi to default | None | Active |
| [`<C WIFI onOff>`](?_▪WIFI▪_▫onoff▫) | Set WiFi on/off name | None | Active |

## Diagnostic Commands

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<D ACK onoff>`](?_▪D▪_▪ACK▪_▫onoff▫) | Enable/Disable PROG track diagnostics | None | Active |
| [`<D ACK LIMIT value>`](?_▪D▪_▪ACK▪_▪LIMIT▪_▫value▫) | Set ACK detection limit mA | `value`: Current limit in mA | Active |
| [`<D ACK MIN value MS>`](?_▪D▪_▪ACK▪_▪MIN▪_▫value▫_▪MS▪) | Set ACK minimum duration mS | `value`: Duration in milliseconds | Active |
| [`<D ACK MIN value>`](?_▪D▪_▪ACK▪_▪MIN▪_▫value▫) | Set ACK minimum duration µS | `value`: Duration in microseconds | Active |
| [`<D ACK MAX value MS>`](?_▪D▪_▪ACK▪_▪MAX▪_▫value▫_▪MS▪) | Set ACK maximum duration mS | `value`: Duration in milliseconds | Active |
| [`<D ACK MAX value>`](?_▪D▪_▪ACK▪_▪MAX▪_▫value▫) | Set ACK maximum duration µS | `value`: Duration in microseconds | Active |
| [`<D ACK RETRY value>`](?_▪D▪_▪ACK▪_▪RETRY▪_▫value▫) | Set ACK retry count | `value`: Retry count | Active |
| [`<D CABS>`](?_▪D▪_▪CABS▪) | Diagnostic display loco state table | None | Active |
| [`<D RAM>`](?_▪D▪_▪RAM▪) | Diagnostic display free RAM | None | Active |
| [`<D CMD onOff>`](?_▪D▪_▪CMD▪_▫onoff▫) | Enable/Disable command input diagnostics | None | Active |
| [`<D RAILCOM onOff>`](?_▪D▪_▪RAILCOM▪_▫onoff▫) | Enable/Disable Railcom diagnostics | None | Active |
| [`<D WIFI onOff>`](?_▪D▪_▪WIFI▪_▫onoff▫) | Enable/Disable WiFi diagnostics | None | Active |
| [`<D WIFI SHOW>`](?_▪D▪_▪WIFI▪_▪SHOW▪) | Shows WiFi settings | None | Active |
| [`<D ETHERNET onOff>`](?_▪D▪_▪ETHERNET▪_▫onoff▫) | Enable/Disable Ethernet diagnostics | None | Active |
| [`<D WIT onOff>`](?_▪D▪_▪WIT▪_▫onoff▫) | Enable/Disable Withrottle diagnostics | None | Active |
| [`<D LCN onOff>`](?_▪D▪_▪LCN▪_▫onoff▫) | Enable/Disable LCN diagnostics | None | Active |
| [`<D WEBSOCKET onOff>`](?_▪D▪_▪WEBSOCKET▪_▫onoff▫) | Enable/Disable Websocket diagnostics | None | Active |
| [`<D EEPROM numentries>`](?_▪D▪_▪EEPROM▪_▫numentries▫) | Dump EEPROM contents | `numentries`: Number of entries | Active |
| [`<D ANOUT vpin position>`](?_▪D▪_▪ANOUT▪_▫vpin▫_▫position▫) | Test analog output ⚠️ Deprecated - use `<z vpin position>` | `vpin`: Pin, `position`: Position | Active |
| [`<D ANOUT vpin position profile>`](?_▪D▪_▪ANOUT▪_▫vpin▫_▫position▫_▫profile▫) | Test analog output with profile ⚠️ Deprecated - use `<z vpin position profile>` | `vpin`: Pin, `position`: Position, `profile`: Profile | Active |
| [`<D SERVO vpin position>`](?_▪D▪_▪SERVO▪_▫vpin▫_▫position▫) | Test servo | `vpin`: Pin, `position`: Position | Active |
| [`<D SERVO vpin position profile>`](?_▪D▪_▪SERVO▪_▫vpin▫_▫position▫_▫profile▫) | Test servo with profile | `vpin`: Pin, `position`: Position, `profile`: Profile | Active |
| [`<D ANIN vpin>`](?_▪D▪_▪ANIN▪_▫vpin▫) | Display analogue input value | `vpin`: Pin number | Active |
| [`<D HAL SHOW>`](?_▪D▪_▪HAL▪_▪SHOW▪) | Show HAL devices table | None | Active |
| [`<D HAL RESET>`](?_▪D▪_▪HAL▪_▪RESET▪) | Reset all HAL devices | None | Active |
| [`<D TT vpin steps>`](?_▪D▪_▪TT▪_▫vpin▫_▫steps▫) | Test turntable | `vpin`: Pin, `steps`: Step count | Active |
| [`<D TT vpin steps activity>`](?_▪D▪_▪TT▪_▫vpin▫_▫steps▫_▫activity▫) | Test turntable with activity | `vpin`: Pin, `steps`: Steps, `activity`: Activity | Active |

## Raw DCC Packets

| Command | Description | Parameters | Status |
| ------- | ----------- | ---------- | ------ |
| [`<M ignore d0 d1 d2 d3 d4 d5>`](?_▪M▪_▫ignore▫_▫d0▫_▫d1▫_▫[d2▫_▫d3▫_▫d4▫_▫d5]▫) | Send up to 5 byte DCC packet on MAIN track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| [`<P ignore d0 d1 d2 d3 d4 d5>`](?_▪P▪_▫ignore▫_▫d0▫_▫d1▫_▫[d2▫_▫d3▫_▫d4▫_▫d5]▫) | Send up to 5 byte DCC packet on PROG track | `ignore`: Ignored, `d0-d5`: Hex bytes | Active |
| [`<c>`](?_▫c▫) | Report main track current | None | ⚠️ Deprecated |

## Signal Commands

==TODO== MEDIUM - Signal Commands

## Reserve/Block Commands

==TODO== MEDIUM - Reserve/Block Commands

## Automation Commands

==TODO== MEDIUM - Automation Commands

## WiFI and Ethernet Commands

==TODO== MEDIUM - WiFi and EthernetCommands

---
tags:
  - _9J9_9R9
  - _9J9_9R9_locoid
  - _9J9_9R9_locoid_name_functionMap
  - _9J9_9R9_9SAVE9
  - _9J9_9R9_locoid_9DELETE9

search:
  boost: 3
---

# Serial commands to: Request or Create Roster info

Serial command to request roster info, or add new roster entries and save them in RAM.

``<J R>``
``<J R «id»>``
``<J R «id» "«name»" "«functions»">``
``<J R «id» DELETE>``
``<J R SAVE>``

----

## Commands

* ``<J R>`` = Request the list of all roster ids
* ``<J R «id»>`` = Request the detailed info on a specific roster id

{{ new_in_v("6.0") }} New Roster commands for v5.9.13 and above:

* ``<J R «id» "«name»" "«functions»">`` adds or replaces a roster in RAM
* ``<J R «id» DELETE>`` removes a roster entry from ram
* ``<J R SAVE>`` saves the current rosters in ram. They will be reloaded again at startup

## Parameters

* **id**: *optional* - unique id and/or DCC address of the Loco/s in the roster
* **name**: *optional* - name of the locos for the roster entry.
* **functions**: *optional* - forward slash (/) separated list of function labels. Labels prefixes with asterisk (*) will be treated as momentary.

## Responses

* Response for ``<j R>``
    * ``<jR [«id1» «id2» «id3» ...]>``
        * **id1..n:** unique id and/or DCC address of each Loco in the roster

* Response for ``<j R «id»>``
    * ``<jR «id» "desc" "funct0/funct1/funct2/.../funct31">``
        * **id1..n:** = unique id and/or DCC address of a Loco in the roster
        * **desc** = in quotes, empty or the description of the loco
        * **funct0..31** = in quotes, empty or the Label for each function 0-31 for the loco

* Response for ``<J R «id» "«name" "«functions»">``

    * none

* Response for ``<J R «id» DELETE>``

    * none

* Response for ``<J R SAVE>``

    * ``<* Roster::save completed *>``

----

## Notes

* Function labels starting with an asterisk (*) should be treated as momentary. Those without should be treated as latching.
* When creating roster entries, the ids (the DCC address) must be unique.
* Creating a roster entry for an id that already exists will replace it with new entry without warning.

----

## Examples

[Also search for 'J R'](?_J_R)

### *Examples Commands*

* request list of locos in the roster: ``<J R>``
* request the details of loco with an id of 100: ``<J R 100>``
* create new roster entry with a DCC address of 4793: ``< J R 4793,"BR Class 47 47593 'Galloway Princess'","Run Lights/Sound On-Off/*Brake Function 1/*Air Horn (High)/*Air Horn (Low)/Heavy Load/*Manual Notching Down/*Manual Notching Up/Manual Notching Logic On-Off/Shunting Mode/*Conductor's Signal/*Uncouple Shuffle/*Radiator Fan/Apply Release Loco Brake (Auto)/*Station Announcement #1/*Volume/Open-Close Cab Door/Brake Function #2 (Emergency)/*Station Announcement #2/Apply-Release Hand Brake/*Air Dump/Windscreen Wiper/*Shunting Radio #1/*Shunting Radio #2/Compressor/Sanding Valve/Sound Fader/Curve Squeal/Rail Clank/*AWS-TPWS/*Spirax Valve/*Air Let Off/">``
* create new roster entry for use with DC, with a notional DCC address of 10: ``<J R 10,"DC Loco 10","/////////////////////////////FQ490 Hz/FQ3400 Hz/FQ62500 Hz">``

### Example Responses

* a list of locos in the roster: <br/>``<jR 100 201 203 1005>``
* details of loco ``100`` from the roster: <br/>``<jR 100, "Class 37 Loram Livery", "Lights/WarmEngineStart/Brake/*Single-Horn/*Double-Horn/Light Engine Mode/Coasting/Speed Lock/Sound Fade OutIn/Flange Squeal//*Buffer Up/*Coupling/STATIONARY-Guard's Whistle MOVING-Detonators/Wagon Snatching & Buffering/High Intensity Light-On/Red Tail Lights On Both Ends Non di/Marker Lights On Both Ends Non di/Cab Light On-No.1 End Fan/Cab Light On-No.2 End non fan/No.1 End Dir Lights Off/No.2 End Dir Lights Off/Compressor/Windscreen Wipers/Engine Room">``
* response if loco ``999`` is not in the roster: <br/> ``<jR 999 X>``

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

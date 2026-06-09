---
tags:
  - _J_R
  - _J_R_id
---

# <small>``<J R [«id»]>``</small> <br/>Request Roster info

Serial command to request roster info.

## Command

* ``J R``

## Parameters

* **id**: *optional* <br/>unique id and/or DCC address of the Loco/s in the roster

## Response

**Response to** ``<j R>``:

``<jR [«id1» «id2» «id3» ...]>``

* ``jR`` = the 'message identifer'
* **id1..n:** unique id and/or DCC address of each Loco in the roster

**Response to** ``<j R «id»>``:

``<jR «id» ""|"desc" ""|"funct0/funct1/funct2/.../funct31">``

* ``jR`` = the 'message identifer'
* **id1..n:** = unique id and/or DCC address of a Loco in the roster
* **desc** = in quotes, empty or the description of the loco
* **funct0..31** = in quotes, empty or the Label for each function 0-31 for the loco

## Notes

* Function labels starting with an asterix (*) should be treated as montentary. Those without should be treated as latching.

----

## Examples

[Also search for 'J R'](?_J_R)

### *Examples Commands*

* request list of locos in the roster: ``<J R>``
* request the details of loco with an id of 100: ``<J R 100>`` 

### Example Responses

* a list of locos in the roster: <br/>``<jR 100 201 203 1005>`` 
* details of loco ``100`` from the roster: <br/>``<jR 100, "Class 37 Loram Livery", "Lights/WarmEngineStart/Brake/*Single-Horn/*Double-Horn/Light Engine Mode/Coasting/Speed Lock/Sound Fade OutIn/Flange Squeal//*Buffer Up/*Coupling/STATIONARY-Guard's Whistle MOVING-Detonators/Wagon Snatching & Buffering/High Intensity Light-On/Red Tail Lights On Both Ends Non di/Marker Lights On Both Ends Non di/Cab Light On-No.1 End Fan/Cab Light On-No.2 End non fan/No.1 End Dir Lights Off/No.2 End Dir Lights Off/Compressor/Windscreen Wipers/Engine Room">`` 

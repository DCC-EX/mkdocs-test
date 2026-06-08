---
tags:
  - _=
  - _equals
  - _equals_track_MAIN
  - _equals_track_MAIN_INV
  - _equals_track_MAIN_AUTO
  - _equals_track_PROG
  - _equals_track_OFF
  - _equals_track_NONE
  - _equals_track_EXT
  - _equals_track_AUTO
  - _equals_track_INV
  - _equals_track_DC_loco
  - _equals_track_DC_INV_loco
  - _equals_track_DC_X_loco
---

# ``<= [«trackletter» «mode»] [«id»]>`` <br/>Request or Configure Track Manager <span style="display:none;">(_equals)</span>

Serial command to request infomation about the mode of all tracks or alter the mode of a track.

## Command

* ``=``

## Parameters

* **trackletter** *optional* - one of:

    * blank = Request the current Track Manager configuration
    * ``A`` through ``H`` representing one of the outputs of the/a motor shield.

* **mode** *required if track letter supplied.* One of:

    * ``MAIN``
    * ``MAIN_INV``
    * ``MAIN_AUTO`` <BR/> Deprecated alias of ``AUTO`` but only when preceeded by a sperate ``MAIN`` command.
    * ``PROG``
    * ``DC``
    * ``DC_INV`` = DC reversed polarity
    * ``DCX`` = DC reversed polarity (same as DC_INV) <br/>With special alias of ``DCX`` for ``DC_INV``
    * ``NONE``

* **id** the cab (loco) ID. *Required when specifying DC or DC_INV / DCX*

## *Response*

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

(for each track/channel) <br/>``<= [«trackletter» «state»] [«cab»]>``

* ``=`` = the 'message identifer'
* **trackletter**: ``A``-``H``
* **state**: ``PROG``, ``MAIN``, ``MAIN_INV``, ``MAIN A``, ``DC``, ``DCX``, ``NONE``
* **id**: cab(loco) equivalent to a fake DCC Address for DC and DCX only

## *Notes*

* Whenever a track's mode is changed, track power is automatically turned off on that track.
* Since only one channel can be ``PROG``, changing a second channel to ``PROG``, will force the other to ``NONE``
* The response to ``DC_INV`` is ``DCX``
* The response to ``DCC_MAIN`` is ``MAIN A``

----

## *Examples*

[Also search for '='](?_equals)

### *Examples Commands*

* Request track status ``<=>``
* Set track A to DC with address 10 ``<= A 10>``
* TBA

### *Example Responses:*

* Response/broadcast to track status for a default EX-CommandStation<br/> ``<= A MAIN>``<br/>``<= B PROG>``
* Response/broadcast to setting track *A* to *DC* with address 10<BR/>``<= A 10>``<br/>``<= B PROG>``<br/>``<p1 A>``<br/>``<p0 B>``
* TBA

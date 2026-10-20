---
tags:
  - _=
  - _8equals8
  - _8equals8_track_9MAIN9
  - _8equals8_track_9MAIN9_9INV9
  - _8equals8_track_9MAIN9_9AUTO9
  - _8equals8_track_9PROG9
  - _8equals8_track_9OFF9
  - _8equals8_track_9NONE9
  - _8equals8_track_9EXT9
  - _8equals8_track_9AUTO9
  - _8equals8_track_9INV9
  - _8equals8_track_9DC9_loco
  - _8equals8_track_9DC9_9INV9_loco
  - _8equals8_track_9DC9_9X9_loco

search:
  boost: 3
---

# Serial commands to: Request or Configure Track Manager

Serial command to request information about the modes of all tracks or alter the mode of a specific track.

``<=>``
``<= «trackletter» «mode»>``
``<= «trackletter» DC|DC_INV «id»>``

----

## Commands

* ``<=>`` = Request the current Track Manager configuration
* ``<= «trackletter» «mode»>`` = set a specific track to a mode (not DC)
* ``<= «trackletter» «mode» «id»>`` = set a specific track to a mode (DC)

## Parameters

* **trackletter** one of:

    * ``A`` through ``H`` representing one of the outputs of the/a motor shield.

* **mode** *required if track letter supplied.* One of:

    * ``MAIN``
    * ``MAIN_INV``
    * ``MAIN_AUTO`` <BR/> Deprecated alias of ``AUTO`` but only when preceded by a separate ``MAIN`` command.
    * ``PROG``
    * ``DC``
    * ``DC_INV`` = DC reversed polarity
    * ``DCX`` = DC reversed polarity (same as DC_INV) <br/>With special alias of ``DCX`` for ``DC_INV``
    * ``NONE``

* **id** the cab (loco) ID. *Required when specifying DC or DC_INV / DCX*

## Response

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

(for each track/channel) <br/>``<= [«trackletter» «state»] [«cab»]>``

* **trackletter**: ``A``-``H``
* **state**: ``PROG``, ``MAIN``, ``MAIN_INV``, ``MAIN A``, ``DC``, ``DCX``, ``NONE``
* **id**: cab(loco) equivalent to a fake DCC Address for DC and DCX only

----

## Notes

* Whenever a track's mode is changed, track power is automatically turned off on that track.
* Since only one channel can be ``PROG``, changing a second channel to ``PROG``, will force the other to ``NONE``
* The response to ``DC_INV`` is ``DCX``
* The response to ``DCC_MAIN`` is ``MAIN A``

----

## Examples

[Also search for '='](?_equals)

### Example Commands

* Request track status ``<=>``
* Set track A to DC with address 10 ``<= A 10>``
* ==TODO== LOW - Example Commands

### Example Responses

* Response/broadcast to track status for a default EX-CommandStation<br/> ``<= A MAIN>``<br/>``<= B PROG>``
* Response/broadcast to setting track *A* to *DC* with address 10<BR/>``<= A 10>``<br/>``<= B PROG>``<br/>``<p1 A>``<br/>``<p0 B>``
* ==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

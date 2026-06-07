---
tags:
  - _:e:
  - _:e:_track_MAIN
  - _:e:_track_MAIN_INV
  - _:e:_track_MAIN_AUTO
  - _:e:_track_PROG
  - _:e:_track_OFF
  - _:e:_track_NONE
  - _:e:_track_EXT
  - _:e:_track_AUTO
  - _:e:_track_INV
  - _:e:_track_DC_loco
  - _:e:_track_DC_INV_loco
  - _:e:_track_DC_X_loco
---

# ``<= [«trackletter» «mode»] [«id»]>`` - Request or Configure Track Manager

Serial command to turn power on or off to all or specific tracks.  Also allows joining the MAIN and PROG tracks together.

## Command

* **=**

## Parameters

* **trackletter:** *optional*

    * blank = Request the current Track Manager configuration
    * ``A`` through ``H`` representing one of the outputs of the/a motor shield.

* **mode:** *required if track letter supplied.* One of:

    * ``MAIN``
    * ``MAIN_INV``
    * ``MAIN_AUTO`` <BR/> Deprecated alias of ``AUTO`` but only when preceeded by a sperate ``MAIN`` command.
    * ``PROG``
    * ``DC``
    * ``DC_INV`` = DC reversed polarity
    * ``DCX`` = DC reversed polarity (same as DC_INV) <br/>With special alias of ``DCX`` for ``DC_INV``
    * ``NONE``

* **id:** the cab (loco) ID. *Required when specifying DC or DC_INV / DCX*

## *Response*

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

(for each track/channel that has changed) ``<= trackletter state cab>``

* **trackletter:** ``A``-``H``
* **state:** ``PROG``, ``MAIN``, ``MAIN_INV``, ``MAIN A``, ``DC``, ``DCX``, ``NONE``
* **id:** cab(loco) equivalent to a fake DCC Address for DC and DCX onl

## *Notes*

* Whenever a track's mode is changed, track power is automatically turned off on that track.
* Since only one channel can be PROG, changing a second channel to PROG, will force the other to ``NONE``
* The response to ``DC_INV`` is ``DCX``
* The response to ``DCC_MAIN`` is ``MAIN A``

----

## *Examples*

### *Examples Commands*

TBA

### *Example Responses:*

TBA

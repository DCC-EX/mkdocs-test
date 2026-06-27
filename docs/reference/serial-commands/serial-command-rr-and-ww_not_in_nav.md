---
tags:
    - _9R9
    - _9R9_cv
    - _9R9_9LOCOID9
    - _9R9_9CONSIST9
    - _r_loco_cv
    - _9V9_cv_bitPosition_bitvalue
    - _9V9_cv_value
    - _9W9_loco
    - _9W9_9CONSIST9_loco
    - _9W9_9CONSIST9_loco_9REVERSE9
    - _9W9_cv_value
    - _9W9_cv_bitPosition_bitValue
    - _w_loco_cv_value
    - _9B9_cv_bitPosition_bitValue
    - _b_loco_cv_bitPosition_bitValue
---

# <small>``<R [«cv»|LOCOID|CONSIST]>`` <br/>``<r «loco» «cv»>`` <br/>``<W [«loco»]|[«cv» «value»]|[«loco» «cv» «bitValue» «bit»]|[CONSIST «loco» [REVERSE]]>`` <br/>``<V [«cv» «value»]|[«cv» «bit» «bitValue»]>`` <br/>``<B «cv» «bit» «bitValue»>`` <br/>``<b «loco» «cv» «bit» «bitValue»>``</small> <br/>Read and write CVs

Serial commands to read and write CVs on the PROG track (Service mode) or on the MAIN track (PoM). This includes reading and writing the decoder DCC Address.

It does not include reading or writing to DCC accessory decoders.

## Commands

### Reading CVs

* ``<R>`` Read the driveable loco id on PROG track. <br/>The response may be the long address, short address or consist address.
* ``<R «cv»>`` Read a cv on PROG track
* ``<R LOCOID>`` Read the loco id (ignoring the consist address) on the PROG track
* ``<R CONSIST>`` Read the consist id on PROG track
* ``<r «loco» «cv»>`` PoM read cv on MAIN track - <span style="color:red">Requires RailCom</span>
* ``<V «cv» bit «bitValue»>`` Fast read bit with expected value
* ``<V «cv» «value»>`` Fast read cv with expected value

### Writing CVs

* ``<W «loco»>`` Write loco address on PROG track
* ``<W CONSIST «loco»>`` write consist address on PROG track
* ``<W CONSIST «loco» REVERSE>`` Write consist address and reverse flag on PROG track
* ``<W «cv» «value»>`` Write cv value on PROG track
* ``<W «cv» «bitValue» «bit»>`` Write cv bit on PROG track
* ``<w «loco» «cv» «value»>`` PoM write cv on MAIN track
* ``<B «cv» «bitValue» «bit»>`` Write cv bit on PROG track
* ``<b «loco» «cv» «bitValue» «bit»>`` PoM write cv bit on MAIN track

## Parameters

* **loco**: DCC address to read or change. <br/>This can be a long or short address.  See note below.
* **cv**: CV to read or change <br/>
Avoid writing CV1, CV17 & CV18 directly. Use the ``<W «loco»>`` command instead.
* **value**: value to read or change the CV to
* **bit**:  cv bit to read or change
* **bitValue**: value to read or change the bit to - one of:
    * ``1``
    * ``0``

## Responses

### Reading CVs - Responses

### Response for ``<R>``

* ``<r «address»>``
    * ``r``: response/broadcast identifier
    * **address** - one of:
        * If the loco is in a consist (CV19), the address returned by will be the consist address.
        * If not in a consist (CV19) DCC Address of the decoder/loco. The short (``1``-``127``) or long (``128``-``10293``) address of the engine decoder
        * ``-1`` = failed read

### Response for ``<R LOCOID>``

* ``<r LOCOID «address»>``
    * ``r``: response/broadcast identifier
    * **address** - one of:
        * DCC Address of the decoder/loco. The short (``1``-``127``) or long (``128``-``10293``) address of the engine decoder
        * ``-1`` = failed read

### Response for ``<R CONSIST>``

* ``<r CONSIST «address»>``
    * ``r``: response/broadcast identifier
    * **address** - one of:
        * If the loco is in a consist (CV19), the address returned by will be the consist address.
        * ``-1`` = failed read or not in a consist

### Response for ``<R «cv»>``

* ``<r «cv» «value»>``
    * ``r``: response/broadcast identifier
    * **cv**: the cv read
    * **value** - one of:
        * the value of the CV read
        * ``-1`` = failed read

### Response for ``<V «cv» «value»>``

* ``<v «cv» «value»>``
    * ``v``: response/broadcast identifier
    * **cv**: the cv read
    * **value** - one of:
        * the value of the CV read
        * ``-1`` = failed read

### Response for ``<V «cv» «bit» «bitValue»>``

* ``<v «cv» «bit» «bitValue»>``
    * ``v``: response/broadcast identifier
    * **cv**: the cv read
    * **bit**: the bit read
    * **bitValue** - one of:
        * ``1``
        * ``0``
        * ``-1`` = failed read

### Response for ``<r «loco» «cv»>``

==TODO== Response for ``<r «loco» «cv»>``

### Writing CVs - Responses

### Response for ``<W «loco»>``

* ``<w «address»>``
    * ``w``: response/broadcast identifier
    * **address** - one of:
        * DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder
        * ``-1`` = failed read

### Response for ``<W CONSIST «loco»>``

==TODO== Response for ``<W CONSIST «loco»>``

### Response for ``<W CONSIST «loco» REVERSE>``

==TODO== Response for ``<W CONSIST «loco» REVERSE>``

### Response for ``<W «cv» «value»>``

* ``<w «cv» «value»>``
    * ``w``: response/broadcast identifier
    * **cv**: the cv written
    * **value** - one of:
        * the value of the CV written/read
        * ``-1`` = failed read

### Response for ``<W «cv» «bitValue» «bit»>``

==TODO== Response for ``<W «cv» «bitValue» «bit»>`

### Response for ``<w «loco» «cv» «value»>``

no response.

### Response for ``<B «cv» «bitValue» «bit»>``

* ``<w «cv» «value»>``
    * ``w``: response/broadcast identifier
    * **cv**: the cv written
    * **bit**: the bit written
    * **biValue** - one of:
        * the value of the bit written/read ``0``|``1``
        * ``-1`` = failed read

### Response for ``<b «loco» «cv» «bitValue» «bit»>``

==TODO== Response for ``<b «loco» «cv» «bitValue» «bit»>``

## Notes

* ``<W «address»>`` will write a short address (CV1) or long address (CV17 plus CV18) depending on the value entered.  It will also adjust CV29 automatically depending on what address type is required.
    * ``1``-``127`` will be a short address
    * ``128``-``10293`` will be a long address

    Note that addresses above `9999`` cannot be used by *some* other brands of command station. So if you plan to take your loco to other layouts it is recommended that you avoid the ``10000``-``10293`` (inclusive) range.

* **IMPORTANT:** If the loco is in a consist (CV19), the address returned by ``<R>`` will be the consist address, not the decoder address. To always get the decoder address, use ``<R LOCOID>`` instead.

* When combined with the ``<D ACK ON>`` Command, the ``<R>`` Command (with or without parameters) can be used for diagnostics, for example when you get a ``-1`` response.

* By design, for safety reasons, the NMRA specification prevents locos from responding to throttle or function commands while on the service track. A loco WILL NOT MOVE on the service track! Don't let the little 'jumps' you may see when you are programming a CV confuse you. The loco pulses the motor to give a jump in current that we read as an 'ACK' (acknowledgment), that causes some locos to stutter ahead slightly every time you read or write a CV.

* The ``<V ..>`` commands are designed to offer faster verification of the value held in a CV and can be used instead of the ``<R>`` commands. Instead of reading a bit value, it compares the bit to an expected value. It will attempt to verify the value first, an if it is successful, will return the value as if it was simply 'read'. If the verify fails, it will perform a read bit command and return the value read.

* ``<R cv callbacknum callbacksub>`` (Deprecated) read cv value on PROG track. Do not use. Not explained here

* ``<W cv value callbacknum callbacksub>`` (Deprecated) Write cv value on PROG track. Do not use. Not explained here.

* ``<B cv bit value callbacknum callbacksub>`` (Deprecated) Do not use. Not explained here.

----

## Examples

[Also search for 'R'](?_R) or [search for 'W'](?_W)

### Example Commands

* Read loco address on PROG track: ``<R>``
* Read cv 4 on PROG track: ``<R 4>``
* Read loco actual DCC address on PROG track: ``<R LOCOID>``
* Read loco consist (CV19) address on PROG track: ``<R CONSIST>``
* ==TODO== LOW - Example Commands

### Example Responses

* read address on PROG track (successful): ``<r 3>``
* read address on PROG track (fail): ``<r -1>``
* read CV 4 on PROG track (successful): ``<r 4 1>``
* ==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

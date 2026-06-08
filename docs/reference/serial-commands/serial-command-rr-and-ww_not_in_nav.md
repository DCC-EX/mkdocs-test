---
tags:
    - _R
    - _R_cv
    - _R_LOCOID
    - _R_CONSIST
    - _r_loco_cv
    - _V_cv_bit_bitvalue
    - _V_cv_value
    - _W_loco
    - _W_CONSIST_loco
    - _W_CONSIST_loco_REVERSE
    - _W_cv_value
    - _W_cv_bitvalue_bit
    - _w_loco_cv_value
    - _B_cv_bit_bitvalue
    - _b_loco_cv_bit_bitvalue
---

# ``<R [«cv»|LOCOID|CONSIST]>`` <br/>``<r «loco» «cv»>`` <br/>``<W [«loco»]|[«cv» «value»]|[«loco» «cv» «bitValue» «bit»]|[CONSIST «loco» [REVERSE]]>`` <br/>``<V [«cv» «value»]|[«cv» «bit» «bitValue»]>`` <br/>``<B «cv» «bit» «bitValue»>`` <br/>``<b «loco» «cv» «bit» «bitValue»>`` <br/>Read and write CVs

Serial command to Read and write CVs on the PROG track (Service mode) or on the MAIN track (PoM).

## Command

* ``R`` <br/>
* ``r`` <br/>
* ``W`` <br/>
* ``w`` <br/>
* ``V`` <br/>
* ``B`` <br/>
* ``b``

### Command Variations

#### Reading CVs

* ``<R>`` Read driveable loco id (may be long, short or consist)
* ``<R «cv»>`` Read cv
* ``<R LOCOID>`` read loco id (ignoring consist) on PROG track
* ``<R CONSIST>`` read consist id on PROG track
* ``<r «loco» «cv»>`` POM read cv on main track
* ``<V «cv» bit «bitValue»>`` Fast read bit with expected value
* ``<V «cv» «value»>`` Fast read cv with expected value

#### Writing CVs

* ``<W «loco»>`` Write loco address on PROG track
* ``<W CONSIST «loco»>`` write consist address on PROG track
* ``<W CONSIST «loco» REVERSE>`` Write consist address and reverse flag on PROG track
* ``<W «cv» «value»>`` Write cv value on PROG track
* ``<W «cv» «bitValue» «bit»>`` Write cv bit on prog track
* ``<w «loco» «cv» «value»>`` POM write cv on main track
* ``<B «cv» «bitValue» «bit»>`` Write cv bit
* ``<b «loco» «cv» «bitValue» «bit»>`` POM write cv bit on main track

## Parameters

* **loco**: DCC address to read or change. This can be a long or short address.
* **cv**: CV to read or change
* **value**: value to change the CV to
* **bit**:  cv bit to change
* **bitValue**: value to change the bit to - one of:
    * ``1``
    * ``0``

## *Response*

### Reading CVs - Responses

**Response to** ``<R>``:

* ``<r «address»>``
    * ``r``: response/broadcast identifier
    * **address** - one of:
        * If the loco is in a consist (CV19), the address returned by will be the consist address.
        * If not in a consist (CV19) DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder
        * ``-1`` = failed read

**Response to** ``<R LOCOID>``:

* ``<r LOCOID «address»>``
    * ``r``: response/broadcast identifier
    * **address** - one of:
        * DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder
        * ``-1`` = failed read

**Response to** ``<R CONSIST>``:

* ``<r CONSIST «address»>``
    * ``r``: response/broadcast identifier
    * **address** - one of:
        * If the loco is in a consist (CV19), the address returned by will be the consist address.
        * ``-1`` = failed read or not in a consist

**Response to** ``<R «cv»>``:

* ``<r «cv» «value»>``
    * ``r``: response/broadcast identifier
    * **cv**: the cv read
    * **value** - one of:
        * the value of the CV read
        * ``-1`` = failed read

**Response to** ``<V «cv» «value»>``:

* ``<v «cv» «value»>``
    * ``v``: response/broadcast identifier
    * **cv**: the cv read
    * **value** - one of:
        * the value of the CV read
        * ``-1`` = failed read

**Response to** ``<V «cv» «bit» «bitValue»>``:

* ``<v «cv» «bit» «bitValue»>``
    * ``v``: response/broadcast identifier
    * **cv**: the cv read
    * **bit**: the bit read
    * **bitValue** - one of:
        * ``1``
        * ``0``
        * ``-1`` = failed read

**Response to** ``<r «loco» «cv»>``

==TODO==

### Writing CVs - Responses

**Response to* ``<W «loco»>``:

* ``<w «address»>``
    * ``w``: response/broadcast identifier
    * **address** - one of:
        * DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder
        * ``-1`` = failed read

**Response to* ``<W CONSIST «loco»>``:

==TODO==

**Response to* ``<W CONSIST «loco» REVERSE>``:

==TODO==

**Response to* ``<W «cv» «value»>``:

* ``<w «cv» «value»>``
    * ``w``: response/broadcast identifier
    * **cv**: the cv written
    * **value** - one of:
        * the value of the CV written/read
        * ``-1`` = failed read

**Response to* ``<W «cv» «bitValue» «bit»>``:

==TODO==

**Response to* ``<w «loco» «cv» «value»>``:

no response.

**Response to* ``<B «cv» «bitValue» «bit»>``:

* ``<w «cv» «value»>``
    * ``w``: response/broadcast identifier
    * **cv**: the cv written
    * **bit**: the bit written
    * **biValue** - one of:
        * the value of the bit written/read ``0``|``1``
        * ``-1`` = failed read

**Response to* ``<b «loco» «cv» «bitValue» «bit»>``:

==TODO==

## *Notes*

* IMPORTANT: If the loco is in a consist (CV19), the address returned by ``<R>`` will be the consist address, not the decoder address.
* By design, for safety reasons, the NMRA specification prevents locos from responding to throttle or function commands while on the service track. A loco WILL NOT MOVE on the service track! Don’t let the little ‘jumps’ you may see when you are programming a CV confuse you. The loco pulses the motor to give a jump in current that we read as an ‘ACK’ (acknowledgment), that causes some locos to stutter ahead slightly every time you read or write a CV.
* When combined with the ``<D ACK ON>`` Command, the ``<R>`` Command (with or without parameters) can be used for diagnostics, for example when you get a ``-1`` response.
* the ``<V ..>`` commands are designed to offer faster verification of the value held in a CV and can be used instead of the ``<R>`` commands. Instead of reading a bit value, it compares the bit to an expected value. It will attempt to verify the value first, an if it is successful, will return the value as if it was simply 'read'. If the verify fails, it will perform a read bit command and return the value read.
* ``<R cv callbacknum callbacksub>`` (Deprecated) read cv value on PROG track. Not explained here
* ``<W cv value ignore1 ignore2>`` (Deprecated) Write cv value on PROG track. Not explained here.
* ``<B cv bit value callbacknum callbacksub>`` (Deprecated) Not explained here.
* ``<W cv value callbacknum callbacksub>`` (Deprecated) Not explained here.

----

## *Examples*

[Also search for !](?_!)

### *Examples Commands*

* Read loco address on PROG track: ``<R>``
* Read cv 4 on PROG track: ``<R 4>``
* Read loco actual DCC address on PROG track: ``<R LOCOID>``
* Read loco consist (CV19) address on PROG track: ``<R CONSIST>``
* ==TODO==

### *Example Responses:*

* read address on PROG track (successful): ``<r 3>``
* read address on PROG track (fail): ``<r -1>``
* read CV 4 on PROG track (successful): ``<r 4 1>``
* ==TODO==

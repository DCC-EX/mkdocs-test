---
tags:
  - _T_id_addr_subadd
  - _T_id_DCC_addr_subadd
  - _T_id_DCC_linearAddr
  - _T_id_vpin_closedValue_thrownValue
  - _T_id_SERVO_vpin_closedValue_thrownValue
  - _T_id_VPIN_vpin
  - _T_id
  - _T
  - _T_id_X
  - _T_id_C
  - _T_id_T
  - _T_id_value
  - _J_T
  - _J_T_id
---

# ``<T [«id»] [«various parameters»]>`` + <br/> ``<J T [«id»]>`` <br/>Define or manage Turnouts/Points

Serial command to define or manage Turnouts/Points.

## Command

* ``T``

Command Variations

### Defining and deleting Turnouts/Points

* ``<T «id» DCC «addr» «subadd»>`` Create DCC turnout/point
* ``<T «id» DCC «»>`` Create DCC turnout/point
* ``<T «id» SERVO «vpin» «closedValue» «thrownValue» «profile»>`` Create Servo turnout/point
* ``<T «id» VPIN «vpin»>`` Create pin turnout/point
* ``<T «id»>`` Delete turnout/point

### Managing Turnouts/Points

* ``<T>`` List all turnouts/points<br/> Equivalent to ``<J T>``
* ``<J T>`` List all turnouts/points<br/> Equivalent to ``<T>``
* ``<T «id» X>`` List turnout/point details<br/> Equivalent to ``<J T «id»>``
* ``<J T «id»>`` List turnout/point details<br/> Equivalent to ``<T «id» X>``
* ``<T «id» «state»>`` Throw/Close turnout/point
* ``<T «id» «value»>`` Close (value=0) ot Throw turnout/point

## Parameters

* **id** id of the Turnout/Point to define or manage (``0``-``32767``)
* **addr** ranges from ``0`` to ``511``
* **subAddr** ranges from ``0`` to ``3``
* **linearAddr** ranges from ``1`` (address 1/subaddress 0) to ``2044`` (address 511/subaddress 3).
* **vpin** vpin to which the servo is attached
* **closedValue** the PWM value corresponding to the servo position for CLOSED state, normally in the range ``102`` to ``490``
* **thrownValue** the PWM value corresponding to the servo position for THROWN state, normally in the range ``102`` to ``490``
* **value**
* **state** one of
    * ``1`` = Throw
    * ``T`` = Throw  (not seen in responses)
    * ``0`` = Close
    * ``C`` = Close  (not seen in responses)
    * ``X`` = eXamine  (not seen in responses)
* **profile**  one of
    • ``0`` = Instant
    • ``1`` = Fast (0.5 sec)
    • ``2`` = Medium (1 sec)
    • ``3`` = Slow (2 sec)
    • ``4`` = Bounce (subject to revision)

## *Response*

The following are not a direct response, but rather a broadcast that will be triggered as a result of any track manager changes.

**For the following commands:**

* ``<T «id» DCC «addr» «subaddr»>``
* ``<T «id» DCC «»>``
* ``<T «id» SERVO «vpin» «closedValue» «thrownValue» «profile»>``
* ``<T «id» VPIN «vpin»>``
* ``<T «id»>``

There is no response.

**For** ``<T>`` and ``<J T>`` **the response/broadcast is:**

Repeated for each defined Turnout/Point:

* Response: ``<H «id» «state»>``
* Response (fail): N/A
* Response (no defined turnouts/points): ``X``
    * **id** - The numeric ID (0-32767) of the turnout/point to control.
    * **state:** one of
        * 1 = Thrown,
        * 0 = Closed

**For** ``<T «id» X>`` and ``<J T «id»>`` **the response/broadcast is:**

* (DCC Accessories): ``<H «id» DCC «addr» «subaddr» «state»>``
* (Servos): ``<H «id» SERVO «vpin» «thrownValue» «closedValue» «profile» «state»>``
* (VPIN): ``<H «id» VPIN «vpin» «state»>``
* (LCN): ``<H «id» LCN «state»>``
* (fail/no such turnout/point): ``<X>``
    * **id** - The numeric ID (0-32767) of the turnout/point to control.
    * **state** one of
        * ``1`` = Thrown,
        * ``0`` = Closed
* (fail): ``<X>``

**For** ``<T «id» «state»>`` **the response/broadcast is:**

* (successful): ``<H «id» «state»>``
    * **id** - The numeric ID (0-32767) of the turnout/point to control.
    * **state** one of
        * ``1`` = Thrown,
        * ``0`` = Closed
* (fail): ``<X>``

**For** ``<T «id» «value»>`` **the response/broadcast is:**

==TODO==

**For** ``<T «id»>`` **the response/broadcast is:**

* *Response:*
  Successful: ``<O>``
  Fail: ``<X>``  (Id does not exist)
    * **id** - The numeric ID (0-32767) of the turnout/point to control.

## *Notes*

* *Servos are not supported on the minimal HAL (Uno or Nano target).*
* The active and inactive positions are defined in terms of the PWM parameter (0-4095 corresponds to 0-100% PWM). The limits for an SG90 servo are about 102 to 490. The standard range of 1ms to 2ms pulses correspond to values 205 to 409.
Profile defines the speed and style of movement: 0=Instant, 1=Fast (0.5 sec), 2=Medium (1 sec), 3=Slow (2 sec) and 4=Bounce (subject to revision).
* ``<T «id» «vpin «closedValue» «thrownValue>`` is a depricated version of the command. It is not documented here.
* ``<T «id» «addr» «subadd»>`` is a depricated version of the command. It is not documented here.

----

## *Examples*

[Also search for !](?_!)

### *Examples Commands*

* *Example:* ``<T 23 DCC 5 0>``

    *Example:* You have a turnout/point on your main line going to warehouse industry. The turnout/point is controlled by an accessory decoder with a address of 123 and is wired to output 3. You want it to have the ID of 10. You would send the following command to the CommandStation: ``<T 10 DCC 123 3>``

    This Command means:

    * **T** = (Upper case T) Define a turnout/point
    * **DCC** = The turnout/point is DCC Accessory Decoder based
    * **10** = ID number I am setting to use this turnout/point
    * **123** = The accessory decoders address
    * **3** = The turnout/point is wired to output 3

* *Example:* ``<T 23 DCC 44>`` (corresponds to address 11 subaddress 3)
* *Example:* ``<T 25 VPIN 30>`` defines a turnout/point that operates Arduino digital output pin D30.
* *Example:* ``<T 26 VPIN 164>`` defines a turnout/point that operates the first pin on the first MCP23017 GPIO expander (if present).

### *Example Responses:*

* ==TODO==

The following list is dynamically built from the **EXRAIL** code. It contains all the **EXRAIL** commands with brief definitions.
In many cases the parameters are self explanatory, for example a speed (which will always be a DCC compatible 0..127 where 0=stop and 1=emergency stop)

## Conventions And Important Information

<details markdown="1">
<summary>Click to expand</summary>

- CAPITALISED words - These are EXRAIL commands and are case sensitive
- lowercase words within brackets/braces ``()`` - These are EXRAIL parameters that must be provided, with multiple parameters separated by a comma ``,``, for example ``SEQUENCE(id)`` or ``DELAYRANDOM(min_delay, max_delay)``
- Quoted ``"text"`` - Text within quote marks ``""`` are used as descriptions, and must include the quote characters, for example ``ROUTE(id, "description")`` becomes ``ROUTE(1, "This is the route description")``
- Square brackets ``[]`` - Parameters within square brackets ``[]`` are optional and may be omitted. If specifying these parameters, do not include the square brackets themselves, for example ``ALIAS(name[, value])`` becomes ``ALIAS(MY_ALIAS)`` or ``ALIAS(MY_ALIAS, 3)``
- ``|`` - Use of the ``|`` character means you need to provide one of the provided options only, for example ``<D POWER ON|OFF>`` becomes either ``<D POWER ON>`` or ``<D POWER OFF>``

---

- *AUTOMATION*, *ROUTE*, and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them
- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by I2C expansion (as virtual pins or vpins).
- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin
- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the sequences. If a sensor is latched by the sequence, it can only be unlatched by the sequence so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once
- All IDs used in commands and functions will be numbers, or an ALIAS name if configured
- Most IDs simply need to be unique, however RESERVE/FREE and LATCH/UNLATCH must be in the range 0 - 255

!!! warning "avoid angle brackets and double quotes"

    You must avoid using these characters in all descriptions: ``<``, ``>``, ``"`` as these are part of the native serial protocol and are likely to prevent descriptions showing up in JMRI and other throttle software/clients.

!!! warning "Do not use leading zeros for any numbers!"
  
    Any number with a leading zero will be treated as an octal number, so for example ``ALIAS(MY_ALIAS, 010)`` will assign the value of ``8`` to MY_ALIAS, not ``10``. This is a common mistake that can lead to very confusing behaviour if you don't know about it. Always use numbers without leading zeros, for example ``ALIAS(MY_ALIAS, 10)`` to assign the value of 10 to MY_ALIAS.

</details>

---

# Consists

A "Consist" refers to multiple locos driving one train. This requires the locos to follow the same throttle commands.

## Consist Types

There are four types of consist:

### 1. All locos have the same address

This involves programming the loco addresses individually. All functions will be read by all locos in the consist. Addresses can be easily programmed on the PROG track with the ```<W locoid>``` command.

Disadvantages, visitors or club members domt like having their CVs changed. Functions sent to the address will affect all locos, which is often wrong for lighting rules etc.

### 2. Decoder consist

 The decoders have CVs (19 and 20) to give an address to which they will all respond. Their normal address is not altered. This consist address may be programmed into each loco with the PROG track ```<W CONSIST id [REVERSE]>``` command or main track ```<w locoid CONSIST consistid [REVERSE]>```. Disadvantages as above for CV changes.

### 3. Throttle Consist (NOT POSSIBLE for EXRAIL)

The locos are unchanged and the throttle sends individual speed command to each loco.
Disadvantages are that only the throttle knows about the relationship between the locos and that information can't easily be shared with other throttles, so another throttle may command one of the locos differently and cause mayhem. EXRAIL drives on one loco id so cannot drive this kind of consist. Which loco gets which functions may be configured at the throttle but are unknown to the command station.

### 4. Command Station consists

The command station knows the locos that are in the consist. Any speed commands to the lead loco are transmitted to all following locos. No CVs are modified and any throttle, including EXRAIL  can drive the lead loco or send function commands to the followers, but functions sent to the lead loco are not shared with the other locos, as there is no guarantee that "horn" on one loco isnt "halt and catch fire" on another.  

Throttle commands sent to the following locos are ignored but the command station broadcasts lead loco throttle changes for each loco.

These consists can be built with
 [commands](/reference/serial-commands.md/#consist-control) or EXRAIL.

## Command Station consists with EXRAIL

Command Station consists can be built up with EXRAIL commands:

```BUILD_CONSIST(newloco)```  adds the new loco to follow the existing task loco. Specifying newloco as negative means the loco is facing the opposite way to the rest of the consist.

For example:

```cpp
SETLOCO(3)        // sets currect loco
BUILD_CONSIST(77)  // Makes 3 a consist of 3 and 77
BUILD_CONSIST(88)  // adds loco 88 to the consist
BUILD_CONSIST(-99) // adds loco 99 facing backwards
FWD(10) // all 4 locos set off together 
```

EXRAIL can also break up a consist with the `BREAK_CONSIST` command which will break up any consist that includes the current loco.

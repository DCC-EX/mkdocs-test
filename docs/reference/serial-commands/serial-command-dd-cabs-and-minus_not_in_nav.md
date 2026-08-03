---
tags:
  - _9D9_9CABS9
  - _-
  - _-_loco
---

# <small>``<D CABS>`` ``<- [«loco»]>`` </small> <br/> Loco state table commands

Serial commands to display and manage the loco state table.

## Command(s)

* ``<D CABS>`` Diagnostic display loco state table
* ``<- [«loco»]>`` Remove one loco or all locos from the state table and reminders

## Parameters

* **parameter**: *optional* Loco to remove from the state table and reminders. If not supplied, all will be removed (cleared).

## Responses

### Responses for ``<D CABS>``

``Used=xxx, max=yyy``  Displayed on the serial monitor only.

### Responses for ``<- [«loco»]>``

==TODO== LOW - Responses

## Notes

### Notes for ``<D CABS>``

==TODO== LOW - Notes

### Notes for ``<- [«loco»]>``

Forgets one or all locos. The 'loco' parameter is optional.

Once you send a throttle command to any loco, throttle commands to that loco will continue to be sent to the track. If you remove the loco, or for testing purposes need to clear the loco from repeating messages to the track, you can use this command. Sending <- loco> will forget/clear that loco. Sending <-> will clear all the locos. This doesn't do anything destructive or erase any loco settings, it just clears the speed reminders from being sent to the track. As soon as a controller sends another throttle command, it will go back to repeating those commands.

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ``<- 74>`` - Forgets loco at address 74
* ``<->`` - Forgets all locos

### *Example Responses:*

* ==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

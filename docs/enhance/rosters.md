---
tags:
  - _9J9_9R9_locoid_name_functionMap
  - _9J9_9R9_9SAVE9
  - _9J9_9R9_id_9DELETE9
---

# Roster

The Roster is a list of loco DCC addresses, with names for convenience and a list of named/labelled function keys that are supported by each loco decoder.

## How to create a Roster

There are three ways to create or manipulate a roster

* [In EXRAIL](#roster-in-exrail-as-per-previous-versions)
* [In a Web Browser](#roster-editing-with-a-web-browser)
* [With Serial Commands](#roster-serial-commands)

----

### Roster in EXRAIL (as per previous versions)

Roster entries in EXRAIL are compiled into the command station and therefore are backward compatible with previous versions. On startup the **EXRAIL** ROSTER entries are loaded into RAM before any locally saved roster entries are loaded from non-volatile storage on the command station.

See the [EXRAIL Rosters](../enhance/exrail/exrail-objects-introduction.md#adding-a-roster) page for more information.

## Roster Editing with a Web Browser

!!! note ""

    Available in v5.9.13 and above of **EX-CommandStation** only.

When using a web browser dialog on the command station, the Config.. Roster Editor menu will show a roster editing dialog. This edits and saves roster entries in RAM.

==TODO== needs detailed instructions

==TODO== needs screenshots

----

## Roster Serial Commands

!!! note ""

    Available in v5.9.13 and above of **EX-CommandStation** only.

There are a selection of roster commands which are normally used by throttles to extract roster information from the command station.

`<JR>` returns a list of the DCC loco addresses in the roster, e.g.
`<jR 3 5 100>`

`<JR 100>` Returns details for DCC address 100 e.g.
`<jR 100 "Thomas" "Lights/*Whistle/Squeal">`
The functions are separated by '/' and a '*' prefix indicates that the function is momentary rather than toggled.
A request for a roster that does not exist (eg `<JR 999>`) is returned as `<jR 999 X>`

New Roster commands for v5.9.13 and above:

`<JR id "name" "functions">`  adds or replaces a roster in RAM.

`<JR id DELETE>`  removes a roster entry from ram.

`<JR SAVE>`  saves the current rosters in ram. They will be reloaded again at startup.

See the [Roster Serial Commands](../reference/serial-commands/serial-command-jj-rr_not_in_nav.md) reference page for more information.

--8<-- "snippets/abbr.md"

---
tags:
    - _a_address_subAddr_activate
    - _a_address_subAddr_activate_onoff
    - _a_address_activate
    - _A_address_value
---

# <small>``<A «address» «value»>``</small> <br/><small>``<a «address» [«subAddr»]|[«activate» [onOff]]>``</small> <br/> Instruct Accessory Decoders

Serial commands to activate or dactivate accessory decoders.

## Command(s)

* ``<A «address» «value»>`` Send DCC extended accessory (Aspect) command
* ``<a «address» «subAddr» «activate»>`` Send DCC accessory command activate: 0=deactivate, 1=activate
* ``<a «address» «subAddr» «activate» «onoff»>`` Send DCC accessory command with onoff control activate: 0=deactivate, 1=activate onoff: 0=off, 1=on, 2=toggle
* ``<a «address» «activate»>`` Send dcc accessory command to linear address activate: 0=deactivate, 1=activate

## Parameters

* **address**: *Required* accessory DCC decoder adress to activate or deactivate
* **subAddr**:  accessory DCC decoder sub-address to activate or deactivate
* **activate**:  - one of:
    * ``0`` = deactivate
    * ``1`` = activate
* **onOff**: *optional* description - one of:
    * ``0`` = off
    * ``1`` = on
    * ``2`` = toggle

## Response

### Response for ``<cmd>``

==TODO== responses

## Notes

* EX‑CommandStation can keep track of the direction of any turnout that is controlled by a DCC stationary accessory decoder once its Defined (Set Up).

* All decoders that are not in an engine are accessory decoders including turnouts.

* Any DCC Accessory Decoder based turnouts, as well as any other DCC accessories connected in this fashion, can always be operated using the DCC COMMAND STATION Accessory command:

* There are two interchangeable commands for controlling Accessory Decoders, the Address/Subaddress method (aka “Dual-Coil” method) and linear addressing method. You can either specify an address and its subaddress (Addresses 0-511 with Subaddresses from 0-3) or the straight linear address (Addresses from 1-2044).

* In the mapping used by the **EX-CommandStation**, linear addresses range from linear address 1, which is address 1 subaddress 0, up to linear address 2040 which is address 510 subaddress 3. Decoder address 511 (linear addresses 2041-2044) is reserved for use as a broadcast address and should not be used for decoders. Decoder address 0 does not have a corresponding linear address. This seems strange, but it is the mapping used by many, but not all, commercial manufacturers. If your decoder does not respond on the expected linear address, try adding and subtracting 4 to see if it works. Or use the address/subaddress versions of the commands.

Here is a spreadsheet in .XLSX format to help you: [Stationary Decoder Address Table (xlsx Spreadsheet)](https://dcc-ex.com/reference/downloads/documents.html#stationary-decoder-address-table-xlsx-spreadsheet).

----

## Examples

<!-- [Also search for 'xxx'](?_xxx) or [search for 'xxx'](?_xxx) -->

### *Example Commands*

* ==TODO== Example Commands

### *Example Responses:*

* ==TODO== Example Responses

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

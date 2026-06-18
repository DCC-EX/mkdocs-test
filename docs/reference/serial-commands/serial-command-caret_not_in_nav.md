---
tags:
  - _^
  - _^_ loco
  - _^_ leadLoco_follower [_follower2..7]
---

# <small>``<^ «loco»|[«leadLoco» «follower» [ «follower2..7»]]>``</small> <br/> Manage EX-CommandStation Consists/MUs

Serial commands to manage in-command-station Consists/Multiple Unit Trains (MUs).  These are created and held temporarily in the **EX-CommandStation** and are lost when the command station restarts.

See [Consists page](/products/ex-commandstation/exrail/cookbooks/driving-trains/consists.md) for information on other types of consist.

## Commands

* ``<^>`` List consists
* ``<^ loco>`` Uncouples any consist containing this loco
* ``<^ leadLoco follower [ follower2..7]>`` Creates a consist from up to 8 loco ids (negative for loco in reverse)

## Parameters

* **loco**: DCC Address of the loco to add or remove from the consist.
* **leadLoco**: Notional address of the loco to become the lead loco. (1-10293``) <br/>This does not need to be a real loco. Nor does tit need to be one of teh actual locos in the consts/MU. <br/>This will be the address that you select with a throttle or **EXRAIL** sequence to control all the locos in the consist/Multiple Unit train at the same time.
* **follower1..7**: loco to add to the consist/Multiple Unit train.<br/> negative for a reversed loco.

## Response

==TODO== response

## Notes

* none at this time

----

## Examples

[Also search for '<^>'](?_^) or [search for 'consist'](?consist)

### *Example Commands*

* ==TODO== LOW - Example Commands

### *Example Responses:*

* ==TODO== LOW - Example Responses

--8<-- "snippets/abbr.md"

<style>
  .md-typeset h1 {
    line-height: 1.1 !important;
  }
</style>

<style>
  .md-typeset h3, .md-typeset a, .md-typeset a code {
    margin-bottom: 0 !important;
    font-style: normal !important;
  }
  .md-typeset h3 + p {
    margin-top: 2px !important;
    padding-left: 1em !important;
  }
</style>

# DCC-EX Serial Command List

The following list is dynamically built from the CommandStation-EX code. It contains all the serial commands with brief definitions.
In many cases the parameters are self explanatory. For example a *tSpeed* will always be -1..127 where 0=stop and 1=emergency stop. (See the [Overview](./serial-command-basics.md) for more information on this and other common elements.)

This list appears in the order in which the command parser will detect command patterns.

*Clicking on a command pattern will search this web site for pages which describe or use that command.*

Note: This list is easily, automatically, generated but the various links spread about the documentation take a lot of effort and will be built over time.

--8<-- "snippets/DCCEXCommands.md"

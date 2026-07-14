# Programming with Engine Driver

The [Engine Driver Android app](https://play.google.com/store/apps/details?id=jmri.enginedriver) is capable of reading and writing CVs from your phone or tablet.

## Accessing the DCC-EX page

Touching either the **DCC-EX** Menu item or the button will open the "DCC-EX" screen.

On the **DCC-EX** Screen you can use the "Action" pulldown to select Programming Track (Service Mode)

The commands do assume that you have the loco on the PROG track, and that it is clean etc.

## Read loco address

To read the address, click the Read button on the same line as the 'DCC Address' label.

## Write loco address

To write a new address, enter the address in the 'DCC Address' field and click Write

## Read and write CVs of decoders on the Programming Track

To read a CV, enter the CV number into the 'CV' field, and click the Read button on the same line as the 'CV' label.

To write a new CV value, enter the CV number into the 'CV' field, enter the new value in the 'Value' field and click Write

Optionally, you can use the 'NRMA CVs' pulldown to select a common CV from a list. This just enters the appropriate CV number in the 'CV' field.

## More Information

See the [Engine Driver documentation web site](https://enginedriver.mstevetodd.com/operation/dcc-ex-native-protocol.html#gsc.tab=0) for more detailed information.

These features are only available when the [DCC-EX Native Protocol preference](https://enginedriver.mstevetodd.com/operation/dcc-ex-native-protocol.html#how-to-enable-the-dcc-ex-native-protocol) is enabled. The WiThrottle protocol does not include programming.

## If things don't work

The best way to diagnose problems is to use a [serial monitor](../../../reference/tools/serial-monitor_not_in_nav.md) and the underlying commands. See [Diagnostics](/products/ex-commandstation/loco-programming/serial-programming.md#diagnostics-when-things-dont-work)

Also refer to the [Programming Tips](programming-tips.md) for additional thoughts.

--8<-- "snippets/abbr.md"

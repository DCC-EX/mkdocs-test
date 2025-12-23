# Programming with Engine Driver

These features are only available when the DCC-EX Native Protocol preference is enabled. The WiThrottle protocol does not include programming.

Touching either the DCC-EX Menu item or the button will open the “DCC-EX” screen.

On the DCC-EX Screen you can use the “Action” pulldown to select Programming Track (Service Mode)

The commands do assume that you have the loco on the PROG track, and that it is clean etc. 

## Read loco address

To read the address, click the Read button on the same line as the ‘DCC Address’ label.

## Write loco address

To write a new address, enter the address in the ‘DCC Address’ field and click Write

## Read and write CVs of decoders on the Programming Track

To read a CV, enter the CV number into the ‘CV’ field, and click the Read button on the same line as the ‘CV’ label.

To write a new CV value, enter the CV number into the ‘CV’ field, enter the new value in the ‘Value’ field and click Write

Optionally, you can use the ‘NRMA CVs’ pulldown to select a common CV from a list. This just enters the appropriate CV number in the ‘CV’ field.

## If things dont work

The best way to diagnose problems is to use a serial monito and the underlying commands. See [Diagnostics](/products/ex-commandstation/loco-programming/10-serial-programming.md#diagnostics-when-things-dont-work)
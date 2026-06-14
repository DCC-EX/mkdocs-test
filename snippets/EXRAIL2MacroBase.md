
## THIS IS A PLACEHOLDER FILE THAT WILL BE BUILT AT GITHUB DEPLOY TIME

It will look a bit like this:

## ACTIVATE(addr,subaddr)

Send DCC Accessory Activate packet (gate on then off)

- addr DCC short address of accessory
- subaddr DCC sub address

## ACTIVATEL(linearaddr)

Send DCC Accessory Activate packet (gate on then off)

- linearaddr DCC linear address of accessory

## AFTER(vpin,timer...)

Wait for sensor activated, then deactivated for given time

- vpin Virtual Pin number of sensor
- timer... optional wait in ms, default 500


# Programming using Serial commands

Serial commands are entered on a [serial monitor](?Serial)

This gives you direct access to the underlying DCC-EX features to access the programming track.

All other programming methods through throttles, toolbox or DecoderPro use this interface.

In other words... If this method doesn't work, don't waste your time trying the others!

## Reading a loco id

The command ```<R>``` examines all the necessary CVs and should return something like ```<r 123>``` to indicate that address 123 will drive the loco.
A negative result like ```<r -3>``` indicates that there was an error. See below for diagnosing this problem.

Contrary to what you may read on the internet, reading CV1 is NOT sufficient to find the address of a DCC loco that you wish to drive. It is important to check up to 6 separate CVs to find the address that will drive the loco, especially if it has been given a DCC consist address.

## Setting a loco id

The command ```<W 123>``` will set the locoid to 123. You should confirm this with ```<R>```.

This command will clear any DCC consist settings, decide whether the address is a long or short type and set all the necessary CVs. As before, writing CV1 is not sufficient.

## Reading a CV value

The command ```<R 123>``` will read the value from CV123 and return it like ```<r 123 99>```

Negative values indicate an error accessing the cv. Refer to diagnostics below.

## Setting a CV value

The command ```<W 123 99>``` will write the value 99 into CV123 and return it like ```<r 123 99>```

A negative return value indicates an error.

## DCC Consists

A loco may be given a DCC consist address, it's actual address is not altered, but it will no longer accept throttle movement commands on the actual address. 

The command  ```<W CONSIST 77>``` will set the consist address to 77.

The command  ```<W CONSIST 77 REVERSE>``` will set the consist address to 77 but indicate that the loco is facing backwards compared to others.

- The ```<R>``` command will then return the consist address because that is the address needed to drive it.
- To obtain the actual locoid, use ```<R LOCOID>```.
- To obtain the consist address, use ```<R LOCOID>```.

## Bit management

For advanced use, the individual bits of a cv make be read or written:

```<R 123 7>``` Reads bit 7 of cv 123
```<W 123 7 1>`` Sets bit 7 of cv 123 to 1

## Diagnostics when things don't work

There are a number of very basic checks that you should do before getting into software disgnostics. The vast majority of support calls are solved easily by checking:

- Is the loco on the PROG track?
- Is the PROG track wired to the correct motor shield output?
- Is the track clean?
- Are the loco wheels clean?
- Are the pickups from the wheels clean?
- Is the track power supply plugged in and switched on?

Following that:

- DO you have a PROG track defined, the ```<=>``` command will tell you.
- Issue the ```<1 PROG>``` command and check that the two leds on the motor shield for the PROG track oputput come on

- Check with a meter that you get power to the PROG track.

Issue the command ```<D ACK ON>```, this will enable the output of detailed diagnostic information of what the Command station is doing when it runs programming commands.

Then try the command ```<R 8>``` , this should attempt to read CV 8 (the Decoder manufacturer id). You will get a long diagnostic trace. If the final response is negatine (eg ```<r 8 -1>```) then copy the entire diagnostic trace to a support ticket and we can help. (Experienced users will soon learn to read the trace)

PLEASE DO NOT SEND A SCREENSHOT OR PHOTO!

If the ```<R 8>``` command respinds with a non-negative number like ```<r 8 123>``` that that command has worked,  so you should re-attempt the command that failed and send in the trace of that.

## ACK detector tuning parameters

There are a variety of advanced tuning parameters that can be adjusted to help detect decoders that fall way outside the supposed "standards". In some cases we can only imagine that the decoder creator misplaced a decimal point as the results are a factor of ten outside the standard limits.

These include:

| Command | Description | Parameters |
|---------|-------------|------------|
| `<D ACK ON>` | Enable PROG track diagnostics | None |
| `<D ACK OFF>` | Disable PROG track diagnostics | None |
| `<D ACK LIMIT value>` | Set ACK detection limit mA | `value`: Current limit in mA |
| `<D ACK MIN value MS>` | Set ACK minimum duration mS | `value`: Duration in milliseconds |
| `<D ACK MIN value>` | Set ACK minimum duration µS | `value`: Duration in microseconds |
| `<D ACK MAX value MS>` | Set ACK maximum duration mS | `value`: Duration in milliseconds |
| `<D ACK MAX value>` | Set ACK maximum duration µS | `value`: Duration in microseconds |
| `<D ACK RETRY value>` | Set ACK retry count | `value`: Retry count |
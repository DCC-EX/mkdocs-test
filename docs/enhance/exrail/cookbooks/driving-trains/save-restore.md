# Saving and Restoring speeds

Under some circumstances, you may need to save and restore the speed of your loco. For example after stopping at a signal or being stopped by a `RESERVE` it is necessary to re-apply speed to the loco in order to carry on.

`RESERVE` does not save the speed before it stops your loco, and it doesnt restore it afterwards.

The `SAVE_SPEED` command will save the current loco speed setting (including direction). Where momentum is involved, this will be the speed that the loco has been commanded to use even though it may be accelerating or decelerating towards that value.

The `RESTORE_SPEED` command will restore the saved throttle setting.

For example you may have a signal and you want to stop the loco if the signal is RED...

```cpp
AT(300)  // when I get to the sensor ahead of the signal
SAVE_SPEED  // in case I am forced to stop
WAIT_WHILE_RED(4) // Wait until signal is green or amber
RESTORE_SPEED // carry on as before
```

In the above scenario, the save and restore will have no real effect if the signal is amber or green.

The `WAIT_WHILE_RED` command will stop the loco if the signal is red and wait until the signal changes. Once the signal changes, the script will resume and `RESTORE_SPEED` will restore the previously saved speed.

Note that speed is saved at the loco level, not the exrail task.

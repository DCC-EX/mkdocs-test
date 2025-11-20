# Controlling trains and decoders directly

For the majority of loco control, a task is running with a specific loco in mind, this means that commands like `STOP`, `SPEED(20)`, `REV(10)` etc. do not need to know the loco id at the time you write the sequence. Indeed, the same sequence may be running in multiple parallel tasks controlling different locos.

In other circumstances, it may be necessary to be more explicit, for example switching the carriage lights on a known train. In these cases the X.. functions exist to make explicit calls to a given decoder without having to know or disturb the current task's loco id.

These commands are

```cpp
XFWD(loco,speed)
XREV(loco,speed)
XFON(loco,function)
XFOFF(loco,function)
XFTOGGLE(loco,function)
XPOM(loco,cv,value)
XSAVE_SPEED(loco)
XRESTORE_SPEED(loco)
```

Note that speed is saved at the loco level, not the exrail task.

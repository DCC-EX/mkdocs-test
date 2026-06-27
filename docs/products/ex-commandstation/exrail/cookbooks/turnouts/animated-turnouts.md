# Animated Turnouts/Points

Switching turnouts/points is easy, but sometimes you want to make it more realistic by introducing signals, delays and other automations.

The combination of hidden and virtual turnouts/points makes this easy.

Lets suppose you have a turnout/point ID 100 and to make it look realistic you need to set some signal to stop, wait for the signalman to walk across the lever frame, throw the turnout/point, wait again and set another signal to green.

First we need to hide the real turnout/point from the throttles. This is done by changing the description to the keyword HIDDEN and giving it a different id so we can refer to it later.

```cpp
  TURNOUTL(100,1,"Coal yard exit")  // for example
```

  is changed to

```cpp
  TURNOUTL(1001,1,HIDDEN)
```

  Now we can create a virtual turnout/point that will be seen by the throttles and specify what we want to happen when it is thrown or closed.

```cpp
   VIRTUAL_TURNOUT(100,"Coal yard exit")

   ONCLOSE(100)
     RED(501)  // set approach signal
     RED(505)  // set approach signal
     DELAY(4000) // wait for signalman to move
     CLOSE(1001) // close the real turnout/point
     DELAY(5000)
     GREEN(501) // set approach signal
     DONE

   ONTHROW(100)
     RED(501)  // set approach signal
     RED(505)  // set approach signal
     DELAY(4000) // wait for signalman to move
     THROW(1001) // throw the real turnout/point
     DELAY(5000)
     GREEN(505) // set approach signal
     DONE
```

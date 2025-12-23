# Configuration

The FastClock can either operate in one of three modes:

- Standalone
- Serial Communication with the CS
- I2C Communication with the CS.

To indicate which mode is in use it is necessary to edit the config.h file.

## Standalone use

The config.h file comes pre-configured to use the clock in standalone mode.  No changes are necessary.

## Serial Mode

To communicate in Serial mode it is necessary to edit the config.h file and uncomment the following line:

```cpp
//#define SEND_VIA_SERIAL true
```

This will load the appropriate code including the Wire library.

## I2C mode

To operate in I2C mode edit the config.h file and uncomment the following lines:

```cpp
//#define I2CAddress 0x55 // default I2C address
//#define SEND_VIA_I2C true
```

In this mode the CS will poll the FastClock to obtain the time.  It is necessary to set the same I2C address here as used in the myHal.cpp file within the CS.  This is set to a default of 0x55 (decimal 85) but can be set to some other value if this conflicts with other I2C devices on your setup.

## Screen Header

By default the top of the clock screen displays the name of my own layout.  To insert your layout name change the following line.

```cpp
char header[HDDR_SIZE] = {"Nantyderry Junction"};
```

### Touchscreen Configuration

Finally insert the output of the touchscreen configuration program into the file in place of the following two lines.

```cpp
const byte XP = 7, XM = A1, YP = A2, YM = 6;
const int TS_LEFT=899,TS_RT=122,TS_TOP=100,TS_BOT=898;
```

## Configure existing clock

If you already have a FastClock there are a number of couple of configuration options which allow you to connect your own clock to a  Command Station.

The various configuration options are outlined below

## Connecting your own FastClock

### Connecting via Serial

Connecting via Serial is the simplest option if available.  

- Run a dupont cable from the TX pin on the arduino to a RX pin on the EX-CommandStation.  It is not usually necessary to run a cable from RX to the TX on the EX-CommandStation as  the FastClock is not receiving data back.
- Find the Serial defines in the config.h file (or copy config.example.h to config.h if you don't have one), locate the following lines:

```cpp
//#define SERIAL1_COMMANDS
//#define SERIAL2_COMMANDS
//#define SERIAL3_COMMANDS
```
  
  and uncomment the appropriate one for the serial port you are using.

- Add the following code to your Setup() function:

```cpp
Serial.begin(115200);
while (!Serial) {
; // wait for serial port to connect. Needed for native USB port only
}
```

- Include the following routine within your code:
  
```cpp
void SendTime(byte hour, byte mins, byte speed) {

  int itime = (hour * 60) + mins;
  char buffer[20];
  sprintf(buffer, "<JC %d %d>", itime, speed);
  Serial.println(buffer);
}
```

- Each time the time changes call the SendTime routine as follows:
  
```cpp
SendTime(HH, MM, clockSpeed);
```

  where HH = the hour, MM = minutes and clockSpeed = the fast speed (e.g. at spped 4, 15 seconds represents a minute).

### Connecting via I2C

Connecting via I2C involves a HAL driver file to the Command Station as well as adding some code to the existing FastClock code.  Follow the following steps:

- In the  Command Station code copy the file myHal.cpp_example.txt to myHal.cpp.
- Edit the file myHal.cpp and uncomment the following line near the beginning of the file

```cpp
//  #include "IO_EXFastClock.h"  // FastClock driver
```

- Uncomment the following line near the end of the file

```cpp
//  EXFastClock::create(0x55);
```
  
  0x55 (decimal 85) is the default address but needs to match that in the FastClock code (see below).
  
- Using Dupont connectors connect SDA/SCL/Gnd on the clock to SDA/SCL/Gnd on the  Command Station
  
- Include the following code in your FastClock code:

  Near the top of the sketch:

```cpp
#include <Wire.h>
```

  Within your Setup():

```cpp
Wire.begin(I2CAddress);
Wire.onRequest(TransmitTime);
```

  Add the following function within the sketch

```cpp
void TransmitTime() {
    // send the data over I2C
    // send the time as <mmmm> as two bytes followed by clockspeed
    int timetosend = (HH * 60) + MM;
    byte TimeArray[2];
  
    TimeArray[0] = (timetosend >> 8);
    TimeArray[1] = timetosend & 0xFF;
    Wire.write(TimeArray, 2);
    Wire.write(clockSpeed);      
}
```  

  In the function above  HH is the time as hours (24hr. clock) and MM is the minutes.

- The CommandStation-EX will now poll the FastClock to request the time.  The frequency at which it does so is influenced by the clock speed (i.e. on a slow clock speed it polls less often).

Now that you know how to connect your existing FastClock, click the "next" button see how you use EX-FastClock.

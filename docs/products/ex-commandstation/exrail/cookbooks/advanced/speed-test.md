# Building a speed test track

It is possible, using the STEALTH facility to create a speed test track that can create a table of DCC speed vs time between sensors. This can then be copied to a streadsheed for analysis.

```cpp
// Speedometer example
// Track is =TS1===TS2===TS3= timing between S2 and S3.

ALIAS(TS1,181) ALIAS(TS2,182) ALIAS(TS3,183)
STEALTH_GLOBAL(
  byte testStartSpeed=2;
  byte testEndSpeed=100;
  byte testStep=10;
  byte testSpeed;
  unsigned long testStartTime;
)

AUTOMATION(9000,"Run Speed Test") // speed test setup
  STEALTH(testSpeed=testStartSpeed;)
  PRINT("Starting speed test")
  REV(20) // reverse loco to start point

SEQUENCE(9001)
  // make sure loco is at start point
  AT(TS1) ESTOP
  // drive loco fwd at testSpeed 
  STEALTH(DCC::setThrottle(loco,testSpeed,true);)
  // At timing-start sensor(s2) record time
  AT(TS2) STEALTH(testStartTime=millis();)
 // at timing-end sensor(s3) stop and calculate and print speed
 AT(TS3) ESTOP STEALTH(
    StringFormatter::send(&USB_SERIAL, 
       F("Speed %d Time %l\n"), testSpeed, millis()-testStartTime);
    testSpeed+=testStep;
    if (testSpeed>testEndSpeed) kill(); // test complete =DONE
    )
// Reverse back to start, and test again
REV(127) FOLLOW(9001)
```

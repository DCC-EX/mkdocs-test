# EX-Turntable FAQ and Troubleshooting

## Frequently Asked Questions

This is a list of common questions that we answer by our various support channels:

==TODO== Frequently Asked Questions

## Troubleshooting tips

In this section, you will find some tips on troubleshooting the various issues encountered with |EX-TT|.

### Homing failure
  
| Symptoms | Common Causes |
| --- | --- |
| Turntable rotates on start up and ends in a random position <br/>Serial console reports "ERROR: Turntable failed to home, setting random home position" | The magnet in the turntable is too far away from the sensor <br/>Hall effect sensor is connected incorrectly |

### Calibration failure

| Symptoms | Common Causes |
| -- | -- |
| Turntable rotates on start up and ends in a random position <br/>Serial console reports "ERROR: Turntable failed to home, setting random home position" <br/> | Serial console reports "CALIBRATION: FAILED, could not home, could not determine step count" <br/>The magnet in the turntable is too far away from the sensor <br/>Hall effect sensor is connected incorrectly |

### Turntable judders, stalls, or fails to rotate

| Symptoms | Common Causes |
| -- | -- |
| When attempting to rotate, the turntable judders or shakes | An incorrect stepper driver has been configured <br/> Stepper motor or driver is not connected correctly, ensure all wiring is securely connected <br/> Something is physically interfering with the turntable or stepper operation, check for interference |
|The turntable does not rotate at all | An incorrect stepper driver has been configured <br/>Something is physically interfering with the turntable or stepper operation, check for interference |

### Track power is cut when locomotive enters turntable bridge track

| Symptoms | Common Causes |
| -- | -- |
| The CommandStation detects a current overload and turns track power off | The DCC phase is out of sync between the layout and bridge track, phase inversion flag is required for the position <br/>Tracks opposite each other around the turntable are wired with inverted phases, wiring must be adjusted |

### EX-CommandStation compile errors with device driver enabled

| Symptoms | Common Causes |
| -- | -- |
| EX-CommandStation software fails to compile with "#include IO_TurntableEX.h" in myHal.cpp | The version of EX-CommandStation is incorrect, you need the "add-turntable-controller" branch of ==TODO== `EX-CommandStation <https://github.com/DCC-EX/CommandStation-EX/tree/add-turntable-controller>`_ |

### EX-Turntable showing as offline with `<D HAL SHOW>`

| Symptoms | Common Causes |
| -- | -- |
| \<D HAL SHOW\> reports **EX-Turntable** as OFFLINE <br/>EX-Turntable does not respond to EXRAIL or diagnostic commands   - | **EX-Turntable** is not powered on, or was powered on after the CommandStation <br/>The I2C (I<sup>2</sup>C) interfaces are not connected correctly, refer to [connect ex-turntable to your EX-CommandStation](assembly.md#9-connect-ex-turntable-to-your-ex-commandstation) <br/>The I2C (I<sup>2</sup>C) address in EX-Turntable's config.h does not match the address in the CommandStation's myHal.cpp file |

--8<-- "snippets/abbr.md"

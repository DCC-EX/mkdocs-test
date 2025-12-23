# Connecting a servo turnout

The details below assume you are using an EX-CSB1 command station or a DIY station with an EX8874 motor shield and Wifi connection. Otherwise the steps are the same but the wiring is trickier without the Qwiic sockets and testing requires command input.

You will need the following for up to 16 servos.

- Your Command Station with power supply and USB connection to your PC.
- Qwiic cable for connection to CSB1, with Qwiic or dupont connectors for connection to PCA9685.
- PCA9685 module
- Up to 16 SG90 servos
- EX-Installer downloaded on your PC
- (Optionally) Android phone with EX-Toolbox installed
- A servo power supply 5V 2A DC -- and not taken from the command station.

## Follow the steps below

1. Turn off power to your Command station and unplug the USB cable and power supply.
2. Connect the Qwiic cable between the CSB1 or EX8874 and the PCA9685 module.<BR>
 ![CSB1](/_static/images/ex-csb1/csb1qwiic.jpg){: style="width: 70%"} <BR>
When using Mega, the I2C bus is 5V.<BR>
Use the I2C headers, where 5V is available (IOREF/Vdd).<BR>
 ![mega](/_static/images/i2c-devices/EX8874_i2c_header.png){: style="width: 70%"} 
3. Run the EX-Installer on your PC and select the cpu type, then the Serial Monitor. You should see output similar to the following where the Command Station enumerates all the I2C devices it can find.
from the startup logs using the serial monitor

    ```cpp
    <* I2C Device found at 0x3C, OLED Display or HMC583L Magnetometer? *>
    <* I2C Device found at 0x40, PWM? *>
    . . .
    and then it shows the OLED is configured
    <* 132x64 OLED display configured on I2C:0x3c *>

    send the command: <D HAL SHOW> to see the vPins configured
    <* Arduino Vpins:2-39 *>
    <* PCA9685 I2C:0x40 Configured on Vpins:100-115  *>
    <* PCA9685 I2C:0x41 Configured on Vpins:116-131 OFFLINE *>
    <* MCP23017 I2C:0x20 Configured on Vpins:164-179 OFFLINE *>
    <* MCP23017 I2C:0x21 Configured on Vpins:180-195 OFFLINE *>
    ```

4. Examine the log to check that your PCA9685 has been detected and note the I2C address it found. This will typically be 0x40. If this address is 0x40 or 0x41 then the CS has defaulted this to be a PCA9685 and automatically assigned a range of 16 [VPINs](?VPIN) to represent the 16 servo outputs.
5. Examine the log further down and you should see where the VPINs are assigned. The following advice assumes that the address was 0x40 and the first VPIN will be 100.
6. Plug a servo into the first output socket. DO NOT mechanically connect the servo arm to any turnout or animation as the servo may move unexpectedly and cause physical damage.  You will connect the servo arm after exercising the servo (step 8).
7. Connect the additional servo power supply to the long-edge turrets on the PCA9685, observing the correct polarity. ![PCA9685](/_static/images/i2c-devices/PCA9685.jpg){: style="width: 70%"}
8. On the installers serial monitor, enter the command ```<D SERVO 100 200>``` which should move the servo. Experiment with other positions than 200. The usable range is approximately 102 to 490.  
9. (Optionally) Use the EX-Toolbox Andoid app to experiment with servo angles and servo arm lengths until you have the required throw distance and angles to suit your servo mounting preferences.

## Define your Turnouts

01. In EX-Installer, edit myAutomation.h and define each turnout to give an id of your choice, the VPIN of the servo, the closed and open servo values you have discovered by experimentation and a suitable decription to show on your throttle.

     ```cpp
     //SERVO_TURNOUT( turnout_id, vpin, active_angle, inactive_angle, profile [, "description"|HIDDEN] )
     SERVO_TURNOUT(1, 100, 350, 120, Slow, "Coal yard exit")
     SERVO_TURNOUT(2, 101, 400, 200, Slow, "Branch line siding")
     SERVO_TURNOUT(3, 102, 400, 200, Slow, HIDDEN)
     ```

02. Reload the command station from the installer.

## Test your turnout definitions

1. Using the serial monitor as before, enter the commands ```<T 1 T>``` to throw turnout 1, ```<T 2 C>``` to close turnout 2 and so on.
2. With your Wifi throttle (Typically Engine Driver) navigate to the turnouts page where you will see the two turnouts listed. From there you can throw or close them as required.

## Connect your servos to turnouts

There are many ways of mounting servos both above and below the baseboard using 3D printed mounts or a strip of plastic L shape. You will probably want to use microswitches to switch frog polarity or use more expensive frog juicers or EXRAIL driven relays.

We recommend that whatever mechanical connection you make allows for protection of you turnout from excess servo movement.

## PCA9685 Configure additional boards

The first two PCA9685 are pre-defined at addresses 0x40 and 0x41, for pins 100-115 and 116-131.<BR>
Configure additional PCA9685 in myAutomation.h.

```cpp
  HAL(PCA9685, 132, 16, 0x42)
  HAL(PCA9685, 148, 16, {I2CMux_0,SubBus_4,0x43})
```

Nucleo-144 boards do not have pre-defined PCA9685 due to pin conflicts, as pins thru 116 are reserved for the microprocessor.  All PCA9685 connected to Nucleo-144 boards require configuration in myAutomation.h.

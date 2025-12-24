# DC Mode - PWM Frequency

The default PWM frequency is 131Hz.  Functions F29-F30-F31 are defined to enable other frequencies.

The functions will toggle the bits ON/OFF as shown in the table.

&nbsp; &nbsp; &nbsp; &nbsp; ![PWM Frenquency](/_static/images/trackmanager/dc-pwm-frequency.png){: style="width: 50%"}

**NOTE:**

- The frequency does not change until a powerON command is sent.

- Tracks are assigned to timers.  Throttles are assigned to tracks.  
  Changing the frequency for one throttle will impact all tracks assigned to the same timer.  
  [more information](dc-track-sync.md/#timers-brake-pins)

- ==TODO==  How to effectively use DC mode when using multiple frequencies.  

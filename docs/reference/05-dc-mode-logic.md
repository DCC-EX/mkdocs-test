# DC mode - Logic gate circuits

This additional information may be useful for those who are not using CSB1 or EX8874, and would like to understand what would be needed for DC mode with other motor boards/shields.

With DC mode, the PWM signal is provided with the brake pin.  The Signal-1 pin provides direction.

These diagrams provide options on how logic gates could be used to provide imputs In1, In2 for motor boards, such as L298N or IBT_2.  

Note that L298P and L298HN motor shields use the XNOR gate.  To enable low side brake in both directions, an additional logic gate can be used.

 &nbsp; &nbsp; &nbsp; &nbsp; ![Logic gate circuits](/_static/images/trackmanager/logic-gate-circuitx3.png){: style="width: 70%"}

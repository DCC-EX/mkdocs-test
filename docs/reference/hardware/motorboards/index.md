# Motor Drivers

A motor driver (aka 'motor controller', aka 'motor shield', aka 'motor board') is just a high voltage, high current switch. While initially designed to power electric motors, we use it to create the DCC signal to the track in a clever misapplication of technology. Normally, a pulse width modulated (PWM) signal would be applied to a motor with the PWM pin to control speed and the direction pin would switch the voltage from positive to negative to control the motor spin direction. Instead, we send full DC track voltage to the PWM pin and switch the direction pin at the DCC frequency (around 8000 times a second) to generate the bi-polar square wave. In this way, we use the 5V DC (or 3.3V) microcontroller output to switch the voltage from separate 12-16v DC power supply [^1] connected to the motor driver, and create a pulse train signal of 1's and 0's that a mobile decoder can interpret as commands.

[^1]: The voltage you need for the Motor Driver depends on the scale/gauge of the layout you are using. Bigger is not always better. Too high a voltage can damage your locos. See the [Selecting a power supply](../../../diy/power.md) for more information.  

## Supported Motor Drivers

*EX‑CommandStation* is compatible with a wide variety of motor drivers, also known as 'dual H-bridges' and 'motor shields'. We’ve sorted them from least difficult to most difficult to use to help you decide what to use. When it comes to selecting a board, some considerations are size, whether it is a shield or needs to be connected with jumper wires, the amount of current you need, and whether it has current sensing capability built-in or if you have to supply it yourself.

If you have trouble finding a particular board from the list, try searching based on it'’'s name or the type of chip on the board and the terms 'H-Bridge' or Motor Shield. There are often many places that sell these, especially the Chinese sites like AliExpress and Banggood.

**TL;DR** (aka short version): We currently recommend the DCC-EX [EX-MotorShield8874](../../../products/ex-motorshield8874/ex-motorshield8874.md), and the Arduino Motor Shield R3 or a supported clone like the Deek-Robot.

## Current List of Motor Drivers

<style>
.md-typeset .md-typeset__scrollwrap {
    overflow-x: auto !important;
    overflow-y: visible !important;
}

.md-typeset__scrollwrap table {
    display: table !important;
    table-layout: fixed !important;
    width: 100% !important;
    border-collapse: separate !important;
    border-spacing: 0 !important;
}

.md-typeset__scrollwrap th:first-child,
.md-typeset__scrollwrap td:first-child,
.md-typeset table tr th:first-child,
.md-typeset table tr td:first-child {
    position: sticky;
    left: 0;
    z-index: 3; /* Keeps the column on top of the scrolling content */
    background: var(--md-default-bg-color--light);
}

.md-typeset__scrollwrap th:nth-child(12),
.md-typeset__scrollwrap td:nth-child(12),
.md-typeset__scrollwrap th:first-child,
.md-typeset__scrollwrap td:first-child {
    width: 100px !important;
}

.md-typeset table td,
.md-typeset table th {
    font-size: smaller !important;
    padding-top: 2px !important;
    padding-bottom: 2px !important;
    padding-left: 2px !important;
    padding-right: 2px !important;
    line-height: 110% !important;
    font-family: 'Roboto Condensed', sans-serif !important;
 }
</style>

In this section we outline the various details that we know of related to each of the different boards that we've either tested, or know to work based on user feedback.

We've compiled this simple summary table to help with this:

| Type / Brand | Recom-mended | Supported | Comfort Level | Form Factor[^1] | Stack-able | Short Circuit Pro-tection | Current Sense[^2] | DC Support | No. Outputs / Tracks | Max Amps[^3] | Comments / Notes |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| [DCC-EX EX-MotorShield8874 RevA](ex-motor-shield-8874.md) | Yes | Yes | Simple | UNO / Mega | Yes [^4] | Yes | Yes | Yes | 2 | 5 | |
| [Arduino Motor Shield R3](l298-shields.md)[^6] | Yes | Yes | Simple | UNO / Mega | Yes [^7] | Yes | Yes | Yes | 2 | 1.3 - 1.5 | |
| [Deek-Robot Motor Shield](l298-shields.md)[^6] | Yes | Yes | Simple | UNO / Mega | Yes [^7] | Yes | Yes | Yes | 2 | 1.3 - 1.5 | |
| Flashtree Motor Shield | No | Yes | Intermediate | UNO / Mega | No | Yes | Yes | Yes | 2 | 1.3 - 1.5 | |
| DIY More L298NH | No | Yes | Intermediate | UNO / Mega | No | Yes | Yes | Yes | 2 | 2 | |
| YFRobot L298P | No | Yes | Intermediate | UNO / Mega | No | No | No | No | 2 | 2 | |
| L298N (dual) | No | Yes | Advanced | | No | No | No | No | 2 | 2 | It doesn’t have current sense |
| Dual Module H-bridge MOSFET IRF3205 | No | Yes | Intermediate | | No | No | No | No | 2 | 15 | |
| Pololu MC33926 | No | Yes | Intermediate | UNO / Mega | No | No | No | No | 2 | 3 | current sense is not acceptable. We recommend using an external current sense board like the MAX471 |
| MiniIBT L6201P (single) | No | Yes | Intermediate | | No | No | ? | No | 1 | 5 | |
| BTS7960 IBT\\_2 (single) | No | Yes | Intermediate | | No | No | ? | No | 1 | 43 | |
| Keyes/Fundumoto (“Beeper Board”) | No | Yes | Advanced | UNO / Mega | No | Yes [^5] | Yes [^5] | No | 2 | 2 | |
| Makerfabs H-Bridge | No | Yes | Advanced | | No | No | No | No | 2 | 8 | |
| Velleman KA03/VMA03 | No | Yes | Advanced | | No | No | No | No | 2 | 2 | |
| DFRobot 2x2A DC Motor Shield (DRI0009) | No | Yes | Advanced | UNO / Mega | No | No | No | No | 2 | 2 | |
| VNH2SP30 - SparkFun Monster Moto and others | - | No | - | - | - | - | - | - | - | - | Does not work. It can’t switch fast enough to generate a reliable DCC signal |
| IFX9202ED - Infineon Dual H-Bridge | - | No | - | - | - | - | - | - | - | - | Does not work. Can’t switch fast enough. |
| DFRobot Romeo V2 | - | No | Advanced | - | - | - | - | - | - | - | Well, an Advanced could perhaps get this one to work. |
| Kuman Board (and any L293D based boards) | - | No | - | - | - | - | - | - | - | - | Does not work. Not enough current. |
| Pololu TB9051FTG based motor shield | - | No | - | - | - | - | - | - | - | - | Does not work. It can’t switch fast enough to generate a reliable DCC signal | 

[^1]: 'UNO/Mega' Refers to the shape and physical connections, not necessariy the compatibility with the UNO, Maga or **EX-CSB1**.
[^2]: Required for CV Programming.
[^3]: Per output.
[^4]: Requires modification of the board to stack the second board.
[^5]: Requires modification of the board to support Current Sense.
[^6]: The *Arduino Motor Shield R38* and the *Deek-Robot Motor Shield* are interchangeably referred to in this documentation as the *standard motor driver*.
[^7]: Can be stacked, but it is complicated.

--8<-- "snippets/abbr.md"

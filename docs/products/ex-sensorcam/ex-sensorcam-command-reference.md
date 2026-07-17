---
tags:
  - _9N9_
  - _9N9_9Q9
  - _9N9_cmd_value
---

# Native EX-SensorCAM Command List

Commands are used through the Command Station input to configure the sensorCAM settings and create virtual sensors.

## Conventions used on this page

**`, space`**	Equivalent parameter separators.  CS must use space character  
**`%%`** &nbsp; &nbsp; &nbsp; &nbsp; Represents a Sensor's bank/sensor two digit identifier (digits 0-7 only)  
**`rr xx`**&nbsp; &nbsp; Represent the row and column position of sensor (range 1-236 & 1-316 only)  
**`#`** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Represents a single decimal digit (0-9)  
**`$`** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Represents a single alpha-numeric character (A-Z or 0-9 as relevant to command)  
**`[ ]`** &nbsp; &nbsp; &nbsp;  &nbsp;Indicates enclosed parameter is optional.  Do NOT type brackets into commands  
**`< >`** &nbsp; &nbsp; &nbsp;  &nbsp;Encloses native CS command and MUST be typed to define CS command

## Native cam USB & CS cmd formats

<style>
  /* force the first two column widths */
.md-typeset table:not([class]) th:nth-child(-n+2),
.md-typeset table:not([class]) td:nth-child(-n+2) {
    width: 25% !important;
}
</style>

| native CAM<br>example | DCC-EX<br>native CS | &nbsp; &nbsp; &nbsp;  Command Description |
| --- | --- | :--- |
| `n/a` | `<N>` | **Show Current CAM selection and others available** <br>lists assigned base vpins |
| `n/a` | `<NQ>` | **Query state of all Sensors**<br> Tabulation of all CAM sensor tripped states |
| **`a%%[,rr,xx]`**<br>a12,32,43 | `<Na %%[ rr xx]>` | **enAble Sensor and refresh reference**<br> Sensor responsive. [coordinates:rr,xx\] |
| **`b#[,$]`**<br>b1 | `<Nb #>` | **Bank occupancy status**<br> bytes of 8 sensors [set Brightness ScaleFactor $\] |
| **`c$$$$`** | `<n/a>` | **ov2640 re-Calibration and re-reference**<br>Refer to manual before use! (deprecate) |
| **`d%%[#]`**<br> | `<n/a>` | **Difference Score for Sensor** [# repeats\]<br>scores for colour, brightness & sum |
| **`e`**<br>e | `<Ne>` | **EPROM write configuration**<br>Save parameters for next Reset |
| **`f%%`**<br>f12 | `<Nf %%>` | **Frame pixel print. Full 16x3 bytes**<br>4x4(RGB) pixels current & reference |
| **`g`**<br>g | `<Ng>` | **Global ov2640 Status to USB**<br>Lists 14 parameter settings |
| **`h$[,#]`**<br>h7,1 | `<Nh $ #>` | **Help (debug\)** h lists options<br>h7,# pauses(w\) scroll on bank # trips |
| **`i%%[,$$]`**<br>i12,02 | `<Ni %%[ $$]>` | **Info on Sensor state & configuration**<br> [add a "twin" sensor (S$$\) to S%%] |
| **`j$,#`**<br>jB2 | `<Nj $ #>` | **adJust ov2640 global parameters & lists 'g' status**<br>Set a single parameter($) for ov2640. **j** lists options |
| **`k%%,rr,xx`**<br>k12,130,205 | `<n/a>` | **locate a basic sensor at row rr, column xx**<br>Defines sensor at rr,xx DOES NOT enable or reference |
| **`l%%`**<br>l12 | `<Nl %%>` | (Lima) **Latch sensor on (occupied = 1)**<br>Sensor disabled, & set 1 until a%%, r%% or o%% |
| **`m$[,%%]`**<br>m2,30 | `<Nm $[ %%]>` | **Min2trip frames setting [MaxSensor setting]** <br>Sets min/max.  m0,%% leaves min2trip unchanged |
| **`n$[,%%]`**<br>n0,10 | `<Nn $[ %%]>` | **Number for bank trip nLED indicator. [minSensor]** <br>Sets LED to indicates when bank $ sensor is tripped |
| **`o%%`**<br>o12 | `<No %%>` | (Oscar) **turn sensor Off (un-occupied = 0)** <br>Sensor disabled, & set 1 until a%%, r%% or o%% |
| **`p#`**<br>p2 | `<Np #>` | **Position table for a bank of sensors** <br>Prints for enAbled sensors of bank #. &nbsp; p%% similar |
| **`q#`**<br>q2 | `<Nq #>` | **Query enAbled state of sensors in bank**<br>Prints state of all 8 sensors (1/0).  Use q9 for ALL banks |
| **`r%%`**<br>r12 | `<Nr %%>` | **Refresh reference image for sensor**<br>enAbles sensor & capture new reference image.  **r00** for ALL |
| **`s%%`**<br>s12 | `<Ns %%>` | **Scan image to locate new Sensor position (superseded)** <br>Scan for brightest spot (LED) & define sensor there. |
| **`t##[,%%]`**<br>t42,12 | `<Nt ##[ %%]>` | **Theshold value (32-98) [pvtThreshold for S%%]** <br>Sets global threshold. [**t0,%%** clears a pvtThreshold] |
| **`t##`**<br>t20 | `<Nt ##>` | **Tabulate ## (2-30 only) rows of scroll data** <br> Note: **t1** toggles scroll on/off & **t99** lists pvtThresholds |
| **`t1,%%`**<br>t1,12 | `<Nt 1 %%>` | **Trash pvtThresholds for S%% bank**<br>clears 1 bank of 8 pvtThresholds. **t1,99** clears ALL pvtThresholds |
| **`u%%`**<br>u12 | `<Nu %%>` | **Un-define Sensor S%%** <br>Resets sensor coordinates to 0,0 |
| **`v[#]`**<br>v1 | `<Nv[ #]>` | **Version [or Video webCAM SSID #]**<br>EX-SensorCAM version info [v# starts SSID # webCAM] |
| **`w`**<br> w | `<Nw>` | **Wait for command. &nbsp; (NOTE: 't1' for alternative action)** <br>suspends image capture & scrolling. Waits for an 'Enter' |
| **``x  y  z``** | `<n/a>` | **Reserved commands for image transfer management**<br>Sends data to USB port for Processing4 (X Y Z) image delivery |
| n/a | `<N[M #00]>` | **Show Current CAM selection and others available (CS only)**<br>Optionally allows switching current cam to CAM# (1-4) |
| n/a | `<NC ###>` | **CAM selection** Switches to CAM<br> at CAM number #(1-4) or vpin ### |
| **``F``** | `<NF>` | **Forces immediate CAM reset**<br>Reset to EX-SensorCAM mode, exting webCAM/WiFi mode |
| **``R``** | `<n/a>` | **Reset EX-SensorCAM &nbsp; (CS <NR\> gives equivalent of <Nr 00\>)**<br>Reset into EX-SensorCAM mode, exting any WiFi mode |
| **``&``** | `<n/a>` | **Print statistics since last '&' cmd.**<br>USB histogram of trips and potential trips of 1-3 frames |
| **``+#,$``** | `<n/a>` | **Add offset of # pixels in $ direction to ALL enabled Sensors**<br>realign ALL sensors by # pixels in direction specified (N-NW) |
| **``\``** **``/``** **``@``** | | **Commands for lines and trip symbol - refer to manual** |

**NOTE:  The EX-SensorCAM USB input will also accept most CS formatted commands.**

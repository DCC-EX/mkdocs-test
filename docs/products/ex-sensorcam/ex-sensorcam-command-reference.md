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
| `n/a` | `<N>` | **Show Current CAM selection and others available**<lists assigned base vpins |
| `n/a` | `<NQ>` | **Query state of all Sensors**<br> Tabulation of all CAM sensor tripped states |
| **`a%%[,rr,xx]`**<br>a12,32,43 | `<Na %%[ rr xx]>` | **enAble Sensor and refresh reference**<br> Sensor responsive. [coordinates:rr,xx\] |
| **`b#[,$]`**<br>b1 | `<Nb #>` | **Bank occupancy status** bytes of 8 sensors [set Brightness ScaleFactor $\] |
| **`c$$$$`** | `<n/a>` | **ov2640 re-Calibration and re-reference**<br>Refer to manual before use! (deprecate) |
| **`d%%[#]`**<br> | `<n/a>` | **Difference Score** for Sensor** [# repeats\]**<br>scores for colour, brightness & sum |
| **`e`**<br>e | `<Ne>` | **EPROM write configuration**<br>Save parameters for next Reset |
| **`f%%`**<br>f12 | `<Nf %%>` | **Frame pixel print. Full 16x3 bytes**<br>4x4(RGB) pixels current & reference |
| **`g`**<br>g | `<Ng>` | **Global ov2640 Status to USB**<br>Lists 14 parameter settings |
| **`h$[,#]`**<br>h7,1 | `<Nh $ #>` | **Help (debug\)** h lists options<br>h7,# pauses(w\) scroll on bank # trips |
| **`i%%[,$$]`**<br>i12,02 | `<Ni %%[ $$]>` | **Info on Sensor state & configuration**<br> [add a "twin" sensor (S$$\) to S%%] |
| **``j$,#``** | `<Nj $ #>` | **adJust ov2640 global parameters & lists 'g' status**<br>Sets a single parameter($) for ov2640. &nbsp; j alone, lists options |
| **``k%%,rr,xx``** | `<n/a>` | **locate a basic sensor at row rr, column xx**<br>Defines sensor at rr,xx but DOES NOT enable or reference/refresh it |
| **``l%%``** | `<Nl %%>` | **(Lima) Latch sensor on (occupied=1)**<br>Sensor disabled, & set 1 until a%%, r%% or cleared by o%% |
| **``m$[,%%]``** | `<Nm $[ %%]>` | **Min2trip frames setting [MaxSensor setting]**<br>Sets min/max parameters.  m0,%% leaves min2trip unchanged |
| **``n$[,%%]``** | `<Nn $[ %%]>` | **Number for bank trip LED indicator. [minSensor]**<br>Sets programmable LED to indicates when bank Number $ is tripped |
| **``o%%``** | `<No %%>` | **(Oscar) turn sensor Off (un-occupied=0)**<br>Sensor disabled, & set 0 until Latched or enabled using a%% or r%% |
| **``p#``** | `<Np #>` | **Position table for a bank of sensors**<br>Prints positions for enAbled sensors of bank #. &nbsp; p%% similar |
| **``q#``** | `<Nq #>` | **Query enAbled state of sensors in bank**<br>Prints enabled state of all 8 sensors (1/0).  Use q9 for ALL banks |
| **``r%%``** | `<Nr %%>` | **Refresh reference image for sensor**<br>enAbles sensor and captures a new reference image.  Use r00 for ALL |
| **``s%%``** | `<Ns %%>` | **Scan video to define a new Sensor position (superseded)**<br>Scan for brightest spot (LED) and position sensor there. |
| **``t##[,%%]``** | `<Nt ##[ %%]>` | **Theshold setting (32-98) global [pvtThreshold for S%%]**<br>Sets new global threshold, [or a  pvtThreshold] (t99 lists pvtThresholds)<br>For ## of (2-31), print ## data rows. &nbsp; (t00,%% clears a pvtThreshold) |
| **``t1[,%%]``** | `<Nt 1[ %%]>` | **Toggle data scroll on/off. &nbsp; [or Trash pvtThresholds for S%% bank]**<br>clears 1 bank of 8 pvtThresholds. &nbsp; (t1,99 clears ALL pvtThresholds) |
| **``u%%``** | `<Nu %%>` | **Un-define Sensor**<br>Resets sensor coordinates to 0,0 |
| **``v[#]``** | `<Nv[ #]>` | **Version [or Video webCAM SSID #]**<br>Displays EX-SensorCAM version info [v# starts SSID # webCAM] |
| **``w``** | `<Nw>` | **Wait for command. &nbsp; (NOTE: 't1' alternative action)**<br>Cam suspends image capture and scrolling and waits for an 'Enter' |
| **``x  y  z``** | `<n/a>` | **Reserved commands for image transfer management**<br>Sends binary data to USB port for Processing4 (X Y Z) image delivery |
| n/a | `<N[M #00]>` | **Show Current CAM selection and others available (CS only)**<br>Optionally allows switching current cam to CAM# (1-4) |
| n/a | `<NC ###>` | **CAM selection** Switches to CAM<br> at CAM number #(1-4) or vpin ### |
| **``F``** | `<NF>` | **Forces immediate CAM reset**<br>Reset into EX-SensorCAM mode, exting any webCAM/WiFi mode |
| **``R``** | `<n/a>` | **Reset EX-SensorCAM &nbsp; (CS <NR\> gives equivalent of <Nr 00\>)**<br>Reset into EX-SensorCAM mode, exting any WiFi mode |
| **``&``** | `<n/a>` | **Print statistics since last '&' cmd.**<br>USB histogram of trips and potential trips of 1-3 frames |
| **``+#,$``** | `<n/a>` | **Add offset of # pixels in $ direction to ALL enabled Sensors**<br>realign ALL sensors by # pixels in direction specified (N-NW) |
| **``\``** **``/``** **``@``** | | **Commands for lines and trip symbol - refer to manual** |

**NOTE:  The EX-SensorCAM USB input will also accept most CS formatted commands.**

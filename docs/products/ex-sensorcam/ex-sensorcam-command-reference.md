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

| native CAM<br>example | DCC-EX<br>Serial Cmd | &nbsp; &nbsp; &nbsp;  Command Description |
| --- | --- | :--- |
| `n/a` | `<N>` | **Show Current CAM selection and others available** <br>lists assigned base vpins |
| `n/a` | `<NQ>` | **Query state of all Sensors**<br> Tabulation of all CAM sensor tripped states |
| **`a%%[,rr,xx]`**<br>a12,32,43 | `<Na %%`<br>`[ rr xx]>` | **enAble Sensor and refresh reference**<br> Sensor responsive. [new coordinates: rr,xx\] |
| **`b#[,$]`**<br>b1 | `<Nb #>` | **Bank occupancy status** bytes of 8 sensors<br> gives a bank 'value' [set Brightness ScaleFactor $\] |
| **`c$$$$`** | `n/a` | **ov2640 re-Calibration and re-reference**<br>Refer to manual before use! (deprecate) |
| **`d%%[,#]`**<br>d12,5 | `n/a` | **Difference Score for Sensor** [# repeats\]<br>scores for colour, brightness & sum |
| **`e`**<br>e | `<Ne>` | **EPROM write sensorCAM configuration**<br>Save parameters for next Reset |
| **`f%%`**<br>f12 | `<Nf %%>` | **Frame S%% pixel array. Full 16x3 bytes**(HEX)<br>4x4(RGB) pixels current & reference frames |
| **`g`**<br>g | `<Ng>` | **Global ov2640 Status to CAM monitor**<br>Lists 14 parameter settings |
| **`h$[,#]`**<br>h7,1 | `<Nh %%>`<br>`<Nh $[ #]>` | **Help (debug\) set *maxSensors*(>9\)** (h lists options)<br>h7,# pauses(w\) scroll on bank # trips |
| **`i%%[,$$]`**<br>i12,02 | `<Ni %% [$$]>` | **Info on Sensor state & configuration**<br> [add a "twin" sensor (S$$\) to S%%] |
| **`j$,#`**<br>jB2 | `<Nj $ #>` | **adJust ov2640 global parameters & lists 'g' stae**<br>Set a single parameter($) for ov2640. **j** lists options |
| **`k%%,rr,xx`**<br>k12,130,205 | `n/a` | **locate a basic sensor at row rr, column xx**<br>Defines sensor at rr,xx DOES NOT enable or reference |
| **`l%%`**<br>l12 | `<Nl %%>` | (Lima) **Latch sensor on (i.e. occupied = 1\)** <br>Sensor disabled, & set 1 until a%%, r%% or o%% |
| **`m$[,%%]`**<br>m2,30 | `<Nm $ [%%]>` | **Min2trip frames setting $(1-4) [*MaxSensor* setting]** <br>Sets min/max.  m0,%% leaves *min2trip* unchanged |
| **`n$[,%%]`**<br>n0,10 | `<Nn $ [%%]>` | **Number for bank trip nLED indicator [set *minSensor*]** <br>Sets LED to indicates when bank $ sensor is tripped |
| **`o%%`**<br>o12 | `<No %%>` | (Oscar) **turn sensor Off (un-occupied = 0)** <br>Sensor disabled, & set 0 until a%%, r%% or l%% |
| **`p#`**<br>p2 | `<Np #>` | **Position table for a bank of sensors** (row,col) <br>List for enAbled sensors of bank #. Also **p%%** |
| **`q#`**<br>q2 | `<Nq #>` | **Query enAbled state of sensors in bank**<br>State of 8 sensors (1/0).  Use **q9** for ALL banks |
| **`r%%`**<br>r12 | `<Nr %%>` | **Refresh reference image for sensor S%%** <br>enAble S%% & capture new ref image.&nbsp; **r00** for ALL |
| **`s%%`**<br>s12 | `<Ns %%>` | **Scan image to locate new S%% position** (superseded)<br>Scan for brightest spot (LED) & define sensor there. |
| **`t##[,%%]`**<br>t42,12 | `<Nt ## [%%]>` | **Theshold value (32-98) [pvtThreshold for S%%]** <br>Sets global threshold. [**t0,%%** delete pvtThreshold] |
| **`t##`**<br>t20 | `<Nt ##>` | **Tabulate ## (2-30 only) rows of scroll data** <br> **t1** toggles scroll on/off & **t99** lists pvtThresholds |
| **`t1,%%`**<br>t1,12 | `<Nt 1 %%>` | **Trash pvtThresholds for S%% bank**<br>Clears 8 pvtThresholds. &nbsp; **t1,99** clears ALL pvtT. |
| **`u%%`**<br>u12 | `<Nu %%>` | **Un-define Sensor S%%** (EPROM unchanged\)<br>Resets sensor coordinates to 0,0 |
| **`v[#]`**<br>v1 | `<Nv[ #]>` | **Version [or Video webCAM mode SSID #]** <br>EX-SensorCAM version info [v# starts SSID # webCAM] |
| **`w`**<br> w | `<Nw>` | **Wait for command. &nbsp; (see 't1' for alternative action)** <br>suspends image capture & scrolling. Waits for 'Enter' |
| **``x  y  z``** | `n/a` | **Reserved commands for image transfer management**<br>Sends image data to USB port for Processing4 (X Y Z) |
| n/a | `<N[M #00]>` | **Show Current CAM selection and others available** <br>[ # optional switching current cam to CAM # (1-4)] |
| n/a | `<NC ###>` | **CAM selection** Switches to CAM number #(1-4)<br> or vpin ### (vpin >99) |
| **`F`** | `<NF>` | **Forces immediate CAM reset**<br>Reset EX-SensorCAM mode, exit webCAM/WiFi mode |
| **`R`** | `n/a` | **Reset EX-SensorCAM** &nbsp; (<NR\> equates to <Nr 00\>) <br>Reset into EX-SensorCAM mode, exit any WiFi mode |
| **`&`** | `n/a` | **Print statistics since last '&' cmd.** <br>Histogram of trips + potential trips of 1-3 frames |
| **`+#,$`**<br>+2,3 | `n/a` | **Add offset of # pixels in $ direction to ALL Sensors** <br>moves by # pixels in $(0-7) direction specified (N-NW) |
| **`\%%,#,$`**<br>\30,2,3 | `n/a` | **linear sensor bank conversion starting at S%%** <br>use r,x step size of #,$(0-31) Slope "down-right" |
| **`/%%,#,$`**<br>/30,2,3 | `n/a` | **linear sensor bank conversion starting at S%%** <br>use r,x step size of #,$(0-31) Slope "down-left" |
| **`@##`**<br>@73 | `n/a` | **change scroll trip symbol - refer to manual**<br><span style="opacity:0">EXISensorCAMIversionIinfoIIvIIstartsISSIDIIIwebCAMIII</span> |

**NOTE:  The SensorCAM USB input will also accept most CS formatted commands.**

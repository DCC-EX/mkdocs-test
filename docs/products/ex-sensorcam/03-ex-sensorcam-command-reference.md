# Native EX-SensorCAM Command List

## Conventions used on this page

**`, space`**	Equivalent parameter separators.  CS must use space character  
**`%%`** &nbsp; &nbsp; &nbsp; &nbsp; Represents a Sensor's bank/sensor two digit identifier (digits 0-7 only)  
**`rr xx`**&nbsp; &nbsp; Represent the row and column position of sensor (range 1-236 & 316 only)  
**`#`** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Represents a single decimal digit (0-9)  
**`$`** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Represents a single alpha-numeric character (A-Z or 0-9 as relevant to command)  
**`[ ]`** &nbsp; &nbsp; &nbsp;  &nbsp;Indicates enclosed parameter is optional.  Do NOT type brackets into commands  
**`< >`** &nbsp; &nbsp; &nbsp;  &nbsp;Encloses native CS command and MUST be typed to define CS command  

## Native cam USB & CS cmd formats

| native CAM | native CS |  &nbsp; &nbsp; &nbsp;  Command Description |
| --- | --- | :--- |
| a%%[,rr,xx] | **`<Na %%[ rr xx]>`** | **enAble Sensor and refresh reference**  
|     |    | Sensor will respond to changing image. rr,xx set as new coordinates  
| b#[,$] | **`<Nb #>`**| **Bank occupancy status [& Brightness S/F]**  
|    |    | Trip status of 8 sensors in a single byte (8 bits) (hex & binary)
| c$$$$ | `<n/a>` | **Camera re-Calibration and re-reference Sensors**  
|     |    | Severe changes to camera settings.  Refer to manuals before use!  
| d%%[#]  | `<n/a>`  | **Difference Score for Sensor [# repeats]**  
|     |    | Prints colour diff score, brightness score and sum of both
| e   | **`<Ne>`**  | **EPROM - save sensorCAM config. to EPROM**  
|     |    | Records parameters in EPROM to be restored upon next Reset
| f%%  | **`<Nf %%>`**  | **Frame print. Full 16x3 byte Sensor pixel values**  
|     |    | Tabulates 4x4 (RGB) pixels for current and reference sensor images
| g   | **`<Ng>`**  | **Get Camera Global Config. Status (to USB)**  
|     |    | Lists 14 different parameters of the ov2640 "Calibration" settings
| h$[,#]  | **`<Nh $ #>`**  | **Help cmd.(debug for devel)**  
|     |    | Debug. h alone lists options. h7,# pauses scroll if bank # trips
| i%%[,$$ ]  | **`<Ni %%[ $$]>`**  | **Info. on Sensor state and configuration**  
|     |    | prints sensor state & full definition.  Can add a "twin" sensor S$$
| j$,# | **`<Nj $ #>`**  | **adJust ov2640 global parameters & list <Ng>**  
|     |    | Sets a single parameter($) for ov2640. j alone lists options for $
| k%%,rr,xx  | `<n/a>`  | **locate a basic sensor at row rr, column xx**  
|     |    | Defines sensor at rr,xx but DOES NOT enable or reference/refresh it
| l%% | **`<Nl %%>`** | **(Lima) Latch sensor on (occupied=1)**  
|     |    | Sensor disabled, & set 1 until a%%, r%% or cleared by o%%
| m$[,%%]  | **`<Nm $[ %%]>`**  | **Min2trip frames setting [MaxSensor setting]**   
|     |    | Sets min/max parameters.  m0,%% leaves min2trip unchanged
| n$[,%%]  | **`<Nn $[ %%]>`**  | **Number for bank trip LED indicator. [minSensor]**  
|     |    | Sets programmable LED to indicates when bank Number $ is tripped
| o%% | **`<No %%>`** | **(Oscar) turn sensor Off (un-occupied=0)**  
|     |    | Sensor disabled, & set 0 until Latched or enabled using a%% or r%%
| p#  | **`<Np #>`**  | **Position table for a bank of sensors**  
|     |    | Prints positions for enAbled sensors of bank #. &nbsp; p%% similar
| q#  | **`<Nq #>`** | **Query enAbled state of sensors in bank**  
|     |    | Prints enabled state of all 8 sensors (1/0).  Use q9 for ALL banks
| r%% | **`<Nr %%>`** | **Refresh reference image for sensor**  
|     |    | enAbles sensor and captures a new reference image.  Use r00 for ALL
| s%% | **`<Ns %%>`** | **Scan video to define a new Sensor position (superseeded)**  
|     |    | Scan for brightest spot (LED) and position sensor there. 
| t##[,%%] | **`<Nt ##[ %%]>`**  | **Theshold setting (33-98) global [pvtThreshold for S%%]**  
|     |    | Sets new global threshold, [or a  pvtThreshold] (t99 lists pvtThresholds)  
|     |    | For ## of (2-31), print ## data rows. &nbsp; (t00,%% clears a pvtThreshold)
| t1[,%%]  | **`<Nt 1[ %%]>`**  | **Toggle data scroll on/off. &nbsp; [or Trash pvtThresholds for S%% bank]**  
|     |    | clears 1 bank of 8 pvtThresholds. &nbsp; (t1,99 clears ALL pvtThresholds) 
| u%% | **`<Nu %%>`**  | **Un-define Sensor**  
|     |    | Resets sensor coordinates to 0,0
| v[#] | **`<Nv[ #]>`**  | **Version [or Video wifi SSID #]**  
|     |    | Displays EX-SensorCAM version info OR v# starts preset SSID webCAM
| w  | **`<Nw>`**  | **Wait for command. &nbsp; NOTE: alternative t1 cmd. action**  
|     |    | Cam suspends image capture and scrolling and waits for a CR
| x &nbsp; y &nbsp; z  | `<n/a>`  | **Reserved commands for image transfer management**  
|     |    | Sends binary data to USB port for Processing4 (X Y Z) image delivery
| n/a  | **`<N>`** | **Current CAM selection and availability (CS only)**  
|     |    | Shows the currently selected CAM and the options available 
| n/a | **`<NC ###>`**  | **CAM selection**  
|     |    | Switches commands to the CAM at vpin ### or CAM number (1-4)
| n/a  | **`<NQ>`**  | **Query state of all Sensors**  
|     |    | Tabulation of all sensor tripped states in banks of 8
| F  | **`<NF>`**  |  **Forces immediate CAM reset**  
|     |    | Reset into EX-SensorCAM mode, exting any WiFi mode
| R  | `<n/a>` | **Reset EX-SensorCAM &nbsp; (CS <NR> gives equivalent of <Nr 00>)**  
|     |    | Reset into EX-SensorCAM mode, exting any WiFi mode 
| & | `<n/a>` | **Print statistics since last '&' cmd.**  
|     |    | USB histogram of trips and potential trips of 1-3 frames
| +#,$ | `<n/a>` | **Add offset of # pixels in $ direction to ALL enabled Sensors**  
|     |    | realign ALL sensors by # pixels in direction specified (N-NW) 
| \ &nbsp; / &nbsp; \@ |    | **Commands for lines and trip symbol - refer to manual**  


**NOTE:  The EX-SensorCAM USB input will also accept most CS formatted commands.**

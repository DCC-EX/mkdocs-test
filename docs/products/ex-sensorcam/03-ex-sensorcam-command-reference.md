# Native EX-SensorCAM Command List

## Conventions used on this page

`, space`	Equivalent parameter separators.  CS must use space character  
`%%`&nbsp; &nbsp; &nbsp; &nbsp; Represents a Sensor's bank/sensor two digit identifier (digits 0-7 only)  
`rr  xx ` Represent the row and column position of sensor (range 1-236 & 316 only)  
`#`&nbsp; &nbsp;  &nbsp; Represents a single decimal digit (0-9)  
`$`&nbsp; &nbsp;  &nbsp; Represents a single alpha-numeric character (A-Z or 0-9 as relevant to command)  
`[ ]` Indicates enclosed parameter is optional.  Do NOT type brackets into commands  
`< >` Encloses native CS command and MUST be typed to define CS command  

## Native cam USB & CS cmd formats

a%%[,rr,xx] `<Na %%[ rr xx]>` **enAble Sensor and refresh reference**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sensor will respond to changing image. rr,xx set as new coordinates  

b#[,$] &nbsp; `<Nb #>` **Bank occupancy status [& Brightness S/F]**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Trip status of 8 sensors in a single byte (8 bits) (hex & binary)

c$$$$ `< n/a >` **Camera re-Calibration and re-reference Sensors**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Severe changes to camera settings.  Refer to manuals before use!  

d%%[#] `< n/a >` **Difference Score for Sensor [# repeats]**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Prints colour diff score, brightness score and sum of both

e &nbsp; &nbsp; &nbsp; &nbsp; `<Ne>`&nbsp; &nbsp; &nbsp; **EPROM - save sensorCAM config. to EPROM**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:*: Records parameters in EPROM to be restored upon next Reset

f%% &nbsp; `<Nf %%>`  **Frame print. Full 16x3 byte pixel values**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Tabulates 4x4 (RGB) pixels for current and reference sensor images

g &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; `<Ng>` **Get Camera Global Config. Status (to USB)**
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Lists 14 different parameters of the ov2640 "Calibration" settings

h$[,#] &nbsp; `<Nh $ #>` **Help cmd.(debug for devel)**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Debug. h alone lists options. h7,# pauses scroll if bank # trips

i%%[,$$ ] `<Ni %%[ $$]>` **Info. on Sensor state and configuration**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* prints sensor state and full definition.  Can add a "twin" sensor S$$

j$,#  &nbsp; &nbsp; &nbsp; `<Nj $ #>` **adJust ov2640 global parameters & list <Ng>**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sets a single parameter($) for ov2640. j alone lists options for $

k%%,rr,xx `< n/a >` **locate a basic sensor at row rr, column xx**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Defines sensor at rr,xx but DOES NOT enable or reference/refresh it

l%% &nbsp; &nbsp; &nbsp; &nbsp; `<Nl %%>` **(Lima) Latch sensor on (occupied=1)**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sensor latched at 1 until cleared by zerO command or enAble command

m$[,%%] &nbsp;`<Nm $[ %%]>` **Min2trip frames setting [MaxSensor setting]**   
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sets min/max parameters.  m0,%% leaves min2trip unchanged

n$[,%%] &nbsp;`<Nn $[ %%]>` **Number for bank trip LED indicator. [minSensor]**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sets programmable LED to indicates when bank Number $ is tripped

o%% &nbsp; &nbsp; &nbsp; `<No %%>` **(Oscar) turn sensor Off (un-occupied=0)**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sensor disabled, set 0 until Latched on, or enabled using a%% or r%%

p# &nbsp; &nbsp; &nbsp; `<Np #>` **Position table for a bank of sensors**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Prints positions for enAbled sensors of bank #. &nbsp; p%% also similar

q# &nbsp; &nbsp; &nbsp; `<Nq #>` **Query enAbled state of sensors in bank**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Prints enabled state of all 8 sensors (1/0).  Use q9 for ALL banks

r%%[,0] &nbsp;`<Nr %%[ 0]>` **Refresh reference image for sensor**  
 &nbsp; &nbsp; &nbsp; &nbsp; **Response:* enAbles sensor and captures a new reference image.  Use r00 for ALL

s%% &nbsp; &nbsp; &nbsp; `< n/a >` **Scan video to define a new Sensor position (deprocate?)**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Scan for brightest spot and position sensor there. (superseeded)

t##[,%%] `<Nt ##[ %%]>` **Theshold setting (33-99) global [pvtThreshold for S%%]**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sets new threshold, global [ pvtThreshold] (t99 lists pvtThresholds)
 &nbsp; &nbsp; &nbsp; &nbsp; For ## of (2-30), print ## rows of scroll data.  t1 toggles scroll

t1,%% &nbsp; &nbsp; `<Nt 1 %%>` **Trash pvtThresholds for S%% bank**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* clears 1 bank of 8 pvtThresholds.  t1,99 clears ALL banks 

u%% &nbsp; &nbsp; `<Nu %%>` &nbsp;**Un-define Sensor**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Resets sensor coordinates to 0,0

v[#] &nbsp; &nbsp; `<Nv %%>` **Version [or Video wifi SSID #]**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Displays EX-SensorCAM version info OR v# starts preset SSID wifi link

w &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;`<Nw>` &nbsp; &nbsp; **Wait for command**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Cam suspends image capture and scrolling and waits for a CR

x y z &nbsp; `< n/a >` **Reserved commands for image transfer management**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Sends binary data to USB port for Processing4 (X Y Z) image delivery

n/a &nbsp; &nbsp; &nbsp; &nbsp;`<N>` &nbsp; **Current CAM selection and availability (CS only)**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Shows the currently selected CAM and the options available 

n/a &nbsp; &nbsp; `<NC ###>` **CAM selection**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Switches commands to the CAM at vpin ### or CAM number (1-4)

n/a &nbsp; &nbsp; `<NQ>` **Query state of all Sensors**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Tabulation of all sensor tripped states in banks of 8

F &nbsp; &nbsp; &nbsp; &nbsp; `<NF>` **Forces immediate CAM reset**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Reset into EX-SensorCAM mode, exting any WiFi mode

R &nbsp; &nbsp; &nbsp;`<n/a>` **Reset EX-SensorCAM &nbsp; (CS <NR> gives equivalent of <Nr 00>)**  
 &nbsp; &nbsp; &nbsp; &nbsp; *Response:* Reset into EX-SensorCAM mode, exting any WiFi mode 

**NOTE:  The EX-SensorCAM USB input will also accept most CS formatted commands.**

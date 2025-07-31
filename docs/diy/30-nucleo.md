# Complex Build - Nucleo

Reasons to consider the supported Nucleo-F4 boards

- Nucleo-144 can have up to 8 districts.  
  -- DCC signals are in sync, as is the case for all of the DCC-EX command stations.  
  -- DC signals can be in sync, which makes Nucleo-144 the better choice if you want 8 DC mode districts.

- Nucleo-144 - Ethernet is onboard/included with F429ZI and F439ZI  
  &nbsp; &nbsp; &nbsp; &nbsp; hint:  minimal cost difference; Mikey likes it!  

- Nucleo boards are quality products.  
  -- Pricing is best when purchased from st.com or one of their distributors:  
  &nbsp; &nbsp; Digikey, Farnell, Mouser

- Nucleo-64  
  Why would someone go this route vs. Nucleo-144 or CSB1/ESP32-WROOM?  
  -- More pins than ESP32  
  -- More memory than Mega  
  -- F411RE could be used as EX-IOExpander  
  -- Already have EX8874 and WiFi shield and/or want the smaller size

## Nucleo-F4 boards supported

- Nucleo-144  
  F429ZI / F439ZI - Ethernet included  
  F446ZE  
  F413ZH

- Nucleo-64  
  F411RE  
  F446RE

- Other notes  
  -- The three Nucleo-144 boards' pin locations are quite consistent with each other.  
  -- Nucleo-144 boards have the Zio headers installed - headers (top) and pins (bottom).  
  &nbsp; &nbsp; Morpho headers will require installation/soldering, if you want to use them.  
  &nbsp; &nbsp;  
  -- Nucleo-64 boards' pin locations are less consistent.  If you are aware, it should not be an issue.  
  -- Nucleo-64 boards have Arduino headers (top) and Morpho pins (top and bottom) installed.  

## Reference - Nucleo

- [Nucleo information](/reference/nucleo/19-nucleo-144-pin-reference.md)

- [Legacy Nucleo documentation](https://dcc-ex.com/legacy-docs/reference/hardware/microcontrollers/stm32-nucleo.html#stmicroelectronics-nucleo-recommended)

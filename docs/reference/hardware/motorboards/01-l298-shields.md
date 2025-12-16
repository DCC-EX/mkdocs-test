---
hide:
  - toc
---

# L298P & L298HN Shields

- DCC mode requires motor boards/shields where the switching frequency is capable of 10kHz on each output wire.

- DC mode uses the brake pin for the PWM signal.  

- Arduino and clone L298 shields use the XNOR gate to provide the inverted signal for DCC, but this does not provide low side brake in both directions for DC mode -- an issue for a reversing loop. [DC mode logic gate circuits](/reference/trackmanager/02-dc-mode-logic.md)

- There is a significant voltage drop when using L298 motor drivers. (see table below)  

- VIN from L298 motor shields should not be used to power the microprocessor board.  
  Cut the VIN trace or bend the VIN pin on L298 shields.  
  
## Genuine Arduino R3

- The Genuine Arduino R3 motor shield can be used with 5V and 3.3V microprocessors.  
  Arduino Motor Shield R3 included updates to the current sense circuit, which has not been adopted by any clones tested.  

## Clone shields

- Some clone shields have current sense circuits and can be used with Mega.  
  With ESP32-WROOM and Nucleo-F4, modifications are needed to protect ADC inputs.  

- Do not buy a motor shield without current sensing.  
  ![L298 clone shields](/_static/images/ex8874/l298-shield-x3.png){: style="width: 70%"}

- We have found no shields which have the same current sensing circuit as the Genuine Arduino R3.

- Clone shields may have current sensing, but will not have the LMV358 op-amp, or the LMV358 op-amp supply voltage is connected to 5V instead of the IOREF pin.

## Voltage drop

- Note the 3V drop at 1.1A with the L298 shield.  
  The 9.36V amplitude is the 'across the tracks' voltage.  
  ![L298 EX8874 voltage table](/_static/images/ex8874/l298-ex8874-voltage.png){: style="width: 90%"}

---
hide:
  - toc
---

# Nucleo - Power

## VIN from EX8874  

- EX-MotorShield8874 provides VIN output, which can be used to power the Nucleo 64/144.  

- In order to take advantage of the EX-MotorShield8874’s single power source capability, you will need to move the Nucleo power source jumper.  

- On the Nucleo-64s it’s jumper JP5 which you move from the U5V position (pins 1+2 jumpered, USB 5V source being used) to the E5V position (pins 2+3 jumpered).  

- On the Nucleo-144s it’s jumper JP3 which you move from the U5V position (centre pins 3+4 jumpered, USB 5V source being used) to the VIN-5V position (rightmost pins 5+6 jumpered).  
 
- In both cases this will power your Nucleo using the EX-MotorShield8874’s onboard switch mode power supply of 7.2V to the VIN pin, and allows some 800mA of 5V power to be available for the Nucleo and peripherals.  

- **Note for programming**: Once you do this it will mean you need both the EX-MotorShield8874 barrel jack to be powered AND the USB cable to enable programming. Or you can temporarily move JP5 back to U5V whilst uploading EX‑CommandStation.  

- **Power connection sequence**: The correct sequence is power on the EX-MotorShield8874 barrel jack, then attach the USB cable according to the STMicroelectronics documentation.  
  <br>
  &nbsp;  &nbsp; ![EX8874 Nucleo-144 pins](/_static/images/nucleo/vin-5v-power.jpg){: style="width: 90%"}  
  <br>

## VIN voltage

- Optimum VIN voltage is 7 volts.  
  VIN range is from 7 V to 12 V only and input current capability is linked to input voltage:  
  &nbsp;  &nbsp; 800 mA input current when Vin = 7 V  
  &nbsp;  &nbsp; 450 mA input current when 7 V < Vin <= 9 V  
  &nbsp;  &nbsp; 250 mA input current when 9 V < Vin <= 12 V

## USB

- USB can be used for power, but accessory power will be limited.  

- Caution:  If VIN jumper is not set to use USB - and - USB is connected prior to EX8874 being powered, expect enumeration issues and reduced power.  

- Refer to st.com user manuals  
  &nbsp;  &nbsp; [UM1974 Nucleo-144](https://www.st.com/resource/en/user_manual/um1974-stm32-nucleo144-boards-mb1137-stmicroelectronics.pdf)  
  &nbsp;  &nbsp; [UM1724 Nucleo-64](https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf)

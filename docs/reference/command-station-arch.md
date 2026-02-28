# Command Station Internal Architecture

The DCC-EX Command Station code is layered to reduce overall complexity and improve the ability to add new features. The most important layers are:

- DCC packet API  (DCC.h)  
    - provides loco speed/function and accessory control functions
    - maintains loco state and issues reminders

- DCC realtime waveform generation (DCCWaveform.h, DCCRMT.h)
    - handles simultaneous track signal for multiuple tracks

- Motor shield driver & track manager (MotorDriver.h, TrackManager.h)
    - handles shield specific pin numbers and current sensing

- ACK Manager (DCCAck.h)
    - handles all program track access and tuning
    - provides high level multi-cv functions

- Serial/Wifi/Ethernet input and output (SerialManager.h, Wifi*.h, EthernetInterface.h)

- Command Distributor  (CommandDistributor.h)
    - Manages multiple simultaneous input streams and broadcasts status changes

- Command Parsing/execution (DCCEXParser.h + others)
    - recognizes commands and calls appropriate internal APIs

- Exrail (EXRAIL*.h)
    - provides EXRAIL language functions
    - acts as single point of contact for almost every user-specific configuration
    - implements multi-tasking virtual machine to execute exrail scripts

- Hardware Abstraction Layer (HAL)  (IODevice.h, IO_*.h)
    - Provides many optional plug-in hardware device drivers for locally attached and i2c connected sensors, turnouts, lights etc.

- WiThrottle (Withrottle.h)
    - provides support for directly connected throttles using WiThrottle protocol

- CPU-specific layer (DCCTimer*.h)
    - provides pin and timer functions which differ between cpu types
  
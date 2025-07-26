# Optionally install a WiFi Shield


Most Arduino ESP8266 WiFi shields, including the dodgy ones with "Shiald" and "Arbuino" spelling mistakes will work well with a DCC-EX command station but the secret to success is to:

1. Ensure that the WiFi shield is physically modified to avoid it communicating over the standard Arduino Tx/Rx Serial pins.

2. Ensure that the WiFi shield is running a supported version of the Espressif AT software.



2. Prepare your WiFi shield (see supported types and notes below) by removing the pins that connect to the Mega Serial port.
3. Mount the WiFi shield on the motor shield.
4. Use two male-female Dupont wires to connect the shields TX pin to the Mega RX1 pin, and the shield RX pin to the Mega TX1 pin.  

TODO Photo.

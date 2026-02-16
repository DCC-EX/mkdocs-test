# Signal Basics

EXRAIL is able to define varuous different signal types depending on their electrical connection and assign each of them a unique signal_id that can be used to change and tese them without reference to their type. In some cases, the signal is made up of individually addressed LEDs, others thgeir own decoder, and in the case of semaphore signals they may be driven by a servo.

Signal definitions are extracted from myAutomation during the compile process and thus can appear anywhere in the EXRAIL script, they do not have to be executed as part of a sequence.

Refer to the following cookbook entries for details of defining signals of various types.

Once a signal has ben defined the following commands can be used:

- ```RED(signal_id)```   ```GREEN(signal_id)```   ```AMBER(signal_id)```   change the signal state
- ```IFRED(signal_id)``` ```IFGREEN(signal_id)``` ```IFAMBER(signal_id)``` test the signal state
- ```ONRED(signal_id)``` ```ONGREEN(signal_id)``` ```ONAMBER(signal_id)``` define event handlers to allow for any other processing associated with a signal change
- ```WAIT_WHILE_RED(signal_id)``` keep a loco stopped until a signal changes

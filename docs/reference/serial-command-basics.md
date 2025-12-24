# Serial Command Basics

- Serial commands are accepted as input from the USB serial connection or a TCP/IP connection.
- Commands have a single case dependent character opcode and optionaly parameters.
- Keyword parameters are shown in upper case but may be entered in mixed case.
- Value parameters are decimal numeric (unless otherwise noted)
- Not all commands have a response, and broadcasts mean that not all responses come from the last commands that you have issued.
- Commands entered like ```<JA>``` are actually read as ```<J A>```, so ```<Ja>``` is also acceptible.
- Commands that produce diagnostic information (which is intended for human reading rather than code) only write to the USB Serial output.
- Commands that cause state changes (such as loco speeds, turnout position) cause broadcasts to all serial connections and, where appropriate, WiThrottle protocol connections.

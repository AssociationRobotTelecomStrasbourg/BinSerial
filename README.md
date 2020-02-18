# BinSerial
BinSerial is a library to transmit data structure in binary via serial link.

## Example
Install BinSerial library.

Open the `echo` example.

Upload it on your board.

Then run in a terminal,
```bash
python3 binserial.py --port-name /dev/ttyUSB0
```
Replace `/dev/ttyUSB0` by the name of your serial port (e.g. `/dev/ttyACM0`, `COM1`…)

It should print `[2.718, 3.14, 5203]`.


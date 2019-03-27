#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""BinSerial is a library to transmit data in binary via serial link.

TODO:
- Finish Documentation.
- Implement multi-treading.

"""

__all__ = ['BinSerial']
__version__ = '1.0'
__author__ = 'Jonathan Plasse'

import serial
import struct
import time


class BinSerial:
    """Send and Receive serial data in binary."""

    def __init__(self, port_name, baud_rate):
        """Open a serial link at port_name with baud_rate."""
        self.types_dict = {'char': 'c', 'bool': '?',
                           'int8': 'b', 'uint8': 'B',
                           'int16': 'h', 'uint16': 'H',
                           'int32': 'i', 'uint32': 'I',
                           'int64': 'l', 'uint64': 'L',
                           'float': 'f'}
        self.port_name = port_name
        self.baud_rate = baud_rate

        # Open serial link
        self.ser = serial.Serial(self.port_name, self.baud_rate, timeout=1)

        # Wait for the arduino to initialize
        time.sleep(2)

    def __del__(self):
        """Close serial link."""
        self.ser.close()

    def _compute_format(self, structFormat):
        """Compute the format string for struct."""
        structTypes = '='

        for t in structFormat:
            structTypes += self.types_dict[t]

        return structTypes

    def read(self, structFormat):
        """Read data from serial link with structFormat."""
        structTypes = self.compute_format(structFormat)
        nbBytes = struct.calcsize(structTypes)

        # Wait until all the data is in the buffer
        while self.ser.in_waiting < nbBytes:
            pass

        # Read the raw data
        rawData = bytearray(nbBytes)
        self.ser.readinto(rawData)

        # Convert the raw data
        data = list(struct.unpack(structTypes, rawData))

        return data

    def write(self, structFormat, data):
        """Write data to serial link with structFormat."""
        structTypes = self.compute_format(structFormat)
        rawData = struct.pack(structTypes, *data)
        self.ser.write(rawData)


if __name__ == '__main__':
    port_name = '/dev/ttyACM0'
    baud_rate = 115200

    # Define the format of the structure of data sent
    structFormatSent = ['float']*2+['int16']
    structFormatReceived = ['float']*2+['int16']

    bser = BinSerial(port_name, baud_rate)

    bser.write(structFormatSent, [2.718, 3.14, 5203])
    data = bser.read(structFormatReceived)

    print(data)

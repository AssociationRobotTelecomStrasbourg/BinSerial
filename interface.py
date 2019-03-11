#!/usr/bin/env python3

import serial
import struct
import time

typesDict = {'char': (1, 'c'), 'bool': (1, '?'),
             'int8': (1, 'b'), 'uint8': (1, 'B'),
             'int16': (2, 'h'), 'uint16': (2, 'H'),
             'int32': (4, 'i'), 'uint32': (4, 'I'),
             'int64': (8, 'l'), 'uint64': (8, 'L'),
             'float': (4, 'f')}

def computeFormat(structFormat):
    """Compute the number of bytes to send and the string for struct.(pack/unpack)"""
    nbBytes = 0
    structTypes = ''

    for t in structFormat:
        nbBytes += typesDict[t][0]
        structTypes += typesDict[t][1]

    return nbBytes, structTypes

def readData(ser, structFormat):
    """Read the data"""
    nbBytes, structTypes = computeFormat(structFormat)
    # Wait until all the data is in the buffer
    while ser.in_waiting < nbBytes:
        pass
    # Read the raw data
    rawData = bytearray(nbBytes)
    ser.readinto(rawData)
    # Convert the raw data
    data = list(struct.unpack(structTypes, rawData))
    return data

def writeData(ser, structFormat, data):
    nbBytes, structTypes = computeFormat(structFormat)
    rawData = struct.pack(structTypes, *data)
    ser.write(rawData)

if __name__ == '__main__':
    portName = '/dev/ttyUSB0'
    baudRate = 115200

    # Define the format of the structure of data sent
    structFormatSent = ['float']*2+['int16']
    structFormatReceived = ['float']*2+['int16']

    with serial.Serial(portName, baudRate, timeout=1) as ser:
        # Wait for the arduino to initilize
        time.sleep(2)
        # Test echo
        # Write some data to the arduino
        writeData(ser, structFormatSent, [2.718, 3.14, 5])
        # Read the data from the arduino
        data = readData(ser, structFormatReceived)
        # The printed data should be the same
        print(data)

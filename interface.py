#!/usr/bin/env python3

import serial
import struct
import time

typesDict = {'char': 'c', 'bool': '?',
             'int8': 'b', 'uint8': 'B',
             'int16': 'h', 'uint16': 'H',
             'int32': 'i', 'uint32': 'I',
             'int64': 'l', 'uint64': 'L',
             'float': 'f'}

def computeFormat(structFormat):
    """Compute the format string for struct.(pack/unpack)"""
    structTypes = '='

    for t in structFormat:
        structTypes += typesDict[t]

    return structTypes

def readData(ser, structFormat):
    structTypes = computeFormat(structFormat)
    nbBytes = struct.calcsize(structTypes)
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
    structTypes = computeFormat(structFormat)
    rawData = struct.pack(structTypes, *data)
    ser.write(rawData)

if __name__ == '__main__':
    portName = '/dev/ttyACM0'
    baudRate = 115200

    # Define the format of the structure of data sent
    structFormatSent = ['float']*2+['int16']
    structFormatReceived = ['float']*2+['int16']

    with serial.Serial(portName, baudRate, timeout=1) as ser:
        # Wait for the arduino to initilize
        time.sleep(2)
        # Test echo
        # Write some data to the arduino
        writeData(ser, structFormatSent, [2.718, 3.14, 5203])
        # Read the data from the arduino
        data = readData(ser, structFormatReceived)
        # The printed data should be the same
        print(data)

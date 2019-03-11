#!/usr/bin/env python3

import serial
import struct
import time

# print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
# try:
#     self.serialConnection = serial.Serial(serialPort, serialBaud, timeout=4)
#     print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
# except:
#     print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')

typesDict = {'char': (1, 'c'), 'bool': (1, '?'),
             'int8': (1, 'b'), 'uint8': (1, 'B'),
             'int16': (2, 'h'), 'uint16': (2, 'H'),
             'int32': (4, 'i'), 'uint32': (4, 'I'),
             'int64': (8, 'l'), 'uint64': (8, 'L'),
             'float': (4, 'f')}

def computeFormat(typeArray):
    nbBytes = 0
    formatType = ''

    for t in typeArray:
        nbBytes += typesDict[t][0]
        formatType += typesDict[t][1]

    return nbBytes, formatType

def readData(ser, typeArray):
    nbBytes, formatType = computeFormat(typeArray)
    # Wait until all the data is in the buffer
    while ser.in_waiting < nbBytes:
        pass
    # Read the raw data
    rawData = bytearray(nbBytes)
    ser.readinto(rawData)
    # Convert the raw data
    data = list(struct.unpack(formatType, rawData))
    return data

def writeData(ser, typeArray):
    nbBytes, formatType = computeFormat(typeArray)
    ser.write(struct.pack(formatType, 2.718, 3.14, 5))

if __name__ == '__main__':
    # portName = 'COM5'     # for windows users
    portName = '/dev/ttyUSB0'
    baudRate = 9600
    typeArray = ['float']*2+['int16']

    with serial.Serial(portName, baudRate, timeout=1) as ser:
        time.sleep(2)
        writeData(ser, typeArray)
        data = readData(ser, typeArray)
        print(data)

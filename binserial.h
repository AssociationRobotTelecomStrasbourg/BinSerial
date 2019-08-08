#ifndef BinSerial_H
#define BinSerial_H

#include <Arduino.h>

void readData(void* data, size_t nbBytes);
void writeData(void* data, size_t nbBytes);

#endif

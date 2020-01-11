#include "binserial.h"

void readData(void* data, size_t nbBytes) {
  while (Serial.available() < nbBytes);
  Serial.readBytes((char*) data, nbBytes);
}

void writeData(const void* data, size_t nbBytes) {
  char* byteData = (char*) data;
  Serial.write(byteData, nbBytes);
}

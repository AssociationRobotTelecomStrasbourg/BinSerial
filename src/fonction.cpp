#include "fonction.hpp"

void writeData(void* data, uint32_t nbBytes) {
  byte* byteData = (byte*)(data);
  Serial.write(byteData, nbBytes);
}

#include "fonction.hpp"
#include <Arduino.h>

void sendToPC(void* data, uint32_t nbBytes)
{
  byte* byteData = (byte*)(data);
  Serial.write(byteData, nbBytes);
}

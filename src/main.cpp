#include "fonction.hpp"
#include <Arduino.h>

typedef struct{float a; float b; int16_t c;} format;

format data;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    Serial.readBytes((byte*)&data, sizeof(format));
    writeData(&data, sizeof(format));
  }
}

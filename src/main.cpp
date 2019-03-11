#include "fonction.hpp"
#include <Arduino.h>

typedef struct{float a; float b; int16_t c;} format;

format data;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    readData(&data, sizeof(format));
    writeData(&data, sizeof(format));
  }
}

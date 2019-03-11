#include <Arduino.h>
#include "binary_serial.hpp"

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

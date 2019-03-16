#include <Arduino.h>
#include "binary_serial.hpp"

typedef struct {float a; float b; int16_t c;} format;

format data;

void setup() {
  Serial.begin(115200);
  readData(&data, sizeof(data));
  writeData(&data, sizeof(data));
}

void loop() {
}

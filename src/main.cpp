#include "fonction.hpp"
#include <Arduino.h>

float data[] = {-3.51, 1.72};

void setup() {
  Serial.begin(115200);
  sendToPC(data, sizeof(float) * 2);
}

void loop() {
}

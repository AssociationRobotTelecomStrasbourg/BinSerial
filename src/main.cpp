#include "fonction.hpp"
#include <Arduino.h>

typedef struct{float a; float b; int16_t c;} test;

test data = {2.2, 6.14, 5};


void setup() {
  Serial.begin(115200);
  writeData(&data, sizeof(test));
}

void loop() {
}

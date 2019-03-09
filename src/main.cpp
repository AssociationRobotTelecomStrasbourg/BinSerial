#include <Arduino.h>
#include "fonction.hpp"

unsigned long timer = 0;
long loopTime = 5000;   // microseconds

void setup() {
  Serial.begin(38400);
  timer = micros();
}

void loop() {
  timeSync(loopTime, timer);
  //int val = analogRead(0) - 512;
  double val = (analogRead(0) -512) / 512.0;
  sendToPC(&val);
}

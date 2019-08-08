#include <binserial.h>

typedef struct {float a; float b; int16_t c;} format;

format data;

void setup() {
  Serial.begin(9600);
}

void loop() {
  readData(&data, sizeof(data));
  writeData(&data, sizeof(data));
}

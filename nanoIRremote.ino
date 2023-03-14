#include <IRremote.h>

#define IR_RECEIVE_PIN 2
#define LED 13

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN, LED);
}

void loop() {
  if (IrReceiver.decode()) {
    IrReceiver.resume();
    Serial.println(IrReceiver.decodedIRData.command);
  delay(100);
  }
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    Serial.print("I received: ");
    Serial.println(incomingByte);
    if (incomingByte == '1') {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write('2');
    }
    else if (incomingByte == '0') {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}

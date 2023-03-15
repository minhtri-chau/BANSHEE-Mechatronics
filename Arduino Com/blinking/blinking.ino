void setup() {
  pinMode(6, OUTPUT);
  digitalWrite(6, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char incomingByte = Serial.read();
//    Serial.print("I received: ");
//    Serial.println(incomingByte);
//    if (incomingByte == '1') {
//      digitalWrite(LED_BUILTIN, HIGH);
//      Serial.write('2');
//    }
//    else if (incomingByte == '0') {
//      digitalWrite(LED_BUILTIN, LOW);
//    }

    switch(incomingByte) {
      case '1':
        digitalWrite(6, HIGH);
        Serial.write(2);
        break;
      case '2':
        digitalWrite(6, LOW);
        break;
      default:
        break;
    }
  }
}

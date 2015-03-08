void setup() {
	Serial.begin(9600);
        Serial1.begin(115200);
        Serial1.print("$$$");
        delay(10);
        Serial1.print("Z");
}

void loop() {
        int incomingByte;
        
	if (Serial.available() > 0) {
		incomingByte = Serial.read();
		Serial.print("USB received: ");
		Serial.println(incomingByte, DEC);
                Serial1.print("USB received:");
                Serial1.println(incomingByte, DEC);
	}
	if (Serial1.available() > 0) {
		incomingByte = Serial1.read();
		Serial.print("UART received: ");
		Serial.println(incomingByte, DEC);
                Serial1.print("UART received:");
                Serial1.println(incomingByte, DEC);
	}
}

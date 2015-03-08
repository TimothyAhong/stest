void setup()
{  
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available())
  {    
     Serial.print("The character typed is: ");
     Serial.write(Serial.read());
     Serial.println("");
  }
}

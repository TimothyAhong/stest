#include <CapacitiveSensor.h> //Capacitive sensing library http://playground.arduino.cc/Main/CapacitiveSensor?from=Main.CapSense

//The library was modified to reduce the amount of time between the high and low pulses from 10usec to 5usec
//This allowed for less noise spikes to occur

//The capacitive sensors require a send pin which generates the high and low pulses, pin 14
CapacitiveSensor cs_c12 = CapacitiveSensor(14,12);//capacitive sensor on pin 12 
CapacitiveSensor cs_c11 = CapacitiveSensor(14,11);//capacitive sensor on pin 11 
CapacitiveSensor cs_c10 = CapacitiveSensor(14,10);//capacitive sensor on pin 10 
CapacitiveSensor cs_c9 = CapacitiveSensor(14,9);  //capacitive sensor on pin 9
CapacitiveSensor cs_c8 = CapacitiveSensor(14,8);  //capacitive sensor on pin 8
CapacitiveSensor cs_c7 = CapacitiveSensor(14,7);  //capacitive sensor on pin 7
CapacitiveSensor cs_c6 = CapacitiveSensor(14,6);  //capacitive sensor on pin 6
CapacitiveSensor cs_c5 = CapacitiveSensor(14,5);  //capacitive sensor on pin 5
CapacitiveSensor cs_c2 = CapacitiveSensor(14,2);  //capacitive sensor on pin 2

const int pA9pin = A9; //pressure sensor on pin A9
const int pA8pin = A8; //pressure sensor on pin A8
const int pA7pin = A7; //pressure sensor on pin A7
const int pA6pin = A6; //pressure sensor on pin A6
const int pA5pin = A5; //pressure sensor on pin A5
const int pA4pin = A4; //pressure sensor on pin A4

const int indicator = 13; //indicator LED on pin 13 (built in) for program ON 

long c12 = 0; //variable to hold capacitive sensor reading on pin 12
long c11 = 0; //variable to hold capacitive sensor reading on pin 11
long c10 = 0; //variable to hold capacitive sensor reading on pin 10
long c9 = 0;  //variable to hold capacitive sensor reading on pin 9
long c8 = 0;  //variable to hold capacitive sensor reading on pin 8
long c7 = 0;  //variable to hold capacitive sensor reading on pin 7
long c6 = 0;  //variable to hold capacitive sensor reading on pin 6
long c5 = 0;  //variable to hold capacitive sensor reading on pin 5
long c2 = 0;  //variable to hold capacitive sensor reading on pin 2

int pA9 = 0; //variable to hold pressure sensor reading on pin A9
int pA8 = 0; //variable to hold pressure sensor reading on pin A8
int pA7 = 0; //variable to hold pressure sensor reading on pin A7
int pA6 = 0; //variable to hold pressure sensor reading on pin A6
int pA5 = 0; //variable to hold pressure sensor reading on pin A5
int pA4 = 0; //variable to hold pressure sensor reading on pin A4

void setup()
{
  Serial1.begin(9600); //Start up Serial1 (not Serial which is USB) which goes to Xbee
  pinMode(indicator,OUTPUT); 
  digitalWrite(indicator,HIGH);
  //delay(1000);
  //digitalWrite(indicator,LOW);
  autoCalibrateOff(); //Turn the autocalibrate OFF so that raw data is kept with no calibration on restart 

  delay(100);
}

void loop()
{
  readCaps(); //Read capacitive sensors 
  readPres(); //Read pressure sensors
  printCapVals(0); //Print values read from capacitive sensors. 0 allows for values to be continued to be printed on same line.
  printPresVals(1);//Print values read from pressure sensors. 1 gives a new line

  delay(30);
}

void readCaps()//function to read in capacitive sensor values
{
  long start = millis();

  c12 = cs_c12.capacitiveSensorRaw(100); //take 30 samples and average
  c11 = cs_c11.capacitiveSensorRaw(100);
  c10 = cs_c10.capacitiveSensorRaw(100);
  c9 = cs_c9.capacitiveSensorRaw(100);
  c8 = cs_c8.capacitiveSensorRaw(100);
  c7 = cs_c7.capacitiveSensorRaw(100);
  c6 = cs_c6.capacitiveSensorRaw(100);
  c5 = cs_c5.capacitiveSensorRaw(100);
  c2 = cs_c2.capacitiveSensorRaw(100);
  
  c12 = sample(c12);
  c11 = sample(c11);
  c10 = sample(c10);
  c9 = sample(c9);
  c8 = sample(c8);
  c7 = sample(c7);
  c6 = sample(c6);
  c5 = sample(c5);
  c2 = sample(c2);
}

void readPres()//function to read in pressure sensor values
{
  pA9 = analogRead(pA9pin);//analog input 
  pA8 = analogRead(pA8pin);
  pA7 = analogRead(pA7pin);
  pA6 = analogRead(pA6pin);
  pA5 = analogRead(pA5pin);
  pA4 = analogRead(pA4pin);
}

void printCapVals(int t)//function to print out capacitive sensor values
{
  Serial1.print(c2); 
  Serial1.print("\t");
  Serial1.print(c5); 
  Serial1.print("\t");
  Serial1.print(c6); 
  Serial1.print("\t");
  Serial1.print(c7); 
  Serial1.print("\t");
  Serial1.print(c8);
  Serial1.print("\t"); 
  Serial1.print(c9); 
  Serial1.print("\t");
  Serial1.print(c10); 
  Serial1.print("\t");
  Serial1.print(c11); 
  Serial1.print("\t");
  Serial1.print(c12);

  if(t == 0) //bias to give new line or allow other printing on same line
    Serial1.print("\t");
  else
    Serial1.println();  
}

void printPresVals(int t)//function to print out pressure sensor values
{
  Serial1.print(pA9); 
  Serial1.print("\t");
  Serial1.print(pA8); 
  Serial1.print("\t");
  Serial1.print(pA7); 
  Serial1.print("\t");
  Serial1.print(pA6); 
  Serial1.print("\t");
  Serial1.print(pA5);
  Serial1.print("\t"); 
  Serial1.print(pA4); 
  Serial1.print("\t");

  if(t == 0)//bias to give new line or allow other printing on same line
    Serial1.print("\t");
  else
    Serial1.println();
}

void autoCalibrateOff()//function to turn autocalibration OFF. The values were obtained from the library documentation
{
  cs_c12.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c11.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c10.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c9.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c8.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c7.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c6.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c5.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_c2.set_CS_AutocaL_Millis(0xFFFFFFFF);
}

long sample(long val)
{
  long total;
  int samples = 40;
  long sampled = 0;
  for(int i=0; i<samples; i++)
  {
    total = total + val;
  }
  sampled = round(total/samples);
  return sampled;
}



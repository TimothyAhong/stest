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
CapacitiveSensor cs_c17 = CapacitiveSensor(14,17);//capacitive sensor on pin 17

const int pA9pin = A9; //pressure sensor on pin A9
const int pA8pin = A8; //pressure sensor on pin A8
const int pA7pin = A7; //pressure sensor on pin A7
const int pA6pin = A6; //pressure sensor on pin A6
const int pA5pin = A5; //pressure sensor on pin A5
const int pA4pin = A4; //pressure sensor on pin A4
const int pA2pin = A2; //pressure sensor on pin A2
const int pA1pin = A1; //pressure sensor on pin A1

const int aA17pin = A17;//accelerometer x-axis on pin A17
const int aA16pin = A16;//accelerometer Y-axis on pin A16
const int aA15pin = A15;//accelerometer Z-axis on pin A15

const int indicator = 13; //indicator LED on pin 13 (built in) for program ON 

//left female to top male connector and right female to bottom male connector
//How the pad layout is with the appropriate pin attachment given the above pluggin was used
/*   Left |  | |  | Right       
 _________|__|_|__|__________
 |            Top             |
 |                            |
 |                            |
 |             9              |
 |                            |
 |            11              |
 |                            |
 |                            |
 |                            |
 |       8             6      |
 |                            | 
 |      10             5      |
 |                            |
 |       7            17      |
 |                            |
 |                            |
 |             2              |
 |                            |
 |            12              |
 |                            |
 |          Bottom            |
 |____________________________| 
 */
const long c9Bias = 109;
const long c11Bias = 121;
const long c8Bias = 130;
const long c6Bias = 105;
const long c10Bias = 128;
const long c5Bias = 145;
const long c7Bias = 132;
const long c17Bias = 153;
const long c2Bias = 152;
const long c12Bias = 146;

const long scaled = 1000;

long c12 = 0; //variable to hold capacitive sensor reading on pin 12
long c11 = 0; //variable to hold capacitive sensor reading on pin 11
long c10 = 0; //variable to hold capacitive sensor reading on pin 10
long c9 = 0;  //variable to hold capacitive sensor reading on pin 9
long c8 = 0;  //variable to hold capacitive sensor reading on pin 8
long c7 = 0;  //variable to hold capacitive sensor reading on pin 7
long c6 = 0;  //variable to hold capacitive sensor reading on pin 6
long c5 = 0;  //variable to hold capacitive sensor reading on pin 5
long c2 = 0;  //variable to hold capacitive sensor reading on pin 2
long c17 = 0;  //variable to hold capacitive sensor reading on pin 17

int pA9 = 0; //variable to hold pressure sensor reading on pin A9
int pA8 = 0; //variable to hold pressure sensor reading on pin A8
int pA7 = 0; //variable to hold pressure sensor reading on pin A7
int pA6 = 0; //variable to hold pressure sensor reading on pin A6
int pA5 = 0; //variable to hold pressure sensor reading on pin A5
int pA4 = 0; //variable to hold pressure sensor reading on pin A4
int pA2 = 0; //variable to hold pressure sensor reading on pin A2
int pA1 = 0; //variable to hold pressure sensor reading on pin A1

int accX = 0; //variable to hold accelerometer x-axis
int accY = 0; //variable to hold accelerometer y-axis
int accZ = 0; //variable to hold accelerometer z-axis

void setup()
{
  Serial1.begin(9600); //Start up Serial1 (not Serial which is USB) which goes to Xbee

  pinMode(indicator,OUTPUT);//set the led as an output
  digitalWrite(indicator,HIGH); //indicator LED turns ON to let us know that the code is running and was loaded properly
  //delay(10);
  //digitalWrite(indicator,LOW);
  autoCalibrateOff(); //Turn the autocalibrate OFF so that raw data is kept with no calibration on restart 
  delay(100);
}

void loop()
{
  readCaps(100,1,2,0); //Read capacitive sensors; (resolution of sensor reading,hardcode down or not,precision,zeroed or not) 
  readPres(); //Read pressure sensors
  readAccel(); //read the accelerometer

  printCapVals(0); //Print values read from capacitive sensors. 0 allows for values to be continued to be printed on same line.
  printPresVals(0);//Print values read from pressure sensors. 1 gives a new line
  printAccel(1); //Print values read from the accelerometer
  delay(30);
}

void readAccel()//function to read and store the acceleromter data from sensor
{
  accX = analogRead(aA17pin); //read and store accelrometer axis in proper variables
  accY = analogRead(aA16pin);
  accZ = analogRead(aA15pin);
}

void readPres()//function to read in pressure sensor values
{
  pA9 = analogRead(pA9pin);//read and store analog input /pressure sensors
  pA8 = analogRead(pA8pin);
  pA7 = analogRead(pA7pin);
  pA6 = analogRead(pA6pin);
  pA5 = analogRead(pA5pin);
  pA4 = analogRead(pA4pin);

  pA2 = analogRead(pA2pin);
  pA1 = analogRead(pA1pin);

  presMap();//call the remapping function
}

void presMap()//function to map the pressure sensors from 0 - 1023 instead of the 1023-0 because it's pulled up to 5V
{  
  pA9 = map(pA9,1023,0,0, 1023);
  pA8 = map(pA8,1023,0,0, 1023);
  pA7 = map(pA7,1023,0,0, 1023);
  pA6 = map(pA6,1023,0,0, 1023);
  pA5 = map(pA5,1023,0,0, 1023);
  pA4 = map(pA4,1023,0,0, 1023);
  pA2 = map(pA2,1023,0,0, 1023);
  pA1 = map(pA1,1023,0,0, 1023);

}

//function to read in capacitive sensor values
void readCaps(int resolution,int input, int precision, int zero) //(resolution of sensor reading,hardcode down or not,precision,zeroed or not)
{
  long start = millis(); //start the timing required for the cap sesnor library to calculate the capcitance level based on timing from 0 - 5V
  int bias;
  c12 = cs_c12.capacitiveSensorRaw(resolution); //read and store the raw sensor values with the desired resolution
  c11 = cs_c11.capacitiveSensorRaw(resolution);
  c10 = cs_c10.capacitiveSensorRaw(resolution);
  c9 = cs_c9.capacitiveSensorRaw(resolution);
  c8 = cs_c8.capacitiveSensorRaw(resolution);
  c7 = cs_c7.capacitiveSensorRaw(resolution);
  c6 = cs_c6.capacitiveSensorRaw(resolution);
  c5 = cs_c5.capacitiveSensorRaw(resolution);
  c2 = cs_c2.capacitiveSensorRaw(resolution);
  c17 = cs_c17.capacitiveSensorRaw(resolution);

  if(zero == 0)
    zero = 0;
  else
    zero = precision;  

  if(input == 1)//call scaling down function based on input
  {

    if(precision == 1) //will tell scaling function to give single to double integer response
      hardcodeDown(scaled,zero);
    if(precision == 2)//will tell scaling function to give double to triple integer response
      hardcodeDown(scaled/10,zero); 
  }
}

//routine to scale down raw sensor readings
void hardcodeDown(int div,int zero) //(how much to divide sensor raw values by, what type of zeroing is it)
{ // to to bottom: 9,11,8(L),6(R),10(L),5(R),7(L),17(R),2,12
  c7 = c7/div;
  c10 = c10/div;  
  c8 = c8/div;
  c11 = c11/div;
  c9 = c9/div;
  c6 = c6/div;
  c5 = c5/div;  
  c17 = c17/div;
  c2 = c2/div;
  c12 = c12/div;

  if(zero == 1)
  {
    c7 = c7 - floor(c7Bias/10);
    c10 = c10 - floor(c10Bias/10);
    c11 = c11 - floor(c11Bias/10);
    c9 = c9 - floor(c9Bias/10);
    c6 = c6 - floor(c6Bias/10);
    c5 = c5 - floor(c5Bias/10);
    c17 = c17 - floor(c17Bias/10);
    c2 = c2 - floor(c2Bias/10);
    c12 = c12 - floor(c12Bias/10);
  }
  if(zero == 2)
  {
    c7 = c7 - c7Bias;
    c10 = c10 - c10Bias;
    c8 = c8 - c8Bias;
    c11 = c11 - c11Bias;
    c9 = c9 - c9Bias;

    c6 = c6 - c6Bias;
    c5 = c5 - c5Bias;
    c17 = c17 - c17Bias;
    c2 = c2 - c2Bias;
    c12 = c12 - c12Bias;
  }
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
  cs_c17.set_CS_AutocaL_Millis(0xFFFFFFFF);
}

//printing routines

void printAccel(int x)
{
  Serial1.print(accX); 
  Serial1.print("\t");
  Serial1.print(accY); 
  Serial1.print("\t");
  Serial1.print(accZ); 

  if(x == 1)  
    Serial1.println();
  else
    Serial1.print("\t");  
}
void printCapVals(int t)//function to print out capacitive sensor values
{

  Serial1.print(c9);  Serial1.print("\t"); 
  Serial1.print(c11); Serial1.print("\t");
  Serial1.print(c8);  Serial1.print("\t"); Serial1.print(c6);  Serial1.print("\t");
  Serial1.print(c10); Serial1.print("\t"); Serial1.print(c5);  Serial1.print("\t");
  Serial1.print(c7);  Serial1.print("\t"); Serial1.print(c17); Serial1.print("\t");
  Serial1.print(c2);  Serial1.print("\t");
  Serial1.print(c12);

  if(t == 0) //bias to give new line or allow other printing on same line
    Serial1.print("\t");
  else
    Serial1.println();  
}

void printPresVals(int t)//function to print out pressure sensor values
{
  Serial1.print(pA7); 
  Serial1.print("\t");
  Serial1.print(pA8); 
  Serial1.print("\t");
  Serial1.print(pA9); 
  Serial1.print("\t");
  Serial1.print(pA2); 
  Serial1.print("\t");
  Serial1.print(pA4); 
  Serial1.print("\t");
  Serial1.print(pA5);
  Serial1.print("\t"); 
  Serial1.print(pA6);
  Serial1.print("\t"); 
  Serial1.print(pA1);   

  if(t == 0)//bias to give new line or allow other printing on same line
    Serial1.print("\t");
  else
    Serial1.println();
}










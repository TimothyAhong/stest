#include <CapacitiveSensor.h> //Capacitive sensing library http://playground.arduino.cc/Main/CapacitiveSensor?from=Main.CapSense

//The library was modified to reduce the amount of time between the high and low pulses from 10usec to 5usec
//This allowed for less noise spikes to occur

//The capacitive sensors require a send pin which generates the high and low pulses, pin 14
CapacitiveSensor cs_12 = CapacitiveSensor(14,12);//capacitive sensor on pin 12 
CapacitiveSensor cs_11 = CapacitiveSensor(14,11);
CapacitiveSensor cs_10 = CapacitiveSensor(14,10);
CapacitiveSensor cs_9 = CapacitiveSensor(14,9);
CapacitiveSensor cs_8 = CapacitiveSensor(14,8);
CapacitiveSensor cs_7 = CapacitiveSensor(14,7);
const int indicator = 13; //indicator LED on pin 13 (built in) for program ON 


long average_values[6];
//int average_bases[6] = {26711, 30879, 32406, 32285, 31763, 26711};
int average_bases[6] = {56,79,82,79,78,65};
int scale_factor = 500;

int average_length = 5;
int average_counter = 0;
int sum = 0;


void setup()
{
  Serial1.begin(9600); //Start up Serial1 (not Serial which is USB) which goes to Xbee
  Serial1.println("AAAAA");
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
  
  updateAverages();
  printCapVals(); //Print values read from capacitive sensors. 0 allows for values to be continued to be printed on same line.
  
  //delay(200);
}

void readCaps()//function to read in capacitive sensor values
{
  long start = millis();
}

void updateAverages() {
 average_values[0]+=cs_12.capacitiveSensorRaw(100);
 average_values[1]+=cs_11.capacitiveSensorRaw(100);
 average_values[2]+=cs_10.capacitiveSensorRaw(100);
 average_values[3]+=cs_9.capacitiveSensorRaw(100);
 average_values[4]+=cs_8.capacitiveSensorRaw(100);
 average_values[5]+=cs_7.capacitiveSensorRaw(100);
}

void printCapVals()//function to print out capacitive sensor values
{
  if(average_counter > average_length) {
    for(int i=0;i<6;i++) {
      Serial1.print((average_values[i]/average_length)/scale_factor - average_bases[i]);
      Serial1.print(',');
      average_values[i] = 0;
    }
    printPressureVals();
    Serial1.println();
    average_counter = 0;
  } else {
    average_counter++;
  }
}

void printPressureVals()
{
    Serial1.print(analogRead(23));
    Serial1.print(',');
    Serial1.print(analogRead(22));
    Serial1.print(',');
    Serial1.print(analogRead(21));
}

void autoCalibrateOff()//function to turn autocalibration OFF. The values were obtained from the library documentation
{
  cs_12.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_11.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_10.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_9.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_8.set_CS_AutocaL_Millis(0xFFFFFFFF);
  cs_7.set_CS_AutocaL_Millis(0xFFFFFFFF);
}

//this doesnt take the average
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



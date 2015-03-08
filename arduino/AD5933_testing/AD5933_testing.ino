#include "AD5933.h"
#include <Wire.h>

#define LOGGING1 1


void query_ad5933(double impedance_magnitudes[]){
  impedance_magnitudes[0] = 1;
  impedance_magnitudes[1] = 1;
  Serial.println("1");
  AD5933.setStartFreq(10000);
  Serial.println("2");
  AD5933.setIncrementinHex(1);
  Serial.println("3");
  AD5933.setNumofIncrement(2);
  Serial.println("4");
  AD5933.setSettlingCycles(0x1FF, 4);
  Serial.println("5");
  AD5933.getTemperature();
  Serial.println("6");
  AD5933.setVolPGA(0,1); 
  Serial.println("7");
  //TODO how do we follow the callibration procedure?
  double gain_factor = AD5933.getGainFactor(4700);//TODO what is this value?
  Serial.println("8");
  AD5933.tempUpdate();
  AD5933.setCtrMode(REPEAT_FREQ);
  Serial.println("9");
  //AD5933.performFreqSweep(gain_factor, impedance_magnitudes);
  impedance_magnitudes[0] = AD5933.getMagOnce();
  Serial.println("10");
}

void setup_ad5933(void) {
  Wire.begin();
  double impedance_magnitudes[20];
  AD5933.setExtClock(false);
  AD5933.resetAD5933();
  query_ad5933(impedance_magnitudes);
  print_double_array(impedance_magnitudes, 10);
}

void setup(void) {
  Serial.begin(9600);
  Serial.println("yolo");
  setup_ad5933();
}



void loop(void) {
  
  //query_ad5933(impedance_magnitudes);
  Serial.println();
  Serial.println("loop");
  //
  delay(1000);
}


void print_double_array(double arr[], int arr_length) {
  int i;
  for (i = 0; i < arr_length - 1; i = i + 1) {
    Serial.println(arr[i]);
  } 
}

import processing.serial.*;
import java.util.Date;

//globals
Serial mySerial;
PrintWriter output;
int xPos = 0;
int maxExpectedValue = 2000;
int intValue;
String line;

int valueCounter = 0;
float runningAverage = 0;
int runningAverageCounter = 0;
int runningAverageMaxValue = 380;

void setupGraph() {
  size(800, 700);
  background(0);
}

void setup() {
  print(Serial.list());
   mySerial = new Serial( this, Serial.list()[4], 9600 );
   setupGraph();
   setupOutput();
}

void draw() {
  if (mySerial.available() > 0 ) {
    String value = mySerial.readStringUntil('\n');
    if ( value != null ) {
  updateFile(value);
      //String[] left_right = split(value, "||");
      //String new_value = join(left_right, '');
      //value = value.replace("||\t","");
      println(value);
      String[] value_array = split(value, ',');
      //println(1023-int(trim(value_array[1])));
      int cap = int(value_array[0])/100;
      int adc1 = 1023-int(trim(value_array[1]));
      int adc2 = 1023-int(trim(value_array[2]));
      int adc3 = 1023-int(trim(value_array[3]));
      int adc4 = 1023-int(trim(value_array[4]));
      
      updateGraph(cap, 255);
      updateGraph(adc1, 100);
      updateGraph(adc2, 120);
      updateGraph(adc3, 130);
      updateGraph(adc4, 140);
    }
    //delay(100);
  }
}

void updateFile(String value) {
  Date d = new Date();
  line = d.getTime() + "," + value;
  output.print(line);
  output.flush();
}

void setupOutput() {
  Date d = new Date();
  String filename = "1_sensor_1_cap_data/data_"+d.getTime()+".csv";
  output = createWriter(filename);
  print("filename: "+filename);
}

void updateGraph(float value, int col) {
  float mappedValue = map(value, 0, 1023, 0, height);
  stroke(255, col, 100);
  point(xPos, height - mappedValue);
  /*
  runningAverage += value/(runningAverageMaxValue+1);
  runningAverageCounter++;
  if(runningAverageCounter > runningAverageMaxValue) {
      stroke(204, 102, 0);
     text((int)runningAverage, xPos, 600);
     line( xPos, height - map(runningAverage, 0, 1023, 0, height), xPos-runningAverageMaxValue, height - map(runningAverage, 0, 1023, 0, height));
     stroke(255);
     runningAverage = 0; 
     runningAverageCounter = 0;
  }*/
  
  valueCounter++;
  if(valueCounter > 50) {
     text((int)value, xPos, 500);
     //draw the average
    valueCounter = 0; 
  }
  if(xPos >= width)
  {
    xPos = 0;
    background(0);
  } else {
   xPos++; 
  }
}

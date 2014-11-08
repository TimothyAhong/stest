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

void setupOutput() {
  Date d = new Date();
  String filename = "node_debug_data/data_"+d.getTime()+".csv";
  output = createWriter(filename);
  print("filename: "+filename);
}

void setupGraph() {
  size(800, 700);
  background(0);
}

void setup() {
  print(Serial.list());
   mySerial = new Serial( this, Serial.list()[4], 9600 );
   setupOutput();
   setupGraph();
}

void draw() {
  if (mySerial.available() > 0 ) {
    String value = mySerial.readStringUntil('\n');
    //println(value);
    if ( value != null ) {
      //String[] left_right = split(value, "||");
      //String new_value = join(left_right, '');
      value = value.replace("||\t","");
      
      int[] value_array = int(split(value, '\t'));
      //print(value_array[3]);
      update_heatmap(value_array);
      updateFile(value.replace('\t',','));
      /*
      if(intValue < maxExpectedValue) {
        updateFile(value);
      }*/
    }
    //delay(100);
  }
}

void updateFile(String value) {
  Date d = new Date();
  line = d.getTime() + "," + value;
  output.println(line);
  output.flush();
}

void updateGraph(float value) {
  float mappedValue = map(value, 0, 1023, 0, height);
  stroke(255);
  point(xPos, height - mappedValue);
  
  runningAverage += value/(runningAverageMaxValue+1);
  runningAverageCounter++;
  if(runningAverageCounter > runningAverageMaxValue) {
      stroke(204, 102, 0);
     text((int)runningAverage, xPos, 600);
     line( xPos, height - map(runningAverage, 0, 1023, 0, height), xPos-runningAverageMaxValue, height - map(runningAverage, 0, 1023, 0, height));
     stroke(255);
     runningAverage = 0; 
     runningAverageCounter = 0;
  }
  
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

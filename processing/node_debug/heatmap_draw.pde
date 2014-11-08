int max_width = 200;
int max_height = 200;
int nodes_wide = 2;
int nodes_tall = 2;

void update_heatmap(int[] value_array) {
  for(int i=0; i<value_array.length; i++) {
  }
  int row = 0;
  int column = 0;
   for(int i=0; i<value_array.length; i++) {
     
     //update the cubes left side first then right side
     if(i<value_array.length/2) {
       row = i;
       column = 1;
     } else {
       row = i-value_array.length/2;
       column = 2;
     }
     
     /* updates cubes L-Front R-Front, L-Mid R-Mid
     int row = i/nodes_tall;
     int column = i%nodes_wide;
     */
     draw_rect(row, column, value_array[i]);
   }
}

void draw_rect(int row, int column, int value) {
  get_fill_value(value/20);
  rect(get_x(column), get_y(row), get_width(), get_height());
  fill(0);
  PFont f = createFont("Georgia",40,true);
  textFont(f);
  textAlign(CENTER);
  text(value,get_x(column)+get_width()/2,get_y(row)+get_height()/2);
}

int get_x(int column) {
  return get_width()*column;
}

int get_y(int row) {
  return get_height()*row;
}

int get_width() {
  return max_width/nodes_wide;
}

int get_height() {
 return max_height/nodes_tall; 
}

void get_fill_value(int value) {
   fill(value, value, 0);
}

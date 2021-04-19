/* functional.ino
 * Imaad Syed
 * 4/19/2021
 * read input and put out appropriate response
 *
 */

// setup pins here
void setup() {
  
  Serial.begin(9600);
}

int x = 0;
int y = 0;
int z = 0;

void loop() {
  
  x = Serial.readLine();
  y = Serial.readLine();
  z = Serial.readLine();
  
  if(x = 1) {
    
    // 1 step
    
  } else if (x = -1) {
  
  }
  
  if(y = 1) {
    
    // 1 step
    
  } else if (y = -1) {
  
  }
  
  if(z = 1) {
    
    // 1 step
    
  } else if (z = -1) {
  
  }
  
  if(digitalRead() == HIGH) {
    //laser on
  } else {
    //laser off
  }
  
}

void xf() {

}

void xb() {

}

void yf() {

}

void yb() {

}

void zf() {

}

void zb() {

}

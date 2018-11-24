#include <Servo.h>
#define s_nothing '0' // ent [0-10]
#define s_heatingup '1' //ent [10-100]
#define s_meh '2' // ent [100-150]
#define s_warm '3' // ent [150-200]
#define s_hot '4' // ent [200 - 250]
#define s_sizzle '5' // ent [250 - 300]
#define s_hell '6' // ent>300
#define s_loyly '7' 
#define s_openDoor '8'

int waterServoPin = 9;
Servo waterServo;  // create a servo object

// Every time water is poured, we increase the angle for the next pour
// Because if we used the same angle every time no more water would come out after the first
// When the water is refilled, the Arduino has to be resetted (not very convenient, but works).
int timesPoured = 0;
// we increment until this
int maxTimesPoured = 1;

// the size of the increment for the angle
int degreeIncrement = 60;

// This is just used to print the angle poured
int anglePoured = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // set the baud rate
  //Serial.println("Ready"); // print "Ready" once
  waterServo.attach(waterServoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    char state = Serial.read();
    char str[2];
    str[0] = state;
    str[1] = '\0';
    Serial.print(str);
    switch(state){
      case s_nothing:
        //do something
        break;
      case s_heatingup:
        //do something
        break;
      case s_meh:
        //do something
        break;
      case s_warm:
        //do something
        break;
      case s_hot:
        //do something
        break;
      case s_sizzle:
        //do something
        break;
      case s_hell:
        //do something
        break;
      case s_loyly:
        //do something

        anglePoured = pourWater();
        //Serial.println("Poured water at angle " + anglePoured);
        // Make sure the servo is in original position
        waterServo.write(0);
        if(timesPoured < maxTimesPoured) {
            timesPoured++;
        }
        
        break;
      case s_openDoor:
        //do something
        break;
    }
  }
}


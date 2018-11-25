//#include <Servo.h>

//int waterServoPin = 9;
//Servo waterServo;  // create a servo object

// Every time water is poured, we increase the angle for the next pour
// Because if we used the same angle every time no more water would come out after the first
// When the water is refilled, the Arduino has to be resetted (not very convenient, but works).
//int timesPoured = 0;

// the size of the increment for the angle
//int degreeIncrement = 30;

/*
 * Returns the degree that the container was turned to
 */
int pourWater() {
  // When löyly
  delay(10);
  int angle = degreeIncrement + degreeIncrement * timesPoured;
  // We'll pour 30' plus timesPoured * 30, times poured can be at max 4 (= 120 degrees)
  waterServo.write(angle);
  // Keep the cup still for a moment
  delay(1500);
  // Return back to original position
  // waterServo.write(0);

  // We only want to do 120 degrees at most
//  if(timesPoured < maxTimesPoured) {
//    timesPoured++;
//  }
  return angle;
}

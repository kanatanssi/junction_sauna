#define no_state 0
#define ent100 1
#define ent200 2

Servo waterServo;  // create a servo object

// Every time water is poured, we increase the angle for the next pour
// Because if we used the same angle every time no more water would come out after the first
// When the water is refilled, the Arduino has to be resetted (not very convenient, but works).
int timesPoured = 0;
// the size of the increments
int degreeIncrement = 30;

void setup() {
  Serial.begin(115200); // set the baud rate
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    char data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '\0';
    Serial.print(str);

    if(data == ent200)
    
  }
  // When löyly
  delay(10);
  // We'll pour 30' plus timesPoured * 30, times poured can be at max 4 (= 120 degrees)
  waterServo.write(degreeIncrement + degreeIncrement * timesPoured);
  // Keep the cup still for a moment
  delay(1500);
  waterServo.write(0);
}


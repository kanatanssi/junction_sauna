#define no_state 0
#define ent100 1
#define ent200 2

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // set the baud rate
  //Serial.println("Ready"); // print "Ready" once
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
}


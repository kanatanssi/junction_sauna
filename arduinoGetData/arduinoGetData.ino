#define s_nothing '0' // ent [0-10]
#define s_heatingup '1' //ent [10-100]
#define s_meh '2' // ent [100-150]
#define s_warm '3' // ent [150-200]
#define s_hot '4' // ent [200 - 250]
#define s_sizzle '5' // ent [250 - 300]
#define s_hell '6' // ent>300
#define s_loyly '7' 
#define s_openDoor '8'

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // set the baud rate
  //Serial.println("Ready"); // print "Ready" once
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
        break;
      case s_openDoor:
        //do something
        break;
    }
  }
}


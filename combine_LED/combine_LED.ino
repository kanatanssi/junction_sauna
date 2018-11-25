#include <Adafruit_NeoPixel.h>
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

#define PIN 10
#define NUM_LEDS 30
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);
char state;
int counter = 40;
int count = 0;

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
  strip.begin();
  strip.show();
  state = s_loyly;
   //waterServo.attach(waterServoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() > 0) {
    state = Serial.read();
    char str[2];
    str[0] = state;
    str[1] = '\0';
    Serial.print(str);
  }
    if(count++>= counter){
      state = s_loyly;
      count = 0;
    }
    switch(state){
      case s_nothing:
        Fade(0xff, 0xa5, 0x00);
        break;
      case s_heatingup:
        Fade(0xff, 0xa5, 0x00);
        break;
      case s_meh:
        Fade(0xff, 0xa5, 0x00);
        break;
      case s_warm:
        Fade(0xff, 0x77, 0x00);
        break;
      case s_hot:
        Fade(0xff, 0x00, 0x00);
        break;
      case s_sizzle:
        Fire(20,100,10);
        break;
      case s_hell:
        Fire(20,100,10);
        break;
      case s_loyly:
        //anglePoured = pourWater();
        //Serial.println("Poured water at angle " + anglePoured);
        // Make sure the servo is in original position
        //waterServo.write(120);
        //delay(1000);
        //for(int i =0; i<=5; i++)
        Fire(50,70,20);
        break;
      case s_openDoor:
        Strobe(0xff, 0x77, 0x00, 10, 100, 1000);
        break;
      default:
        Fire(20,100,40);
      delay(700);
  }
  waterServo.write(0);
}

void Fire(int Cooling, int Sparking, int SpeedDelay) {
  static byte heat[NUM_LEDS];
  int cooldown;
  
  // Step 1.  Cool down every cell a little
  for( int i = 0; i < NUM_LEDS; i++) {
    cooldown = random(0, ((Cooling * 10) / NUM_LEDS) + 2);
    
    if(cooldown>heat[i]) {
      heat[i]=0;
    } else {
      heat[i]=heat[i]-cooldown;
    }
  }
  
  // Step 2.  Heat from each cell drifts 'up' and diffuses a little
  for( int k= NUM_LEDS - 1; k >= 2; k--) {
    heat[k] = (heat[k - 1] + heat[k - 2] + heat[k - 2]) / 3;
  }
    
  // Step 3.  Randomly ignite new 'sparks' near the bottom
  if( random(255) < Sparking ) {
    int y = random(7);
    heat[y] = heat[y] + random(160,255);
    //heat[y] = random(160,255);
  }

  // Step 4.  Convert heat to LED colors
  for( int j = 0; j < NUM_LEDS; j++) {
    setPixelHeatColor(j, heat[j] );
  }

  showStrip();
  delay(SpeedDelay);
}

void setPixelHeatColor (int Pixel, byte temperature) {
  // Scale 'heat' down from 0-255 to 0-191
  byte t192 = round((temperature/255.0)*191);
 
  // calculate ramp up from
  byte heatramp = t192 & 0x3F; // 0..63
  heatramp <<= 2; // scale up to 0..252
 
  // figure out which third of the spectrum we're in:
  if( t192 > 0x80) {                     // hottest
    setPixel(Pixel, 255, 255, heatramp);
  } else if( t192 > 0x40 ) {             // middle
    setPixel(Pixel, 255, heatramp, 0);
  } else {                               // coolest
    setPixel(Pixel, heatramp, 0, 0);
  }
}

void Fade(byte red, byte green, byte blue){
  float r, g, b;
//fade in:
  for(int k = 0; k < 256; k=k+2) { 
    r = (k/256.0)*red;
    g = (k/256.0)*green;
    b = (k/256.0)*blue;
    setAll(r,g,b);
    showStrip();
    delay(15);
  }
  
//fade out:
  for(int k = 255; k >= 0; k=k-2) {
    r = (k/256.0)*red;
    g = (k/256.0)*green;
    b = (k/256.0)*blue;
    setAll(r,g,b);
    showStrip();
    delay(15);
  }
}


void Strobe(byte red, byte green, byte blue, int StrobeCount, int FlashDelay, int EndPause){
  for(int j = 0; j < StrobeCount; j++) {
    setAll(red,green,blue);
    showStrip();
    delay(FlashDelay);
    setAll(0,0,0);
    showStrip();
    delay(FlashDelay);
  }
 
 delay(EndPause);
}

void showStrip() {
 #ifdef ADAFRUIT_NEOPIXEL_H 
   // NeoPixel
   strip.show();
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H
   // FastLED
   FastLED.show();
 #endif
}

void setPixel(int Pixel, byte red, byte green, byte blue) {
 #ifdef ADAFRUIT_NEOPIXEL_H 
   // NeoPixel
   strip.setPixelColor(Pixel, strip.Color(red, green, blue));
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H 
   // FastLED
   leds[Pixel].r = red;
   leds[Pixel].g = green;
   leds[Pixel].b = blue;
 #endif
}

void setAll(byte red, byte green, byte blue) {
  for(int i = 0; i < NUM_LEDS; i++ ) {
    setPixel(i, red, green, blue); 
  }
  showStrip();
}


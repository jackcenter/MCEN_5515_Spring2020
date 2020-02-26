
#include <LiquidCrystal.h>
#include <Wire.h>

#define LED_PIN 13
boolean ledon = HIGH;
// initialize the library with the numbers of the interface pins
//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

byte slave_address = 7;
byte CMD_ON = 0x00;
byte CMD_OFF = 0x01;

void setup() {
//   set up the LCD's number of columns and rows:
//  lcd.begin(16, 2);
//   Print startup message to the LCD.
//  lcd.print("Arduino Uno");
  Serial.begin(9600);
  Serial.println("Hello Pi!");
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  
  Wire.begin(slave_address);
  Wire.onReceive(receiveEvent);
}

void loop() {

}

void receiveEvent(int howMany) {
//  lcd.clear();
  
  int numOfBytes = Wire.available();
  //display number of bytes and cmd received, as bytes
//  lcd.setCursor(0, 0);

  Serial.print("len:");
  Serial.println(numOfBytes);
//  lcd.print(" ");
  
  byte cmd = Wire.read();  //cmd
  Serial.print("cmd:");
  Serial.println(cmd);

//  lcd.print(" ");

  if (cmd == CMD_ON){
    digitalWrite(LED_PIN, HIGH);
  }else if(cmd == CMD_OFF){
    digitalWrite(LED_PIN, LOW);
  
  //display message received, as char
//  lcd.setCursor(0, 1);
  for(int i=0; i<numOfBytes-1; i++){
    char data = Wire.read();
    Serial.print(data);
  }
  
//  toggleLED();
}

//void toggleLED(){
//  ledon = !ledon;
//  if(ledon){
//    digitalWrite(LED_PIN, HIGH);
//  }else{
//    digitalWrite(LED_PIN, LOW);
//  }
}

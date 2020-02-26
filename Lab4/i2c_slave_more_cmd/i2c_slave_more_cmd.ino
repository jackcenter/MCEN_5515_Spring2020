#include <Wire.h>

#define LED_PIN 13
boolean ledon = HIGH;
byte slave_address = 7;
byte CMD_ON = 0x00;
byte CMD_OFF = 0x01;

void setup() {
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
  int numOfBytes = Wire.available();

  Serial.print("len:");
  Serial.println(numOfBytes);
  
  byte cmd = Wire.read();  //cmd
  Serial.print("cmd:");
  Serial.println(cmd);

  if (cmd == CMD_ON){
    digitalWrite(LED_PIN, HIGH);
  }else if(cmd == CMD_OFF){
    digitalWrite(LED_PIN, LOW);

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

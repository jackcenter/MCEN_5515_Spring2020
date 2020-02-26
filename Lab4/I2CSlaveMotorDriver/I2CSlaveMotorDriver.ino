#include <Encoder.h>
#include <SparkFun_TB6612.h>
#include <Wire.h>

#define AIN1 12
#define BIN1 7
#define AIN2 4
#define BIN2 8
#define PWMA 5
#define PWMB 6
#define STBY 9
#define ENC1A 2
#define ENC1B 10 
#define ENC2A 3
#define ENC2B 13

const int offsetA = -1;
const int offsetB = 1;
const double radius = 2;    // radius of the wheel in inches
const double axel = 10;
const int cpr = 8400;
const int res = 10;

Motor motor1 = Motor(AIN1, AIN2, PWMA, offsetA, STBY);
Motor motor2 = Motor(BIN1, BIN2, PWMB, offsetB, STBY);

Encoder encLeft(ENC1A, ENC1B);
Encoder encRight(ENC2A, ENC2B);

byte slave_address = 7;
byte CMD_ON = 0x00;
byte CMD_OFF = 0x01;

void setup() {
  // Start I2C Bus as Slave
  Wire.begin(slave_address);
  Wire.onReceive(receiveEvent);
  
  Serial.begin(9600);
  Serial.println("Encoder Test:");
}

long positionLeft = -999;
long positionRight = -999;

void loop() {

}
void receiveEvent(int howMany) {
  byte cmd = Wire.read();
  if (cmd == CMD_ON){
    forward(6);
  }else if(cmd == CMD_OFF){
    turnLeft(30);
  }
}

void forward(int dist)
{
  long rotations = dist/(2*PI*radius);
  long LeftFinalPos = positionLeft + rotations*res;
  long RightFinalPos = positionRight + rotations*res;

  motor1.drive(255);
  motor2.drive(255);
  while (positionLeft < LeftFinalPos || positionRight < RightFinalPos)
  {
    positionLeft = -encLeft.read()/(cpr/res);  
    positionRight = encRight.read()/(cpr/res); 

    if (positionLeft >= LeftFinalPos){
        motor1.brake();
    }

    if (positionRight >= RightFinalPos){
        motor2.brake();
    }       
  }
}

void reverse(int dist)
{
  long rotations = dist/(2*PI*radius);
  long LeftFinalPos = positionLeft - rotations*res;
  long RightFinalPos = positionRight - rotations*res;

  motor1.drive(-255);
  motor2.drive(-255);
  
  while (positionLeft > LeftFinalPos || positionRight > RightFinalPos)
  {
    positionLeft = -encLeft.read()/(cpr/res);  
    positionRight = encRight.read()/(cpr/res); 

    if (positionLeft <= LeftFinalPos){
        motor1.brake();
    }

    if (positionRight <= RightFinalPos){
        motor2.brake();
    }       
  }
}

void turnLeft(int deg)
{ 
  int steps = axel/radius/720*deg*res;
  long LeftFinalPos = positionLeft + steps;
  long RightFinalPos = positionRight - steps;
  motor1.drive(255);
  motor2.drive(-255);

  while (positionLeft < LeftFinalPos || positionRight > RightFinalPos)
  {
    positionLeft = -encLeft.read()/(cpr/res);  
    positionRight = encRight.read()/(cpr/res); 

    if (positionLeft >= LeftFinalPos){
        motor1.brake();
    }

    if (positionRight <= RightFinalPos){
        motor2.brake();
    }       
  }
}

void turnRight(int deg)
{
  int steps = axel/radius/720*deg*res;
  long LeftFinalPos = positionLeft - steps;
  long RightFinalPos = positionRight + steps;
  
  motor1.drive(-255);
  motor2.drive(255);

  while (positionLeft > LeftFinalPos || positionRight < RightFinalPos)
  {
    positionLeft = -encLeft.read()/(cpr/res);  
    positionRight = encRight.read()/(cpr/res); 

    if (positionLeft <= LeftFinalPos){
        motor1.brake();
    }

    if (positionRight >= RightFinalPos){
        motor2.brake();
    }       
  }
}

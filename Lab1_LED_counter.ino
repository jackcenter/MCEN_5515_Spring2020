const int counterButtonPin = 2;
const int resetButtonPin = 11;

int leds[] = {3, 4, 5, 6, 7, 8, 9, 10};
int numberOfLeds = 8;

unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers

int count = 0;
int lastCounterButtonState = LOW;
int lastResetButtonState = LOW;

void setup() {
  Serial.begin(9600);

  // Initialize the pins
  for(byte i = 0; i < numberOfLeds; ++i)
  {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  pinMode(counterButtonPin, INPUT);
  pinMode(resetButtonPin, INPUT);
}

void loop() {
  int counterReading = digitalRead(counterButtonPin); 
  int resetReading = digitalRead(resetButtonPin);

  if (counterReading != lastCounterButtonState){
    if (counterReading == HIGH) 
    {  
      count = countIncrement(count);
    }
    delay(50);  // debounce 
  }
  lastCounterButtonState = counterReading;

  if (resetReading != lastResetButtonState){
    if (resetReading == HIGH) 
    {  
      count = turnOffLeds();
    }
    delay(50); 
  }
  lastResetButtonState = counterReading;
 
}

int countIncrement(int count)
{
  if (count == 8)
  {
    count = turnOffLeds();
  }

  else
  {
    digitalWrite(leds[count++], HIGH);
  }

  return count;
}

int turnOffLeds()
{
  for(byte i = 0; i < numberOfLeds; ++i)
  {
    digitalWrite(leds[i], LOW);
  }
  
  return 0;
}

import RPi.GPIO as GPIO
from time import process_time, sleep

GPIO.setmode(GPIO.BCM)

green_pin = 21
but_pin = 23

GPIO.setup(green_pin, GPIO.OUT)
GPIO.output(green_pin, False)
GPIO.setup(but_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(23, GPIO.RISING, bouncetime=200)

while True:

    GPIO.output(green_pin, True)

    if GPIO.event_detected(23):
        break

GPIO.output(green_pin, False)
GPIO.cleanup()

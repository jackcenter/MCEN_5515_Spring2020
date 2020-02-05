import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#initialize pwm


def printFunction(channel):
	print("Button 1 pressed")

GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=300)


while True:
	GPIO.output(18, False)
	"""
	GPIO.wait_for_edge(23, GPIO.RISING)
	print("Button 1 pressed")

	GPIO.wait_for_edge(23, GPIO.FALLING)
	print("Button 1 released")
	"""

GPIO.cleanup()
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

current_state = False
#


def button_press():
    print("Button 1 pressed")
    return True
    # stop the light and keep it lit


def button_release():
    print("Button 1 released")
    return False
    # flash the light a few times
    # restart the game


GPIO.add_event_detect(23, GPIO.BOTH, bouncetime=50)

game_count = 0
while game_count < 3:
    pressed = False

    while not pressed:
        GPIO.output(18, False)
        # TODO: make lights flash

        if GPIO.event_detected(23) and not current_state:
            current_state = button_press()

        elif GPIO.event_detected(23) and current_state:
            current_state = button_release()

    game_count += 1

GPIO.cleanup()

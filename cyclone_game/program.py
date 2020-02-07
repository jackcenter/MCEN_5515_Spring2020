import RPi.GPIO as GPIO
from time import process_time, sleep

GPIO.setmode(GPIO.BCM)

led_pins = [18, 19, 20, 21, 24, 26, 27]
but_pin = 23

GPIO.setup(led_pins, GPIO.OUT)
GPIO.output(led_pins, False)
GPIO.setup(but_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

current_state = False


def button_press():
    print("Button 1 pressed")
    return True
    # stop the light and keep it lit


def button_release():
    print("Button 1 released")
    return False
    # flash the light a few times
    # restart the game


# def whatIsHappening(channel):
#     if GPIO.input(channel) == 1:
#         print("rising?")
#         time.sleep(3)
#     else:
#         print("falling?")


GPIO.add_event_detect(23, GPIO.BOTH, bouncetime=100)

game = True
wait_time = .1

while game:

    for pin in led_pins:
        GPIO.output(pin, True)

        time_start = process_time()
        time_now = time_start
        while time_now - time_start < wait_time:
            time_now = process_time()

            if GPIO.event_detected(23):
                sleep(2)
                game = False

                # if GPIO.input(23) == 1:
                #     print("rising?")
                #     pressed = True
                #     break
                # else:
                #     print("falling?")
        if not game:
            break

        GPIO.output(pin, False)

GPIO.cleanup()

import RPi.GPIO as GPIO
from time import process_time, sleep


def main():
    led_pins = [18, 19, 20, 21, 24, 26, 27]
    win_pin = 21
    but_pin = 23
    wait_time = .1

    setup(led_pins, but_pin)
    GPIO.add_event_detect(23, GPIO.RISING, bouncetime=200)

    game_on = True

    while game_on:
        for pin in led_pins:
            GPIO.output(pin, True)

            # Keep led on for a bit while waiting for a detect ======================================================
            time_start = process_time()
            time_now = time_start
            while time_now - time_start < wait_time:
                time_now = process_time()

                if GPIO.event_detected(23):
                    sleep(2)                # glow the selected pin

                    if pin == win_pin:      # right pin!
                        game_on = False
                        flash_pin(win_pin)
                        break

            if not game_on:
                break

            GPIO.output(pin, False)
    GPIO.cleanup()


def setup(led_pins, but_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pins, GPIO.OUT)
    GPIO.output(led_pins, False)
    GPIO.setup(but_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def flash_pin(pin):
    for i in range(0, 3):
        GPIO.output(pin, True)
        sleep(.5)
        GPIO.output(pin, False)
        sleep(.5)


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


if __name__=="__main__":
    main()

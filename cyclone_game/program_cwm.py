# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:52:33 2020

@author: chadd
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pins = [18, 19, 20, 21, 24, 26, 27]
but_pin = 23

GPIO.setup(led_pins, GPIO.OUT)
GPIO.output(led_pins, False)
GPIO.setup(but_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


run = True

while run == True:
    for pin in led_pins:
        GPIO.output(pin, True)
        
        #delay and check button press function
            #break if you detect a button press
            
    GPIO.output(pin,True)
    time.sleep(0.4)                
    GPIO.output(pin, False)
    time.sleep(0.4)
    GPIO.output(pin,True)
    time.sleep(0.4)
    GPIO.output(pin, False)
    time.sleep(0.4)
    GPIO.output(pin,True)
    time.sleep(0.4)
    
    # same delay and check button press function while waiting for like 3 seconds
        # run == False if button press




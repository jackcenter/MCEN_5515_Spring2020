# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:23:29 2020

@author: chadd
"""

# File: threaded_videostream_demo.py

import time
import RPi.GPIO as GPIO

import cv2
import numpy as np
from imutils.video import VideoStream
import imutils

GPIO.setmode(GPIO.BCM)
push_pin = 17
GPIO.setup(push_pin, GPIO.OUT)
GPIO.output(push_pin, False)

# Are we using the Pi Camera?
usingPiCamera = True
# Set initial frame size.
frameSize = (320, 240)

# Initialize mutithreading the video stream.
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
                 framerate=32).start()
# Allow the camera to warm up.
time.sleep(2.0)

timeCheck = time.time()
while True:
    # Get the next frame.
    frame = vs.read()

    # If using a webcam instead of the Pi Camera,
    # we take the extra step to change frame size.
    if not usingPiCamera:
        frame = imutils.resize(frame, width=frameSize[0])

    # Show video stream
    # cv2.imshow('orig', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 10, 200])
    upper_green = np.array([120, 245, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    # for x in mask:
    mask_summed = [sum(x) for x in mask]
    light_reading = sum(mask_summed)
    # print(light_reading)
    # print("hi chadd")
    
    if light_reading > 2500:
        GPIO.output(push_pin, True)
        time.sleep(1)
        GPIO.output(push_pin, False)
        
    
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('mask', mask)
    # cv2.imshow('result', result)

    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop.
    if key == ord("q"):
        break

    # print(1 / (time.time() - timeCheck))
    timeCheck = time.time()

# Cleanup before exit.
cv2.destroyAllWindows()
vs.stop()
GPIO.cleanup()

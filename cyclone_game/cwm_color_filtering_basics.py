# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:45:59 2020

@author: chadd
"""

import cv2
import numpy as np



while True:
    # frame = Jack gets
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([0,0,0])
    upper_green = np.array([255,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res =  cv2.bitwise_and(frame, frame, mask = mask)
    
    
    
    
cv2.destroyAllWindows()

    
    
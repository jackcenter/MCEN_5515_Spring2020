# import the necessary packages
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
## rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera

cap = cv2.VideoCapture(0)
while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(np.float32(frame), cv2.COLOR_BGR2HSV)

	lower_green = np.array([0, 0, 0])
	upper_green = np.array([255, 255, 255])

	mask = cv2.inRange(hsv, lower_green, upper_green)
	result = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', result)

	if mask:
		print("GREEN!!!!")

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

cv2.destroyAllWindows()
cap.release()

# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
# 	# grab the raw NumPy array representing the image, then initialize the timestamp
# 	# and occupied/unoccupied text
# 	hsv = cv2.cvtColor(np.float32(frame), cv2.COLOR_BGR2HSV)
#
# 	lower_green = np.array([0, 0, 0])
# 	upper_green = np.array([255, 255, 255])
#
# 	mask = cv2.inRange(hsv, lower_green, upper_green)
# 	result = cv2.bitwise_and(frame, frame, mask=mask)
#
# 	if mask:
# 		print("GREEN!!!!")
#
# 	image = frame.array
# 	# show the frame
# 	cv2.imshow("Frame", image)
# 	key = cv2.waitKey(1) & 0xFF
# 	# clear the stream in preparation for the next frame
# 	rawCapture.truncate(0)
# 	# if the `q` key was pressed, break from the loop
# 	if key == ord("q"):
# 		break
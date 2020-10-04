# This program uses the OpenCV library to read & display the image on the screen.
import cv2

img = cv2.imread('profile.png')

gray = cv2.imread('profile.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('pf-pic',img)

cv2.imshow('pf-pic-gray',gray)

cv2.waitKey(0)

# THe window isn't being destroyed

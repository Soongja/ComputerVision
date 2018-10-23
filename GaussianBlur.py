import cv2
import numpy as np


def onMouse(x):
    pass


img = cv2.imread('saeron.jpg')

cv2.namedWindow('GaussianBlur')
cv2.createTrackbar('Blur', 'GaussianBlur', 0, 5, onMouse)

val = cv2.getTrackbarPos('Blur', 'GaussianBlur')

while True:
    val = val * 2 + 1

    blur = cv2.GaussianBlur(img, (val, val), 0)

    cv2.imshow('GaussianBlur', blur)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    val = cv2.getTrackbarPos('Blur', 'GaussianBlur')

cv2.destroyAllWindows()
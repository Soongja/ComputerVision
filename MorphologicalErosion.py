import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hand_canny.png', 0)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.dilate(img, kernel, iterations=1)

stack = np.hstack((img, erosion))
cv2.imshow('Morphological Erosion', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/hand_erosion.png', erosion)
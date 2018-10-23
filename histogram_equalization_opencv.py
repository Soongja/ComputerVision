import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('saeron.jpg', 0)

equ = cv2.equalizeHist(img)
stack = np.hstack((img, equ))

cv2.imshow('Histogram Equalization', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
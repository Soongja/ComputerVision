import cv2
import numpy as np
from matplotlib import pyplot as plt

# Opencv는 H W C!!!!
img = cv2.imread('images/hand.png')

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

cv2.imshow('ycrcb', ycrcb[:, :, 2])
cv2.waitKey(0)
cv2.destroyAllWindows()
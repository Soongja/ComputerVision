import cv2
import numpy as np
from matplotlib import pyplot as plt

# Opencv는 H W C!!!!
img = cv2.imread('imageshand.png')

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

np.savetxt('images/cb.txt', ycrcb[:, :, 2], fmt='%d')

cv2.imshow('Y', ycrcb[:, :, 0])
cv2.imshow('Cr', ycrcb[:, :, 1])
cv2.imshow('Cb', ycrcb[:, :, 2])
cv2.waitKey(0)
cv2.destroyAllWindows()
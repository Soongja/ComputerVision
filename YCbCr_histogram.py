import cv2
import numpy as np
from matplotlib import pyplot as plt

# Opencv는 H W C!!!!
img = cv2.imread('images/hand.png')

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([ycrcb], [i], None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

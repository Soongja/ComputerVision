import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('saeron2.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('saeron2.jpg')

# gray
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
plt.plot(hist1)
plt.show()


# gray + color
plt.hist(img1.ravel(), 256, [0, 256])

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

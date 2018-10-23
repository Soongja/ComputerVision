import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('images/hand.png', 0)
img2 = cv2.imread('images/hand.png')

# gray
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
plt.plot(hist1)
plt.show()


# gray + color
# plt에도 hist기능이 있다. 위에꺼와 같지만 색칠이 되어있네.
plt.hist(img1.ravel(), 256, [0, 256])

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    # histSize는 Bin갯수 즉, 가로축. ranges는 픽셀값 범위. 보통[0, 256]
    hist = cv2.calcHist([img2], [i], None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

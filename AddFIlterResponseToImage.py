import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('images/hand.png').astype(np.int32)
img2 = cv2.imread('images/hand_canny.png').astype(np.int32)

added = np.add(img1, img2)

maxed = np.clip(addition, 0, 255).astype(np.uint8)

cv2.imshow('show', maxed)
cv2.waitKey(0)
cv2.destroyAllWindows()
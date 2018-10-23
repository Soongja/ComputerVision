import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('saeron2.jpg')

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img2 = clahe.apply(img)

stack = np.hstack((img, img2))
cv2.imshow('CLAHE', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
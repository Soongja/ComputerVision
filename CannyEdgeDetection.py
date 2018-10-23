import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/hand_clahe.png')

edges = cv2.Canny(img, 100, 200, L2gradient=True)

# stack = np.hstack((img, edges))
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/hand_canny.png', edges)
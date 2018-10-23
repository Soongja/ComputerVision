import cv2
import numpy as np
from matplotlib import pyplot as plt

bgr = cv2.imread('saeron2.jpg')

lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
lab_planes = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)

bgr2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

stack = np.hstack((bgr, bgr2))
cv2.imshow('CLAHE color', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
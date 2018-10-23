import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('saeron2.jpg', 0)

hist, bins = np.histogram(img.ravel(), 256, [0, 256])
cdf = hist.cumsum()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m-cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

img2 = cdf[img]

stack = np.hstack((img, img2))
cv2.imshow('Histogram Equalization', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
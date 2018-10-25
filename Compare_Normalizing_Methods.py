import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.expand_dims(cv2.imread('hand.png', 0), axis=2)
scale = np.multiply(img, 1.0/255)
norm = (img - np.min(img))/(np.max(img)-np.min(img))
stand = (img - np.mean(img))/np.std(img)

plt.hist(img.ravel(), 256, [0, 256])
plt.show()
plt.hist(scale.ravel(), 256, [0, 1])
plt.show()
plt.hist(norm.ravel(), 256, [0, 1])
plt.show()
plt.hist(stand.ravel(), 256, [-2.5, 2.5])
plt.show()

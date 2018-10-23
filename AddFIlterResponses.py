import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = np.array(cv2.imread('images/hand_canny.png', 0), dtype=np.uint8)
img2 = np.array(cv2.imread('images/hand_erosion.png', 0), dtype=np.uint8)

lst = []

white = np.logical_and(img1, img2)
for i in range(white.shape[0]):
    for j in range(white.shape[1]):
        if white[i, j] == True:
            lst.append((i, j))
print(lst)
print(len(lst))
# np.savetxt('images/white.txt', white, fmt='%d')

addition = np.add(img1, img2)
np.savetxt('images/addition.txt', addition, fmt='%d')
print(addition[0, 288])

val = np.full(addition.shape, 255)

# print(addition)
# print(val)
import cv2
import numpy as np
from matplotlib import pyplot as plt

skin_ycrcb_min = np.array([0, 133, 77])
skin_ycrcb_max = np.array((255, 173, 127))
# ycrcb 중 각 채널의 range가 어떻게 되는지 찾기!

img = cv2.imread('images/hand_filter_added.png')
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

mask = cv2.inRange(ycrcb, skin_ycrcb_min, skin_ycrcb_max)

_, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, 2)
# 이거 두번째 세번째 argument 공부

areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

cv2.drawContours(img, cnt, -1, (0,255,0), 3)

# cv2.imshow('ycrcb0', ycrcb[:, :, 0])
# cv2.imshow('ycrcb1', ycrcb[:, :, 1])
cv2.imshow('show', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
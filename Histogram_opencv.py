import cv2
import numpy as np

img = cv2.imread('images/hand.png')
h = np.zeros((256, 256, 3))

bins = np.arange(256).reshape(256,1) # [[0], [1], [2], ..., [255]]
colors = [(255,0,0),(0,255,0),(0,0,255)]

for ch, color in enumerate(colors):
    hist_item = cv2.calcHist([img],[ch],None,[256],[0,255])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX) # normalization
    hist=np.int32(np.around(hist_item)) # np.around는 원하는 자릿수로 반올림
    pts = np.column_stack((bins,hist)) # [[0, 105], [1, 219], [2, 351]] 이런식으로 stack
    print(pts)
    print(pts.shape)
    cv2.polylines(h,[pts],False,color) # isClosed argument가 False인건데 true로 하면 마지막이랑 처음 연결됨.

h=np.flipud(h)

cv2.imshow('colorhist',h)
cv2.waitKey(0)

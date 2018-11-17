import numpy as np
import cv2
import matplotlib.pyplot as plt

#set the rockwall to img
img = cv2.imread('IMG_20181117_185058.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv_red_high = np.asarray([245,255,255])
hsv_red_low = np.asarray([0,155,155])

mask = cv2.inRange(img_hsv,hsv_red_low,hsv_red_high)

plt.imshow(mask,cmap='gray')
plt.show()

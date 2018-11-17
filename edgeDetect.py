import numpy as np
import cv4
import matplotlib.pyplot as plt

#set the rockwall to img
img = cv2.imread('rockWallExample.jpg')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv_red = np.asarray([255,0,0])
hsv_pink = np.asarray([240,128,128])

mask = cv2.inRange(img_hsv,hsv_pink,hsv_red)

plt.imshow(mask,cmap='gray')
plt.show()

import numpy as np
import cv2
import matplotlib.pyplot as plt

#set the rockwall to img
img = cv2.imread('rockWallExample.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv_green_high = np.asarray([27,95,79])
hsv_green_low = np.asarray([159,226,224])

mask = cv2.inRange(img_hsv,hsv_green_high,hsv_green_low)

blur = cv2.blur(mask,(7,7))
plt.imshow(blur, cmap='gray')
plt.show()

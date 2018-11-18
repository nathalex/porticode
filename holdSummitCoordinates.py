import numpy as np
import cv2
import matplotlib.pyplot as plt

#set the rockwall to img
img = cv2.imread('rockWallExample.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv_green_high = np.asarray([27,95,79])
hsv_green_low = np.asarray([159,226,224])

#blurs the holds so they become whole blobs
mask = cv2.inRange(img_hsv,hsv_green_high,hsv_green_low)
#plt.imshow(mask, cmap='gray')
blur = cv2.blur(mask,(15,15))
#plt.imshow(blur, cmap='gray')
#sets back to binary so the contour can find the edges
ret,BWblur = cv2.threshold(blur,5,255,cv2.THRESH_BINARY)
plt.imshow(BWblur, cmap='gray')
#contours the edges
im2, contours, hierarchy = cv2.findContours(BWblur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
BWblur = cv2.cvtColor(BWblur, cv2.COLOR_GRAY2BGR)
BWblur = cv2.cvtColor(BWblur, cv2.COLOR_BGR2HSV)
coordinates = []
for c in contours:
    #finds the coordinates summit of the contour of the hold
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    print(extTop)
    coordinates.append(extTop)
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri,True)
    cv2.drawContours(BWblur, [approx], -1, (0,255,0), 3)
    cv2.circle(BWblur, extTop, 8, (255, 0, 0), -1)
cv2.imshow("hey",BWblur)
print(coordinates)
plt.show()

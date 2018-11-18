import numpy as np
import cv2
import csv
import matplotlib.pyplot as plt
import climberInputs

#set the rockwall to img
img = cv2.imread('rockWallExample.jpg')
if climberInputs.color == "green":
    color_high = np.asarray([60,160,60])
    color_low = np.asarray([185,255,185])
elif climberInputs.color == "red":
    color_high = np.asarray([57,50,140])
    color_low = np.asarray([107,100,255])

mask = cv2.inRange(img,color_high,color_low)
mask = cv2.medianBlur(mask,5)
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
    coordMax = tuple(climberInputs.scale*c[c[:, :, 1].argmin()][0])
    coordinates.append(coordMax)
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*peri,True)
    cv2.drawContours(BWblur, [approx], -1, (0,255,0), 3)
    cv2.circle(BWblur, extTop, 8, (255, 0, 0), -1)
cv2.imshow("hey",BWblur)
print(coordinates)
with open('coordinatesList.csv', mode='w') as coordinatesList:
    coordinatesList = csv.writer(coordinatesList, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    coordinatesList.writerow((len(coordinates),0))
    for i in range(0,len(coordinates)):
        coordinatesList.writerow(coordinates[i])
plt.show()

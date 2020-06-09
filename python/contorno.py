# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:49:52 2020

@author: rafae
"""

import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt




imA=cv2.imread("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo\\E1_B_1")
imA = imA[110:3000, 450:3025] #Cropping image 
lower_green = np.array([50,50,50])
upper_green = np.array([255,255,255])
hsv_imgA = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)
image = cv2.inRange(hsv_imgA, lower_green, upper_green)
image = np.invert(image)

thresh = cv2.threshold(image, 45, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 50, (100, 10, 55), -1)
cv2.circle(image, extRight, 50, (100, 10, 55), -1)
cv2.circle(image, extTop, 50, (100, 10, 55), -1)
cv2.circle(image, extBot, 50, (100, 10, 55), -1)


plt.imshow(image2)

cv2.imshow('image', image)
cv2.waitKey()

image2=image[1:1000,1:1000]
count = (image2 == 255).sum()
count

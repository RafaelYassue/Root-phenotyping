# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:54:35 2020

Calculating number of pixels for hull convex area  and extremes points

@author: Rafael Yassue
"""


import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt
import os as os 
from skimage.morphology import convex_hull_image
import pandas as pd
import math



# Fuction to obtain angle
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang


os.chdir("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo")  
img_list = os.listdir()
img_list = [v for v in img_list if v.endswith('.jpeg') and not v.endswith('mask.jpg')]
i=1

HULL = [] #saving number of pixer for Hull convex area
trat = [] #saving treatment 
Left = [] # Salving extremes points 
Right = []
Top = []
Bot = []
for i in range(len(img_list)):
    a = cv2.imread(img_list[i])
    imA = a[100:3000, 600:3025] #Cropping image 
    lower_green = np.array([50,50,50])
    upper_green = np.array([255,255,255])
    hsv_imgA = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)
    image = cv2.inRange(hsv_imgA, lower_green, upper_green)
    image=np.invert(image)
    chull = convex_hull_image(image)
    HULL.append((chull == True).sum()) #Obtain HULL convex area
    trat.append(img_list[i])
    cnts = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    Left.append(tuple(c[c[:, :, 0].argmin()][0])) #obtain extreme points 
    Right.append(tuple(c[c[:, :, 0].argmax()][0]))
    Top.append(tuple(c[c[:, :, 1].argmin()][0]))
    Bot.append(tuple(c[c[:, :, 1].argmax()][0]))
    print(i)

### Obtain angle
i=2
for i in range(len(img_list[1:10])):
    print(getAngle(Left[i], Top[i],Right[i] ))

for i in range(len(img_list[1:10])):
    print(getAngle(Right[i], Left[i], Top[i]))

for i in range(len(img_list[1:10])):
    print(getAngle(Left[i],Right[i], Top[i], ))

for i in range(len(img_list[1:10])):
    print(getAngle(Top[i],Right[i], Left[i]))

for i in range(len(img_list[1:10])):
    print(getAngle(Right[i],Top[i],Left[i]))

for i in range(len(img_list[1:10])):
    print(getAngle(Top[i],Left[i],Right[i] ))









#Salving results
HULLConvexArea = pd.DataFrame({'Area':HULL} ,trat)


                                
                    
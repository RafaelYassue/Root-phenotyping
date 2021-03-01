# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:09:55 2020

Calculating roots angle from images

@author: Rafael Massahiro Yassue
"""

import cv2
import numpy as np
import imutils
import os as os 
import pandas as pd
import math

os.chdir("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo")  
img_list = os.listdir()
img_list = [v for v in img_list if v.endswith('.jpeg') and not v.endswith('mask.jpg')]

## Function to obtain angles
def getAngle(Top, Left, Right):
    a=math.sqrt((Top[1]-Left[1])**2 +(Left[0]-Top[0])**2) 
    c=math.sqrt((Left[1]-Right[1])**2 +(Right[0]-Left[0])**2) 
    b=math.sqrt((Top[1]-Right[1])**2 +(Right[0]-Top[0])**2) 
    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))

trat = [] 
Left = [] 
Right = []
Top = []
Bot = []
Angle=[]

for i in range(len(img_list)):
    a = cv2.imread(img_list[i])
    imA = a[100:3000, 600:3025] #Cropping image 
    lower_green = np.array([50,50,50])
    upper_green = np.array([255,255,255])
    hsv_imgA = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)
    image = cv2.inRange(hsv_imgA, lower_green, upper_green)
    image=np.invert(image)
    trat.append(img_list[i])
    cnts = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    Left.append(tuple(c[c[:, :, 0].argmin()][0])) #obtain extreme points 
    Right.append(tuple(c[c[:, :, 0].argmax()][0]))
    Top.append(tuple(c[c[:, :, 1].argmin()][0]))
    Bot.append(tuple(c[c[:, :, 1].argmax()][0]))
    Angle.append(getAngle(Top[i], Left[i],Right[i]))
    cv2.circle(imA, (tuple(c[c[:, :, 0].argmin()][0])), 50, (100, 10, 55), -1)
    cv2.circle(imA, (tuple(c[c[:, :, 0].argmax()][0])), 50, (100, 10, 55), -1)
    cv2.circle(imA, (tuple(c[c[:, :, 1].argmin()][0])), 50, (100, 10, 55), -1)   
    plt.imshow(imA, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis('off')
    plt.savefig(img_list[i][:-5]+"hull.jpg", dpi=300)
    plt.show()

    print(i)


Angle_data = pd.DataFrame({'Angle_all':Angle, 'Angle_10': Angle10} ,trat)





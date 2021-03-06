# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:54:35 2020

Calculating number of pixels for hull convex area 

@author: Rafael Yassue
"""


import cv2
import numpy as np
import os as os 
from skimage.morphology import convex_hull_image
import pandas as pd
import matplotlib.pyplot as plt




os.chdir("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo")  
img_list = os.listdir()
img_list = [v for v in img_list if v.endswith('.jpeg') and not v.endswith('mask.jpg')]
i=1

HULL = [] 
trat = [] 
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
    print(i)



HULLConvexArea = pd.DataFrame({'Area':HULL, 'Area_10':HULL} ,trat)

                    

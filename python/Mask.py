# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:39:03 2020

Applyng mask and hull convex area 

@author: Rafael Yassue


"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os as os 
from skimage.morphology import convex_hull_image



os.chdir("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo")  
img_list = os.listdir()
###Rename files 
#for i in range(len(img_list)):
#  os.rename(img_list[i], img_list[i]+".jpeg")
  
##########################
imgs = sorted(os.listdir())
img_list = [v for v in img_list if v.endswith('.jpeg') and not v.endswith('mask.jpg')]

for i in range(len(img_list)):
    a = cv2.imread(img_list[i])
    imA = a[100:3000, 600:3025] #Cropping image 
    lower_green = np.array([50,50,50])
    upper_green = np.array([255,255,255])
    hsv_imgA = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)
    image = cv2.inRange(hsv_imgA, lower_green, upper_green)
    image=np.invert(image)
    chull = convex_hull_image(image)
    plt.imshow(image)
    plt.savefig(img_list[i][:-5]+"mask.jpg")
    plt.imshow(chull, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis('off')
    plt.savefig(img_list[i][:-5]+"hull.jpg", dpi=300)
    plt.show()


    
    
    

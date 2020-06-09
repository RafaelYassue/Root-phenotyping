# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:13:44 2020

@author: rafae
"""


######################################
# -*- coding: utf-8 -*-
#####################################
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import convex_hull_image
import cv2
import os as os
#


im_dir = ("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo")  
os.chdir(im_dir)
imgs = sorted(os.listdir(im_dir))

i = 2

names = []
for i in range(len(imgs)):
    names.append(imgs[i]+"_mask"+".jpeg")


for i in range(len(imgs)):
    a = cv2.imread(imgs[i])
    imA = a[110:3000, 450:3025] #Cropping image 
    lower_green = np.array([50,50,50])
    upper_green = np.array([255,255,255])
    hsv_imgA = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)
    image = cv2.inRange(hsv_imgA, lower_green, upper_green)
    image=np.invert(image)
    chull = convex_hull_image(image)
    img=plt.imshow(chull, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis('off')
    plt.savefig(names[i], dpi=300)
    plt.show()
















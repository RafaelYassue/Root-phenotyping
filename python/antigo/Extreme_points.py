
import cv2
import os as os
import numpy as np
import pandas as pd


os.chdir(("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo\\mask"))

imgs = sorted(os.listdir())

img = cv2.imread(imgs[2])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]
sz=thresh.shape
top=divmod(np.flatnonzero(thresh)[0], sz[0])[::-1]
botton=divmod(np.flatnonzero(thresh)[-1], sz[0])[::-1]
thresh=thresh.T
left=divmod(np.flatnonzero(thresh)[0], sz[1])
right=divmod(np.flatnonzero(thresh)[-1], sz[1])
print(left, right, top, botton, sep='\n')



cv2.imshow('teste',img)
cv2.waitKey (0)
cv2.destroyAllWindows()



trat = []
top = []
bottom = []
right = []
left = []
i = 0
for i in range(len(imgs)): #add 5 rows of data
    img = cv2.imread(imgs[i])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]
    sz=thresh.shape
    thresh=thresh.T
    trat.append(imgs[i])
    top.append(divmod(np.flatnonzero(thresh)[0], sz[0])[::-1])
    bottom.append(divmod(np.flatnonzero(thresh)[-1], sz[0])[::-1])
    left.append(divmod(np.flatnonzero(thresh)[0], sz[1]))
    right.append(divmod(np.flatnonzero(thresh)[-1], sz[1]))
import cv2
import os as os
import numpy as np


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
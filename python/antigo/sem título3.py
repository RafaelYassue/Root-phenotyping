#Calculing HULL area
import cv2
import numpy as np

imA=cv2.imread("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo\\E1_B_1")
imA = imA[110:3000, 450:3025] #Cropping image 


mask=cv2.imread("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\certo\\mask\\E1_B_4_mask.jpeg")


lower_green = np.array([50,50,50])
upper_green = np.array([255,255,255])
hsv_imgA = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
image = cv2.inRange(hsv_imgA, lower_green, upper_green)




contours = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.drawContours(imA, contours, -1, (0, 200, 0), 3)

cnts = cv2.findContours(imA, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
c = max(cnts, key=cv2.contourArea)





cv2.imshow('img', imA)
cv2.waitKey()

lower_green = np.array([50,50,50])
upper_green = np.array([255,255,255])
hsv_imgA = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)
image = cv2.inRange(hsv_imgA, lower_green, upper_green)



cv2.imshow('image', image)
cv2.waitKey()





contours=ResizeWithAspectRatio(contours, 500)


image=ResizeWithAspectRatio(image, 500)
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
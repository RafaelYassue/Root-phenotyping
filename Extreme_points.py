import cv2



img = cv2.imread("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\DSCN8473.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contours = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.drawContours(img, contours, -1, (0, 200, 0), 3)

cv2.imshow('img', img)
cv2.waitKey()
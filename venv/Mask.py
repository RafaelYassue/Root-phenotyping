
#!/usr/bin/env python
# coding: utf-8

# In[6]:


from PIL import Image
import matplotlib.pyplot as plt
import numpy
import numpy as np
from skimage.morphology import convex_hull_image
from skimage import data, img_as_float
from skimage.util import invert
import cv2
a = cv2.imread("C:\\Users\\rafae\\Desktop\\teste\\DSCN8469.JPG")
b = cv2.imread("C:\\Users\\rafae\\Desktop\\teste\\DSCN8470.JPG")


# In[60]:


#left = 430
#top = 200
#right = 3025
#bottom = 3000
#imA = a.crop((left, top, right, bottom))
#imA.show()
#imB = b.crop((left, top, right, bottom))
#imB.show()


# In[3]:


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


# In[31]:


imA = a[110:3000, 450:3025]
imB = b[110:3000, 450:3025]

resize = ResizeWithAspectRatio(imA, width=1280)
resize2 = ResizeWithAspectRatio(imB, width=1280)

cv2.destroyAllWindows()
cv2.imshow("HSV Image", resize2)
cv2.waitKey()


# In[32]:


lower_green = np.array([50,50,50])
upper_green = np.array([255,255,255])
hsv_img = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)

masking = cv2.inRange(hsv_img, lower_green, upper_green)
masking = ResizeWithAspectRatio(masking, width=1280)

imA=numpy.invert(imA)
imB=numpy.invert(imB)


#cv2.imshow("Original Image", teste)



hsv_imgA = cv2.cvtColor(imA, cv2.COLOR_BGR2HSV)
hsv_imgB = cv2.cvtColor(imB, cv2.COLOR_BGR2HSV)

maskingA = cv2.inRange(hsv_imgA, lower_green, upper_green)
maskingB = cv2.inRange(hsv_imgB, lower_green, upper_green)
cv2.destroyAllWindows()
cv2.waitKey()


# In[ ]:





# In[33]:




# The original image is inverted as the object must be white.
image = maskingA

chull = convex_hull_image(image)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].set_title('Original picture')
ax[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[0].set_axis_off()

ax[1].set_title('Transformed picture')
ax[1].imshow(chull, cmap=plt.cm.gray, interpolation='nearest')
ax[1].set_axis_off()

plt.tight_layout()
plt.show()


# In[34]:




# The original image is inverted as the object must be white.
image = maskingB

chull = convex_hull_image(image)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[0].set_title('Original picture')
ax[0].imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax[0].set_axis_off()

ax[1].set_title('Transformed picture')
ax[1].imshow(chull, cmap=plt.cm.gray, interpolation='nearest')
ax[1].set_axis_off()

plt.tight_layout()
plt.show()


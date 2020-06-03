from pyzbar.pyzbar import decode
from PIL import Image
import os as os 
import cv2 as cv2
################

im_dir = ("C:\\Users\\rafae\\Desktop\\100NIKON - Copy")  
os.chdir(im_dir)
imgs = sorted(os.listdir(im_dir))

foto = []
plotid = []
plotid2 = []
# Obtain barcode information
for i in range(len(imgs)):
   plotid.append(decode(Image.open(imgs[i])))
   foto.append(imgs[i]) 
   print(i)

# Removing tags   
for i in range(len(plotid)):
    if plotid[i]==[]:
        plotid2.append(plotid[i])
    else: 
        plotid2.append(plotid[i][0].data)

for i in range(1,len(plotid2)):
    if plotid2[i]==[]:
            print("no code")
    else:
           os.rename( imgs[i], plotid2[i])
       
#img_list = [v for v in img_list if v.endswith('.JPG')]
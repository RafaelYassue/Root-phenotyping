image = ("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON\\DSCN8473.JPG")
from pyzbar.pyzbar import decode
from PIL import Image
import os as os 

##################################
a = decode(Image.open(image))
a2 = a[0]
a2.data

print(a[0].data)
##################################

im_dir = ("G:\\My Drive\\doutorado\\projeto\\dados\\imagens\\exp01\\raizes\\100NIKON")  
os.chdir(im_dir)
imgs = sorted(os.listdir(im_dir))

foto = []
plotid = []
plotid2 = []
print(a)

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

#Renaming pictures
for i in range(len(plotid)):
    if plotid[i]==[]:
        print(i)
    else:
       os.rename( imgs[i], plotid2[i])

        
        
        

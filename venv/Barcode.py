image = ("C:\\Users\\rafae\\Desktop\\codigde_barras_54589.jpg")
from pyzbar.pyzbar import decode
from PIL import Image
a = decode(Image.open(image))
a2 = a[0]
a2.data
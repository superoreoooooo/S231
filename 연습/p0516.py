import os
from PIL import Image, ImageFilter

img = Image.open("C:/Users/user/Documents/python/source/photo/picture20.jpg")

img = img.transpose(Image.FLIP_TOP_BOTTOM)
img = img.rotate(45, expand = True)
img = img.filter(ImageFilter.CONTOUR())

img.show()
img.save("연습/photo/op02.jpg")
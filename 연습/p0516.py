import os
import random
from PIL import Image, ImageFilter

num = str(random.randint(1, 99))

if (int(num) < 10) :
    num = "0" + num

img = Image.open("C:/Users/user/Documents/python/source/photo/picture" + num + ".jpg")

img = img.transpose(Image.FLIP_TOP_BOTTOM)
img = img.rotate(45, expand = True)
img = img.filter(ImageFilter.CONTOUR())

img.show()
img.save("연습/photo/output" + num + ".jpg")

print("File saved : output" + num + ".jpg")
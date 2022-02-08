from PIL import Image
import os, sys

path = "E:/Box_detection/preparing_data/OpenLabeling-master/OpenLabeling-master/main/input/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        #if os.path.isfile(path+item):
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((910,595), Image.ANTIALIAS)
        imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
#!/bin/python

from PIL import Image

original = Image.open('static/images/master/youtube.jpg')
(width, height) = original.size
scale1 = 40.0/width
scale2 = 640.0/width

downscaled = original.resize((int(width*scale1),int(height*scale1)), Image.ANTIALIAS)
upscaled = downscaled.resize((int(width*scale2),int(height*scale2)), Image.NEAREST)
upscaled.save('static/images/processed/youtube.jpg')

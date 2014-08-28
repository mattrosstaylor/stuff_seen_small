#!/usr/bin/python

from PIL import Image

sizes = [10, 20, 40, 80, 160, 320]

original = Image.open('source_images/youtube.jpg')
(width, height) = original.size
restore = 640.0/width

for size in sizes:
	scale = float(size)/width
	downscaled = original.resize((int(width*scale),int(height*scale)), Image.ANTIALIAS)
	upscaled = downscaled.resize((int(width*restore),int(height*restore)), Image.NEAREST)
	name = 'youtube-' + str(size)
	print name
	upscaled.save('static/images/' +name +'.jpg')

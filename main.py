#!/usr/bin/python
# -*-coding:UTF-8 -*-

import json
from PIL import Image

filename = 'lena512color.tiff'

image = Image.open(filename)
len([p for p in image.getdata()])

i = image.load()

width, height = image.size

def avg_color(color_list):
    

for x in range(0, width, 2):
    for y in range(0, height, 2):
        i[x, y], i[x+1, y], i[x, y+1], i[x+1, y+1]
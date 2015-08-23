#!/usr/bin/python
# -*-coding:UTF-8 -*-

import json
from PIL import Image
import numpy as np

filename = 'lena512color.tiff'

image = Image.open(filename)
len([p for p in image.getdata()])

i = image.load()

width, height = image.size


def avg_color(color_list):
    # Given a list of pixels, return the average color of them
    return tuple(pixel / len(color_list) for pixel in reduce(lambda p, q: map(lambda x, y: x + y, p, q), color_list))


zoomed_pixels = np.zeros((3, width/2, height/2))


def zoom_pic(radio=2):
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            color = avg_color((i[x, y], i[x+1, y], i[x, y+1], i[x+1, y+1]))
            for i in range(3):
                zoomed_pixels[i][x/2, y/2] = color[i]
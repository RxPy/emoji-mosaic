#!/usr/bin/python
# -*-coding:UTF-8 -*-

from PIL import Image
import numpy as np
from itertools import product

filename = 'lena512color.tiff'

image = Image.open(filename)
len([p for p in image.getdata()])

img = image.load()

width, height = image.size


def avg_color(color_list):
    # Given a list of pixels, return the average color of them
    return tuple(pixel / len(color_list) for pixel in reduce(lambda p, q: map(lambda x, y: float(x) + float(y), p, q), color_list))


def zoom_pic(radio=2):
    zoomed_pixels = np.zeros((3, width/radio, height/radio))
    for x in range(0, width, radio):
        for y in range(0, height, radio):
            # TODO: 不整除的情况
            color = avg_color([img[location] for location in map(lambda p: (x+p[0], y+p[1]), product(range(radio), range(radio)))])
            for rgb in range(3):
                zoomed_pixels[rgb][x/radio, y/radio] = color[rgb]
    return zoomed_pixels

zoom_pic(4)

#!/usr/bin/python
# -*-coding:UTF-8 -*-

from PIL import Image
import numpy as np
from itertools import product

filename = 'lena512color.tiff'

image = Image.open(filename)

img = image.load()


def avg_color(colors):
    # Given a list of pixels, return the average color of them
    return tuple(pixel / len(colors) for pixel in reduce(lambda p, q: map(lambda x, y: float(x)+y, p, q), colors))


def zoom_pic(radio=2):
    width, height = image.size
    zoomed_pixels = np.zeros((3, width/radio, height/radio))

    width_limit = width - radio if width % radio != 0 else width
    height_limit = height - radio if height % radio != 0 else height
    for x, y in product(range(0, width_limit, radio), range(0, height_limit, radio)):
        ran = range(radio)
        color = avg_color([img[loc] for loc in map(lambda p: (x+p[0], y+p[1]), product(ran, ran)) if loc[0] < width and loc[1] < height])
        for rgb in range(3):
            zoomed_pixels[rgb][x/radio, y/radio] = color[rgb]
    return zoomed_pixels


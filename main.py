#!/usr/bin/python
# -*-coding:UTF-8 -*-

from PIL import Image
import numpy as np
from itertools import product

filename = 'lena512color.tiff'

image = Image.open(filename)

img = image.load()

DEFAULT_EMOJI_SIZE = 32

EMOJI_FOLDER = 'emoji'


def avg_color(colors):
    """
    Calculate average color
    :param colors: a list of RGB colors
    :return: a single tuple of RGB color
    """
    return tuple(pixel / len(colors) for pixel in reduce(lambda p, q: map(lambda x, y: float(x)+y, p, q), colors))


def zoom_image(ratio=DEFAULT_EMOJI_SIZE):
    """
    :param ratio: the size of a mosaic block
    """
    width, height = image.size

    # Initialize a zere RGB matrix with zoomed size
    zoomed_image = np.zeros((3, width/ratio, height/ratio))

    # For each block, take the averge color and fill it into the zoomed image matrix
    for x, y in product(range(0, width - ratio if width % ratio != 0 else width, ratio),
                        range(0, height - ratio if height % ratio != 0 else height, ratio)):
        ran = range(ratio)
        color = avg_color([img[loc] for loc in map(lambda p: (x+p[0], y+p[1]), product(ran, ran)) if loc[0] < width and loc[1] < height])
        for rgb in range(3):
            zoomed_image[rgb][x/ratio, y/ratio] = color[rgb]
    return zoomed_image


def zoom_emoji(file=None, size=DEFAULT_EMOJI_SIZE):
    emoji = Image.open('/'.join([EMOJI_FOLDER, file]))
    emoji.thumbnail((size, size), Image.ANTIALIAS)
    return emoji

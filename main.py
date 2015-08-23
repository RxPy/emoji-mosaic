#!/usr/bin/python
# -*-coding:UTF-8 -*-

from PIL import Image
import numpy as np
from itertools import product


# The default size of each emoji, and also the default size of each mosaic block when zooming
DEFAULT_EMOJI_SIZE = 32

# The folder of emoji images
EMOJI_FOLDER = 'emoji'


def avg_color(colors):
    """
    Calculate average color of a block
    :param colors: a list of RGB colors
    :return: a single tuple of RGB color
    """
    return tuple(pixel / len(colors) for pixel in reduce(lambda p, q: map(lambda x, y: float(x)+y, p, q), colors))


def zoom_image(image, ratio=DEFAULT_EMOJI_SIZE):
    """
    Convert images into mosaic blocks with their average colors
    :param image: the input image
    :param ratio: the size of a mosaic block
    :return: image
    """
    # Get the image size
    width, height = image.size

    # Load the image matrix
    image_data = image.load()

    # Initialize a zere RGB matrix with zoomed size
    zoomed_image = np.zeros((3, width/ratio, height/ratio))

    # get the location of each pixel in a block
    ran = range(ratio)
    blocks = np.array(tuple(product(ran, ran)))

    # For each block, take the averge color and fill it into the zoomed image matrix
    for x, y in product(range(0, width - ratio if width % ratio != 0 else width, ratio),
                        range(0, height - ratio if height % ratio != 0 else height, ratio)):
        color = avg_color([image_data[loc[0], loc[1]] for loc in blocks + (x, y) if loc[0] <= width and loc[1] <= height])
        for rgb in range(3):
            zoomed_image[rgb][x/ratio, y/ratio] = color[rgb]
    return zoomed_image


def zoom_emoji(file=None, size=DEFAULT_EMOJI_SIZE):
    emoji = Image.open('/'.join([EMOJI_FOLDER, file]))
    emoji.thumbnail((size, size), Image.ANTIALIAS)
    return emoji


# For test
# readin the filename
filename = 'lena512color.tiff'

# the opened image is called "image"
image = Image.open(filename)

# load the pixels and call the matrix "image_data"
image_data = image.load()

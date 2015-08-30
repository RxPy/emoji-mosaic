#!/usr/bin/python
# -*-coding:UTF-8 -*-

from PIL import Image
import numpy as np
from itertools import product
import json
import random


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
    return tuple(pixel / len(colors) for pixel in reduce(lambda p, q: map(lambda x, y: float(x) + y, p, q), colors))

def zoom_emoji(file=None, size=DEFAULT_EMOJI_SIZE):
    """
    :param file: emoji file name
    :return: Image
    """
    emoji = Image.open('/'.join([EMOJI_FOLDER, file]))
    emoji.thumbnail((size, size), Image.ANTIALIAS)
    return emoji


# loading emoji data from existing JSON file
with open('emoji.json') as data_file:
    EMOJI_DATA = json.load(data_file)

# extract the avg emoji color in RGB
EMOJI_AVG_COLOR = map(lambda d: d['avg_color'], EMOJI_DATA)

def rolling(image, ratio=DEFAULT_EMOJI_SIZE):
    width, height = image.size

    # Load the image matrix
    image_data = image.load()

    # get the location of each pixel in a block
    ran = range(ratio)
    blocks = np.array(list(product(ran, ran)))

    new = []
    new_data = []
    for i in range(4):
        new_image = Image.new('RGBA', (width+70, height+70))
        new.append(new_image)
        new_data.append(new_image.load())

    # For each block, take the averge color and fill it into the zoomed image matrix
    for x, y in product(range(0, width - ratio if width % ratio != 0 else width, ratio / 2),
                        range(0, height - ratio if height % ratio != 0 else height, ratio / 2)):
        try:
            color = avg_color(
                # TODO:
                [image_data[loc[0], loc[1]] for loc in blocks + (x, y) if loc[0] <= width and loc[1] <= height])
            emoji = zoom_emoji(file=EMOJI_DATA[np.argmin(
                [sum([abs(color[c] - EMOJI_AVG_COLOR[e][c]) for c in range(3)]) for e in range(len(EMOJI_AVG_COLOR))])][
                'image'], size=DEFAULT_EMOJI_SIZE)
            emoji_width, emoji_height = emoji.size
            emoji_data = emoji.load()
            for e_x, e_y in product(range(emoji_width), range(emoji_height)):
                # TODO:
                new_data[random.randint(0, 3)][x * DEFAULT_EMOJI_SIZE + e_x,
                                               y * DEFAULT_EMOJI_SIZE + e_y] = emoji_data[e_x, e_y]
        except:
            pass

    result = Image.new('RGBA', (width, height))
    result_data = result.load()
    for x, y in product(range(width), range(height)):
        for i in range(4)[::-1]:
            if new_data[i][x, y][3] != 0:
                result_data[x, y] = new_data[i][x, y]
                break
    return result


# For test
# readin the filename
filename = 'tower.jpg'

# the opened image is called "image"
image = Image.open(filename)

# load the pixels and call the matrix "image_data"
image_data = image.load()

zoomed_image = rolling(image)

zoomed_image.save('result.jpg')

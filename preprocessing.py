#!/usr/bin/python
# -*-coding:UTF-8 -*-

import json
from PIL import Image

with open('emoji-data.json') as data_file:
    data = json.load(data_file)


def average_color(image):
    colour_tuple = [None, None, None]
    for channel in range(3):
        # Get data for one channel at a time
        pixels = image.getdata(band=channel)

        values = []
        for pixel in pixels:
            values.append(pixel)

        colour_tuple[channel] = sum(values) / len(values)
    return colour_tuple

result = []
for d in data:
    try:
        image = Image.open('emoji/' + d['image'])
        image.load()
        d_result = {'avg_color': average_color(image),
                    'image': d['image'],
                    'short_name': d['short_name'],
                    'sort_order': d['sort_order']}

        result.append(d_result)
    except Exception:
        print d['image']

with open('emoji.json', 'w') as outfile:
    json.dump(result, outfile)

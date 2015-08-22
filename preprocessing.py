#!/usr/bin/python
# -*-coding:UTF-8 -*-

import json
from PIL import Image

with open('emoji-data.json') as data_file:
    data = json.load(data_file)


def average_color(image):
    def single_channel(channel):
        pixel = [p for p in image.getdata(band=channel)]
        return sum(pixel) / len(pixel)
    return map(single_channel, range(3))

result = []
for d in data:
    try:
        image = Image.open('emoji/' + d['image'])
        d_result = {'avg_color': average_color(image),
                    'image': d['image'],
                    'short_name': d['short_name'],
                    'sort_order': d['sort_order']}

        result.append(d_result)
    except Exception:
        print d['image']

with open('emoji.json', 'w') as outfile:
    json.dump(result, outfile)

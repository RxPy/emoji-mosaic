#!/usr/bin/python
# -*-coding:UTF-8 -*-

import json
from PIL import Image

with open('emoji-data.json') as data_file:
    data = json.load(data_file)


def average_color(image):
    sum_r, sum_g, sum_b = 0, 0, 0
    for pixel in image.getdata():
        sum_r += pixel[0] * pixel[3] / 255.0
        sum_g += pixel[1] * pixel[3] / 255.0
        sum_b += pixel[2] * pixel[3] / 255.0
    length = len(image.getdata())
    return [round(sum_r / length, 0), round(sum_g / length, 0), round(sum_b / length, 0)]

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

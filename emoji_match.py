__author__ = 'Jin'

import json


from pprint import pprint

with open('emoji.json') as data_file:
    data = json.load(data_file)

pprint(data)


length = len(data)

emoji_avg_color = data[]['avg_color']

map(lambda d:d['avg_color'], data)

def colordiff(array):





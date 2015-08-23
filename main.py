#!/usr/bin/python
# -*-coding:UTF-8 -*-

from PIL import Image
import json

with open('emoji.json') as data_file:
    emoji = json.load(data_file)
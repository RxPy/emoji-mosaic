__author__ = 'Jin'

import json

import numpy as np

from itertools import product

# loading emoji data from existing JSON file
with open('emoji.json') as data_file:
    EMOJI_DATA = json.load(data_file)

# extract the avg emoji color in RGB
EMOJI_AVG_COLOR = map(lambda d:d['avg_color'], EMOJI_DATA)

# Calculate the diffenrence in color for blocks in original pic
def colordiff(zoomed_image):
    # set width and height according to zoomed pic
    zoomed_width, zoomed_height = zoomed_image.shape[1],zoomed_image.shape[2]
    # initialize color difference matrix, dim(number of emoji, 3 for RGB, width, height)
    colordiff_matrix = np.zeros((len(EMOJI_AVG_COLOR), 3, zoomed_width, zoomed_height)) # THIS IS GOING TO BE CRAZY

    # N loops to get diff from each block with respect to every emoji
    for i in range(len(EMOJI_DATA)):
        for rgb in range(3):
            for m,n in product(range(0,zoomed_width),range(0,zoomed_height)):
                colordiff_matrix[i,rgb,m,n] = abs(EMOJI_AVG_COLOR[i][rgb]-zoomed_image[rgb,m,n])
    # return
    return colordiff_matrix

def closest_match(colordiff_matrix):
    # summarize RGB color diff for every emoji according to the given pic
    total_color_diff = np.zeros((len(EMOJI_AVG_COLOR),colordiff_matrix.shape[2],colordiff_matrix.shape[3]))
    # initialize index matrix recoding matching emoji
    index = np.zeros((colordiff_matrix.shape[2],colordiff_matrix.shape[3]))
    # you know this crazy shit... just identify the smallest diff with respect to each block among all the emojis
    for m,n in product(range(0,colordiff_matrix.shape[2]),range(0,colordiff_matrix.shape[3])):
        for i in len(EMOJI_AVG_COLOR):
            total_color_diff[i,m,n] = sum(colordiff_matrix[i,:,m,n])
        index[m,n] = np.unravel_index(total_color_diff[:,m,n].argmin(),total_color_diff[:,m,n].shape)[0]
    # return
    return index









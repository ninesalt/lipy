import os
import pickle
import urllib.request
import numpy as np


def downloadimages(src, destination):

    # download images given location of scraped.json

    if not os.path.exists(destination):
        os.makedirs(destination)

    data = pickle.load(open(src, 'rb'))
    i = 0
    for _, pictures in data.items():
        for picture in pictures:
            urllib.request.urlretrieve(
                picture['img-small'], destination + 'img' + str(i) + '.jpeg')
            i += 1


def getlikes(src, destination):

    # get number of likes for each image given  location of scraped.json

    data = pickle.load(open(src, 'rb'))
    likes = []

    for _, pictures in data.items():
        for picture in pictures:
            likes.append(picture['likes'])

    return np.array(likes)

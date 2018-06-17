import os
import pickle
import itertools
import urllib.request
import numpy as np
from os.path import dirname, join


def downloadimages(src, destination):

    # download images given location of pickle dump

    directory = dirname(__file__)
    src = join(directory, src)
    destination = join(directory, destination)

    if not os.path.exists(destination):
        os.makedirs(destination)

    data = pickle.load(open(src, 'rb'))
    spinner = itertools.cycle(['.', '..', '...'])
    i = 0

    for _, pictures in data.items():
        print('\rDownloading images{}'.format(next(spinner)), end="")
        for picture in pictures:
            urllib.request.urlretrieve(picture['img-small'],
                                       destination + 'img' + str(i) + '.jpeg')
            i += 1


def getlikes(src):

    # get number of likes for each image given location of pickle dump
    directory = dirname(__file__)
    src = join(directory, src)

    data = pickle.load(open(src, 'rb'))
    likes = []

    for _, pictures in data.items():
        for picture in pictures:
            likes.append(picture['likes'])

    return np.array(likes)

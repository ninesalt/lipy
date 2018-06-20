from os.path import dirname, join
from keras.models import load_model
import tensorflow as tf
import numpy as np
import cv2

graph = tf.get_default_graph()
directory = dirname(__file__)
modelpath = join(directory, '../models/regv1.h')
model = load_model(modelpath)


def readresize(imagepaths):

    # parse and resize images to use in predictions

    images = []

    for image in imagepaths:
        parsed = cv2.imread(image)
        resized = cv2.resize(parsed, (200, 200))
        images.append(resized)

    return np.array(images)


def getprediction(images):

    global graph

    with graph.as_default():
        pred = model.predict(images)

        # multiply by -1 to sort in descending order
        argsorted = np.argsort(pred.flatten() * -1)
        return argsorted

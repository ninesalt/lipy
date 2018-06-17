from os.path import dirname, join
from keras.models import load_model
import numpy as np

directory = dirname(__file__)
modelpath = join(directory, '../models/regv1.h')
model = load_model(modelpath)


def getprediction(images):
    pred = model.predict(images)

    # times -1 to sort in descending order
    argsorted = np.argsort(pred.flatten() * -1)
    return argsorted

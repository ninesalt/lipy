from features import downloadimages, getlikes
from keras.models import Sequential
from keras.layers import Conv2D, Activation, MaxPool2D, Flatten, Dense
import numpy as np
import cv2
import glob


IMAGESIZE = (200, 200)
TRAININGPERCENT = 0.7

# downloadimages(src='../data/pickledump',
#                destination='../data/download/')

# get likes array where Nth element corresponds to the number of likes
# on image ../data/download/N.jpeg
likes = getlikes(src='../data/pickledump',
                 destination='../data/download/')

likes = np.array(likes)
likes = (likes - np.mean(likes))/np.std(likes)  # normalize

images = []

# read images and resize them
for imgfile in glob.glob('../data/download/*.jpeg'):
    img = cv2.imread(imgfile)
    resized = cv2.resize(img, IMAGESIZE)
    images.append(resized)

images = np.array(images)

# partition training/testing sets
training_num = int(TRAININGPERCENT * len(images))

x_train = images[: training_num]
y_train = likes[:training_num]

x_test = images[training_num:]
y_test = likes[training_num:]


# create model and add layers
model = Sequential()

model.add(Conv2D(10, 3, 3, activation='relu',
                 input_shape=(IMAGESIZE[0], IMAGESIZE[1], 3)))

model.add(Conv2D(10, 3, 3, activation='relu'))
model.add(MaxPool2D((5, 5)))
model.add(Flatten())
model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dense(1))

print(model.summary())
model.compile(loss='mse',
              optimizer='rmsprop')

model.fit(x_train, y_train, epochs=10)
score = model.evaluate(x_test, y_test)
print('test set mse is {}'.format(score))

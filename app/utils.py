import re
import os
import time


def cleanfilename(filename):

    # clean filename from dangerous characters

    filename = str(filename).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', filename)


def upload(request, destination):

    # upload images to destination and return
    # filepaths (directory + filename)

    images = request.files.getlist("file")
    filepaths = []

    for img in images:
        filename = str(int(time.time())) + cleanfilename(img.filename)
        filepath = os.path.join(destination, filename)
        img.save(filepath)
        filepaths.append(filepath)

    return filepaths


def cleanup(filepaths):

    # delete unwanted uploaded images after prediction

    for image in filepaths:
        os.remove(image)

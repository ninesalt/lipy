from flask import Flask, jsonify, request
from api import getprediction, readresize
from utils import upload, cleanup
import time
import os
import re

app = Flask(__name__)
directory = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(directory, './uploads')


@app.route('/isAlive')
def index():
    return "true"


@app.route('/', methods=['GET'])
def homepage():
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file accept=image/* multiple>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/', methods=['POST'])
def predict():

     # upload all images in request to folder on server
    filepaths = upload(request, UPLOAD_FOLDER)

    # parse and resize images then get prediction
    parsed = readresize(filepaths)
    result = getprediction(parsed)

    # cleanup and return result
    cleanup(filepaths)
    print('result : ', result)
    return jsonify(result)


if __name__ == '__main__':

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(port=5000, host='0.0.0.0')

import json
import numpy as np
import urllib.request

from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
from profanity_check import predict_prob

from helper import preprocess, vectorize

app = Flask(__name__)
FILEPATH='simple_nn.h5'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/item')
def item():
    id = request.args.get('id',
                          default='10309052',
                          type=str)
    url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
    
    model = load_model(FILEPATH)
    
    with urllib.request.urlopen(url) as response:
        charset = response.headers.get_content_charset()
        text = response.read().decode(charset)
    
    json_item = json.loads(text)
    json_item['text'] = preprocess(json_item['text'])
    json_item['prob_offensive'] = predict_prob([json_item['text']])[0]
    print(model.predict([vectorize(json_item['text'])])[0][0])
    json_item['custom_pred'] = np.float64(model.predict([vectorize(
            json_item['text'])])[0][0])
    
    return jsonify(json_item)
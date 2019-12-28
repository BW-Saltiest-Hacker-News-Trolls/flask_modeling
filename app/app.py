from flask import Flask, jsonify, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/comment')
def comment():
    id = request.args.get('id',
                          default='10309052',
                          type=str)
    url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
    with urllib.request.urlopen(url) as response:
        charset = response.headers.get_content_charset()
        text = response.read().decode(charset)
    
    return jsonify(json.loads(text))
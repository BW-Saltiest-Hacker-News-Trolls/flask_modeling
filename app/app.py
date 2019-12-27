from flask import Flask, request
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
    fp = urllib.request.urlopen(url)
    urlbytes = fp.read()
    fp.close()
    return urlbytes
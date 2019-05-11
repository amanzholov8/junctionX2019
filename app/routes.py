from app import app
from app import fa

from flask import render_template, request

import json

from flask_fontawesome import FontAwesome

from utils import nlp

@app.route('/')
@app.route('/index')
def index():
    stories = [
        {
            'name': 'The Sea Wolf',
            'author': 'Jack London',
            'img': 'https://images-na.ssl-images-amazon.com/images/I/5169HPG833L._SX312_BO1,204,203,200_.jpg'
        },
        {
            'name': 'Kill the mocking bird',
            'author': 'Harper Lee',
            'img': 'https://upload.wikimedia.org/wikipedia/en/thumb/7/79/To_Kill_a_Mockingbird.JPG/220px-To_Kill_a_Mockingbird.JPG'
        }
    ]
    return render_template('index.html', stories=stories)

@app.route('/reader')
def reader():
    return render_template('audioplay.html')

@app.route('/receive_audio', methods=['GET'])
def command():
    #TODO: (@Kunduz, @Alim)
    print(request.args)
    data = request.get_json()
    print(data)
    #text = sst(data)
    #text = 'Go back to four sentences'
    #return nlp.identify(text)
    return 'yes'

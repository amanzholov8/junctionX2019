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
            'title': 'My Little Pony',
            'short_description': 'Interesting book about ponnies.',
            'src': "ponnies.jpg",
            'content': 'Once in a while ...'
        },
        {
            'title': 'Aldar Kose',
            'short_description': 'Kazakh national fairytale about rich and poor',
            'src': "aldar_kose.jpg",
            'content': 'In the Kazakh steppes ...'
        },
        {
            'title': 'My Little Pony',
            'short_description': 'Interesting book about ponnies.',
            'src': "ponnies.jpg",
            'content': 'Once in a while ...'
        },
        {
            'title': 'My Little Pony',
            'short_description': 'Interesting book about ponnies.',
            'src': "ponnies.jpg",
            'content': 'Once in a while ...'
        },
        {
            'title': 'My Little Pony',
            'short_description': 'Interesting book about ponnies.',
            'src': "ponnies.jpg",
            'content': 'Once in a while ...'
        },
        {
            'title': 'My Little Pony',
            'short_description': 'Interesting book about ponnies.',
            'src': "ponnies.jpg",
            'content': 'Once in a while ...'
        },
        {
            'title': 'My Little Pony',
            'short_description': 'Interesting book about ponnies.',
            'src': "ponnies.jpg",
            'content': 'Once in a while ...'
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

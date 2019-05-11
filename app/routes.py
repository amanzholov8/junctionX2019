from app import app
from app import fa

from flask import render_template, request

from flask_fontawesome import FontAwesome

from utils import nlp

@app.route('/')
@app.route('/index')
def index():
    stories = [
        {
            'name': 'My Little Pony',
            'content': 'Once in a while ...'
        },
        {
            'name': 'Kazakh National Fairytale: Aldar Kose',
            'content': 'In the Kazakh steppes ...'
        }
    ]
    return render_template('index.html', stories=stories)

@app.route('/reader')
def reader():
    return render_template('audioplay.html')

@app.route('/receive_audio', methods=['POST'])
def command():
    #TODO: (@Kunduz, @Alim)
    print(request.data)
    #text = sst(data)
    text = 'Go back to four sentences'
    return nlp.identify(text)

from app import app

from flask import render_template

from flask_fontawesome import FontAwesome

fa = FontAwesome(app)

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
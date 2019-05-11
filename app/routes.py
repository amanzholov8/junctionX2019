from app import app

from flask import render_template

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
from app import app
from app import fa

from flask import render_template, request, Response, send_file, send_from_directory, url_for

import json
import wave

from flask_fontawesome import FontAwesome

from utils import nlp, mediator

import requests

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
    paragraphs = [
        {
            'id': "id0",
            'content': 'I scarcely know where to begin, though I sometimes facetiously place the cause of it all to Charley Furuseth’s credit.  He kept a summer cottage in Mill Valley, under the shadow of Mount Tamalpais, and never occupied it except when he loafed through the winter months and read Nietzsche and Schopenhauer to rest his brain.  When summer came on, he elected to sweat out a hot and dusty existence in the city and to toil incessantly.  Had it not been my custom to run up to see him every Saturday afternoon and to stop over till Monday morning, this particular January Monday morning would not have found me afloat on San Francisco Bay.'
        },
        {
            'id': 'id1',
            'content': "Not but that I was afloat in a safe craft, for the Martinez was a new ferry-steamer, making her fourth or fifth trip on the run between Sausalito and San Francisco.  The danger lay in the heavy fog which blanketed the bay, and of which, as a landsman, I had little apprehension.  In fact, I remember the placid exaltation with which I took up my position on the forward upper deck, directly beneath the pilot-house, and allowed the mystery of the fog to lay hold of my imagination.  A fresh breeze was blowing, and for a time I was alone in the moist obscurity—yet not alone, for I was dimly conscious of the presence of the pilot, and of what I took to be the captain, in the glass house above my head."
        },
        {
            "id": 'id2',
            'content': "A red-faced man, slamming the cabin door behind him and stumping out on the deck, interrupted my reflections, though I made a mental note of the topic for use in a projected essay which I had thought of calling “The Necessity for Freedom: A Plea for the Artist.”  The red-faced man shot a glance up at the pilot-house, gazed around at the fog, stumped across the deck and back (he evidently had artificial legs), and stood still by my side, legs wide apart, and with an expression of keen enjoyment on his face.  I was not wrong when I decided that his days had been spent on the sea."
        }

    ]
    return render_template('audioplay.html', paragraphs = paragraphs)

@app.route('/receive_audio', methods=['POST'])
def command():
    #data = request.files['audio'].stream.read()
    #with open('tmp123456.wav', 'wb') as f:
    #    f.write(data)
    #print(data)
    #with open('tmp123.mp3', 'wb') as f:
    #    f.write(requests.get(url).content)
    #return 'yes'
    #text = mediator.sendAudioQuestion(url)
    #text = 'Go back to four sentences'
    #print(text)
    #req = nlp.identify(text)
    #send it to fronend req
    return 'yes'

@app.route('/narrator', methods=['POST'])
def narration():
    #data = request.get_json()
    #print(request.form['text'])
    #print(data)
    text = request.form['text']
    #print(text)
    response = mediator.text_to_audio(text)
    #new_file = '{}/{}'.format(url_for('static'), 'assets/narr123.mp3')
    with open('narr.mp3', 'wb') as f:
        f.write(response)
    return url_for('static', filename='assets/narr.mp3')
    #send to fronend
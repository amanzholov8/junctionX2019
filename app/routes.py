from app import app
from app import fa

from flask import render_template, request, Response, send_file, send_from_directory, url_for

import json
import wave

from flask_fontawesome import FontAwesome

from utils import nlp, mediator, askcontext

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

@app.route('/reader/')
def reader():
    book = {
        'title': 'Sea Wolf',
        'paragraphs': [
            "I scarcely know where to begin, though I sometimes facetiously place the cause of it all to Charley Furuseth's credit. He kept a summer cottage in Mill Valley, under the shadow of Mount Tamalpais, and never occupied it except when he loafed through the winter months and read Nietzsche and Schopenhauer to rest his brain. When summer came on, he elected to sweat out a hot and dusty existence in the city and to toil incessantly. Had it not been my custom to run up to see him every Saturday afternoon and to stop over till Monday morning, this particular January Monday morning would not have found me afloat on San Francisco Bay.",
            "Not but that I was afloat in a safe craft, for the Martinez was a new ferry-steamer, making her fourth or fifth trip on the run between Sausalito and San Francisco. The danger lay in the heavy fog which blanketed the bay, and of which, as a landsman, I had little apprehension. In fact, I remember the placid exaltation with which took up my position on the forward upper deck, directly beneath the pilot-house, and allowed the mystery of the fog to lay hold of my imagination. A fresh breeze was blowing, and for a time I was alone in the moist obscurity; yet not alone, for I was dimly conscious of the presence of the pilot, and of what I took to be the captain, in the glass house above my head.",
            "I remember thinking how comfortable it was, this division of labor which made it unnecessary for me to study fogs, winds, tides, and navigation, in order to visit my friend who lived across an arm of the sea. It was good that men should be specialists, I mused. The peculiar knowledge of the pilot and captain sufficed for many thousands of people who knew no more of the sea and navigation than I knew. On the other hand, instead of having to devote my energy to the learning of a multitude of things, I concentrated it upon a few particular things, such as, for instance, the analysis of Poe's place in American literature, an essay of mine, by the way, in the current Atlantic. Coming aboard, as I passed through the cabin, I had noticed with greedy eyes a stout gentleman reading the Atlantic, which was open at my very essay. And there it was again, the division of labor, the special knowledge of the pilot and captain which permitted the stout gentleman to read my special knowledge on Poe while they carried him safely from Sausalito to San Francisco.",
            "A red-faced man, slamming the cabin door behind him and stumping out on the deck, interrupted my reflections, though I made a mental note of the topic for use in a projected essay which I had thought of calling 'The Necessity for Freedom: A Plea for the Artist.' The red-faced man shot a glance up at the pilot-house, gazed around at the fog, stumped across the deck and back (he evidently had artificial legs), and stood still by my side, legs wide apart, and with an expression of keen enjoyment on his face. I was not wrong when decided that his days had been spent on the sea.",
            "'It's nasty weather like this here that turns heads gray before their time,' he said, with a nod toward the pilot-house.",
            "The vessels came together before I could follow his advice. We must have been struck squarely amidships, for I saw nothing, the strange steamboat having passed beyond my line of vision. The Martinez heeled over, sharply, and there was a crashing and rending of timber. I was thrown flat on the wet deck, and before I could scramble to my feet I heard the scream of the women. This it was, I am certain, -- the most indescribable of blood-curdling sounds, -- that threw me into a panic. I remembered the life-preservers stored in the cabin, but was met at the door and swept backward by a wild rush of men and women. What happened in the next few minutes I do not recollect, though I have a clear remembrance of pulling down life-preservers from the overhead racks, while the red-faced man fastened them about the bodies of an hysterical group of women. This memory is as distinct and sharp as that of any picture I have seen. It is a picture, and I can see it now, -- the jagged edges of the hole in the side of the cabin, through which the gray fog swirled and eddied; the empty upholstered seats, littered with all the evidences of sudden flight, such as packages, hand satchels, umbrellas, and wraps; the stout gentleman who had been reading my essay, encased in cork and canvas, the magazine still in his hand, and asking me with monotonous insistence if I thought there was any danger; the red-faced man, stumping gallantly around on his artificial legs and buckling life-preservers on all comers; and finally, the screaming bedlam of women."
        ]
    }
    return render_template('audioplay.html', book=book)

@app.route('/receive_audio', methods=['POST'])
def command():
    data = request.files['audio_data'].stream.read()

    #with open('request.wav', 'wb') as f:
    #    f.write(data)
    text = mediator.audio_to_text(data)

    ps = [
            "I scarcely know where to begin, though I sometimes facetiously place the cause of it all to Charley Furuseth's credit. He kept a summer cottage in Mill Valley, under the shadow of Mount Tamalpais, and never occupied it except when he loafed through the winter months and read Nietzsche and Schopenhauer to rest his brain. When summer came on, he elected to sweat out a hot and dusty existence in the city and to toil incessantly. Had it not been my custom to run up to see him every Saturday afternoon and to stop over till Monday morning, this particular January Monday morning would not have found me afloat on San Francisco Bay.",
            "Not but that I was afloat in a safe craft, for the Martinez was a new ferry-steamer, making her fourth or fifth trip on the run between Sausalito and San Francisco. The danger lay in the heavy fog which blanketed the bay, and of which, as a landsman, I had little apprehension. In fact, I remember the placid exaltation with which took up my position on the forward upper deck, directly beneath the pilot-house, and allowed the mystery of the fog to lay hold of my imagination. A fresh breeze was blowing, and for a time I was alone in the moist obscurity; yet not alone, for I was dimly conscious of the presence of the pilot, and of what I took to be the captain, in the glass house above my head.",
            "I remember thinking how comfortable it was, this division of labor which made it unnecessary for me to study fogs, winds, tides, and navigation, in order to visit my friend who lived across an arm of the sea. It was good that men should be specialists, I mused. The peculiar knowledge of the pilot and captain sufficed for many thousands of people who knew no more of the sea and navigation than I knew. On the other hand, instead of having to devote my energy to the learning of a multitude of things, I concentrated it upon a few particular things, such as, for instance, the analysis of Poe's place in American literature, an essay of mine, by the way, in the current Atlantic. Coming aboard, as I passed through the cabin, I had noticed with greedy eyes a stout gentleman reading the Atlantic, which was open at my very essay. And there it was again, the division of labor, the special knowledge of the pilot and captain which permitted the stout gentleman to read my special knowledge on Poe while they carried him safely from Sausalito to San Francisco.",
            "A red-faced man, slamming the cabin door behind him and stumping out on the deck, interrupted my reflections, though I made a mental note of the topic for use in a projected essay which I had thought of calling 'The Necessity for Freedom: A Plea for the Artist.' The red-faced man shot a glance up at the pilot-house, gazed around at the fog, stumped across the deck and back (he evidently had artificial legs), and stood still by my side, legs wide apart, and with an expression of keen enjoyment on his face. I was not wrong when decided that his days had been spent on the sea.",
            "'It's nasty weather like this here that turns heads gray before their time,' he said, with a nod toward the pilot-house.",
            "The vessels came together before I could follow his advice. We must have been struck squarely amidships, for I saw nothing, the strange steamboat having passed beyond my line of vision. The Martinez heeled over, sharply, and there was a crashing and rending of timber. I was thrown flat on the wet deck, and before I could scramble to my feet I heard the scream of the women. This it was, I am certain, -- the most indescribable of blood-curdling sounds, -- that threw me into a panic. I remembered the life-preservers stored in the cabin, but was met at the door and swept backward by a wild rush of men and women. What happened in the next few minutes I do not recollect, though I have a clear remembrance of pulling down life-preservers from the overhead racks, while the red-faced man fastened them about the bodies of an hysterical group of women. This memory is as distinct and sharp as that of any picture I have seen. It is a picture, and I can see it now, -- the jagged edges of the hole in the side of the cabin, through which the gray fog swirled and eddied; the empty upholstered seats, littered with all the evidences of sudden flight, such as packages, hand satchels, umbrellas, and wraps; the stout gentleman who had been reading my essay, encased in cork and canvas, the magazine still in his hand, and asking me with monotonous insistence if I thought there was any danger; the red-faced man, stumping gallantly around on his artificial legs and buckling life-preservers on all comers; and finally, the screaming bedlam of women."
        ]
    ret = askcontext.answer("".join(ps), mediator.generate_question(text['text']))
    #print(paragraph)
    #print(res)
    #print(text['text'])
    #return res
    return ret[0][0]

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
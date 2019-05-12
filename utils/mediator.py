import requests
from utils import askcontext

CSS_URL = 'https://naveropenapi.apigw.ntruss.com/voice/v1/tts'

CSR_URL = 'https://naveropenapi.apigw.ntruss.com/recog/v1/stt'

CSS_headers = {
    'X-NCP-APIGW-API-KEY-ID': 'bgwipyhdia',
    'X-NCP-APIGW-API-KEY': '64SWkLBWMgMTLefm3sAn0EbwFr8SCzZA6byi05Wp',
    'Content-Type': 'application/x-www-form-urlencoded'
}

CSR_headers = {
    'X-NCP-APIGW-API-KEY-ID': 'bgwipyhdia',
    'X-NCP-APIGW-API-KEY': '64SWkLBWMgMTLefm3sAn0EbwFr8SCzZA6byi05Wp',
    'Content-Type': 'application/octet-stream'
}

#From sequence diagram: sendChunkText AND vocalizeText
def text_to_audio(text):
    body = {
    'speaker': 'clara',
    'speed': 0,
    'text': text
    }
    r = requests.post(CSS_URL, body, headers=CSS_headers)
    response_body = r.content
    if r.status_code == requests.codes.ok :
        return response_body
    else:
        return "Error code: {}".format(r.status_code)

#Not tested yet
def audio_to_text(sound_data):
    Eng = "?lang=" + "Eng"
    response = requests.post(CSR_URL+Eng, sound_data, headers=CSR_headers)
    rescode = response.status_code
    if(rescode == 200):
        return response.json()
    else:
        return "Error : " + response.text

#attaches question mark to the end of the text sentence
def generate_question(user_message):
    if not (user_message[len(user_message) - 1] == '?'):
        return "{0}?".format(user_message)
    return user_message




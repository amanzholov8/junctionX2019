"""
Clova speech synthesis example (CSS)
"""
import requests

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

def sendChunkText(text):
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

def sendAudioQuestion(url):
    data = requests.get(url).content
    Eng = "?lang=" + "Eng"
    response = requests.post(CSR_URL+Eng,  data=data, headers=CSR_headers)
    rescode = response.status_code
    if(rescode == 200):
        return response.text
    else:
        return "Error : " + response.text  
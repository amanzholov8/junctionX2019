"""
Clova speech synthesis example (CSS)
"""
import requests

CSS_URL = 'https://naveropenapi.apigw.ntruss.com/voice/v1/tts'

headers = {
    'X-NCP-APIGW-API-KEY-ID': 'bgwipyhdia',
    'X-NCP-APIGW-API-KEY': '64SWkLBWMgMTLefm3sAn0EbwFr8SCzZA6byi05Wp',
    'Content-Type': 'application/x-www-form-urlencoded'
}

body = {
    'speaker': 'clara',
    'speed': 0,
    'text': 'Hello world'
}

r = requests.post(CSS_URL, body, headers=headers)
response_body = r.content
if r.status_code == requests.codes.ok:
    with open('tmp.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error code: {}".format(r.status_code))

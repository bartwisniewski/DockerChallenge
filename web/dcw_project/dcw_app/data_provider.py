import os
import requests
import jwt

from django.conf import settings

API_HOST = 'http://'+os.environ['API_HOST_NAME']+':'+os.environ['API_PORT_NAME']
ENDPOINT = 'patient'


def request_with_token(url):
    token = jwt.encode({}, settings.API_SECRET_KEY, algorithm='HS256')
    response = requests.get(url, headers={'X-Access-Token': token})
    return response


def get_patient_data(id: int) -> dict:
    url = API_HOST + '/' + ENDPOINT + '/' + str(id)
    response = request_with_token(url)
    if response:
        return response.json()

    return {}

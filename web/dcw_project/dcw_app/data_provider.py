import requests
import jwt
from django.conf import settings

API_URL = 'http://data-api:8000'
ENDPOINT = 'patient'


def request_with_token(url):
    token = jwt.encode({}, settings.API_SECRET_KEY, algorithm='HS256')
    response = requests.get(url, headers={'X-Access-Token': token})
    return response


def get_patient_data(id: int) -> dict:
    url = API_URL + '/' + ENDPOINT + '/' + id
    response = request_with_token(url)
    if response:
        return response.json()

    return {}

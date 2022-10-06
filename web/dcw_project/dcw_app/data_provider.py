import requests

API_URL = 'http://127.0.0.1:8001'
ENDPOINT = 'patient'


def get_patient_data(id: int) -> dict:
    url = API_URL + '/' + ENDPOINT + '/' + id
    response = requests.get(url)
    if response:
        return response.json()

    return None

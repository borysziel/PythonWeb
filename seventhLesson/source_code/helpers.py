from json import JSONDecodeError
from urllib.parse import urljoin

import requests

API_URL = 'https://swapi.co/api/'


def build_url(path, *args):
    return urljoin(API_URL, path)


def handle_response(response):
    if response.ok:
        try:
            return response.json()
        except JSONDecodeError:
            return {response.status_code: response.text}
    else:
        return {response.status_code: response.text}


def get_root():
    response = requests.get(API_URL)
    return handle_response(response)


def get_people_list(url=build_url('people/')):
    response = requests.get(url)
    return handle_response(response)


def get_person(id, url=build_url('people/')):
    url = url + str(id)
    response = requests.get(url)
    return handle_response(response)


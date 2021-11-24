import requests
import json
import random
import unittest


def get_url():
    return 'https://test.jasgme.com/sgme/api'


def get_valid_credentials():
    return {'login': 'lucas.bertoldo@dellead.com', 'password': '123'}


def get_token():
    url = get_url()
    body = get_valid_credentials()
    response = requests.post(f'{url}/authenticate/login', json=body)
    assert response.status_code == 200

    json_data = json.loads(response.text)

    token = json_data['token']

    auth = f'Bearer {token}'

    return auth


def get_company_id():
    url = get_url()
    token = get_token()
    header = {'authorization': token}
    response = requests.get(f'{url}/companies', headers=header)

    json_data = json.loads(response.text)

    n = len(json_data) - 1
    company_index = random.randint(0, n)
    company_id = json_data[company_index]['id']

    return company_id


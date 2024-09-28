import requests

ZERONET_URL = 'http://127.0.0.1:43110'

def create_site(site_name, site_content):
    url = f'{ZERONET_URL}/create'
    data = {
        "site_name": site_name,
        "content": site_content
    }
    response = requests.post(url, json=data)
    return response.json()

def update_site(site_address, new_content):
    url = f'{ZERONET_URL}/update'
    data = {
        "site_address": site_address,
        "new_content": new_content
    }
    response = requests.post(url, json=data)
    return response.json()

def get_site_data(site_address):
    url = f'{ZERONET_URL}/data/{site_address}'
    response = requests.get(url)
    return response.json()

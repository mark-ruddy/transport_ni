from django.db import Error
from django.forms.forms import ErrorDict
import requests

api_url = "https://api.postcodes.io/postcodes"

def query_postcode(postcode):
    request_addr = f"{api_url}/{postcode}"
    resp = requests.get(request_addr)
    resp_json = resp.json()
    if resp_json['status'] != 200:
        raise Error
    return resp_json

def get_soa_of_postcode(postcode):
    resp_json = query_postcode(postcode)
    return get_soa_from_resp_json(resp_json)

def get_soa_from_resp_json(resp_json):
    res = resp_json['result']
    return res['lsoa']

def get_lon_from_resp_json(resp_json):
    res = resp_json['result']
    return res['longitude']

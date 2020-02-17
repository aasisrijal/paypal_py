
import requests
import base64
import json

client_id = 'your paypal app client id'
client_secret = 'your paypal app client secret'

credentials = "%s:%s" % (client_id, client_secret)
encode_credential = base64.b64encode(credentials.encode('utf-8')).decode('utf-8').replace("\n", "")

def get_token(encode_credential=encode_credential):

    headers = {
        "Authorization": ("Basic %s" % encode_credential),
        'Accept': 'application/json',
        'Accept-Language': 'en_US',
    }
    param = {
    'grant_type': 'client_credentials',
    }
    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
    r = requests.post(url, headers=headers, data=param)
    response = json.loads(r.text)

    return response['access_token']


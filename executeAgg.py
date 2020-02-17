import requests
import json

class executeAgg:

    def __init__(self, app_token, token):
        self.app_token = app_token
        self.token = token

    def executeAgg(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ self.app_token,
            
            }
        url = 'https://api.sandbox.paypal.com/v1/payments/billing-agreements/{}/agreement-execute'.format(self.token)
        r = requests.post(url, headers=headers)
        return json.loads(r.text)
     
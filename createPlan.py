import requests
import json

class createPlan:

    def __init__(self, arr):
        self.token = arr['token']
        self.name = arr['name']
        self.description = arr['description']
        self.frequency = arr['frequency']
        self.frequency_interval = arr['frequency_interval']
        self.currency_code = arr['currency_code']
        self.price = arr['price']
        self.cycles = arr['cycles']
        self.shipping_charge = arr['shipping_charge']
        self.setupfee = arr['setupfee']
        self.tax = arr['tax']

  
    def createPlan(self):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ self.token,
            
            }

        url = 'https://api.sandbox.paypal.com/v1/payments/billing-plans/'



        data = {
            "name": self.name,
            "description": self.description,
            "type": "fixed",
            "payment_definitions": [
            {
              "name": "Regular payment definition",
              "type": "REGULAR",
              "frequency": self.frequency,
              "frequency_interval": self.frequency_interval,
              "amount":
              {
                "value": self.price,
                "currency": self.currency_code
              },
              "cycles": self.cycles,
              "charge_models": [
              {
                "type": "SHIPPING",
                "amount":
                {
                  "value": self.shipping_charge,
                  "currency": self.currency_code
                }
              },
              {
                "type": "TAX",
                "amount":
                {
                  "value":self.tax
                  "currency": self.currency_code
                }
              }]
            }
            ],
            "merchant_preferences":
            {
              "setup_fee":
              {
                "value": self.setupfee,
                "currency": self.currency_code
              },
              "return_url": "https://example.com/return",
              "cancel_url": "https://example.com/cancel",
              "auto_bill_amount": "YES",
              "initial_fail_amount_action": "CONTINUE",
              "max_fail_attempts": "0"
            }
        }
            
        data = json.dumps(data)
        # print(data)

        r = requests.post(url, headers=headers, data=data)

        if r.status_code == 201:
            return r
        return 'not successful in creating plan'
     
from datetime import datetime
import requests
import json
import uuid

class paypalSubscription:

    # Initializer / Instance Attributes
    def __init__(self, arr):
        self.token = arr['token']
        self.plan_id = arr['plan_id']
        self.email = arr['email']
        self.name = arr['name']
        self.currency_code = arr['currency_code']
        self.price = arr['price']

    def addSubscription(self):

        headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer '+ self.token        
      
        }
        dateObj = datetime.now()
        date = str(dateObj)
        date =date[:19]
        date = date.replace(' ', 'T')
        date = date + 'Z'
       
        data={
          "plan_id": self.plan_id,
          "start_time": date,
          "quantity": "1",
          "shipping_amount": {
            "currency_code": self.currency_code,
            "value": self.price
          },
          "subscriber": {
            "name": {
              "given_name": self.name,
            
            },
            "email_address": self.email,
            "shipping_address": {
              "name": {
                "full_name": self.name
              },
              "address": {
                "address_line_1": "2211 N First Street",
                "address_line_2": "Building 17",
                "admin_area_2": "San Jose",
                "admin_area_1": "CA",
                "postal_code": "95131",
                "country_code": "US"
              }
            }
          },
          "application_context": {
            "brand_name": "walmart",
            "locale": "en-US",
            "shipping_preference": "SET_PROVIDED_ADDRESS",
            "user_action": "SUBSCRIBE_NOW",
            "payment_method": {
              "payer_selected": "PAYPAL",
              "payee_preferred": "IMMEDIATE_PAYMENT_REQUIRED"
            },
            "return_url": "https://example.com/returnUrl",
            "cancel_url": "https://example.com/cancelUrl"
          }
        }
        # return data
        data = json.dumps(data)

        url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions'
     

        r = requests.post(url, headers=headers, data=data)

        # url = 'https://api.sandbox.paypal.com/v1/billing/plans'
        # r = requests.get(url=url, headers=headers)

        response = json.loads(r.text)
        return response
        if r.status_code == 201:
            return response
        return 'not successful in creating plan'

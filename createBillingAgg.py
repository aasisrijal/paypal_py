import requests
import json

class createBillingAgg:
    def __init__(self, token):
        self.token = token
        # self.name = name
        # self.description = description


    def createBillingAgg(self):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ self.token,
            
            }

        url = 'https://api.sandbox.paypal.com/v1/payments/billing-agreements/'

        data ={
          "name": "Service Subscription",
          "description": "Monthly agreement with a regular monthly payment definition",
          "start_date": "2020-03-01T00:00:00Z",
          "plan":
          {
            "id": "P-4NC60250LL934420HHYH422Y"
          },
          "payer":
          {
            "payment_method": "paypal"
          },
          "shipping_address":
          {
            "line1": "751235 Stout Drive",
            "line2": "0976249 Elizabeth Court",
            "city": "Quimby",
            "state": "IA",
            "postal_code": "51049",
            "country_code": "US"
          }
        }
        data = json.dumps(data)    
        r = requests.post(url=url, headers=headers, data=data)
        response = json.loads(r.text)
        return response



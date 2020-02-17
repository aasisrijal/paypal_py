import requests
import json

class activatePlan:

    def __init__(self, token, plan_id):
        self.token = token
        self.plan_id = plan_id

    def activateplan(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ self.token,
            
            }

        url = 'https://api.sandbox.paypal.com/v1/payments/billing-plans/{}'.format(self.plan_id)
        data = [{
          "op": "replace",
          "path": "/",
          "value":
          {
            "state": "ACTIVE"
          }
        }]
        data = json.dumps(data)
        r = requests.patch(url, headers=headers, data=data)

        if r.status_code == 200:
            return 'plan activated'
        return 'not successful in activating plan'
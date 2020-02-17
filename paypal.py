from get_token import get_token
from createPlan import createPlan
from paypalSubscription import paypalSubscription 
from createBillingAgg import createBillingAgg
from activatePlan import activatePlan
from executeAgg import executeAgg
import webbrowser

import json


###importing get_token to generate token for the paypal api authentication
token = get_token()
# print(token)


###data needed to create plan
plandata={
    "token": token,
    "name": "simple cheap plan",
    "description": "good very good plan",
    "frequency": "MONTH",
    "frequency_interval": "1",
    "cycles": "12"
    "currency_code":"USD",
    "price": "12",
    "shipping_charge": "5"
    "setupfee": "2",
    "tax": "12"
}

##create a plan after passing the above plandata
disply = createPlan(plandata)
d = disply.createPlan()
print(d.text)

##after plan is created, response gives us plan_id which is used to activate the plan
##activating the plan
aplan = activateplan(token=token, plan_id='P-4NC60250LL934420HHYH422Y')
a= aplan.activateplan()
print(a)


##after activating the subscription plan, we need to create billing agreement
###creating billing agg
aggrement = createBillingAgg(token=token)
billagg = aggrement.createBillingAgg()
print(billagg)

# print(type(billagg))

##the creation of billing agreement gives us a approval_url which is opened using webbrowser where the user enter payapal credentials for further execution

for link in billagg['links']:
    if link['rel'] == "approval_url":
        approval_url = link['href']
        webbrowser.open_new_tab(approval_url)



##the creation of billing agreement returns response data with a token in approval_url in links
##execution of billing aggrement using the same returned token
final_aggrement = executeAgg(app_token=token, token='EC-2LA98836DS586004A')
finalagg = final_aggrement.executeAgg()
print(finalagg)




# response = disply.createPlan()
# print(response.text)
# print(json.loads(response.text)['id'])
# print('plan_name:{}'.format(json.loads(response.text)['name']))


''' starting point for docusign intergration '''
import json
import requests


DOCU_URL = 'https://demo.docusign.net/restapi/v2/accounts/{accountID}/envelopes'

with open('user_agreement.json', 'r') as agree_data:
    DATA = json.load(agree_data)
with open('credsData.json', 'r') as credData:
    AUTH = json.load(credData)


def user_agreement(admin, user, asset):
    ''' composing of the agreement '''
    querystring = {"api_password": "true"}
    headers = {
        'X-DocuSign-Authentication': "",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
    }
    headers['X-DocuSign-Authentication'] = AUTH['docu_user']
    # admin user
    DATA["recipients"]["signers"][1]["email"] = (admin['email'])
    DATA["recipients"]["signers"][1]["name"] = (admin['name'])
    # end-user
    DATA["recipients"]["signers"][0]["email"] = (user['email'])
    DATA["recipients"]["signers"][0]["name"] = (user['name'])
    # asset
    DATA["recipients"]["signers"][1]["tabs"]["textTabs"][0]["value"] = (asset)
    DATA["recipients"]["signers"][0]["tabs"]["textTabs"][0]["value"] = (asset)
    req = requests.request("POST", url=DOCU_URL, data=json.dumps(
        DATA), headers=headers, params=querystring)
    return req.text

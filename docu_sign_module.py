import requests
import cata_it
import json
#need to be moved to json
docusignUrl='https://demo.docusign.net/restapi/v2/accounts/{accountID}/envelopes'
data = userAgreementFile.data

with open('credsData.json', 'r') as credData:
    auth2=json.load(credData)

def userAgreement(admin,user,asset):
    querystring = {"api_password":"true"}
    headers = {
        'X-DocuSign-Authentication': "",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        }
    headers['X-DocuSign-Authentication']=auth2['docu_user']
    #admin user
    data["recipients"]["signers"][1]["email"]=(admin['email'])
    data["recipients"]["signers"][1]["name"]=(admin['name'])
    #end-user
    data["recipients"]["signers"][0]["email"]=(user['email'])
    data["recipients"]["signers"][0]["name"]=(user['name'])
    #asset
    data["recipients"]["signers"][1]["tabs"]["textTabs"][0]["value"]=(asset)
    data["recipients"]["signers"][0]["tabs"]["textTabs"][0]["value"]=(asset)
    r = requests.request("POST", url=docusignUrl, data=json.dumps(data), headers=headers, params=querystring)
    print(r.text)
    return('done')


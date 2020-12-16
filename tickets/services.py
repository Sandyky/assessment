import os
import requests
import json

#'niket@codewave.com'

# post request to ZOHO API
def post_ticket(data=None):

    url='https://desk.zoho.in/api/v1/tickets'
    headers={"orgId":"60001280952","Authorization": "9446933330c7f886fbdf16782906a9e0"}
    response = requests.post(url=url, headers=headers, data=data)
    # print (response)
    return response

# get request to ZOHO API
def get_tickets(email='niket@codewave.com'):

    url='https://desk.zoho.in/api/v1/tickets'

    headers={"orgId":"60001280952","Authorization": "9446933330c7f886fbdf16782906a9e0"}

    response = requests.get(url=url,headers=headers)

    res_data=None

    tickets_list = ''

    try:
        res_data = json.loads(response.text)
    except:
        pass

    tickets_data = res_data.get('data')

    if email:
        
        tickets_list =list(filter(lambda x:x.get('email')==email, [i for i in tickets_data]))

    # print(tickets_list)

    return tickets_list
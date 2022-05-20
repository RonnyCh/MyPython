
################### Type Client ID Here ##################################
client_id = '7FE3EB1A5A43422690AFF5C850F2B2DF'    # LCA PKCE


######################################################
#                      USER SETUP
######################################################
import json
import base64
import requests
import pandas as pd


redirect_url = 'https://developer.xero.com'
scope = 'offline_access accounting.reports.read'
setting = '%20accounting.reports.read%20accounting.settings.read'
#client_secret = 'VpSRRlg7dUGtVy52pLv0FB19p8tc3IJb67PSJ0rITrD90HH8'
#client_secret = 'YjCN3z8HlGKnO9Uliup70IMXvLkZTtuP8okzz4MumSfqRBZr'
client_secret = 'fUr9qANQNTne6sXMaCoXzGzHty3i1dE2sVJe8iWFAUDUpehe'    # Reza API
b64_id_secret = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')
state = '123'


################### PKCE METHOD ########################
# GENERATE URL TO BRING USER TO WEBSITE TO GET THE CODE#
########################################################

import pkce 
code_verifier = pkce.generate_code_verifier(length=128)
code_challenge = pkce.get_code_challenge(code_verifier)


auth_url = ('https://login.xero.com/identity/connect/authorize?' +
'response_type=code' +
'&client_id=' + client_id +
'&redirect_uri=' + redirect_url +
'&scope=' + scope +
'&code_challenge=' + code_challenge +
'&code_challenge_method=S256' )

print (auth_url)


############ COPY THE CODE FROM THE WEB AND PUT TO code ##########################
############ AND EXCHANGE TOKEN                         ##########################

code = '6e93916c550a34211e0991fedac0212fb8e08e63d82e21caa5c967a34e72faf9'

exchange_code_url = 'https://identity.xero.com/connect/token'
response = requests.post(exchange_code_url,
           headers={
               'Content-Type': 'application/x-www-form-urlencoded'
           },
           data={
              'grant_type': 'authorization_code',
              'client_id' : client_id,
              'code': code,
              'redirect_uri': redirect_url,
              'code_verifier' : code_verifier
})
    
############ SAVE TOKEN FROM THE ABOVE JSON      ##########################
f = open('LCA_PCKETest.txt','w')
refresh_token = response.json()['refresh_token']
f.write(refresh_token)

print (response)



############# IF TIME OUT , REFRESH TOKEN #############
############# REFRESH TOKEN LAST 60 DAYS  #############
########## IT WILL GENERATE NEW ACCESS TOKEN ##########
# open refresh token
f = open('LCA_PCKETest.txt','r')

# get new access token and refresh token
url = 'https://identity.xero.com/connect/token'
response = requests.post(url,
           headers={
               'Content-Type': 'application/x-www-form-urlencoded'
           },
           data={
               'grant_type': 'refresh_token',
               'client_id' : client_id,
               'refresh_token': f
           })

response_dict = response.json()
access_token = response_dict['access_token']
refresh_token = response_dict['refresh_token']


print (refresh_token)


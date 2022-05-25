
############### User Setup ###################

import requests
import base64
import os
import json
import pandas as pd
import base64
import warnings
# turn off pandas warning
warnings.simplefilter(action='ignore', category=FutureWarning)


mymonth = input('YYYY-MM-DD  >>') #### setup your date here before running #######

client_id = 'B628C81B8827482AAC0E3E7BA73676F2'     # LCA REZA API
client_secret = 'fUr9qANQNTne6sXMaCoXzGzHty3i1dE2sVJe8iWFAUDUpehe'    # Reza API


redirect_url = 'https://developer.xero.com'
scope = 'offline_access accounting.reports.read'
setting = '%20accounting.reports.read%20accounting.settings.read'

b64_id_secret = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')
state = '123'



############### Refresh Token ###################


b64_id_secret = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')


# open last refresh token
f = open('LCA_OATHFINAL.txt','r')
refresh_token = f.read()



# get new access token and refresh token
url = 'https://identity.xero.com/connect/token'
response = requests.post(url,
           headers={
               'Authorization': 'Basic ' + b64_id_secret
           },
           data={
               'grant_type': 'refresh_token',
               'client_id' : client_id,
               'refresh_token': refresh_token
           })


response.json()
response_dict = response.json()
access_token = response_dict['access_token']
refresh_token = response_dict['refresh_token']


# save new refresh token
f = open('LCA_OATHFINAL.txt','w')
f = f.write(refresh_token)



############### Test Connection ###################



url = 'https://api.xero.com/connections'
response = requests.get(url,
           headers={
               'Authorization' : 'Bearer '+access_token,
               'Accept' : 'application/json'})

if str(response) != '<Response [200]>':
    print ('********* Token Error **********')
else:
    print ('********* Token Good **********')

####################################################



############### Create CSV ###################

final = pd.DataFrame(columns=['GBL_Period','XRO_Clinic','Section','Desc','XRO_Account','Description','Dr','Cr','YTD Dr','YTD Cr','Amount'])

############# some def for DF ################
def myacct(a):
    # check how many time '(' occur
    # otherwise it will cause problem with the def
    count = 0
    for i in a:
        if i == '(':
            count += 1
    
    # if occur more than once do this and strip spaces  
    if count > 1:
        start = 1
        for j in range(0,count):
            n = a.find('(',start)
            start += n
        
        # get left and righ brackets
        left = n + 1
        right = a.find(')',left)
        return a[left:right]

    # otherwise just do below and strip spaces       
    else:
        # get left and righ brackets
        n = a.find('(')
        left = n + 1
        right = a.find(')',left)
        return a[left:right]


def mydesc(a):
    # check how many time '(' occur
    # otherwise it will cause problem with the def
    count = 0
    for i in a:
        if i == '(':
            count += 1
    
    # if occur more than once do this and strip spaces  
    if count > 1:
        start = 1
        for j in range(0,count):
            n = a.find('(',start)
            start += n
        return a[:n].strip()

    # otherwise just do below and strip spaces       
    else:
        n = a.find('(')
        return a[:n].strip()

################################################

############ get list of tenants ################
url = 'https://api.xero.com/connections'
response = requests.get(url,
           headers={
               'Authorization' : 'Bearer '+access_token,
               'Accept' : 'application/json'})
myjson = json.loads(response.text)


mytenants = []
for i in myjson:
    mytenants.append(i['tenantId'])
###################################################


# let's test just 2 clinics  , you can delete this code later
mytenants = mytenants[:25]


############ put parameter for month ##############
########## Change URL for TRIAL BALANCE ###########


url = 'https://api.xero.com/api.xro/2.0/Reports/TrialBalance?date='+mymonth+'&paymentsOnly=false'

###################################################


######### Get JSON API for each tenant ############
for mytenant in mytenants:
    response = requests.get(url,
            headers={
           'Authorization' : 'Bearer '+access_token,
           'Accept' : 'application/json',
           'Xero-tenant-id' : mytenant})
    data = json.loads(response.text)
###################################################



#### Modified the Json to DataFrame and CSV #######
    for i in data['Reports']:
        for j in i['ReportTitles']:
            if 'Trial' not in j and 'As at' not in j:
                clinicname = j
                

    # get Values from JSON API
    mycell = []
    for i in data['Reports']:
        for j, l1 in enumerate(i['Rows']):
            # only get the data from second row onwards, ignore headers 
            if j != 0:

                # grab section
                mysection = l1['Title']

                # go to dictionary rows section and loop it to find cells
                # from cells you can get all the values for each row
                for l2 in l1['Rows']:
                    #print (l2,'\n')
                    chk = l2['RowType']
                    if chk != 'SummaryRow':
                        myrow = []
                        myrow.append(mysection)
                        for l3 in l2['Cells']:
                            #print (l3['Value'])
                            myrow.append(l3['Value'])
                            mycell.append(myrow)

    # create draft dataframe            
    df = pd.DataFrame(mycell)
    df.columns = ['Section','Desc','Dr','Cr','YTD Dr','YTD Cr']
    print ("This Clinic Completed >>> " + clinicname)
     
    # add additional information to dataframe
    df['XRO_Clinic'] = clinicname
    df['GBL_Period'] = mymonth
    df['XRO_Account'] = df['Desc'].apply(lambda x:myacct(x))
    df['Description'] = df['Desc'].apply(lambda x:mydesc(x))
    
    # convert to numeric, fill na and do calc
    df['YTD Dr'] = pd.to_numeric(df['YTD Dr'],errors='coerce')
    df['YTD Cr'] = pd.to_numeric(df['YTD Cr'],errors='coerce')
    df['YTD Dr'].fillna(0,inplace=True)
    df['YTD Cr'].fillna(0,inplace=True)
    df['Amount'] =  df['YTD Dr'] - df['YTD Cr']

    # final dataframe
    df = df[['GBL_Period','XRO_Clinic','Section','Desc','XRO_Account','Description','Dr','Cr','YTD Dr','YTD Cr','Amount']]
    #df.to_csv(clinicname+'.csv',index=False)
    final = final.append(df)
######################################################   

# remove duplicates in pandas, need to check later why there are duplicates #
final = final.drop_duplicates()


########### CSV for TM1 and Final ###################
tm1 = final[['XRO_Clinic','XRO_Account','Amount']] 
#tm1['XRO_Measure_Trial_Balance'] = 'Balance'
#tm1['GBL_Version'] = 'Actual'
#tm1['GBL_Reporting_Currency'] = 'Local'
tm1.to_csv('TM1.csv',index=False)
final.to_csv('Xero.csv',index=False)
print ("Process Completed!!!!!!!")



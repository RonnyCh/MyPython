
############### User Setup ###################

import requests
import base64
import os
import json
import pandas as pd
import base64
import warnings
import csv
from datetime import datetime, timedelta
import calendar

# turn off pandas warning
warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(r'C:\Users\r.christianto\MyPython\XeroAPI\TBDownload')


##### setup your date here before running #######


x = datetime.now()
yr = x.year
mth = str(x.month - 1)
day = calendar.monthrange(x.year, x.month - 1)
day = str(day[1])

if len(mth) == 1:
    mth = '0' + str(mth)
else:
    mth = str(mth)

mymonth = str(x.year) + '-' + mth + '-' + day

print ("Ready to run ",mymonth)

####################################################################################

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
    print ('********* Token Exchanged Successfully **********')

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

def amt(section,mtd,ytd):
            if section == 'Revenue' or section == 'Expenses':
                return mtd
            else:
                return ytd


########### REZA Code - Org #######################
def XeroOrgFile(access_tokens, xero_tenant_id):
    try:
        # get organisation details and add to file
        ExportFileOrganisations = 'Organisations.txt'
        get_url = 'https://api.xero.com/api.xro/2.0/Organisation'
        response = requests.get(get_url,
                                headers={
                                    'Authorization': 'Bearer ' + access_token,
                                    'Xero-tenant-id': xero_tenant_id,
                                    'Accept': 'application/json'
                                })
        json_response = response.json()["Organisations"]

        # if file doesnt exist, created it and then write header
        if not os.path.exists(ExportFileOrganisations):
            with open(ExportFileOrganisations, "w", newline="", encoding="utf-8") as csvfile:
                f = csv.writer(csvfile, delimiter=";")
                f.writerow(
                    ["Name", "LegalName", "PaysTax", "Version", "OrganisationType", "BaseCurrency", "CountryCode","IsDemoCompany","OrganisationStatus","RegistrationNumber","TaxNumber","FinancialYearEndDay","FinancialYearEndMonth"
                        ,"SalesTaxBasis","SalesTaxPeriod","DefaultSalesTax","DefaultPurchasesTax","PeriodLockDate","CreatedDateUTC","OrganisationEntityType","Timezone","ShortCode","OrganisationId","Edition","Class"])
        # if it exists, append row (use "a+" to append)
        if os.path.exists(ExportFileOrganisations):
            with open(ExportFileOrganisations, "a+", newline="", encoding="utf-8") as csvfile:
                f = csv.writer(csvfile, delimiter=";")
                for organisation in json_response:
                    return_org = organisation.get("Name")
                    f.writerow([
                        organisation.get("Name")
                        , organisation.get("LegalName")
                        , organisation.get("PaysTax")
                        , organisation.get("Version")
                        , organisation.get("OrganisationType")
                        , organisation.get("BaseCurrency")
                        , organisation.get("CountryCode")
                        , organisation.get("IsDemoCompany")
                        , organisation.get("OrganisationStatus")
                        , organisation.get("RegistrationNumber")
                        , organisation.get("TaxNumber")
                        , organisation.get("FinancialYearEndDay")
                        , organisation.get("FinancialYearEndMonth")
                        , organisation.get("SalesTaxBasis")
                        , organisation.get("SalesTaxPeriod")
                        , organisation.get("DefaultSalesTax")
                        , organisation.get("DefaultPurchasesTax")
                        , organisation.get("PeriodLockDate")
                        , organisation.get("CreatedDateUTC")
                        , organisation.get("OrganisationEntityType")
                        , organisation.get("Timezone")
                        , organisation.get("ShortCode")
                        , organisation.get("OrganisationId")
                        , organisation.get("Edition")
                        , organisation.get("Class")
                    ])

        #status = 'Organisation for ' + return_org + ' added into text file'
        #return status
    except:
        return "Error"
    ###################################################

########### REZA Code - Acct #######################


def XeroAcct(access_token, xero_tenant_id, xero_organisation_name):
    try:
        ExportFileAccounts = 'Accounts.txt'
        get_url = 'https://api.xero.com/api.xro/2.0/Accounts'
        response = requests.get(get_url,
                            headers={
                                'Authorization': 'Bearer ' + access_token,
                                'Xero-tenant-id': xero_tenant_id,
                                'Accept': 'application/json'
                            })
        json_response = response.json()["Accounts"]

        # if file doesnt exist, created it and then write header
        if not os.path.exists(ExportFileAccounts):
            with open(ExportFileAccounts, "w", newline="", encoding="utf-8") as csvfile:
                f = csv.writer(csvfile, delimiter=";")
                f.writerow(
                    ["XeroOrganisation","Code", "Name","Type","BankAccountNumber","Status","Description","BankAccountType","CurrencyCode","TaxType","EnablePaymentsToAccount"
                    ,"ShowInExpenseClaims","AccountID","Class","SystemAccount","ReportingCode","ReportingCodeName","HasAttachments","UpdatedDateUTC"])
        # if it exists, append row (use "a+" to append)
        if os.path.exists(ExportFileAccounts):
            with open(ExportFileAccounts, "a+", newline="", encoding="utf-8") as csvfile:
                f = csv.writer(csvfile, delimiter=";")
                for account in json_response:
                    f.writerow([
                        xero_organisation_name
                        , account.get("Code")
                        , account.get("Name")
                        , account.get("Type")
                        , account.get("BankAccountNumber")
                        , account.get("Status")
                        , account.get("Description")
                        , account.get("BankAccountType")
                        , account.get("CurrencyCode")
                        , account.get("TaxType")
                        , account.get("EnablePaymentsToAccount")
                        , account.get("ShowInExpenseClaims")
                        , account.get("AccountID")
                        , account.get("Class")
                        , account.get("SystemAccount")
                        , account.get("ReportingCode")
                        , account.get("ReportingCodeName")
                        , account.get("HasAttachments")
                        , account.get("UpdatedDateUTC")
                    ])
        #status = 'Account for ' + xero_organisation_name + ' added into text file'
        #return status
    except:
        return "Error"


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
    id = i['tenantId']
    name = i['tenantName']
    mytenants.append([id,name])
###################################################


# let's test just 2 clinics  , you can delete this code later
#mytenants = mytenants[1:10]


######### Get JSON API for each tenant ############

total = len(mytenants)

for index,mytenant in enumerate(mytenants):

####### RUN REZA CODES FOR ACCTS AND ORGS ########
    XeroOrgFile(access_token, mytenant[0])
    XeroAcct(access_token, mytenant[0], mytenant[1])

########## URL FOR TRIAL BALANCE #################
    url = 'https://api.xero.com/api.xro/2.0/Reports/TrialBalance?date='+mymonth+'&paymentsOnly=false'
    response = requests.get(url,
            headers={
           'Authorization' : 'Bearer '+access_token,
           'Accept' : 'application/json',
           'Xero-tenant-id' : mytenant[0]})
    data = json.loads(response.text)
###################################################



#### Modified the Json to DataFrame and CSV #######
    for i in data['Reports']:
        for j in i['ReportTitles']:
            if 'Trial' not in j and 'As at' not in j:
                clinicname = j
                
                # amend some clinic names due to name changes
                if clinicname == 'LCNZ St Lukes':
                    clinicname = 'LCNZ St Lukes Pty Limited'
                

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
    if mycell != []:
        df = pd.DataFrame(mycell)
        df.columns = ['Section','Desc','Dr','Cr','YTD Dr','YTD Cr']
        print (index,total,clinicname)
        
        # add additional information to dataframe
        df['XRO_Clinic'] = clinicname
        df['GBL_Period'] = mymonth
        df['XRO_Account'] = df['Desc'].apply(lambda x:myacct(x))
        df['Description'] = df['Desc'].apply(lambda x:mydesc(x))
        
        # convert to numeric, fill na and do calc
        df['Dr'] = pd.to_numeric(df['Dr'],errors='coerce')
        df['Cr'] = pd.to_numeric(df['Cr'],errors='coerce')
        df['YTD Dr'] = pd.to_numeric(df['YTD Dr'],errors='coerce')
        df['YTD Cr'] = pd.to_numeric(df['YTD Cr'],errors='coerce')
        df['Dr'].fillna(0,inplace=True)
        df['Cr'].fillna(0,inplace=True)
        df['YTD Dr'].fillna(0,inplace=True)
        df['YTD Cr'].fillna(0,inplace=True)
        df['MTD'] =  df['Dr'] - df['Cr']
        df['YTD'] =  df['YTD Dr'] - df['YTD Cr']
        df['Amount'] = df.apply(lambda x:amt(x.Section,x.MTD,x.YTD),axis=1)

        # final dataframe
        df = df[['GBL_Period','XRO_Clinic','Section','Desc','XRO_Account','Description','Dr','Cr','YTD Dr','YTD Cr','Amount']]
        #df.to_csv(clinicname+'.csv',index=False)
        final = final.append(df)
    else:
        print (index,total,clinicname + ' *** Warning - No Data *** ')
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


########## convert my TB to Reza text format for FTP ##############

filename = 'TrialBalance_' + mymonth + '_' + mymonth + '.txt'
ftpTB = final[['GBL_Period', 'XRO_Clinic', 'Section', 'XRO_Account',
       'Description', 'Dr', 'Cr', 'YTD Dr', 'YTD Cr']]
ftpTB.columns = ['Date','XeroOrganisation','SectionName','AccountCode','AccountName','Debit','Credit','YTD Debit','YTD Credit']
ftpTB.to_csv(filename,sep=';',index=False)

print ("Process Completed!!!!!!!")

print ('Starting FTP Upload......')

################# FTP Upload #################
import os
import ftplib
from ftplib import FTP_TLS

ftp = FTP_TLS('ccapaprod.planning-analytics.ibmcloud.com')
ftp.login(user='FileShare', passwd='3KThy8DJpk6RWH')
ftp.prot_p()    # you have to run this otherwise won't work
# change remote directory
ftp.cwd("/prod/LCA/XeroImport/XeroExport/dist/api_output")




########## upload the file to FTP Server ###############
########## finallly working ######################
trialbalance = filename
#ftp.set_debuglevel(2)
##ftplib._SSLSocket = None   #### this is key to make upload work!!!! (from reza code)
##with open(filename, "rb") as file:
##    ftp.prot_p()    # you have to run this otherwise won't work
##    # Command for Uploading the file "STOR filename"
##    ftp.storbinary(f"STOR {filename}", file,1024)


for filename in (trialbalance,'Accounts.txt','Organisations.txt'):
    
    try :
        ftplib._SSLSocket = None   #### this is key to make upload work!!!! (from reza code)
        with open(filename, "rb") as file:   #upload Trial Balance
            ftp.prot_p()    # you have to run this otherwise won't work
            # Command for Uploading the file "STOR filename"
            ftp.storbinary(f"STOR {filename}", file,1024)
            print ('This file loaded >> ',filename)
    except:
        print ('Error uploading this >> ',filename)

ftp.quit()



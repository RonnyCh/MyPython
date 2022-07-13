

## download the latest text files from FTP server

import pandas as pd
import os
import ftplib
from ftplib import FTP_TLS


ftp = FTP_TLS('ccapaprod.planning-analytics.ibmcloud.com')
ftp.login(user='FileShare', passwd='3KThy8DJpk6RWH')
ftp.prot_p()    # you have to run this otherwise won't work
# change dir
ftp.cwd("/prod/LCA/XeroImport/XeroExport/dist/api_output")
#ftp.cwd("/prod/LCA/Upload Templates")
# list files
ftp.dir()


# download from FTP server
os.chdir(r'C:\Users\r.christianto\MyPython\XeroAPI\TBDownload')

myfiles = ('TrialBalance_2021-07-31_2021-07-31.txt',
            'TrialBalance_2021-08-31_2021-08-31.txt',
            'TrialBalance_2021-09-30_2021-09-30.txt',
            'TrialBalance_2021-10-31_2021-10-31.txt',
            'TrialBalance_2021-11-30_2021-11-30.txt',
            'TrialBalance_2021-12-31_2021-12-31.txt',
            'TrialBalance_2022-01-31_2022-01-31.txt',
            'TrialBalance_2022-02-28_2022-02-28.txt',
            'TrialBalance_2022-03-31_2022-03-31.txt',
            'TrialBalance_2022-04-30_2022-04-30.txt',
            'TrialBalance_2022-05-31_2022-05-31.txt',
            'TrialBalance_2022-06-30_2022-06-30.txt',)


for filename in myfiles:
    with open(filename, "wb") as file:
        # Command for Downloading the file "RETR filename"
        ftp.retrbinary(f"RETR {filename}", file.write)
ftp.quit()


# read all text files and put to a dataframe
mydf = pd.DataFrame()

for file in myfiles:
    df = pd.read_csv(file,sep=';',skiprows=[0],header=None)
    mydf = mydf.append(df)

mydf.columns = ['Date', 'XeroOrganisation' ,'SectionName', 'AccountCode', 'AccountName',
       'Debit', 'Credit', 'YTD Debit', 'YTD Credit']


mydf['Debit'].fillna(0,inplace=True)
mydf['Credit'].fillna(0,inplace=True)
mydf['YTD Debit'].fillna(0,inplace=True)
mydf['YTD Credit'].fillna(0,inplace=True)


#### fix some of the name issues #####
mydf['XeroOrganisation'].replace('LCUK  Chelmsford Ltd','LCUK Chelmsford Ltd',inplace=True)
mydf['XeroOrganisation'].replace('LCUK  Luton Ltd','LCUK Luton Ltd',inplace=True)
mydf['XeroOrganisation'].replace('LCUK Clapham Ltd','LCUK CLAPHAM LTD',inplace=True)

############################################## load to my sql ###########################################################

from sqlalchemy import create_engine

# Credentials to database connection
hostname="localhost"
dbname="lca"
uname="root"
pwd="Ronchi1989!"


# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
mydf.to_sql('xero_trialbalance', engine, if_exists = 'replace', index=False)
# option for if_exist >>>>> {‘fail’, ‘replace’, ‘append’}

##########################################################################################################################



















##################### ignore lines below for now ##############################


################################## Grab TM1 API CSV and Load to MYSQL #####################################################

tm1 = pd.read_csv('TM1.csv')
tm1.to_sql('xerotm1api', engine, if_exists = 'replace', index=False)
##########################################################################################################################






################################## Reconcile Xero TB vs Xero TM1 #####################################################

import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(r'C:\Users\r.christianto\MyPython\XeroAPI')

# Credentials to database connection
hostname="localhost"
dbname="lca"
uname="root"
pwd="Ronchi1989!"


# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))


# SQL to retrieve from mysql database
SQL = '''
select * from vxero_trialbalance
'''

con = engine.connect()
df1 = pd.read_sql(SQL,con)



SQL = '''
select * from vxero_tm1
'''

con = engine.connect()
df2 = pd.read_sql(SQL,con)


con.close()


exception = pd.merge(df1,df2,how="left",on=['Period','ClinicCodes','Code-Name','ClinicNames','Country','Accountcode','AccountNames','PLBS'])
exception['Amt_x'].fillna(0,inplace=True)
exception['Amt_y'].fillna(0,inplace=True)


exception['Var'] = exception['Amt_x'] - exception['Amt_y']
exception = exception[abs(exception['Var']) > 10]
exception.rename(columns = {'Amt_x':'XEROTB'}, inplace = True)
exception.rename(columns = {'Amt_y':'XEROTM1'}, inplace = True)
   
exception.to_csv('recTM1.csv')   





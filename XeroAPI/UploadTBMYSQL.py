import pandas as pd
import os

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

# read all text files and put to a dataframe
mydf = pd.DataFrame()

for file in myfiles:
    df = pd.read_csv(file,sep=';',skiprows=[0],header=None)
    mydf = pd.concat([mydf,df])

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


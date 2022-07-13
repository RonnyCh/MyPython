
import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')
filetype = 'PNL'
#df = pd.read_csv('Timesheet.csv',parse_dates = ['Start Date','Approved Date','Filled Date'],dayfirst=True)
df = pd.read_csv('20220616PNL.cma',header=None)
#df = pd.read_csv('HierAcct.csv')


if filetype == 'PNL':
    df.columns = ['Cube','Version','Period','Company','Account','CostCentre','Brand','Currency','Type','Amount']
    mycube = 'pnl'
    for i in ['Account','CostCentre','Company']:
        df[i] = df[i].astype('str')
elif filetype == 'FA':   
    df.columns = ['Cube','Version','Period','Company','Centre','Brand','Desc1','AssetNo','Desc2','Amount']
    mycube = 'fixedasset'
elif filetype == 'XeroHier':
    #df.columns = ['XeroAcct','L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','Type']
    df.fillna('',inplace=True)
    mycube = 'xerohier'
elif filetype == 'ClinicMap':
    df.columns = ['ClinicNames','ClinicCodes','Code-Name','Country']
    df.fillna('',inplace=True)
    mycube = 'clinicmap'
elif filetype == 'Xero':
    df.columns = ['Cube','Version','Period','Clinic','Account','Currency','Measure','Amount']
    df.fillna('',inplace=True)
    mycube = 'tm1xero'
elif filetype == 'empcost':
    df.columns = ['Cube','Version','Period','Currency','Company','Centre','Brand','EMPID','Account','Amount']
    df.fillna('',inplace=True)
    mycube = 'empcost'
elif filetype == 'empmaster':
    df.columns = ['Cube','Company','Centre','Brand','EMPID','Header','Values']
    df.fillna('',inplace=True)
    mycube = 'empmaster'
elif filetype == 'empannual':
    df.columns = ['Cube','Version','FinYr','System Code','Header','Values']
    df.fillna('',inplace=True)
    mycube = 'empannual'
elif filetype == 'XeroSource':
    mycube = 'xeroapi'
elif filetype == 'TM1':
    mycube = 'tm1load'
elif filetype == 'MapPeriod':
    mycube = 'mapperiod'
elif filetype == 'hierctr':
    mycube = 'hierctr'
elif filetype == 'hieracct':
    mycube = 'hieracct'



############################################## load to my sql ###########################################################

# Credentials to database connection
hostname="localhost"
dbname="lca"
uname="root"
pwd="Ronchi1989!"


# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
df.to_sql(mycube, engine, if_exists = 'replace', index=False)
# option for if_exist >>>>> {‘fail’, ‘replace’, ‘append’}

##########################################################################################################################




################################# modify emp master #####################################################################

a = df[df['Header']=='System Code']
a = a.drop(columns='Header')
a.columns = ['Cube','Company','Centre','Brand','EMPID','System Code']
mycol = ['Cube','Company','Centre','Brand','EMPID','System Code']


header = [
    'Employee URN',
    'Employee ID',
    'First Name',
    'Last Name',
    'Employee Name',
    'Start Date',
    'Currency',
    'Department',
    'Country',
    'State',
    'Cost Centre Name',
    'Role',
    'Status',
    'Employment Status',
    'FTE',
    'Service',
    'Service Months',
    'End Date']


mykey = ['Cube','Company','Centre','Brand','EMPID']


for i in header:
    b = df[df['Header']==i]
    b = b.drop(columns='Header')
   
    a = pd.merge(a,b,on=mykey, how = 'left')
    
    mycol.append(i)
    a.columns = mycol


df = a
####################################################################################################################################
    




################################# modify emp annual #####################################################################

a = df[df['Header']=='Employee URN']
a = a.drop(columns='Header')
a.columns = ['Cube','Version','FinYr','System Code','Employee URN']
mycol = ['Cube','Version','FinYr','System Code','Employee URN']


header = [
'Last Name',
'Employee Name',
'Employee ID',
'Start Date',
'Company',
'Currency',
'Country',
'State',
'Department',
'Cost Centre',
'Cost Centre Name',
'Brand',
'Role',
'Status',
'Employment Status',
'FTE',
'Service',
'First Name',
'End Date',
'Superannuation %',
'Payroll Tax %',
'Workers Compensation %',
'Base Salary',
'Calculated Salary',
'Calculated Salary - Before Increase',
'Calculated Salary - After Increase',
'Budgeted Salary',
'Phone Allowance',
'Car Allowance',
'Superannuation',
'Payroll Tax',
'Workers Compensation',
'STI %',
'STI $ inc oncosts',
'Annual Increase',
'Annual Increase Start Month',
'Start Month',
'Override Salary',
'End Month',
'% charge',
    ]


mykey = ['Cube','Version','FinYr','System Code']


for i in header:
    b = df[df['Header']==i]
    b = b.drop(columns='Header')
   
    a = pd.merge(a,b,on=mykey, how = 'left')
    
    mycol.append(i)
    a.columns = mycol


df = a




############################## read from mysql and export csv ###################################################
import pandas as pd
from sqlalchemy import create_engine

# Credentials to database connection
hostname="localhost"
dbname="lca"
uname="root"
pwd="Ronchi1989!"


# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))




SQL = '''

select * from vpnldataset

'''


con = engine.connect()
frame = pd.read_sql(SQL,con)


import os
os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')
frame.to_csv('PNL.csv',index=False)
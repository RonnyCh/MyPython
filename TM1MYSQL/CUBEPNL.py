
import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')
filetype = 'hieracct'
#df = pd.read_csv('Timesheet.csv',parse_dates = ['Start Date','Approved Date','Filled Date'],dayfirst=True)
#df = pd.read_csv('20220628Xero.cma',header=None)
df = pd.read_csv('PNLLatest.cma',header=None)


df.columns = ['Cube','Version','Period','Company','Account','CostCentre','Brand','Currency','Type','Amount']
mycube = 'pnl'
for i in ['Account','CostCentre','Company']:
    df[i] = df[i].astype('str')



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

select 
company,
account,
costcentre,
case when costcentre in (0,10,20,30,40,50,130) then 'GROUP'
else Brand end as Brand,
'Manual Input' as submodule,
currency,
concat(version,'_r') as version,
sum(case when period = '2021-01' then amount else 0 end) as '2021-01',
sum(case when period = '2021-02' then amount else 0 end) as '2021-02',
sum(case when period = '2021-03' then amount else 0 end) as '2021-03',
sum(case when period = '2021-04' then amount else 0 end) as '2021-04',
sum(case when period = '2021-05' then amount else 0 end) as '2021-05',
sum(case when period = '2021-06' then amount else 0 end) as '2021-06',
sum(case when period = '2021-07' then amount else 0 end) as '2021-07',
sum(case when period = '2021-08' then amount else 0 end) as '2021-08',
sum(case when period = '2021-09' then amount else 0 end) as '2021-09',
sum(case when period = '2021-10' then amount else 0 end) as '2021-10',
sum(case when period = '2021-11' then amount else 0 end) as '2021-11',
sum(case when period = '2021-12' then amount else 0 end) as '2021-12'
from pnl
where version = 'actual'
group by 1,2,3,4,5,6,7

'''


con = engine.connect()
frame = pd.read_sql(SQL,con)


import os
os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')
frame.to_csv('UploadBrandFY21.csv',index=False)

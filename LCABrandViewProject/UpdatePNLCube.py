
import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')

##################### read files prior up to FY21 and load to mysql #######################################

df1 = pd.read_csv('20220616PNL.cma',header=None)
df1.columns = ['Cube','Version','Period','Company','Account','CostCentre','Brand','Currency','Type','Amount']
mycube = 'pnl'
for i in ['Account','CostCentre','Company']:
    df1[i] = df1[i].astype('str')

df1 = df1[df1['Period'].isin(['2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06',
       '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12',
       '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06',
       '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12',
       '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06',
       '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12'])]

##################### read files after FY22 and load to mysql #######################################

df2 = pd.read_csv('PNLLatest.cma',header=None)
df2.columns = ['Cube','Version','Period','Company','Account','CostCentre','Brand','Currency','Type','Amount']
for i in ['Account','CostCentre','Company']:
    df2[i] = df2[i].astype('str')


################## merge dataframes ######################################
df = pd.concat([df1,df2],ignore_index=True)



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








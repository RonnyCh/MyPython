import snowflake.connector
import pandas as pd
import numpy as np
ctx = snowflake.connector.connect(
    account = 'xb05962.australia-east.azure',
    user = 'PWC_XERO_TM1',
    password = 'wBnb15hz4CaS',
    warehouse = 'XS_READERS',
    database = 'XERO',
    schema = 'JOURNALS'
)
cur = ctx.cursor()


# run sql

sql = '''
SELECT 
DATE,
XEROORGANISATION,
SECTIONNAME,
ACCOUNTCODE,
ACCOUNTNAME,
DEBIT,
CREDIT,
YTDDEBIT,
YTDCREDIT
FROM XERO.JOURNALS.CLINICTRIALBALANCE
where date between '2022-05-01' and '2022-05-31'
'''

x  = cur.execute(sql)
m = cur.fetchall()

df = pd.DataFrame(m)
df.columns = ['Date', 'XeroOrganisation' ,'SectionName', 'AccountCode', 'AccountName',
       'Debit', 'Credit', 'YTD Debit', 'YTD Credit']



############################################## load to my sql ###########################################################

# Credentials to database connection
hostname="localhost"
dbname="lca"
uname="root"
pwd="Ronchi1989!"


# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table                                   
df.to_sql('tm1snowflake', engine, if_exists = 'replace', index=False)
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
select * from TM1vsSnowflake

'''

con = engine.connect()
frame = pd.read_sql(SQL,con)


import os
os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')
frame.to_csv('RecSnowflake.csv',index=False)



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


####################################################################################################################




SQL = '''


select 
period,
case when length(company) = 1 then concat('0',company) else company end as company,
account,
case when length(CostCentre) = 1 then concat('000',costcentre)
when length(CostCentre) = 2 then concat('00',costcentre)
when length(CostCentre) = 3 then concat('0',costcentre)
else CostCentre end as costcentre,
Brand,
'Manual Input' as submodule,
'Local' as currency,
'FY22 Base V5',
sum(case when company in (14,15) then (amount/0.91)
when company in (20,21,26,27) then (amount/1.75)
when company in (24,25) then (amount/1.11)
when company in (22,23) then (amount/1.04)
else amount end) as amt
from pnl
where version in ('FY22 Base V5')

group by 1,2,3,4,5,6,7,8



'''








con = engine.connect()
frame = pd.read_sql(SQL,con)


import os
os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')
frame.to_csv('TM1RerunBrandFY22.csv',index=False)






## Upload File to FTP Server (PAW)
## just go to private folder and click button to refresh

import pandas as pd
import os
import ftplib
from ftplib import FTP_TLS


ftp = FTP_TLS('ccapaprod.planning-analytics.ibmcloud.com')
ftp.login(user='FileShare', passwd='3KThy8DJpk6RWH')
ftp.prot_p()    # you have to run this otherwise won't work
# change dir
ftp.cwd("/prod/LCA/Data/model_upload")
#ftp.cwd("/prod/LCA/Upload Templates")
# list files
ftp.dir()


os.chdir(r'C:\Users\r.christianto\MyPython\TM1MYSQL\DataLatest')
filename = 'TM1RerunBrandFY22.csv'
ftplib._SSLSocket = None   #### this is key to make upload work!!!! (from reza code)
with open(filename, "rb") as file:   #upload Trial Balance
    ftp.prot_p()    # you have to run this otherwise won't work
    # Command for Uploading the file "STOR filename"
    ftp.storbinary(f"STOR {filename}", file,1024)
    print ('This file loaded >> ',filename)


ftp.quit()
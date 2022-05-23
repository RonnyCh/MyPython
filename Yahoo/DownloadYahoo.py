import pandas as pd
import datetime
import math
import numpy as np
from pandas import Series, DataFrame
from sklearn import preprocessing
import matplotlib.pyplot as plt
from datetime import date, timedelta
import datetime
import yfinance as yf

pd.set_option('mode.chained_assignment',None)    # turn off chain error warning since I use loc function properly

# get master file of margin
mycsv = 'https://raw.githubusercontent.com/RonnyCh/mydsbook/master/margin.csv'
mycsv = pd.read_csv(mycsv)
mycsv = mycsv[['ASX Code','Security Name','LVR','Industry','Valuation']]
mycsv = mycsv.rename(columns = {'ASX Code':'Code'})
mystock = mycsv['Code']

# convert to string to make it better with dowloanding tracker
mystring = ''
mylist = []
for i in mystock:
    if i in ['^AORD','^DJI','^FTSE','CL=F']:     # indexes no need to add .AX
        mystring = mystring + ' ' + i
        mylist.append(i)
    elif i in ['TGG','CCL','BIN','JHC','AHY','RDC','VOC','ALF','MLT','AQR','MHH']:
        # EXCLUDE THE CODES ABOVE SINCE THEY HAVE BEEN DELISTED
        continue
    else:
        mystring = mystring + ' ' + i + '.AX'
        mylist.append(i+'.AX')


# pick up data from yahoo finance
start = datetime.date.today() + datetime.timedelta(days=-31)
end = datetime.date.today() + datetime.timedelta(days=1)
data = yf.download(mystring, start=start, end=end, group_by="ticker")


# create columns for dataframe and the dataframe itself
mycol = []
mytbl = pd.DataFrame(columns=mycol)


# looping through the list to modify table
for i in mylist:
    #df = web.DataReader(i, 'yahoo', start, end)[['Close','Volume']]    # old code using datareader (not working well)
    #df = yf.download(i, start=start, end=end)[['Close','Volume']]      # old Yfinance code
    
    df = data[i]     # new one using Yfinance
    df['Code'] = i
    mytbl = mytbl.append(df)


mytbl.to_csv("Yahoo.csv")





import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")


mytbl = pd.read_csv('Yahoo.csv')

list = ['MPL.AX','WPL.AX','AGL.AX','BXB.AX','CSL.AX','AZJ.AX',
        'ORG.AX','ARG.AX','BHP.AX','CBA.AX','ORI.AX','WES.AX',
       'ALD.AX','LLC.AX','CPU.AX','IAG.AX']

plt.figure(figsize=(25, 25))
#plt.rc('xtick',labelsize=8)
#plt.rc('ytick',labelsize=8)
#plt.subplots_adjust(top=1.25, bottom=1.2)

for i, desc in enumerate(list):
   #series = mytbl[mytbl['Code']==list[i]]['Close']    # change the column to vol etc.... 
    #date = mytbl[mytbl['Code']==list[i]]['Date'] 
    plt.subplot(4,4,i+1)
    y = mytbl[mytbl['Code']==list[i]]['Close']
    x = mytbl[mytbl['Code']==list[i]]['Date']
    plt.plot(x,y,linewidth = 1)  
    plt.xticks(fontsize=7,rotation =45)
    #plt.ylabel('Close', fontsize = 10)
    #plt.xlabel(None)
    plt.title(f"{list[i]}",fontsize=8)


plt.show()

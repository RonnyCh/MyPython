def download():
    
        import pandas as pd
        import datetime
        import math
        import numpy as np
        from pandas import Series, DataFrame
        from sklearn import preprocessing
        import matplotlib.pyplot as plt
        from datetime import date, timedelta
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





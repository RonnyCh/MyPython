
def download():

    import pandas as pd
    import datetime
    import yfinance as yf

    ############ create a list/string of codes to download from yahoo finance ##############

    mycsv = pd.read_csv('Margin.csv')
    mycsv = mycsv[['ASX Code','Security Name','LVR']]
    mycsv = mycsv.rename(columns = {'ASX Code':'Code'})


    mystock = mycsv['Code']
    # add some more stocks not in the margin list
    mystock = mystock.append(pd.Series(['^AORD','^DJI','^FTSE','CL=F']),ignore_index=True)

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



    ############ pick up data from yahoo finance (last 120 days) #############################

    start =  datetime.date.today() + datetime.timedelta(days=-31)
    end = datetime.date.today() + datetime.timedelta(days=1)
    data = yf.download(mystring, start=start, end=end, group_by="ticker")



    ######################## create dataframe and export to csv ###############################

    mycol = []
    mytbl = pd.DataFrame(columns=mycol)

    # looping through the list to modify table

    for i in mylist:
        df = data[i]     # new one using Yfinance
        df['Code'] = i
        mytbl = mytbl.append(df)

    # export csv
    mytbl.dropna(inplace=True)
    mytbl.to_csv("Yahoo.csv")




def buy(pctg):
    import os
    import datetime
    import pandas as pd
    import matplotlib.pyplot as plt
    import yfinance as yf
    import seaborn as sns
    pd.set_option('mode.chained_assignment',None)    # turn off chain error warning since I use loc function properly

    # read the original yahoo download from folder
    os.chdir(r'C:\Users\r.christianto\MyPython\Yahoo')
    df = pd.read_csv('Yahoo.csv')
    margin = pd.read_csv('Margin.csv')
    margin['Code'] = margin['ASX Code'] + '.AX'


    df = pd.merge(df,margin,on='Code',how='left')
    df = df.dropna(subset=['LVR'])  # only filter the one with margin 


    # create empty dataframe to combine the loop later

    final = pd.DataFrame()

    # loop all stocks and add new calc
    for i in df.Code.unique().tolist():

        new = df[df['Code'] == i]
        new['Max'] = new['Close'].max()
        new['Min'] = new['Close'].min()
        new['DistMin'] = round((new['Close'] - new['Min'])/new['Close'] * 100,2)
        new['DistMax'] = round((new['Close'] - new['Max'])/new['Close'] * 100,2)
        new['Movement'] = new['Close'].diff(1)
        final = final.append(new)


    # finalise the final dataframe    
    final['Date'] = pd.to_datetime(final['Date'])
    mydate = pd.to_datetime(datetime.date.today())
    final = final[final['Date'] == mydate]


    # filter the result, less than 1% (closer to min) and more than 5% below max (potential upside)
    # basically you trying to buy cheap to be able to sell later 
    final = final[(final['DistMin'] < 1) & (abs(final['DistMax']) > 5) & (final['LVR'] == str(pctg))]

    # produce the list for charting
    list = pd.DataFrame({'Mylist':final.Code.unique().tolist()})
    list.to_csv('mylist.csv',index=False)

    sns.set_style('whitegrid')
    plt.style.use("fivethirtyeight")


    list = pd.read_csv('mylist.csv')['Mylist'].tolist()
    mytbl = df


    plt.figure(figsize=(15, 19))
    #plt.subplots_adjust(top=1.25, bottom=1.2)

    for i, desc in enumerate(list):
        #series = mytbl[mytbl['Code']==list[i]]['Close']    # change the column to vol etc.... 
        #date = mytbl[mytbl['Code']==list[i]]['Date'] 
        plt.subplot(4,4,i+1)
        mytbl[mytbl['Code']==list[i]]['Close'].plot(linewidth = 1)  
        plt.ylabel(None)
        plt.xlabel(None)
        plt.title(f"{list[i]}", fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.xticks(fontsize = 8)

    plt.show()
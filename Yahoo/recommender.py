
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
        mydate = mydate = max(final['Date'])
        final = final[final['Date'] == mydate]


        # filter the result, less than 1% (closer to min) and more than 5% below max (potential upside)
        # basically you trying to buy cheap to be able to sell later 
        final = final[(final['DistMin'] < 1) & (abs(final['DistMax']) > 5) & (final['LVR'] == pctg)]

        # produce the list for charting
        list = pd.DataFrame({'Mylist':final.Code.unique().tolist()})
        list = list[:16]  # pick first 16 only 
        list.to_csv('mylist.csv',index=False)

        sns.set_style('whitegrid')
        plt.style.use("fivethirtyeight")


        list = pd.read_csv('mylist.csv')['Mylist'].tolist()
        mytbl = df


        plt.figure(figsize=(10, 5))
        #plt.subplots_adjust(top=1.25, bottom=1.2)

        for i, desc in enumerate(list):
            plt.subplot(4,4,i+1)


	    # turn of axis in X
            plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            #bottom=False,      # ticks along the bottom edge are off
            #top=False,         # ticks along the top edge are off
            labelbottom=False
            ) # labels along the bottom edge are off


            y = mytbl[mytbl['Code']==list[i]]['Close']
            #x = mytbl[mytbl['Code']==list[i]]['Date']
            plt.plot(y,linewidth = 1)
            plt.yticks(fontsize=7)
            plt.title(f"{list[i]}",fontsize=8)

        plt.show()
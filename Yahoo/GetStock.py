def myshare(mycode):
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    os.chdir(r'C:\Users\r.christianto\MyPython\Yahoo')
    df = pd.read_csv('Yahoo.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Day'] = pd.to_datetime(df['Date']).dt.day_name()
    
    result = df[df['Code']==mycode]

    result['Diff'] = result['Close'].diff(1)
    
     
    plt.figure(figsize=(20, 2.8))
    plt.suptitle(mycode,fontsize=20)

    plt.subplot(2,3,1)
    plt.plot(result['Date'],result['Close'])
    plt.xticks(rotation=45, fontsize=8)
    plt.title('Close')

    plt.subplot(2,3,2)
    plt.bar(result['Date'],result['Volume'])
    plt.xticks(rotation=45, fontsize=8)
    plt.title('Volume')

    plt.subplot(2,3,3)
    plt.bar(result['Date'],result['Diff'])
    plt.xticks(rotation=45)
    plt.title('Daily Movement')

    plt.subplot(2,3,4)
    result['Close'].hist()
    plt.title('Histogram')

    plt.subplot(2,3,5)
    import seaborn as sns
    #order = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday']
    #ax = sns.boxplot(x=result['Day'],y=result['Close'],order=order,data=result)
    ax = sns.boxplot(y=result['Diff'],data=result)
    ax.set_xticklabels(ax.get_xticklabels(),rotation=30)
    ax.set_xlabel(None)
    ax.set_title('Box Plot')

    plt.subplot(2,3,6)
    result['Diff'].hist()
    plt.title('Histogram Daily Movement')


    plt.show()
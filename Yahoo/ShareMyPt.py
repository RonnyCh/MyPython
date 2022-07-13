

def mypt():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    os.chdir(r'C:\Users\r.christianto\MyPython\Yahoo')
    mytbl = pd.read_csv('Yahoo.csv')


    list = ['A200.AX','IAG.AX', 'WOW.AX','BHP.AX','RMD.AX','WDS.AX']


    plt.figure(figsize=(10, 10))
   
    for i, desc in enumerate(list):
        
        plt.subplot(5,4,i+1)
        
        # turn of axis in X
        plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        #bottom=False,      # ticks along the bottom edge are off
        #top=False,         # ticks along the top edge are off
        labelbottom=False
        ) # labels along the bottom edge are off
        
        y = mytbl[mytbl['Code']==list[i]]['Close']
        
        plt.plot(y,linewidth = 1)  
        plt.yticks(fontsize=8)
        plt.title(f"{list[i]}",fontsize=8)

    plt.show()
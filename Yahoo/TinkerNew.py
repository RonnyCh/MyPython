import tkinter as tk
import yahoo 
from tkinter import ttk
import os

# root window
root = tk.Tk()
root.geometry("300x300")
#root.geometry("300x300")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# put some functions for buttons
def click1():
     #os.system('python "DownloadYahoo.py"')
     import yahoo as x
     x.download()


def click2():
     import recommender as x
     myselection = str(selected.get())
     x.buy(myselection)

def click3():
     import GetStock as x
     mycode = username_entry.get()
     if mycode in ['^AORD','^DJI','^FTSE','CL=F']:
        mycode = mycode
     else:
        mycode = mycode.upper() + '.AX'
     x.myshare(mycode)


def click4():
    import Sharetop25 as x
    x.mypt()

def click5():
    import ShareMyPt as x
    x.mypt()
     



###################### Label        #################################
username_label = ttk.Label(root, text="ASX Code:")
username_label.grid(column=0, row=6, padx=5, pady=5)


###################### User Input   #################################
username_entry = ttk.Entry(root)
username_entry.grid(column=0, row=7, sticky=tk.E, padx=5, pady=5)


###################### Radio buttons #################################
selected = tk.StringVar()
r1 = ttk.Radiobutton(root, text='75%', value='75%', variable=selected)
r2 = ttk.Radiobutton(root, text='70%', value='70%', variable=selected)
r3 = ttk.Radiobutton(root, text='65%', value='65%', variable=selected)
r4 = ttk.Radiobutton(root, text='60%', value='60%', variable=selected)

r1.grid(column=0,row=2, padx=5, pady=5) 
r2.grid(column=0,row=3, padx=5, pady=5)    
r3.grid(column=0,row=4, padx=5, pady=5) 
r4.grid(column=0,row=5, padx=5, pady=5)     
    
    
###################### Normal Buttons ################################
buttondl = ttk.Button(root, text="Download Yahoo", command = click1)
buttondl.grid(column=0, row=1, padx=5, pady=5)    


buttonst1 = ttk.Button(root, text="TOP 20 Stocks", command = click4)
buttonst1.grid(column=0, row=8, padx=5, pady=5)    

buttonst2 = ttk.Button(root, text="My Portfolio", command = click5)
buttonst2.grid(column=1, row=8, padx=5, pady=5)    


# button for a stock
login_button = ttk.Button(root, text="Show", command = click3)
login_button.grid(column=1, row=7, padx=5, pady=5)

# button for buy recommendation
buttonbuy = ttk.Button(root, text="Buy Recommendation", command = click2)
buttonbuy.grid(column=1, row=3, padx=5, pady=5)

##########################################################

root.mainloop()
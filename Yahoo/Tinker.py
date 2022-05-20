import tkinter as tk
import os
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('600x400')
root.title('Yahoo Finance')

root.grid()


def download():
    os.system('python "DownloadYahoo.py"')

def pct75():
    os.system('python "Scan75pct.py"')

def pct70():
    os.system('python "Scan70pct.py"')

def pct65():
    os.system('python "Scan65pct.py"')



# start button
start_button = ttk.Button(
    root,
    text='Download',
    command= download
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)


# button 1
start_button = ttk.Button(
    root,
    text='75 Pcter',
    command= pct75
)
start_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)



# button 2
start_button = ttk.Button(
    root,
    text='70 Pcter',
    command= pct70
)
start_button.grid(column=2, row=1, padx=10, pady=10, sticky=tk.E)



# button 3
start_button = ttk.Button(
    root,
    text='65 Pcter',
    command= pct65
)
start_button.grid(column=3, row=1, padx=10, pady=10, sticky=tk.E)



root.mainloop()
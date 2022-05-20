
# create a simple tinker with a button and link to the above py file

import os
#-*- coding: utf-8 -*-
from tkinter import *
master = Tk()

master.geometry('300*200')

def callback():
    os.system('python "DownloadYahoo.py"')

b = Button(master, text="OK", command=callback)

b.pack()


mainloop()
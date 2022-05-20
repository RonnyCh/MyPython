
# create a simple tinker with a button and link to the above py file

import os
#-*- coding: utf-8 -*-
from tkinter import *
master = Tk()

#master.geometry('300*200')


def callback():
    # record until you click right
    import mouse as m    
    events = m.record()
    print (events)

def playback():
    import Replay as x
    x.play()

b = Button(master, text="Record", command=callback)
b.pack()

b = Button(master, text="Replay", command=playback)
b.pack()




mainloop()
import pyautogui
import time
import datetime
import pickle
import mouse
import keyboard
import os

path = os.getcwd()
pyautogui.FAILSAFE = False
newpath = path + '\\Available'
os.chdir(newpath)

# open the file and replay all steps
pickle_off = open ('mysteps.txt', "rb")
myfiles = pickle.load(pickle_off)

# replay all the steps
for myfile in  myfiles:
        pickle_off = open (myfile, "rb")
        event = pickle.load(pickle_off)
    
        if 'kb' in myfile:
            print (event)
            keyboard.play(event)
        else:
            mouse.play(event)

    


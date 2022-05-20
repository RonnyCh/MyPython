import pyautogui
import time
import datetime
import pickle
import mouse
import keyboard
import os

path = os.getcwd()
pyautogui.FAILSAFE = False

# keep the laptop alive until certain time by clicking window button
mydate = datetime.date.today()
awake1 = datetime.time(hour=23,minute=25, second=10)
awake1 = datetime.datetime.combine(mydate,awake1)

away1 = datetime.time(hour=23,minute=25, second=59)
away1 = datetime.datetime.combine(mydate,away1)

awake2 = datetime.time(hour=23,minute=25, second=30)
awake2 = datetime.datetime.combine(mydate,awake2)


while datetime.datetime.now() < awake1:
    # keep computer awake
    pyautogui.click(28,1055)
    time.sleep(8)
    
while datetime.datetime.now() < away1:
    newpath = path + '\\Away'
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

    

    
while datetime.datetime.now() < awake2:
    
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

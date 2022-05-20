import os
import pickle
import mouse
import keyboard

path = os.getcwd()
os.chdir(path)

# open the file and replay all steps
pickle_off = open ('mysteps.txt', "rb")
myfiles = pickle.load(pickle_off)

# replay all the steps
for myfile in  myfiles:
    pickle_off = open (myfile, "rb")
    event = pickle.load(pickle_off)
    
    if 'kb' in myfile:
        keyboard.play(event)
    else:
        mouse.play(event)
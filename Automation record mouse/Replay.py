
import pickle
import mouse
import keyboard
import os

path = os.getcwd()
path = path + '\\Away'
os.chdir(path)

# open the file and replay all steps
pickle_off = open ('mysteps.txt', "rb")
myfiles = pickle.load(pickle_off)

print (myfiles)

# replay all the steps
for myfile in  myfiles:
    pickle_off = open (myfile, "rb")
    event = pickle.load(pickle_off)
    
    if 'kb' in myfile:
      print (event)
      keyboard.play(event)
    else:
      mouse.play(event)
    
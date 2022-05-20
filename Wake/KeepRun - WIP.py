import pyautogui
import time
import datetime
import os
import mouse
import keyboard

path = os.getcwd()
pyautogui.FAILSAFE = False


mydate = datetime.date.today()
mytime = datetime.time(hour=23,minute=55)
mytime = datetime.datetime.combine(mydate,mytime)

while datetime.datetime.now() < mytime:
	pyautogui.click(28,1055)
	time.sleep(15)
	lunchdate = datetime.date.today()
	lunch = datetime.time(hour=23,minute=52)
	lunch = datetime.datetime.combine(mydate,mytime)

	if datetime.datetime.now() > lunch:
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
		    keyboard.play(event)
		else:
		    mouse.play(event)

	
        	
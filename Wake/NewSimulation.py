import pyautogui
import time
import datetime
import os
import mouse
import keyboard

path = os.getcwd()
pyautogui.FAILSAFE = False

hour = pyautogui.prompt(text='Enter Hour in 24 Hr format', title='Hour' , default='17')
minutes = pyautogui.prompt(text='Enter minutes', title='Minutes' , default='30')

mydate = datetime.date.today()


# morning drop off, make it online
startchildcare = datetime.time(hour=int(8),minute=int(30))
finishchildcare = datetime.time(hour=int(9),minute=int(15))

# lunch make it away
startlunch = datetime.time(hour=int(12),minute=int(15))
finishlunch = datetime.time(hour=int(12),minute=int(55))

# school pick up make it online
startpickup = datetime.time(hour=int(14),minute=int(40))
finishpickup = datetime.time(hour=int(15),minute=int(30))

# finish
finaltime = datetime.time(hour=int(hour),minute=int(minutes))
finaltime = datetime.datetime.combine(mydate,mytime)


def teamstatus(event,status):
    # lunch time starts at 12.15
    mytime = datetime.time(hour=int(12),minute=int(15))
    mytime = datetime.datetime.combine(mydate,mytime)



# just click windows button to keep the computer awake
while datetime.datetime.now() < mytime:
	pyautogui.click(28,1055)
	time.sleep(15)
	
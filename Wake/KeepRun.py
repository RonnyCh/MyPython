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
mytime = datetime.time(hour=int(hour),minute=int(minutes))
mytime = datetime.datetime.combine(mydate,mytime)


# just click windows button to keep the computer awake
while datetime.datetime.now() < mytime:
	pyautogui.click(28,1055)
	time.sleep(15)
	
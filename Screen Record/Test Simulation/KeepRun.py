import pyautogui
import time
import datetime
import os
import mouse
import keyboard
import offline
import away

path = os.getcwd()
pyautogui.FAILSAFE = False

hour = pyautogui.prompt(text='Enter Hour in 24 Hr format', title='Hour' , default='17')
minutes = pyautogui.prompt(text='Enter minutes', title='Minutes' , default='30')

# start the timer
start = time.time()

mydate = datetime.date.today()
mytime = datetime.time(hour=int(hour),minute=int(minutes))
mytime = datetime.datetime.combine(mydate,mytime)


# just click windows button to keep the computer awake
status = "Nothing"
while datetime.datetime.now() < mytime:
        # check timer
        duration = time.time() - start

        # if duration > 1 hour, change status to away 
        if duration > 25 and status == "Nothing":
           away.away()
           status = "Next"
        elif duration > 50 and status == "Next":
           offline.offline()
           status = "Done"
        else:
           pyautogui.click(28,1055)
           time.sleep(15)
	
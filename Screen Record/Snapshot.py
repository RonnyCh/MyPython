

############################################################## 
####      This code will take snapshot
####      You have to click two times, beg of point 
####      to end of the frame of the picture. Lastly, press 
####      shift to take snapshot of that frame.
##############################################################

from pynput import mouse
from pynput import keyboard
import time
import pandas as pd
import pyautogui as s

newlist = [] 


def on_click(x, y, button, pressed):
    if pressed:
        newlist.append(['Coordinate',x,y,button])
        print ('Press',x,y,button)
    else:
        print ('Release',x,y,button)


def on_press(key):
    if 'shift' in str(key).lower():
        x1 = newlist[-2][1]
        x2 = newlist[-1][1]
        y1 = newlist[-2][2]
        y2 = newlist[-1][2]
        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)   
        file = 'Snapshot' + str(x1) + '-' + str(y1) + '.png'
        newlist.append(['Snapshot',x1,y1,dx,dy]) 
        s.screenshot(file,region=(x1,y1,dx,dy))
    # if users press esc, stop mouse recording as well as keyboard    
    if key == keyboard.Key.esc:
        m_listener.stop()  # stop mouse
        return False        # exit keyboard 

# Collect events until released
with keyboard.Listener(on_press=on_press) as k_listener, \
        mouse.Listener(on_click=on_click) as m_listener:
    k_listener.join()
    m_listener.join()



############## test ############
x = s.locateCenterOnScreen('SAPLookUp.png')
s.click(x)

s.write('Users')

 
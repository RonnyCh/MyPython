

###################################################################
####      This code will take snapshot
####      You have to click two points to create a frame 
####      Press SHIFT for Snapshot
####      Press ALT for working out delta x and delta ysnap
####      It will print on command prompt
##################################################################

from pynput import mouse
from pynput import keyboard
import time
import pandas as pd
import pyautogui as s
import os

newlist = []    
os.chdir(r'C:\Users\r.christianto\MyPython\Screen Record\Snapshot')
#s.alert('Shift for snapshot, ALT for delta x and y')
filename = s.prompt('Filename??')

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
        
        file = filename + '.png'
        fullfile = filename + str(x1) + '-' + str(y1) + '-' + str(dx) + '-' + str(dy) + '.png'    
        #file = s.prompt('Enter Filename','User Input','Snaphot.png')
        #file = file + '.png'
        try:
            newlist.append(['Snapshot',x1,y1,dx,dy]) 
            s.screenshot(file,region=(x1,y1,dx,dy)) # normal file
            s.screenshot(fullfile,region=(x1,y1,dx,dy)) # full file in case image stuff up pyauto
        except:
            print ('wrong dimension, negative delta')
        print ('Snapshot',x1,y1,dx,dy)
    if 'alt' in str(key).lower():
        x1 = newlist[-2][1]
        x2 = newlist[-1][1]
        y1 = newlist[-2][2]
        y2 = newlist[-1][2] 
        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)   
        newlist.append(['delta',x1,y1,dx,dy]) 
        print (' Delta X >>',dx,' Delta Y >>',dy)

    
    # if users press esc, stop mouse recording as well as keyboard    
    if key == keyboard.Key.esc:
        m_listener.stop()  # stop mouse
        return False        # exit keyboard 

# Collect events until released
with keyboard.Listener(on_press=on_press) as k_listener, mouse.Listener(on_click=on_click) as m_listener:
    k_listener.join()
    m_listener.join()




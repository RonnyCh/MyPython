
# version 2 ( work in progress)

from pynput import mouse
from pynput import keyboard
import pyautogui as s
import time
import json
import pandas as pd

newlist = []
mystring = []
status = ''

def on_move(x, y):
    myx = x
    myy = y
    
def on_click(x, y, button, pressed):
    if len(newlist) > 1 and newlist[-1] == 'Quit':    
        return False
    elif not pressed:
        # if last x,y when pressing different to when release, meaning dragging
        if newlist[-1][1] != x or newlist[-1][2] != y:
            newlist[-1][0] = 'MoveTo'
            if 'left' in str(button):
                button = 'left'
            else:
                button = 'right'
            newlist.append(['DragTo',x,y,button,time.time()])
    elif pressed:
        if 'left' in str(button):
            button = 'left'
        else:
            button = 'right'
        newlist.append(['Click',x,y,button,time.time()])

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    

    if 'Key' in str(key):
         mykey = str(key)[4:len(str(key))]
         newlist.append(['Key',mykey,'','',time.time()])
         #print ('mykey',key,mykey)
    # numlock pad... has different codes
    # write extra codes later
    elif '96' in str(key):
         newlist.append(['Write','0','','',time.time()])
    elif '97' in str(key):
         newlist.append(['Write','1','','',time.time()])
    elif '98' in str(key):
         newlist.append(['Write','2','','',time.time()])
    elif '99' in str(key):
         newlist.append(['Write','3','','',time.time()])
    elif '100' in str(key):
         newlist.append(['Write','4','','',time.time()])
    elif '101' in str(key):
         newlist.append(['Write','5','','',time.time()])
    elif '102' in str(key):
         newlist.append(['Write','6','','',time.time()])
    elif '103' in str(key):
         newlist.append(['Write','7','','',time.time()])
    elif '104' in str(key):
         newlist.append(['Write','8','','',time.time()])
    elif '105' in str(key):
         newlist.append(['Write','9','','',time.time()])
    elif '110' in str(key):
         newlist.append(['Write','.','','',time.time()])
    else:
        letter = str(key)[1:2]
        newlist.append(['Write',letter,'','',time.time()])
        #print ('myletter',key,letter)
    if key == keyboard.Key.esc:
        newlist.append('Quit')
        s.alert("Recording completed!!")
        
       # save the results
       
    
        df = pd.DataFrame(newlist[:-2])
        df.columns = ['Event','X','Y','Button','Time']
        df.to_csv('record.csv',index=False)    
        #textfile = open("a_file.txt", "w")
        
        #for element in newlist:
        #    textfile.write(str(element) + "\n")
        
        #textfile.close()
        
        # Stop listener
        return False 

# Collect events until released
  

with keyboard.Listener(on_release=on_release) as k_listener, mouse.Listener(on_click=on_click, on_scroll=on_scroll) as m_listener:
    k_listener.join()
    m_listener.join()
       
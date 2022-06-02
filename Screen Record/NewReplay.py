

######################################################## 
####      Replay , use pyautogui for keyboard
####      Will prompt which file to open
########################################################

import pyautogui as s 
import pandas as pd
import time
from pynput.mouse import Button, Controller


##### def to change name from keyboard to pyautugui ####
def changename(name):
    if name == 'page_down':
        name = 'pgdn'
    elif name == 'page_up':
        name = 'pgup'
    elif name == 'ctrl_l':
        name = 'ctrl'
    else:
        name = name
    return name
#########################################################

filename = s.prompt('Enter Filename to Replay')
filename = filename + '.csv'

df = pd.read_csv(filename)
mylist = df.values.tolist()
mouse = Controller()


for i in range(len(mylist)):
    action = mylist[i][0]
    x = mylist[i][1]
    y = mylist[i][2]
    add_action = mylist[i][3]
    duration = mylist[i][5]

    if 'Move' in action:
        
        mouse.position = (x,y)
        time.sleep(duration)
    elif 'press' in action:
        
        mouse.press(Button.left)
        time.sleep(duration)
    elif 'release' in action:
        mouse.release(Button.left)
    elif 'Write' in action:
        s.write(x)  
        # need to add other keys
    elif 'key' in action.lower():
        x = str(x)[4:]
        x = changename(x)
        
        if x != 'ctrl' and x != 'esc':
            s.press(x)  
            time.sleep(duration)
    elif 'hot' in action.lower():
        s.hotkey('Ctrl',y)
        time.sleep(duration)
        # need to add other keys

    elif 'Scroll' in action:  
        print (add_action)
        mouse.scroll(0,int(add_action))
        time.sleep(duration)







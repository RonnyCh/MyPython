

############# working with pyautogui writing ###########

# replay
import pyautogui as s 
import pandas as pd
import time
from pynput.mouse import Button, Controller

x = s.prompt('Enter Filename to Replay')
x = x + '.csv'

df = pd.read_csv(x)
mylist = df.values.tolist()
mouse = Controller()


for i in range(len(mylist)):
    action = mylist[i][0]
    x = mylist[i][1]
    y = mylist[i][2]
    add_action = mylist[i][3]

    if 'Move' in action:
        
        mouse.position = (x,y)
        time.sleep(0.025)
    elif 'press' in action:
        
        mouse.press(Button.left)
    elif 'release' in action:
        mouse.release(Button.left)
    elif 'Char' in action:
        s.write(x)  
        # need to add other keys
    elif 'Key' in action:
        x = str(x)[4:]

        # change some of the names for pyautogui
        if x == 'page_down':
            x = 'pgdn'
        elif x == 'page_up':
            x = 'pgup'
        print (x)
        s.press(x)  
        time.sleep(0.15)
        # need to add other keys
    elif 'Scroll' in action:  
        print (add_action)
        mouse.scroll(0,int(add_action))
        time.sleep(0.7)




######################################################## 
####      Record the steps
####      Please note, threading takes a while 
####      so give a few seconds before starting 
####      moving and record
####      Will prompt file save name
########################################################



from pynput import mouse
from pynput import keyboard
import time
import pandas as pd
import pyautogui as s

x = s.prompt('Enter Filename')
x = x + '.csv'

newlist = []

# give a few seconds for user to setup 
#s.alert(text='', title='', button='Start recording, press esc to end')

def on_scroll(x, y, dx, dy):
    newlist.append(['Scroll',x,y,dy])
    print ('Scroll',x,y,dx,dy)

def on_move(x,y):
    newlist.append(['Move',x,y,''])   
    print ('Move',x,y)

def on_click(x, y, button, pressed):
    if pressed:
        newlist.append(['press',x,y,button])
        print ('Press',x,y,button)
    else:
        newlist.append(['release',x,y,button])
        print ('Release',x,y,button)


def on_press(key):
    try:
        print ('Press Char',key.char)       
        newlist.append(['Char',key.char,'','']) 
    except:
        print ('Press',key)    
        newlist.append(['Key',key,'','']) 

def on_release(key):
    print ('Release',key)
    newlist.append(['Release',key,'','']) 
        
    # if users press esc, stop mouse recording as well as keyboard    
    if key == keyboard.Key.esc:
        m_listener.stop()  # stop mouse
        return False       # exit keyboard 

# Collect events until released
with keyboard.Listener(on_release=on_release,on_press=on_press) as k_listener, \
        mouse.Listener(on_click=on_click,on_move=on_move,on_scroll=on_scroll) as m_listener:
    k_listener.join()
    m_listener.join()



df = pd.DataFrame(newlist)
df.columns = ['Action','X','Y','ButtonOrScroll']

df.to_csv(x,index=False)



######################################################## 
####      Replay , use pyautogui for keyboard
####      Will prompt which file to open
########################################################

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
        time.sleep(0.01)
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
        elif x == 'ctrl_l':
            x = 'ctrl'

        print (x)
        s.press(x)  
        time.sleep(0.15)
        # need to add other keys
    elif 'Scroll' in action:  
        print (add_action)
        mouse.scroll(0,int(add_action))
        time.sleep(0.7)


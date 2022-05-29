

from pynput import mouse
from pynput import keyboard
import time
import pandas as pd
import pyautogui as s



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
        newlist.append(['Keyboard enter',key.char,'','']) 
    except:
        print ('Press',key)    
        newlist.append(['Keyboard exit',key,'','']) 

def on_release(key):
    print ('Release',key)
    newlist.append(['Keyboard exit',key,'','']) 
        
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

df.to_csv('test.csv')






# replay
import pyautogui as s 
mylist = df.values.tolist()
keyboard = Controller()
mouse = Controller()


for i in range(len(mylist)):
    action = mylist[i][0]
    x = mylist[i][1]
    y = mylist[i][2]
    add_action = mylist[i][3]
    print (action,'first')
    

    if 'Move' in action:
        
        mouse.position = (x,y)
        time.sleep(0.02)
    elif 'press' in action:
        
        mouse.press(Button.left)
    elif 'release' in action:
        mouse.release(Button.left)
    elif 'enter' in action:
        s.write(x)  # use pyautogui since keyboard module having issue
    elif 'Scroll' in action:
        mouse.scroll(0,add_action)






x = mylist[i][1]
value(x)


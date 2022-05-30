

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
        mykey = key.char
        action = 'Write'
        
    except:
        mykey = key
        action = 'Key'
              
    newlist.append([action,mykey,'','']) 
    print (action,key)
    
def on_release(key):
######################################################## 
####      Added some ctrl function, like
####      ctrl a, ctrl c, ctrl v, ctrl f
####      add more lines as required for ctrl
########################################################


    mykey = key
    if 'x06' in str(mykey):
         # capture Ctrl F
        newlist.append(['Hot','Ctrl','f',''])
        print ('Ctrl F')
    elif 'x01' in str(mykey):
         # capture Ctrl A
        newlist.append(['Hot','Ctrl','a',''])
        print ('Ctrl A')
    elif 'x03' in str(mykey):
         # capture Ctrl C
        newlist.append(['Hot','Ctrl','c',''])
        print ('Ctrl C')
    elif 'x16' in str(mykey):
         # capture Ctrl V
        newlist.append(['Hot','Ctrl','v',''])
        print ('Ctrl V')
    else:
        action = 'Release'
        #newlist.append([action,mykey,'',''])
        print ('Release',mykey)

    
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




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
import os
os.chdir(r'C:\Users\r.christianto\MyPython\Screen Record')

x = s.prompt('Enter Filename')
x = x + '.csv'

newlist = []

# give a few seconds for user to setup 
#s.alert(text='', title='', button='Start recording, press esc to end')

def on_scroll(x, y, dx, dy):
    newlist.append(['Scroll',x,y,dy,time.time()])
    print ('Scroll',x,y,dx,dy)

def on_move(x,y):
    newlist.append(['Move',x,y,'',time.time()])   
    print ('Move',x,y,'',time.time())

def on_click(x, y, button, pressed):
    if pressed:
        newlist.append(['press',x,y,button,time.time()])
        print ('press',x,y,button,time.time())
    else:
        newlist.append(['release',x,y,button,time.time()])
        print ('release',x,y,button,time.time())


def on_press(key):
    try:
        mykey = key.char
        action = 'Write'
        
    except:
        mykey = key
        action = 'Key'
              
    newlist.append([action,mykey,'','',time.time()]) 
    print (action,mykey,'','',time.time())
    
def on_release(key):
######################################################## 
####      Added some ctrl function, like
####      ctrl a, ctrl c, ctrl v, ctrl f
####      add more lines as required for ctrl
########################################################


    mykey = key
    if 'x06' in str(mykey):
         # capture Ctrl F
        newlist.append(['Hot','Ctrl','f','',time.time()])
        print ('Ctrl F')
    elif 'x01' in str(mykey):
         # capture Ctrl A
        newlist.append(['Hot','Ctrl','a','',time.time()])
        print ('Ctrl A')
    elif 'x03' in str(mykey):
         # capture Ctrl C
        newlist.append(['Hot','Ctrl','c','',time.time()])
        print ('Ctrl C')
    elif 'x16' in str(mykey):
         # capture Ctrl V
        newlist.append(['Hot','Ctrl','v','',time.time()])
        print ('Ctrl V')
    else:
        action = 'Release'
        #newlist.append([action,mykey,'','',time.time()])
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


for i in range(len(newlist)):
    
    if i == 0:
        newlist[i].append(0)
    else:
        time_now    = newlist[i][4]
        time_before = newlist[i-1][4]
        newlist[i].append(time_now - time_before)


df = pd.DataFrame(newlist)
df.columns = ['Action','X','Y','ButtonOrScroll','Time','Duration']

df.to_csv(x,index=False)



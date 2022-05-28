

from pynput import mouse
from pynput import keyboard
import time
import pandas as pd
import pyautogui as s

orig_list = []
newlist = []

# give a few seconds for user to setup 
s.alert(text='', title='', button='Start recording, press esc to end')


def on_move(x,y):
    newlist.append(['Move',x,y,'',time.time()])   
    print (x,y)

def on_click(x, y, button, pressed):
    if pressed:
        orig_list.append([x,y,button,"pressed"])   # record original list
        if 'left' in str(button):
            button = 'left'
        else:
            button = 'right'
        newlist.append(['Click',x,y,button,time.time()])
    elif not pressed and newlist != []:
        orig_list.append([x,y,button,"not pressed"])
        # if last x,y when pressing different to when release, meaning dragging
        if newlist[-1][1] != x or newlist[-1][2] != y:
            
            newlist[-1][0] = 'MoveTo'
            x = newlist[-1][1]  # keep x the same for dragging
            if 'left' in str(button):
                button = 'left'
            else:
                button = 'right'
            newlist.append(['DragTo',x,y,button,time.time()])
        
        
def on_release(key):

    orig_list.append([key])     
    if 'Key' in str(key):
         mykey = str(key)[4:len(str(key))]
         newlist.append(['Key',mykey,'None','None',time.time()])    
    else :
        letter = str(key)[1:2]
        newlist.append(['Write',letter,'None','None',time.time()])
        
    # if users press esc, stop mouse recording as well as keyboard    
    if key == keyboard.Key.esc:
        m_listener.stop()  # stop mouse
        return False       # exit keyboard 

# Collect events until released
with keyboard.Listener(on_release=on_release) as k_listener, \
        mouse.Listener(on_click=on_click,on_move=on_move) as m_listener:
    k_listener.join()
    m_listener.join()


# create pandas dataframe and to csv
df = pd.DataFrame(newlist, columns = ['Event','X', 'Y','Button','Time'])
df['TimeDiff'] = df['Time'].diff(1)
df = df.fillna(0) # first row of diff will na, so just put zero
df.to_csv(r"C:\Users\r.christianto\MyPython\Screen Record\record.csv",index=False)

# record original list
with open(r"C:\Users\r.christianto\MyPython\Screen Record\mylist.txt","w") as file:
    # write elements of list
    for item in orig_list:
        file.write('%s\n' %item)
file.close()



s.alert(text='', title='', button='Recording finished')
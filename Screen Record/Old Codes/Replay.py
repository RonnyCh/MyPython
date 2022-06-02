import pyautogui as s
import time
import pandas as pd

# give a few seconds for user to setup 
s.alert(text='', title='', button='Start Replay')


newlist = pd.read_csv("record.csv")
newlist = newlist.values.tolist()

print (newlist)

# replay

# add duration to the list

for index, i in enumerate(newlist):
   try :
    if index != 0:
        now = newlist[index][4]
        before = newlist[index-1][4]
        duration = now - before
        newlist[index].append(duration)
    else:
        newlist[index].append(0)
   except:
        break

# remove the last 2 which is esc and quit commands
list = newlist

for i in range(len(list)):
    if 'Click' in list[i][0]:
        x = int(list[i][1])
        y = int(list[i][2])
        button = list[i][3]
        duration = list[i][5]
        s.moveTo(x,y,0.5)
        # pause to let web refresh etc
        time.sleep(duration)
        s.click(button=button)
        
        #time.sleep(0.9)
    elif 'Write' in list[i][0]:
        s.write(list[i][1],0.1)
    elif 'Key' in list[i][0]:
        s.press(list[i][1])
        time.sleep(0.5)
    elif 'MoveTo' in list[i][0]:
        x = list[i][1]
        y = list[i][2]
        
        duration = list[i][5]
        print (x,y)
        s.moveTo(x,y,0.8)
        # pause to let web refresh etc
        time.sleep(duration)
       
        s.moveTo(x,y,1)
    elif 'DragTo' in list[i][0]:
        x = list[i][1]
        y = list[i][2]
       
        s.dragTo(x,y,1)
        
s.alert("Done")    
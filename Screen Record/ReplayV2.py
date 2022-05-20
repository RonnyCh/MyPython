import pyautogui as s
import pandas as pd
import time

s.alert(text='', title='', button='Press OK to Replay')

df = pd.read_csv(r"C:\Users\r.christianto\MyPython\Screen Record\record.csv")
df = df[:-1]
#df['X'] = df['X'].astype(int)
#df['Y'] = df['Y'].astype(int)

list = df.values.tolist()

for i in range(len(list)):
    if 'Click' in list[i][0]:
        x = int(list[i][1])
        y = int(list[i][2])
        button = list[i][3]
        duration = list[i][5]
        s.moveTo(x,y,duration)
        # pause to let web refresh etc
        #time.sleep(duration)
        s.click(button=button)
        
        #time.sleep(0.9)
    elif 'Write' in list[i][0]:
        s.write(list[i][1],0.1)
    elif 'Key' in list[i][0]:
        
        # some of the names need to be changed for pyautogui
        if list[i][1] == 'page_down':
            list[i][1] = 'pgdn'
        elif list[i][1] == 'page_up':
            list[i][1] = 'pgup'
        s.press(list[i][1])
        time.sleep(0.5)
    elif 'MoveTo' in list[i][0]:
        x = int(list[i][1])
        y = int(list[i][2])
        duration = list[i][5]
        print (x,y,duration)
        s.moveTo(x,y,duration)
        # pause to let web refresh etc
        #time.sleep(duration)
       
    elif 'DragTo' in list[i][0]:
        x = int(list[i][1])
        y = int(list[i][2])
        duration = list[i][5]
       
        s.dragTo(x,y,duration)

s.alert("Replay completed")
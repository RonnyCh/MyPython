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
	
        if duration > 1:
            # if duration greater that 1 seconds, just limit the move to 1 second. Otherwise too slow!
            s.moveTo(x,y,1)
            time.sleep(duration)
            s.click(button=button)
        else:
            s.moveTo(x,y,duration)
            s.click(button=button)
            
        #time.sleep(0.9)
    elif 'Write' in list[i][0]:
        duration = list[i][5]
        s.write(list[i][1],duration)
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
        s.moveTo(x,y,1)
        time.sleep(duration)
        # pause to let web refresh etc
        #time.sleep(duration)
       
    elif 'DragTo' in list[i][0]:
        x = int(list[i][1])
        y = int(list[i][2])
        duration = list[i][5]
       
        s.dragTo(x,y,duration)

s.alert("Replay completed")
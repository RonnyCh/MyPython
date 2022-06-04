##### Automate SAP User Add #####

import pyautogui as s
import time
import os

userid = 'U01258'
username = 'hayley.kong'
useremail = 'h.kong@laserclinics.com.au'
usergroup = 'finance'   # this is finance group, change accordingly
supplierapproval = 'No'
db = 'LCS Operations'

os.chdir(r'C:\Users\r.christianto\MyPython\SAP\Snapshot')
###########################################################################################################

###########################################################################################################
def findimage(image, mylimit = 10,acc = 0.99, click = 1, dx = 0, dy=0, duration = 0.7, sleep=0, write = 'None'):
    # chdir to snapshot so images can be picked
    os.chdir(r'C:\Users\r.christianto\MyPython\SAP\Snapshot')
    # put new images here
    
    start = time.time()
      
    # try to find image within the timer given, otherwise print errors
    while True:
        x = s.locateCenterOnScreen(image, confidence = acc)
        #x = s.locateCenterOnScreen(myimage[number])
        
        if x is not None:   # found the pic
            print ('Executing... ', image)
            s.moveTo(x[0],x[1],1.5)

            if dx != 0 or dy !=0:  #offset if user asks
                s.move(dx,dy, duration)
                s.click(clicks=click)
            else:
                s.click(clicks=click) 
            
            if write != 'None':
                s.write(write,interval=0.15)
                s.press('enter')
            
            time.sleep(sleep)
            return x
            break
        else:  # do timer to stop searching after 10 seconds
            timer = time.time() - start
            #print (timer)
            if timer > mylimit:
                print ('Abort due to missing ',image)
                return x
                break
###########################################################################################################


############## change database ##############

x = findimage('SAP_name.png')
x = findimage('filter.png')
x = findimage('clear.png')

x = findimage('rule.png')
for i in range(1,16):
    s.press('up')

for i in range(1,9):
    s.press('down')

s.press('enter')

x = findimage('value.png',write=db,click=2)
x = findimage('filterword.png',click=4)
x = findimage('companyname.png',dy=20,click=4)
#############################################

start = time.time()
## Find SAP Look up Menu
x = findimage('SAP_lookup.png')

## If hidden, open it
if x == None:
    x = findimage('SAP_menu.png')
    # try again!
    x = findimage('SAP_lookup.png',write='users')
else:
    x = findimage('SAP_lookup.png',write='users')

## Click on Users
x = findimage('SAP_user.png',acc=0.9)

## Click on binocolar to find user id
x = findimage('SAP_binocular.png',write=userid)

## If supplier approval not there, show it
x = findimage('SAP_supplierapproval.png')
if x is None:
        s.hotkey('alt','v')
        time.sleep(0.5)
        s.press('u')
        x = findimage('SAP_supplierapproval.png')


x = findimage('generaltab.png',acc=0.9)
x = findimage('username.png',click = 2, dx=250,write=username)
x = findimage('email.png',dx=250,click = 2, write=useremail)
x = findimage('group.png',dx=420)

# assign diff user group, update as required
if usergroup == 'finance':
    x = findimage('1.png',dx=30)
else:
    x = findimage('5.png',dx=30)

x = findimage('update.png',click=3)

## set supplier approval status
if supplierapproval == 'Yes':
    x = findimage('supplierapproval.png',dx=100)
    s.press('up')
    s.press('enter')
    #s.screenshot('GeneralTab.png')

## display tab
x = findimage('display.png')
x = findimage('font.png',dx=182,write='a')
x = findimage('fontsize.png',dx=182,write='12')

## service tab
x = findimage('services.png')
x = findimage('perform.png',dx=-35,dy=32)
x = findimage('perform.png',dx=-35,dy=52)
x = findimage('perform.png',dx=-30,dy=72)
x = findimage('perform.png',dx=-30,dy=140)
x = findimage('perform.png',dx=-30,dy=410, click=3)

finish = time.time()
total = round((finish - start)/60,2)
print ('Finish in ...',total)


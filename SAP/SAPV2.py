##### Automate SAP User Add #####

userid = 'u01122'
username = 'laxmi.gopalkrishnan'
useremail = 'l.gopalkrishnan@laserclinics.ca'
usergroup = 'finance'   # this is finance group, change accordingly
supplierapproval = 'Yes'
db = 'UKSL'


###############################################################################################
# best way to change database 
# note issue is with images not found by pyautogui
# known issue from my westpac days
# need to find a way to get around this
###############################################################################################
import pyautogui as s
import time
import os


###########################################################################################################
def findimage(image, mylimit,acc = 0.99):
    # chdir to snapshot so images can be picked
    os.chdir(r'C:\Users\r.christianto\MyPython\Screen Record\Snapshot')
    # put new images here
    
    start = time.time()
      
    # try to find image within the timer given, otherwise print errors
    while True:
        x = s.locateCenterOnScreen(image, confidence = acc)
        #x = s.locateCenterOnScreen(myimage[number])
        
        if x is not None:   # found the pic
            print ('Executing... ', image)
            s.moveTo(x[0],x[1],1.5)
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


myimages =  ['SAP_name.png','filter.png','clear.png','Rule.png','value.png','filterword.png','companyname.png',
            'SAP_Menu.png','SAP_lookup.png','SAP_user.png','SAP_binocular.png','generaltab.png','username.png',
            'email.png','group.png',
            'filtercompany.png','databasewindow.png','SAP_lookup.png','SAP_supplierapproval.png',
            '1.png','5.png','supplierapproval.png',
            'display.png','font.png','fontsize.png','DisplayTab.png']

# below codes categorise typical actions against images
# add more as you find new scenarios
# you just need to assign each image to each action/category below
for index,image in enumerate(myimages):

    # action 1, find and click
    if index in (0,1,2,5,9,11,14):
       

        if index == 5:
            clicks = 2
            myconfidence = 0.99
        elif index == 9:
            clicks = 1
            myconfidence = 0.9
        else:
            clicks = 1
            myconfidence = 0.99

        findme = findimage(image,10,myconfidence)
        if findme is None:
            break

        s.click(clicks = clicks)
        time.sleep(1.5)

    # action 2, find, click and press
    elif index == 3:
        findme = findimage(image,10)
        if findme is None:
            break

        s.click()
        
        for i in range(1,16):
            s.press('up')
        
        for i in range(1,9):
            s.press('down')
        s.press('enter')

        time.sleep(1.5)

    # action 3, find, click and write
    elif index in (4,10):
        findme = findimage(image,10,0.9)
        if findme is None:
            break

        if index == 4:
            s.click(clicks=2)
            s.write('UKSL')

        
        if index == 10:
            s.write(userid)
            s.press('enter')


    # action 4, find , offset and click
    elif index in (6,12,13):
        if index == 6:
            myx = 0
            myy = 20
            myclick = 6
            myconfidence = 0.9
            sleep = 10 # give database more time
        elif index in (12,13):
            myx = 250
            myy = 0
            myclick = 1
            myconfidence = 0.9
            sleep = 1 # give database more time

        else:
            myx = 0
            myy = 20
            myclick = 1
            myconfidence = 0.9
            sleep = 1
        
        findme = findimage(image,10,myconfidence) # companyname
        if findme is None:
            break

        s.move(myx,myy,1) # offset
        s.click(clicks=myclick,interval=0.2)
        time.sleep(sleep)

    # action 5, wait screen to refresh until the picture can be found
    elif index == 7:
        findme = findimage(image,180)
        if findme is None:
            break
        else:
            print ('Refresh finish, continue .....')

    # action 6, search twice....after unhiding
    if index == 8 :
        findme = findimage(image,10)

        if findme is None:
            findme = findimage('SAP_Menu.png',10)
            s.click()

        # search again
        findme = findimage(image,10)
        if findme is None:
            break

        # write    
        s.click()
        s.write('users')    



########################## tested up to the above #################################


x = s.locateCenterOnScreen('generaltab.png',confidence=0.9)
s.moveTo(x[0],x[1],1.5)


findimage(0,10) # click name Ronny C (shortcut to get list of databases)
s.click()
time.sleep(1.5)

findimage(1,10) # filter button
s.click()
time.sleep(1.5)

findimage(2,10) # clear button
s.click()
time.sleep(1.5)



# Field Rule *****
# move to drop down box , go up (reset)
# move to word contains, 9th row
findimage(3,10) # filter company
s.move(143,1) # offset
s.click()
for i in range(1,16):
    s.press('up')
for i in range(1,9):
    s.press('down')
s.press('enter')

# Field Value *****
findimage(3,10) # filter company
s.move(281,1) # offset
s.click(clicks = 2)
s.write(db, interval=0.2) # type search word
findimage(4,10) # filter button
s.click(clicks=4,interval=0.5)

findimage(5,10,0.7) # companyname
s.move(0,20,1) # offset
s.click(clicks=6,interval=0.2)

print ('Give 10 seconds for database to start')
time.sleep(10) # let the database starting


menu = findimage(8,180) # find menu panel (timer 180 seconds)
print (menu)
lookup = findimage(9,4) # find lookup button

if lookup is None:
    s.click(menu)   # ready to setup use now!
    time.sleep(2)
    
## Type Users
findimage(9,4) # search again
s.click()
s.write('users', interval = 0.25)

## Click on Users
findimage(10,5,0.9)  # user
s.click(clicks = 2, interval = 0.25)

## Click on binocolar to find user id
findimage(11,10)  # binocolar
s.click()

## Write user id to search
time.sleep(1)
s.write(userid)
time.sleep(0.2)
s.press('enter')


## check supplier approval
x = findimage(12,10)

if x is None:
    s.hotkey('alt','v')
    time.sleep(0.5)
    s.press('u')
    x = findimage(12,10) # check again





####################################################################
#                  General Tab                                      
####################################################################

## general tab
findimage(13,10)   # general tab
s.click()

## username
findimage(14,10)   # user name
s.move(250,0)    # move right 10 pixels
s.click(clicks=2)
s.write(username,interval = 0.25)

## email
findimage(15,10)   # user name
s.move(250,0)    # move right 10 pixels
s.click(clicks=2)
s.write(useremail,interval = 0.25)

## Open User Group Panel
findimage(16,10)   # user group
s.move(420,0)    # move right 10 pixels
s.click()

## Assign group e.g finance


if usergroup == 'finance':
    number = 17
elif usergroup == 'financesuperuser':
    number = 18

findimage(number,10)
s.move(30,0)    # move right 10 pixels
s.click()

## set supplier approval status
if supplierapproval == 'Yes':
    findimage(number,19)
    s.move(100,0)    # move right 10 pixels
    s.click()
    s.press('up')
    s.press('enter')
    s.screenshot('GeneralTab.png')


####################################################################
#                  Display Tab                                      
####################################################################



## diplay tab
findimage(number,20)
s.click()
time.sleep(1)

## font
findimage(number,21)
s.click()
s.move(182,0)    # move right 10 pixels
s.click()
s.write('a') # font type ARIAL
time.sleep(1)
s.press('enter')

## font size
findimage(number,22)
s.click()
s.move(182,0)    # move right 10 pixels
s.click()
s.write('12')  # font size 10
time.sleep(1)
s.press('enter')

s.screenshot()

finish = time.time()
duration = finish - start
print (duration/60)



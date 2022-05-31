##### Automate SAP User Add #####

userid = 'u01224'
username = 'matthew.howell'
useremail = 'm.howell@laserclinics.com.au'
usergroup = '5.png'   # this is finance group, change accordingly
supplierapproval = 'Yes'
dbname = 'DRR'

#################################


import pyautogui as s
import time


start = time.time()
## Find SAP Look up Menu
x = s.locateCenterOnScreen('SAP_lookup.png', confidence=0.9)

## If hidden, open it
if x == None:
    print ('found nothing')
    x = s.locateCenterOnScreen('SAP_menu.png', confidence=0.9)
    s.moveTo(x[0],x[1],2)
    s.click()
    # try again!
    time.sleep(2)
    x = s.locateCenterOnScreen('SAP_lookup.png', confidence=0.9)


## Search User Panel
s.moveTo(x[0],x[1],2)
s.click()
time.sleep(0.8)
s.write('users', interval = 0.25)

## Click on Users
time.sleep(1)
x = s.locateCenterOnScreen('SAP_user.png', confidence=0.9)
s.moveTo(x[0],x[1],2)
s.click()

## Click on binocolar to find user id
time.sleep(1)
x = s.locateCenterOnScreen('SAP_binocular.png', confidence=0.9)
s.moveTo(x[0],x[1],2)
s.click()

## Write user id to search
s.write(userid)
time.sleep(0.2)
s.press('enter')


### check image errors before running the steps ###
### fucking pyautogui issue!!!   
### you can also do this for testing to see if images
### consisten and can be applied accross databases
###################################################

myimages = ['SAP_supplierapproval.png','generaltab.png','username.png','email.png','group.png',
            'display.png']
count = 0
for i in myimages:
    x = s.locateCenterOnScreen(i, confidence=0.7)
    if x is None:
        count += 1
        print (i,'is missing')
    else:
        print (i,'is found')
        s.moveTo(x[0],x[1],1)

if count != 0 :
    print ('IMAGE ERRORS!! CANT PROCEED')

else:
    #################################################################
    #### if no errors, continue with the rest of the codes below ####
    #################################################################

    ## If supplier approval not there, show it
    x = s.locateCenterOnScreen('SAP_supplierapproval.png', confidence=0.9)

    if x is None:
        s.hotkey('alt','v')
        time.sleep(0.5)
        s.press('u')
        if x is None:
            print ('issue, image error')

    time.sleep(0.6)

    ####################################################################
    #                  General Tab                                      
    ####################################################################

    ## general tab
    x = s.locateCenterOnScreen('generaltab.png', confidence=0.9) 
    s.moveTo(x[0],x[1],2)
    s.click()
    time.sleep(1)


    ## username
    x = s.locateCenterOnScreen('username.png', confidence=0.9)  # no 5 is finance superuser
    s.moveTo(x[0],x[1],2)
    s.move(250,0)    # move right 10 pixels
    s.click()
    s.write(username,interval = 0.25)

    ## email
    x = s.locateCenterOnScreen('email.png', confidence=0.9)  # no 5 is finance superuser
    s.moveTo(x[0],x[1],2)
    s.move(250,0)    # move right 10 pixels
    s.click()
    s.write(useremail,interval = 0.25)


    ## Open User Group Panel
    x = s.locateCenterOnScreen('group.png', confidence=0.9)  # no 5 is finance superuser
    s.moveTo(x[0],x[1],2)
    s.move(420,0)    # move right 10 pixels
    s.click()
    time.sleep(1)

    ## Assign Group to user
    x = s.locateCenterOnScreen(usergroup, confidence=0.9)  # no 5 is finance superuser
    s.moveTo(x[0],x[1],2)
    s.move(30,0)    # move right 10 pixels
    s.click()
    x = s.locateCenterOnScreen('update.png', confidence=0.9) # update button
    s.moveTo(x[0],x[1],2)
    s.click(clicks=2)

    ## set supplier approval status
    if supplierapproval == 'Yes':
        x = s.locateCenterOnScreen('supplierapproval.png', confidence=0.9)  
        s.moveTo(x[0],x[1],2)
        s.move(100,0)    # move right 10 pixels
        s.click()
        s.press('up')
        s.press('enter')
        s.screenshot('GeneralTab.png')

    ####################################################################
    ##### add codes to send email with screen shot once completed, 
    ##### that would be cool!! 
    ####################################################################


    ####################################################################
    #                  Display Tab                                      
    ####################################################################

    ## diplay tab
    x = s.locateCenterOnScreen('display.png', confidence=0.9) 
    s.moveTo(x[0],x[1],2)
    s.click()
    time.sleep(1)

    ## font
    x = s.locateCenterOnScreen('font.png', confidence=0.9) 
    s.moveTo(x[0],x[1],2)
    s.move(182,0)    # move right 10 pixels
    s.click()
    s.write('a') # font type ARIAL
    time.sleep(1)
    s.press('enter')

    ## font size
    x = s.locateCenterOnScreen('fontsize.png', confidence=0.9) 
    s.moveTo(x[0],x[1],2)
    s.move(182,0)    # move right 10 pixels
    s.click()
    s.write('12')  # font size 10
    time.sleep(1)
    s.press('enter')

    s.screenshot('DisplayTab.png')

    finish = time.time()
    duration = finish - start
    print (duration/60)










###############################################################################################
# best way to change database 
# note issue is with images not found by pyautogui
# known issue from my westpac days
# need to find a way to get around this
###############################################################################################


dbname = 'DRR'

x = s.locateCenterOnScreen('SAP_name.png', confidence=0.9) # click name Ronny C (shortcut to get list of databases)
s.moveTo(x[0],x[1],2)
s.click()
time.sleep(1.5)

x = s.locateCenterOnScreen('filter.png', confidence=0.7)  # filter button
s.moveTo(x[0],x[1],2)
s.click()
time.sleep(1)

x = s.locateCenterOnScreen('filtercompany.png', confidence=0.7)  # filter company


# Field Rule *****
# move to drop down box , go up (reset)
# move to word contains, 9th row
s.moveTo(x[0],x[1],2)
s.move(143,1) # offset
s.click()
for i in range(1,16):
    s.press('up')
for i in range(1,9):
    s.press('down')
s.press('enter')

# Field Value *****
s.moveTo(x[0],x[1],2)
s.move(281,1) # offset
s.click(clicks = 2)
s.write(dbname) # type search word
x = s.locateCenterOnScreen('filterword.png')  # filter button
s.moveTo(x[0],x[1],2)
s.click(clicks=4,interval=0.5)


x = s.locateCenterOnScreen('companyname.png',confidence=0.9)  # filter choose company
s.moveTo(x[0],x[1],2)
s.move(0,20,1)
s.click(clicks=4,interval=0.5)

###############################################################################################











co = s.locateCenterOnScreen('filtertable.png', confidence=0.9) # select company within filter
s.moveTo(co[0],co[1],1)
s.move(160,66) # click rule box 
s.click()
s.move(0,197,0.5) # select word contains
s.click()
time.sleep(0.5)
s.moveTo(co[0],co[1],1) # baseline point
s.move(348,61) # click value box
s.click(clicks=2)
s.write(dbname) # type search word
s.moveTo(co[0],co[1],1) # baseline point
s.move(20,487,0.5) # click filter
s.click(clicks=2,interval=0.2)


## use this for scroll down
#s.moveTo(1141,154,2)
s.moveTo(co[0],co[1],1)
s.move(680,0,1)
s.mouseDown(button='left')
s.move(0,100)
s.mouseUp(button='left')



x = s.locateCenterOnScreen('filterword.png', confidence=0.9) # press filter
s.moveTo(x[0],x[1],2)
s.click(clicks=2,interval=0.2)
time.sleep(0.5)
x = s.locateCenterOnScreen('choosecompany.png', confidence=0.9) 
s.moveTo(x[0],x[1],2) # select database and double click
s.move(27,133,0.5) 
s.click(clicks=2,interval=0.2)
########################################






## this code can be used for looping database
## not ideal .....  but might be usefull later
deltay = 0
for i in range(1,5):
    x = s.locateCenterOnScreen('SAP_name.png', confidence=0.9)
    s.moveTo(x[0],x[1],2)
    s.click()
    time.sleep(1.5)

    x = s.locateCenterOnScreen('choosecompany.png', confidence=0.7)
    s.moveTo(x[0],x[1],2)
    s.move(54,0)
    s.click(clicks=2)

    deltay += 18    ### move by 30 pixels each time to next db
    
    print (deltay)
    s.move(0,deltay)
    #time.sleep(15)  # give 15 seconds for db to start


## keep looping until a picture pops up
## give time limit 10 seconds >> change accordingly


import pyautogui as s
start = time.time()
while True:
    x = s.locateCenterOnScreen('SAP_user.png', confidence=0.9)
    
    if x is not None:   # found the pic
        print ('found it')
        break
    else:  # do timer to stop searching after 10 seconds
        timer = time.time() - start
        print (timer)
        if timer > 10:
            s.alert("Sorry can't find the picture on your screen")
            break
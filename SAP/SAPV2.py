##### Automate SAP User Add #####

userid = 'U01258'
username = 'hayley.kong'
useremail = 'h.kong@laserclinics.com.au'
usergroup = 'finance'   # this is finance group, change accordingly
supplierapproval = 'Yes'
db = 'LCS Franchising'


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
def findimage(image, mylimit = 10,acc = 0.99, click = 1, dx = 0, dy=0, duration = 0.2, sleep=0, write = 'None'):
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
                    s.write(write)

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

os.chdir(r'C:\Users\r.christianto\MyPython\SAP\Snapshot')

#myimages =  ['SAP_name.png','filter.png','clear.png','Rule.png','value.png','filterword.png',
#             'companyname.png','SAP_Menu.png','SAP_lookup.png','SAP_user.png','SAP_binocular.png',
#             'generaltab.png','username.png','email.png','group.png','1.png',
#             '5.png','update.png','display.png','font.png','fontsize.png',
#            'filtercompany.png','databasewindow.png','SAP_lookup.png','SAP_supplierapproval.png','supplierapproval.png',
#            'DisplayTab.png']



findimage('SAP_name.png')
findimage('filter.png')
findimage('clear.png')
findimage('rule.png')






x = s.locateCenterOnScreen('SAP_name.png', confidence = 0.9)

s.moveTo(x[0],x[1],1.5)




#mycat = [1,1,1,2,1,1,3,4,5,1,1,1,3,3,3,6,6,1,1,3,3]

myimages =  [
'SAP_Menu.png','SAP_lookup.png','SAP_user.png','SAP_binocular.png',
'generaltab.png','username.png','email.png','group.png','1.png',
'5.png','update.png','display.png','font.png','fontsize.png',
'filtercompany.png','databasewindow.png','SAP_lookup.png','SAP_supplierapproval.png','supplierapproval.png',
'DisplayTab.png']
mycat = [4,5,1,1,1,3,3,3,6,6,1,1,3,3]


mydict = dict(zip(myimages,mycat))

mywords  = {'value.png':db, 'SAP_binocular.png':userid, 'username.png':username,'email.png':useremail,'font.png':'a','fontsize.png':'12'}
mygroup = {'finance':'1.png','superuser':'5.png'}


# below codes categorise typical actions against images
# add more as you find new scenarios
# you just need to assign each image to each action/category below
for image in myimages:

    # find the category to use
    cat = mydict[image]

    # action 1, find and click
    if cat == 1:

        if index in (4,5,17):
            clicks = 2
            if index == 4:
                myconfidence = 0.7
            else:
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
    elif cat == 2:
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

    # action 3, find , offset and click
    elif cat == 3:
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
        elif index == 14:
            myx = 420
            myy = 0
            myclick = 1
            myconfidence = 0.9
            sleep = 1 # give database more time
        elif index in (19,20):
            myx = 182
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

    # action 4, wait screen to refresh until the picture can be found
    elif cat ==  4:
        findme = findimage(image,180)
        if findme is None:
            break
        else:
            print ('Refresh finish, continue .....')

    # action 5, search twice....after unhiding
    elif cat == 5:
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

    # action 6, deals with radio button options, e.g finance, superuser etc
    elif cat == 6:
        if mygroup[usergroup] == image:
            findme = findimage(image,10)
            if findme is None:
                break
            else:
                s.moveTo(30,0)
                s.click()
        else:
            continue


     ### the write section

    try:
        writethis = mywords[image]
        s.write(writethis,interval=0.2)

        if image == 'SAP_binocular.png':
            s.press('enter')

    except:
        continue
        



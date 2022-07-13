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


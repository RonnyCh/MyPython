

import pyautogui as s
import mouse
import keyboard
import pickle
import time


#s.alert('You need to record Mouse and Keyboard separately')

# flag the status to start looping
count = 0    # for filename purpose
status = 'Go' # for looping purpose
mylist = []   # capture all the filenames
        
while status == 'Go':
    
    chk_mouse = s.confirm("Record mouse, press Q to stop", buttons = ['Yes','No'])
    
    # if user response cancel, set status = blank to stop the loop
    if chk_mouse == 'Yes':
        count += 1
        file = 'Step' + str(count) + 'm' + '.txt'  # m stands for mouse
    
        mouse_event = []
        mouse.hook(mouse_event.append)
    
        if not keyboard.wait("Tab"):
            # save the events
            mouse.unhook_all()
            with open(file, 'wb') as fh:
                pickle.dump(mouse_event, fh)    
                mylist.append(file) # save the step to the list
    else:
        status = ''
        s.alert("Recording completed!!")


    chk_keyboard = s.confirm("Record keyboard, press Q to stop", buttons = ['Yes','No'])

    if chk_keyboard == "Yes":  
    # record keyboard events
        count += 1
        file = 'Step' + str(count) + 'kb' +'.txt'  # kb stands for keyboard
        
        keyboard_event = []
        keyboard.hook(keyboard_event.append)
        if not keyboard.wait("Tab"):
            keyboard.unhook_all()
            s.alert("Keyboard recording finished")
            # save the events
            with open(file, 'wb') as fh:
               pickle.dump(keyboard_event, fh)
               mylist.append(file)  
    else:  
    # user does not want to proceed with keyboard events
        status = ''
        s.alert("Recording completed!!")
   
                   
    
# save the steps from mylist to a file
with open('mysteps.txt', 'wb') as fh:
   pickle.dump(mylist, fh)
   

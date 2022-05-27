import mouse
import keyboard

mouse_events = []

mouse.hook(mouse_events.append)
keyboard.start_recording()       #Starting the recording

keyboard.wait("a")

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()  #Stopping the recording. Returns list of events


for i in keyboard_events:
    print (i)
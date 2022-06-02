

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("180x100")
root.title('Login')
root.resizable(0, 0)

def callback():
    import Record as x 
    x.record()


def callback2():
    print ('my message')
    
# download button
buttondl = ttk.Button(root, text="Record",command=callback)
buttondl.pack()  



# download button
button2 = ttk.Button(root, text="Message",command=callback2)
button2.pack()  

root.mainloop()
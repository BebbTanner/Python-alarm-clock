"""
Alarm clock mini project June 19th 2025 10:44

I will be starting by just practicing with the documentation examples provided.
"""

import time
from tkinter import *
from tkinter import ttk
from datetime import datetime

def updateTime():
    while True:
        update_time = datetime.now().strftime("%H:%M")
        time.sleep(1)

current_time = datetime.now().strftime("%H:%M")

root = Tk()
root.title("Alarm Clock")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

"""
I need to figure out what this stringVar does, I might need another one for my update funtion.
This one should currently be the master stringvar since it has no parameters.
"""
alarm = StringVar()
alarm_entry = ttk.Entry(mainframe, width=7, textvariable=alarm)
alarm_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Set Alarm").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="What time?").grid(column=1, row=1, sticky=W)

"""
These are labels that are displayed on the GUI.
The first one displays text that says current time 
The second will eventually display the current time with an update function
The Third one displays CST for the central timezone.
"""
ttk.Label(mainframe, text=" Current time: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text=current_time).grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, text= " CST ").grid(column=3, row=2, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)

root.mainloop()
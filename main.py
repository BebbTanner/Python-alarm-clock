"""
Alarm clock mini project June 19th 2025 10:44
"""

import time
from tkinter import *
from tkinter import ttk
from datetime import datetime

def setAlarm(*args):
    try:
        alarmTime = float(alarm.get())
        currentAlarm.set(int(alarmTime))
        
    except ValueError:
        pass

root = Tk()
root.title("Alarm Clock")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

alarm = StringVar()
alarm_entry = ttk.Entry(mainframe, width=7, textvariable=alarm)
alarm_entry.grid(column=2, row=1, sticky=(W, E))
currentAlarm = StringVar()

ttk.Label(mainframe, text="What time?").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text= " Alarm set for: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text= " Current time: ").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, textvariable=currentAlarm).grid(column=2, row=2, sticky=E)
time_label = ttk.Label(mainframe, textvariable=time_var).grid(column=2, row=3, sticky=E)
ttk.Button(mainframe, text="Set Alarm", command=setAlarm).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text= " CST ").grid(column=3, row=3, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)

root.mainloop()
"""
Alarm clock mini project June 19th 2025 10:44

CURRENT OBJECTIVE:
Create the alarm function
    the function should have access to the currentAlarm variable
    It should then take currentAlarm variable and compare it to the time_var
    If the values match, display a pop up that says alarm finished or something, maybe include and audio file that goes off.

"""

import time
from tkinter import *
from tkinter import ttk
from datetime import datetime

"""
    My current_time variable is stored as a string data type, and my alarmTime is stored as an integer.
These are going to need to be the same data type in order to compare them.
"""
#def checkAlarm():


def update_time():
    """Updates the time displayed in the label and reschedules itself."""
    current_time = datetime.now().strftime("%H:%M")
    time_var.set(current_time)
    root.after(60000, update_time)

def setAlarm(*args):
    try:
        alarmTime = alarm.get()
        currentAlarm.set(alarmTime)
        
    except ValueError:
        pass

root = Tk()
root.title("Alarm Clock")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

alarm = StringVar()
time_var = StringVar()
currentAlarm = StringVar()
alarm_entry = ttk.Entry(mainframe, width=7, textvariable=alarm)

ttk.Label(mainframe, text="What time?").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text= " Alarm set for: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text= " Current time: ").grid(column=1, row=3, sticky=E)
alarm_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=currentAlarm).grid(column=2, row=2, sticky=E)
time_label = ttk.Label(mainframe, textvariable=time_var).grid(column=2, row=3, sticky=E)
ttk.Button(mainframe, text="Set Alarm", command=setAlarm).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text= " CST ").grid(column=3, row=3, sticky=E)


update_time()

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)

root.mainloop()
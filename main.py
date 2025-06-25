"""
Alarm clock mini project June 19th 2025 10:44
"""

import time
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

"""
    This is the current function that I am working on. 
"""


def update_time():
    current_time = datetime.now().strftime("%H:%M")
    time_var.set(current_time)
    root.after(60000, update_time)

    return time_var

def setAlarm(*args):
    try:
        alarmTime = alarm.get()
        currentAlarm.set(alarmTime)

        return currentAlarm
        
    except ValueError:
        pass

def compareTime():
    newAlarm = alarm.get()
    alarmNoColon = newAlarm.replace(":", "")

    myTimeVar = time_var.get()
    noColon = myTimeVar.replace(":", "")

    if alarmNoColon == noColon:
        messagebox.showwarning("Error", "Your're smelly")


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
ttk.Label(mainframe, textvariable=time_var).grid(column=2, row=3, sticky=E)
ttk.Button(mainframe, text="Set Alarm", command=setAlarm).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text= " CST ").grid(column=3, row=3, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)

update_time()

root.mainloop()
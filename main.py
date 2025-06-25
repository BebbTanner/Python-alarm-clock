"""
Alarm clock mini project June 19th 2025 10:44

CURRENT OBJECTIVE:
Run a check to be sure that the alarm clock function is triggering when the times values are the same.

"""

import time
from tkinter import *
from tkinter import ttk
from datetime import datetime

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

"""
    I am currently attempting to take a stringvar and convert it to a int value.
I a doing this so that I can create a function that will compare the user's alarm time
to the current time so that I may display a popup when the alarm is finished.

    Ok, so it appears that it is making the comparison of the variables correctly, but it 
is not displalying the popup window. So I believe that the next issue that I need to work on
is fixing the pop up window.

I am not sure if I am going to make it a seperate function then call it in the alarmclock function.
Or just program directly into the alarmclock function.
"""
update_time()

root.mainloop()

#This is taking the stringvar and converting it back to a string.
#idk if its recogonizing the get function.

newAlarm = alarm.get()
alarmNoColon = newAlarm.replace(":", "")

print(alarmNoColon)

myTimeVar = time_var.get()
noColon = myTimeVar.replace(":", "")

print(noColon)

if alarmNoColon == noColon:
    print("The values are the same.")

else:
    print("The values are not the same.")
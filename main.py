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
    """Updates the time displayed in the label and reschedules itself."""
    current_time = datetime.now().strftime("%H:%M")
    time_var.set(current_time)
    root.after(60000, update_time)

    return time_var

def setAlarm(*args):
    try:
        alarmTime = alarm.get()
        currentAlarm.set(alarmTime)
        
    except ValueError:
        pass

def popUpWindow():
    new_window = Toplevel(root)
    new_window.title("Alert")
    new_window.geometry("300x200")

    label = ttk.Label(new_window, text="Time is up!")
    label.pack(pady=20)

    close_button = ttk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)

"""
The 2 comparsion values are:
time_var        current_alarm

1.) Remove the colons from both of the values
2.) Comapare the 2 values

    Update: this shit does not appear to comaparing the times. I am not sure as to why.
"""
def alarmClock():
    clockValue = currentAlarm.get()
    timeValue = time_var.get()

    strAlarm = clockValue.replace(":", "")
    strValue = timeValue.replace(":", "")

    if strAlarm == strValue:
        print("They are the same.")

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
#userAlarm = input("Please enter a time: ")
#alarmNoColon = userAlarm.replace(":", "")

#print(alarmNoColon)
#print(type(alarmNoColon))

#myTimeVar = "15:00"
#noColon = myTimeVar.replace(":", "")

#print(noColon)
#print(type(noColon))

#if alarmNoColon == noColon:
#    print("The values are the same.")

update_time()
root.mainloop()
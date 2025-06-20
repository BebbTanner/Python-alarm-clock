"""
Alarm clock mini project June 19th 2025 10:44

I will be starting by just practicing with the documentation examples provided.

CURRENT OBJECTIVES:
Program and test the update time funciton
Create a label that can hold that the updateTime function and display it on the GUI
Figure out how the StringVar() tkinter function works.
"""

import time
from tkinter import *
from tkinter import ttk
from datetime import datetime

"""
    This is the update time function. This funciton is using a while loop that will update the current time
and store it in the update_time variable. Using time.sleep(), it waits for one second to run the loop again. 
In theory this should update the time every minute. The format is: HH:MM.
"""
def updateTime():
    while True:
        update_time = datetime.now().strftime("%H:%M")
        time.sleep(60)

"""
    This is the current time variable that will hold the current time on the machine. 
The format is: HH:MM. The datetime.now() funciton is getting the current date and time.
The strftime() is parsing the hour and minute data. This is the only data that I want.
"""
current_time = datetime.now().strftime("%H:%M")

"""

"""
root = Tk()
root.title("Alarm Clock")

"""
    It seems like the mainframe is basically just the window that will pop up that 
will allow me to display things on. I see this as something like a table and the
labels, buttons, ect are the plates being placed on the table.
"""
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

"""
    I need to figure out what this stringVar does, I might need another one for my update function.
This one should currently be the master stringvar since it has no parameters.
"""
#alarm = StringVar()
#alarm_entry = ttk.Entry(mainframe, width=7, textvariable=alarm)
#alarm_entry.grid(column=2, row=1, sticky=(W, E))

"""
    This is a tkinter button that will eventually be linked to a function that will
allow the user to set an alarm.
"""
#ttk.Button(mainframe, text="Set Alarm").grid(column=3, row=1, sticky=W)

"""
    These are labels that are displayed on the GUI.
The first one displays text that says current time 
The second will eventually display the current time with an update function
The Third one displays CST for the central timezone.
The fourth one displays text that says what time.
"""
#ttk.Label(mainframe, text=" Current time: ").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text=current_time).grid(column=2, row=2, sticky=E)
#ttk.Label(mainframe, text= " CST ").grid(column=3, row=2, sticky=E)
#ttk.Label(mainframe, text="What time?").grid(column=1, row=1, sticky=W)

"""
    This is a for loop that is checking for every child class in the mainframe.
It is then taking those child classes and adjusting them to the padding that is specified.
Basically, if you want to change the spacing between each of the labels or buttons, 
change the padding variables in this loop.
"""
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)

"""
    This is just calling the mainloop function that will run all of the related 
code from above.
"""
root.mainloop()
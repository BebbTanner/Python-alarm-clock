"""
Alarm clock mini project June 19th 2025 10:44

    I have added an example from online that works to try and figure out where I went wrong.
This example does not have a label that will display the current time. However, from looking 
at the example I might beable to set my function up to display it. So, rather than using a 
label outside of the function I will try to use a label inside the update time function then
that should properly display the updated current time to the window without having to jump 
through all these damn hoops.

    So, I think I am going to restart on the setAlarm function. The way I see it is that,
the example declares the variables outside of the functions. Then inside the functions 
they get the values stored in the variables. Finally, the most important part here, they
create the labels to be displayed in the window rather than outside of the function.

"""

"""
def update_time():
    current_time = datetime.now().strftime("%H:%M")
    time_var.set(current_time)
    root.after(60000, update_time)

    return time_var
"""

import tkinter as tk
from tkinter import messagebox
import datetime
import time

def setAlarm():
    alarmTimeString = alarmEntry.get()

    try:
        alarmTime = datetime.datetime.strptime(alarmTimeString, "%H:%M").time()

        if alarmTime < datetime.datetime.now().time():
            messagebox.showerror("Error", "Time must be in the future!")
            return
        
        label_alarm.config(text=f"Alarm set for: {alarmEntry}")

        setAlarm(alarmTime)

    except ValueError:
        messagebox.showerror("Error", "Incorrect format!")


"""
    The setAlarm function is allowing the user to set a time to wake up to.
This is using the alarmEntry as the parameters.
"""
def checkAlarm(alarmEntry):
    """
        The currentTime varible uses the datetime library to get the current time.
    The current time is the value that is stored in this variable.
    """
    currentTime = datetime.datetime.strptime("%H:%M").time()

    """
        If statement
    """
    if (alarmEntry.hour and alarmEntry.minute) == (currentTime.hour and currentTime.minute):
        messagebox.showwarning("Alarm", "Time to get up!")

    else:
        root.after(60000, checkAlarm, alarmEntry)


root = tk.Tk()
root.title("Alarm Clock")

alarmEntry = tk.Entry(root)
alarmEntry.pack()

alarmSet = tk.Button(root, text="Set Alarm", command=setAlarm)
alarmSet.pack()

label_alarm = tk.Label(root, text="")
label_alarm.pack()

"""
    This is calling the mainloop function. This should compile everything used for 
the main loop.
"""
root.mainloop()
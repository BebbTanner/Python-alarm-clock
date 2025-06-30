"""
Alarm clock mini project June 19th 2025 10:44

    I have added an example from online that works to try and figure out where I went wrong.
This example does not have a label that will display the current time. However, from looking 
at the example I might beable to set my function up to display it. So, rather than using a 
label outside of the function I will try to use a label inside the update time function then
that should properly display the updated current time to the window without having to jump 
through all these damn hoops.
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

"""Example line"""
def set_alarm():
    # Get alarm time from user input
    alarm_time_str = entry_time.get()
    try:
        #This a variable that is getting the current time using the datetime library.
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M").time()

        # If the alarm time value is less than the current time, Throw a message that 
        # tells the user that the alarm time must be in the future.
        if alarm_time < datetime.datetime.now().time():
             messagebox.showerror("Error", "Alarm time must be in the future")
             return
        
        """
            So in this example, rather than declaring the label outside of the function,
        it is instead putting the label in the function. This label will display the 
        value stored in alarm_time_str. This label will then be displayed to the window.
        """
        label_alarm.config(text=f"Alarm set for: {alarm_time_str}")
        """
            This is calling the check_alarm function and uses the alarm_time variable 
        for the parameters. Check_alarm will be explained in that fuction.
        """
        check_alarm(alarm_time)

        """
            This is an exception that will inform the user that the did not use
        a proper format.
        """
    except ValueError:
         messagebox.showerror("Error", "Invalid time format. Use HH:MM")
"""END"""


def setAlarm(*args):
    #This is a variable declaration that is using .get() to get the value stored
    #in the alarm variable.
    alarmTime = alarm.get()

    try:
        currentAlarm.set(alarmTime)
        return currentAlarm
        
    except ValueError:
        pass


"""Example line"""
def check_alarm(alarm_time):
    """
        This is the current_time variable. Using the datetime library, they are storing the 
    current date and time.
    """
    current_time = datetime.datetime.now().time()

    """
        if the current time hour and current time minute are both equal to the alarm time hour
    and alarm time minute then run the loop. If the times do not match, then run the function
    again.
    """
    if (current_time.hour, current_time.minute) == (alarm_time.hour, alarm_time.minute):
         # If the condition of the loop are met, this will display a message box.
         messagebox.showinfo("Alarm", "Time to wake up!")

    else:
        # Check again after a delay (e.g., 1 minute)
        root.after(60000, check_alarm, alarm_time) # 60000 milliseconds = 1 minute
"""END"""

def compareTime():
    newAlarm = alarm.get()
    alarmNoColon = newAlarm.replace(":", "")

    myTimeVar = time_var.get()
    noColon = myTimeVar.replace(":", "")

    if alarmNoColon == noColon:
        messagebox.showwarning("Error", "Your're smelly")

root = tk.Tk()
root.title("Alarm Clock")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

alarm = StringVar()
time_var = StringVar()
currentAlarm = StringVar()
alarm_entry = ttk.Entry(mainframe, width=7, textvariable=alarm)


"""Example line"""
label_time = tk.Label(root, text="Enter alarm time (HH:MM):")
label_time.pack()

"""
    This is the entry time variable. This is using the Entry widget to accept user input
via a entry box. In the parameters they use root, this is taking the entry and displaying it 
on the parent window.
"""
entry_time = tk.Entry(root)

"""
    The pack() widget is away to arrange the main window. This is being used on the 
previously declared variable entry_time. I dont know how pack works excatly, but 
I know that I was using a grid format.
"""
entry_time.pack()

button_set = tk.Button(root, text="Set Alarm", command=set_alarm)
button_set.pack()

label_alarm = tk.Label(root, text="")
label_alarm.pack()
"""END"""

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)

root.mainloop()
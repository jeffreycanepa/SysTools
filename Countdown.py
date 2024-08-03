# /usr/bin/python3
'''
--------------------------------------------------------------
-   Countdown.py.
-       This is a countdown timer.  Script is from 
-       geeksided.com (https://geeksided.com/posts/step-by-step-guide-countdown-timer-with-alarm-in-python-01j1e6hqafh2).
-
-   Required:
-       time
-       tkinter
-       pygame
-       subprocess
-
-   Methods:
-       countdown()
-       start_timer()
-       on_return()
-       main()

-   Jeff Canepa 8/3/2024
-   jeff.canepa@gmail.com
-   08/03/2024
--------------------------------------------------------------
'''

import time
import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize pygame mixer for playing sound
pygame.mixer.init()

def countdown(count, label):
    mins, secs = divmod(count, 60)
    time_format = '{:02d}:{:02d}'.format(mins, secs)
    label.config(text=time_format)

    if count > 0:
        root.after(1000, countdown, count-1, label)
    else:
        pygame.mixer.music.load('alarm.mp3')
        pygame.mixer.music.play() 
        messagebox.showinfo("Time's up!", "Time's up!")

# Create Tkinter window
root = tk.Tk() 
root.title("Countdown Timer")

# Set the window size
root.geometry("200x200")

# Create the input fields and labels
input_label_minutes = tk.Label(root, text="Enter minutes:")
input_label_minutes.pack()
time_entry_minutes = tk.Entry(root, width=5)
time_entry_minutes.insert(0, 0)
time_entry_minutes.pack()
input_label_seconds = tk.Label(root, text="Enter seconds:")
input_label_seconds.pack()
time_entry_seconds = tk.Entry(root, width=5)
time_entry_seconds.insert(0, 0)
time_entry_seconds.pack()

# Create the countdown display label
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_label.pack()

# Create the start button.  Bind return key to button to start timer.
def start_timer():
    try:
        minutes = int(time_entry_minutes.get())
        seconds = int(time_entry_seconds.get())
        total_seconds = minutes * 60 + seconds
        countdown(total_seconds, timer_label)

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for minutes and seconds")

def on_return(event):
    start_timer()
start_button = tk.Button(root, text="Start", command=start_timer)
start_button.bind('<Return>', on_return)
start_button.pack()

# Run the application
def main():
   root.mainloop()

if __name__ == "__main__":
    main()

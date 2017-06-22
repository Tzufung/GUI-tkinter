# Add an Entry to GUI
import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")
ttk.Label(win, text="Entry a name:").grid(column=0, row=0)

# Add a textbox
name = tk.StringVar()    # Entry a string; we have to declare the variable name as the type tk.StringVar()
textbox = ttk.Entry(win, width=12, textvariable=name)    # hard-coded it to a width of 12
# textbox Entry widget did not expand
textbox.grid(column=0, row=1)
textbox.focus()    # Place cursor into Entry; we can type into this text box without having to click it first


# Button click event callback function
def click_me():
    button.configure(text="Hello " + name.get())

# Add a button
button = ttk.Button(win, text="Click Me", command=click_me)    # button click event is a callback function
button.grid(column=1, row=1)
# button.configure(state="disabled")    # Disable the button widget

win.mainloop()

# Creating buttons and changing their text property
import tkinter as tk
from tkinter import ttk

win = tk.Tk()    # create an instance

win.title("Python GUI")

# Add a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)


# (2) Button click event callback function
def click_button():    # event handler that is being invoked once the button gets clicked
    button.configure(text="** I have been clicked! **")
    aLabel.configure(foreground="red")

# (1)Add a button
# GUIs are event-driven. Clicking the button creates an event.
button = ttk.Button(win, text="Click Me!", command=click_button)    # we do not use parentheses; only the name clickMe
button.grid(column=1, row=0)

win.mainloop()

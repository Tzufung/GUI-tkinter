# Adding drop-down combo boxes that can have initial default values.
# While we can restrict the user to only certain choices, at the same time,
# we can allow the user to type in whatever they wish.

# 去掉name, number 语句和相应位置，亦无大碍

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

# title
win.title("Python GUI")

# label
label_1 = ttk.Label(win, text="Enter a name:")
label_1.grid(column=0, row=0)
label_2 = ttk.Label(win, text="Choose a number:")   # 1
label_2.grid(column=1, row=0)


# button click event callback function
def click_me():
    button.configure(text="Hello " + name.get() + number.get())

# button
button = ttk.Button(win, text="Click Me!", command=click_me)
button.grid(column=2, row=1)

# textbox
name = tk.StringVar()
textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)
textbox.focus()    # cursor

# combo box
number = tk.StringVar()    # 2 value is assigned to the number variable.
# numberChoose = ttk.Combobox(win, width=12, textvariable=number)    # 3
# restrict the user to only be able to select the values we have programmed into the Combobox,
numberChoose = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
numberChoose["values"] = (1, 2, 3, 4)    # 4
numberChoose.grid(column=1, row=1)    # 5
numberChoose.current(0)    # 6

win.mainloop()

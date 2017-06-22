# Creating a check button with different initial states

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

# label
label_1 = ttk.Label(win, text="Enter a name:")
label_1.grid(column=0, row=0)
label_2 = ttk.Label(win, text="Choose a number:")
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
textbox.focus()

# combo box
number = tk.StringVar()
numberChoosen = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
numberChoosen["values"] = (1, 2, 3, 4)
numberChoosen.grid(column=1, row=1)
numberChoosen.current(0)

# create three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()
# Setting the sticky property of the grid to tk.W means that the widget will be aligned to the west of the grid.
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

win.mainloop()

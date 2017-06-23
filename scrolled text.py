# Using scrolled text widgets

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext # 2

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
textbox = ttk.Entry(win, textvariable=name, width=12)
textbox.grid(column=0, row=1)
textbox.focus()

# combo box
number = tk.StringVar()
numberChoose = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
numberChoose["values"] = (1, 2, 3, 4)
numberChoose.grid(column=1, row=1)
numberChoose.current(0)

# check button
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.deselect()
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enable", variable=chVarEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

# scrolled text
# By setting the wrap property to tk.WORD we are telling the ScrolledText widget to break
# lines by words, so that we do not wrap around within a word. The default option is tk.CHAR,
# which wraps any character regardless of whether we are in the middle of a word.
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)    # 6
scr.grid(column=0, columnspan=3)

win.mainloop()

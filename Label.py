# Add a label widget; ttk(themed tk) is an extension within tkinter
import tkinter as tk
from tkinter import ttk

win = tk.Tk()    # create an instance

win.title("Python GUI")
ttk.Label(win, text="A label").grid(column=0, row=0)
# We are passing our window instance into the ttk.Label constructor and setting the text property

win.mainloop()    # start GUI

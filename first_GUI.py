# Creating first Python GUI
import tkinter as tk

win = tk.Tk()    # turn TK class into an instance

win.title("Python GUL")    # win is short for window; set one property
win.resizable(0, 0)    # Disable resizing the GUL

win.mainloop()    # start the window's event loop

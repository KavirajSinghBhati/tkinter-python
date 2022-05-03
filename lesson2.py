# positioning using grid system

from tkinter import *

root = Tk()

label1 = Label(root, text="Hello world").grid(row=0, column=0)
label2 = Label(root, text="My name is Kaviraj").grid(row=1, column=5)

root.mainloop()
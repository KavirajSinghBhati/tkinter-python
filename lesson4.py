# taking input
from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")

def myClick():
    txt = "Hello " + e.get()
    lb1 = Label(root, text=txt)
    lb1.pack()

btn = Button(root, text="Click me!", command=myClick).pack()

root.mainloop()
# buttons

from tkinter import *

from numpy import pad

root = Tk()

# but = Button(root, text="Click me!", state=DISABLED).pack()

# but = Button(root, text="Click me!", padx=10, pady=20).pack()

def myClick():
    label1 = Label(root, text="A button was just clicked!!").pack()

but = Button(root, text="Click me!", command=myClick, fg="white", bg="black").pack()
root.mainloop()
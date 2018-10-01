import tkinter
from tkinter import *
root=Tk()
var=StringVar()
label=Message(root,textvariable=var,relief=RAISED)
var.set("hey!? how are you doing, attend lect&pracs or give ATKT")
label.pack()
root.mainloop()

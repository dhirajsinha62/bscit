import tkinter
from tkinter import *
top=Tk()
L1=Label(top,text="UserName")
L1.pack(side=LEFT)
E1=Entry(top,bd=5)
E1.pack(side=RIGHT)
top.mainloop()

import tkinter
from tkinter import *
root=Tk()
var=StringVar()
label=Message(root,textvariable=var,relief=RAISED)
var.set("hey!? how are you doing, attend lect&pracs or give ATKT")
label.pack()
root.mainloop()

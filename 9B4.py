#RadioButton.py
import tkinter
from tkinter import *
def sel():
        selection="You selected the option " + str(var.get())
        Label.config(text=selection)
root=Tk()
var=IntVar()
R1=Radiobutton(root,text="DROP",variable=var,value=1,command=sel)
R1.pack(anchor=W)
R2=Radiobutton(root,text="STUDY",variable=var,value=2,command=sel)
R2.pack(anchor=W)
R3=Radiobutton(root,text="ATKT",variable=var,value=3,command=sel)
R3.pack(anchor=W)
label=Label(root)
label.pack()
root.mainloop()

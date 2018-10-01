#Scale.py
import tkinter
from tkinter import *
def sel():
        selection="Value =" + str(var.get())
        label.config(text=selection)
root=Tk()
var=IntVar()
var=DoubleVar()
scale=Scale(root,variable=var)
scale.pack(anchor=CENTER)
button=Button(root,text="get scale value",command=sel)
button.pack(anchor=CENTER)
label=Label(root)
label.pack()
root.mainloop()

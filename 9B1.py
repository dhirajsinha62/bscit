 
import tkinter
import tkMessageBox

top = tkinter.Tk()
def hello():
   tkmessageBox.showinfo("Say Hello", "Hello World")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()

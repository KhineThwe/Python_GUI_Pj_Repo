from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Look!I clicked a Button!")
    myLabel.pack()

myButton2 = Button(root,text="Click Me!",command=myClick,fg="blue",bg="red")
myButton2.pack()
root.mainloop()


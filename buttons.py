#in tkinter everything is a widget
#create and put
#in python everything is object 
#tkinter ---> window-->root
from tkinter import *

root = Tk()#it must be first line of your project

myButton = Button(root,text="Click Me!")
myButton1 = Button(root,text="Click Me!",state="disabled")
myButton2 = Button(root,text="Click Me!",padx=50,pady=50)
myButton.pack()
myButton1.pack()
myButton2.pack()
root.mainloop()


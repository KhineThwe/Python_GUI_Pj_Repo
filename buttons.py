#in tkinter everything is a widget
#create and put
#in python everything is object 
#tkinter ---> window-->root
from tkinter import *

root = Tk()#it must be first line of your project

def myClick():
    myLabel = Label(root,text="Look!I clicked a Button!")
    myLabel.pack()

myButton2 = Button(root,text="Click Me!",command=myClick,fg="blue",bg="red")#function call not () parenthesis
myButton2.pack()
root.mainloop()


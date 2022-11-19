#in tkinter everything is a widget
#create and put
#in python everything is object 
#tkinter ---> window-->root
from tkinter import *

root = Tk()#it must be first line of your project

myLabel1 = Label(root,text="Hello World!NCC Training Course!").grid(row=0,column=0)
myLabel2 = Label(root,text="My name is khine").grid(row=1,column=5)

#create lable widget and put that widget into our root widget

#shoving it onto the screen
# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1,column=5)
# myLabel3.grid(row=1,column=1)

#event loop
root.mainloop()


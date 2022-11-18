#in tkinter everything is a widget
#tkinter ---> window-->root
from tkinter import *

root = Tk()#it must be first line of your project

myLabel = Label(root,text="Hello World!")#create lable widget and put that widget into our root widget

#shoving it onto the screen
myLabel.pack()

#event loop
root.mainloop()

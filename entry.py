from tkinter import *

root = Tk()

e = Entry(root,width=50,bg="blue",fg="red",borderwidth=5)#input box ---> with Entry
e.pack()
e.insert(0,"Enter Your Name: ")#will create default text inside of the text-box

def myClick():
    hello = "Hello " + e.get()#what ever you type we will get
    myLabel = Label(root,text=hello)
    myLabel.pack()

myButton = Button(root,text="Enter your name!",command=myClick,fg="blue",bg="red")
myButton.pack()
root.mainloop()


import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Hello World!", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, height=3, font=('Arial', 16))  # multiline
        self.textbox.pack(padx=20)

        self.checkState = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Message Box!", font=('Arial', 18), variable=self.checkState)
        self.check.pack(padx=20, pady=20)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message())
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def show_message(self):
        if self.checkState.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message",message=self.textbox.get('1.0',tk.END))


GUI()

from tkinter import *

from time import strftime


root=Tk()
root.title("Clock by HerixTheHacker")


def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
    
    


label=Label(foreground='cyan',background='black')
label.pack(anchor='center')
time()

mainloop()

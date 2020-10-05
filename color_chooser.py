from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
a = Tk()

def mcolor():
    color = colorchooser.askcolor()
    label = Label(text=color,bg=color[1])
    label.pack()
def mfileopen():
    file1 = filedialog.askopenfile()
   # label = Label(text=file1)
    #label.pack()
    file2 = file1.name
    f = open(file2)
    label2 = Label(text= f.read(),font=('arial',24,'bold'))
    label2.pack()
button =  Button(text="Choose Your Color",width=30, command=mcolor)
button.pack()
button =  Button(text="Open File",width=30, command=mfileopen)
button.pack()
a.mainloop()
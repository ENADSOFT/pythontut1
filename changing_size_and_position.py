from tkinter import *
from tkinter import messagebox

myGui = Tk()

def hello():
    b = a.get()
    myLabel2 = Label(myGui,text='Entered into programming ',fg='red',bg='yellow',font=('arial',24,'italic'))
    myLabel2.pack()    
def deleted():
    myLabel3 = Label(myGui,text='deleted',fg='red',bg='yellow',font=('arial',24,'italic'))
    myLabel3.pack()
def newf():
    myLabel4 = Label(myGui,text='Clicked on new file',font=('roman',24,'italic'))
    myLabel4.pack()
def msave():
    messagebox.showinfo(title='save',message='Are you sure you want to save')
def mquit():
    mess = messagebox.askyesno(title='quit',message='Are you sure you want to quit?')
    if mess == 1:
        myGui.destroy()

    

    
a = StringVar()

myGui.title("Hello")
myGui.geometry("500x500+150+150")


myLabel1 = Label(myGui,text='label one',fg='red',bg='yellow',font=('arial',24,'italic'))
myLabel1.pack()

myButton1 = Button(myGui,text='Enter',fg='blue',bg='red',command=hello,font=('arial',24,'bold'))
myButton1.pack()

myButton2 = Button(myGui,text='Delete',fg='blue',bg='red',command=deleted,font=('arial',24,'bold'))
myButton2.pack()

text = Entry(myGui,textvariable = a)
text.pack()

mymenu = Menu(myGui)
listfile = Menu(myGui)
listfile.add_command(label='New File',command = newf)
listfile.add_command(label='Open File')
listfile.add_command(label='Save File',command = msave)
listfile.add_command(label='Quit',command = mquit)


listedit = Menu(myGui)
listedit.add_command(label='Undo')
listedit.add_command(label='Redo')
listedit.add_command(label='Cut')
listedit.add_command(label='Copy')
listedit.add_command(label='Paste')
listedit.add_command(label='Select all')

mymenu.add_cascade(label="File",menu=listfile)
mymenu.add_cascade(label="Edit",menu=listedit)
mymenu.add_cascade(label="View")
mymenu.add_cascade(label="Run")
mymenu.add_cascade(label="Device")
mymenu.add_cascade(label="Tools")
mymenu.add_cascade(label="Help")
myGui.config(menu=mymenu)

myGui.mainloop()
from tkinter import *
root=Tk()
root.geometry('250*250')

username = label(root,from tkinter import *text="Username").grid(row=0,column=0)
t1 = Entry(root).grid(row=0,column=1)
password = label(root,text="Password").grid(row=2,column=0)
t2 = Entry(root).grid(row=2,column=1)
b1 =Button(root,text="Login",).grid(row=4,column=1)

root.mainloop()


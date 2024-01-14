from tkinter import *
root = Tk()
root.geometry('250*250')

lb=Button(root,text="Left",fg="red")
lb.pack(side=LEFT)
rb=Button(root,text="Right",fg="yellow")
rb.pack(side=RIGHT)
tb=Button(root,text="Top",fg="green")
tb.pack(side=TOP)
bb=Button(root,text="Bottom",fg="blue")
bb.pack(side=Bottom)

root.mainloop()

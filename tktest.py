

from Tkinter import Tk, Frame, LEFT, RIGHT, Label, Entry, Button, StringVar


tk = Tk()
#
myvar = StringVar()

def do_plus(*args):
    value = float(aEntry.get()) + float(bEntry.get())
    myvar.set(value)

frameA, frameB, frameC = Frame(tk), Frame(tk), Frame(tk)
btn = Button(tk,text="Add",command=do_plus)
Label(frameA,text="NumA:").pack(side=LEFT)
aEntry = Entry(frameA)
aEntry.pack()
Label(frameB,text="NumB:").pack(side=LEFT)
bEntry = Entry(frameB)
bEntry.pack()
Label(frameC,text="NumC:").pack(side=LEFT)
cEntry = Entry(frameC,textvariable=myvar)
cEntry.pack()

frameA.pack()
frameB.pack()
frameC.pack()

btn.pack(side=RIGHT)

tk.mainloop()

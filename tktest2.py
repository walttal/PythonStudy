
from Tkinter import *

win = Tk()
v = StringVar()

def setText(word):
  v.set(word)


a = Button(win, text="plant", command=setText("plant"))
a.pack()
b = Button(win, text="animal",command=setText("animal"))
b.pack()
c = Entry(win, textvariable=v)
c.pack()
win.mainloop()
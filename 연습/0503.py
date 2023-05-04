from tkinter import *
from tkinter import messagebox

import random

root = Tk()

root.title("테스트")
root.geometry("1024x768")
root.resizable(width = False , height = False)


cnt = 0
chk = IntVar()
mv = IntVar()

def set() :
    l1.configure(text = mv.get())

def reset() :
    global cnt
    cnt = 0
    l2.configure(text = cnt)

def fun() :
    global cnt
    cnt += 1
    l2.configure(text = cnt)

def fun2() :
    if (chk.get() == 1) :
        l1.configure(text = "ON")
    else :
        l1.configure(text = "OFF")

l1 = Label(root, text = "?")
l1.pack()

l2 = Label(root, text = 0)
l2.pack()

b1 = Button(root, text = "Button", command = fun)
b1.pack(side = LEFT)

b2 = Button(root, text = "Reset", command = reset)
b2.pack(side = LEFT)

cb1 = Checkbutton(root, text = "테스트", variable=chk, command=fun2)
cb1.pack()

rb1 = Radiobutton(root, text = "1", variable = mv, value = 1, command = set)
rb1.pack(side = RIGHT, padx= 5, pady= 5)

rb2 = Radiobutton(root, text = "2", variable = mv, value = 2, command = set)
rb2.pack(side = RIGHT, padx= 5, pady= 5)

rb3 = Radiobutton(root, text = "3", variable = mv, value = 3, command = set)
rb3.pack(side = RIGHT, padx= 5, pady= 5)

root.mainloop()
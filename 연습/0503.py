from tkinter import *
from tkinter import messagebox

root = Tk()

cnt = 0
chk = IntVar()

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

root.title("테스트")
root.geometry("1024x768")
root.resizable(width = False , height = False)

l1 = Label(root, text = "OFF")
l1.pack()

l2 = Label(root, text = 0)
l2.pack()

b1 = Button(root, text = "버튼", command = fun)
b1.pack()

b2 = Button(root, text = "Reset", command = reset)
b2.pack()

cb1 = Checkbutton(root, text = "테스트", variable=chk, command=fun2)
cb1.pack()

root.mainloop()
from tkinter import *
from tkinter import messagebox

cnt = 0

def fun() :
    global cnt
    __c = cnt
    __c += 1
    messagebox.showinfo("a", __c)
    cnt = __c

root = Tk()

root.title("테스트")
root.geometry("1024x768")
root.resizable(width = False , height = False)

l1 = Label(root, text = "test")
l1.pack()

b1 = Button(root, text = "버튼", command = fun)
b1.pack()

chk = IntVar()
cb1 = Checkbutton(root, text = "테스트", variable=chk, command=fun)
cb1.pack()

root.mainloop()
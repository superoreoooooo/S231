from tkinter import *
from tkinter import messagebox

import random

root = Tk()

root.title("테스트")
root.geometry("1024x768")
root.resizable(width = False , height = False)

c1 = Canvas(root, width=1024, height=768)
c1.pack()

colors = ["red", "blue", "white", "yellow", "black"]

x1 = 0
y1 = 0
x2 = 0
y2 = 0

def clickL(event) :
    global x1, y1
    
    x1 = event.x
    y1 = event.y

def releaseL(event) :
    global x2, y2
    
    x2 = event.x
    y2 = event.y
    
    draw()

def clear(event) :
    c1.delete("all")
    
def draw() :
    global x1, x2, y1, y2
    c1.create_rectangle(x1, y1, x2, y2, fill = random.choice(colors))
    
root.bind("<Button-1>", clickL)
root.bind("<Button-2>", clear)
root.bind("<ButtonRelease-1>", releaseL)


"""
def clickL(event) :
    l.configure(text = random.randint(1, 10))

def clickR(event) :
    l.configure(text = f"mouse X:{event.x}\nmouse Y:{event.y}")

root.bind("<Button-1>", clickL)
root.bind("<Button-3>", clickR)

l = Label(root, text = 0, font=("", 100))
l.pack()
"""

"""

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
rb1.pack(side = LEFT, padx= 5, pady= 5)

rb2 = Radiobutton(root, text = "2", variable = mv, value = 2, command = set)
rb2.pack(side = LEFT, padx= 5, pady= 5)

rb3 = Radiobutton(root, text = "3", variable = mv, value = 3, command = set)
rb3.pack(side = LEFT, padx= 5, pady= 5)
"""

root.mainloop()
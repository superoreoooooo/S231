from tkinter import *
from tkinter import messagebox

import random

root = Tk()

root.title("테스트")
root.geometry("1024x768")
root.resizable(width = False , height = False)

colors = ["red", "blue", "white", "yellow", "black"]
color = random.choice(colors)

l1 = Label(root, text = color)
l1.pack()

c1 = Canvas(root, width=1024, height=768)
c1.pack()

x1 = 0
y1 = 0
x2 = 0
y2 = 0

def clickL(event) :
    global x1, y1, color
    
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
    global x1, x2, y1, y2, color
    c1.create_rectangle(x1, y1, x2, y2, fill = color)
    
    swapColor()
    
def swapColor(event = None) :
    global color
    color = random.choice(colors)
    l1.configure(text = color)
    
root.bind("<Button-1>", clickL)
root.bind("<Button-2>", clear)
root.bind("<ButtonRelease-1>", releaseL)
root.bind("<Button-3>", swapColor)

root.mainloop()
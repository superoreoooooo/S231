from tkinter import *

root = Tk()

root.title("Draw")
root.geometry("1024x768")
root.resizable(width = False , height = False)

canv = Canvas(root, width=1024, height=768)
canv.pack()

def drawCircle(event) :
    canv.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, width = 5, outline = "green")

def drawRectangle(event) :
    canv.create_rectangle(event.x - 50, event.y - 50, event.x + 50, event.y + 50, width = 5, outline = "red")

root.bind("<Button-1>", drawCircle)
root.bind("<Button-3>", drawRectangle)

root.mainloop()
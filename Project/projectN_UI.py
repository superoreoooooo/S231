from tkinter import *
from tkinter import messagebox
import projectN_main

root = Tk()
root.title("Project N")
#root.geometry("1024x768")
root.resizable(width=False, height=False)

bg = StringVar()
role = StringVar()
npcData = {}

def view() :
    pass

def exitUI() :
    root.destroy()

def clickGenButton() :
    global new, bg, role, npcData

    if (bg.get() == "" or role.get() == "") :
        messagebox.showinfo("ERROR","배경과 역할을 입력해 주세요.")
        return

    new = Toplevel()
    new.title("Message")
    new.resizable(width=False, height=False)

    lab = Label(new, text="Complete!", font=("Ariel", 15))
    lab.grid(row=0, column=0)


    npcData = projectN_main.run(bg.get(), role.get())

def check() :
    msg = "이름 : " + npcData["이름"] + "\n스토리 : " + npcData["스토리"] + "\n퀘스트" + "\n퀘스트1 : " + str(npcData["퀘스트"]["퀘스트1"]) + "\n퀘스트2 : " + str(npcData["퀘스트"]["퀘스트2"]) + "\n퀘스트3 : " + str(npcData["퀘스트"]["퀘스트3"]) + "\n퀘스트4 : " + str(npcData["퀘스트"]["퀘스트4"])
    messagebox.showinfo("check", msg)

label_MainText = Label(root, text="Project N ~게임 NPC 생성기~", font=("Ariel", 15))
label_bg = Label(root, width=10, text="배경")
label_role = Label(root, width=10, text="역할")

textbox_bg = Entry(root, width=30, textvariable=bg)
textbox_role = Entry(root, width=30, textvariable=role)

button_Generate = Button(root, text="Generate", width=10, command=clickGenButton)
button_Check = Button(root, text="Check", width=10, command=check)
button_view = Button(root, text="view", width=10, command=view)
button_exit = Button(root, text="Exit", width=10, command=exitUI)

label_MainText.grid(row=0, column=0, columnspan=4)
label_bg.grid(row=1, column=0)
label_role.grid(row=2, column=0)
textbox_bg.grid(row=1, column=1, columnspan=3)
textbox_role.grid(row=2, column=1, columnspan=3)
button_Generate.grid(row=3, column=0)
button_Check.grid(row=3, column=1)
button_view.grid(row=3, column=2)
button_exit.grid(row=3, column=3)


root.mainloop() 
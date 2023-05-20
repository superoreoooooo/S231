from tkinter import *
from tkinter import messagebox
import projectN_main

root = Tk()
root.iconbitmap("Project/Data/icon.ico")
root.title("Project N")
#root.geometry("1024x768")
root.resizable(width=False, height=False)

bg = StringVar()
role = StringVar()
npcData = {}

def view() : #미구현
    pass

def exitUI() :
    root.destroy()

def clickGenButton() :
    global new, bg, role, npcData

    if (bg.get() == "" or role.get() == "") :
        messagebox.showinfo("ERROR", "배경과 역할을 입력해 주세요.")
        return

    new = Toplevel()
    new.title("Message")
    new.resizable(width=False, height=False)

    lab = Label(new, text="Complete!", font=("appleSDGothicNeoL00", 15))
    lab.grid(row=0, column=0)


    npcData = projectN_main.run(bg.get(), role.get())

def check() :
    global npcData
    if (len(npcData) == 0) :
        messagebox.showerror("ERROR", "생성을 먼저 해주세요.")
    else :
        msg = "이름 : " + npcData["이름"] + "\n스토리 : " + npcData["스토리"] + "\n퀘스트" + str(npcData["퀘스트"])
        messagebox.showinfo("check", msg)

image = PhotoImage(file="Project/Data/ico_128.png")
label_img = Label(root, image=image)
label_bg = Label(root, width=10, text="Genre", font=("appleSDGothicNeoL00"))
label_role = Label(root, width=10, text="Role", font=("appleSDGothicNeoL00"))

textbox_bg = Entry(root, width=30, textvariable=bg) 
textbox_role = Entry(root, width=30, textvariable=role)

button_Generate = Button(root, text="Generate", width=10, font=("appleSDGothicNeoL00"), command=clickGenButton)
button_Check = Button(root, text="Check", width=10, font=("appleSDGothicNeoL00"), command=check)
button_view = Button(root, text="view", width=10, font=("appleSDGothicNeoL00"), command=view)
button_exit = Button(root, text="Exit", width=10, font=("appleSDGothicNeoL00"), command=exitUI)

#label_MainText.grid(row=0, column=0, columnspan=1)
label_img.grid(row=0, column=1, columnspan=2)
label_bg.grid(row=1, column=0)
label_role.grid(row=2, column=0)
textbox_bg.grid(row=1, column=1, columnspan=3)
textbox_role.grid(row=2, column=1, columnspan=3)
button_Generate.grid(row=3, column=0)
button_Check.grid(row=3, column=1)
button_view.grid(row=3, column=2)
button_exit.grid(row=3, column=3)


root.mainloop() 
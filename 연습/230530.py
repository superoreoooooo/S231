from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageTk

def displayPhoto(img, width, height) :
    global root, canvas, inPhoto, outPhoto, inX, inY
    if canvas != None :
        canvas.destroy()
    root.geometry(str(width)+"x"+str(height))
    print(str(width)+"x"+str(height))
    cImage = ImageTk.PhotoImage(img)
    canvas = Canvas(root, width=width, height=height)
    canvas.create_image(0, 0, anchor = NW, image=cImage)
    canvas.pack()
    root.mainloop()
    
def func_open() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    filename = askopenfilename(parent=root, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif"), ("모든 파일", "*.*") ))
    inPhoto = Image.open(filename)
    inX = inPhoto.width
    inY = inPhoto.height
    outPhoto = inPhoto.copy()
    outX = outPhoto.width
    outY = outPhoto.height
    displayPhoto(outPhoto, outX, outY)

def func_save() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    if outPhoto == None:
        return
    saveFp = asksaveasfile(parent=root, mode="w", defaultextension=".jpg",filetypes=(("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")))
    outPhoto.save(saveFp.name)

def func_exit() :
    exit()

def func_zoomin() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=8)
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.resize((int(inX * scale), int(inY * scale)))
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)
    
def func_zoomout() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    scale = askinteger("축소배수", "축소할 배수를 입력하세요", minvalue=2, maxvalue=8)
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.resize((int(inX / scale), int(inY / scale)))
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)

def func_mirror1() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.transpose(Image.FLIP_TOP_BOTTOM)
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)
    
def func_mirror2() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.transpose(Image.FLIP_LEFT_RIGHT)
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)

def func_rotate() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.rotate(degree, expand=True)
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)

def func_bright() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    value = askfloat("밝게/어둡게", "값을 입력하세요(0.0~5.0)", minvalue=0.0, maxvalue=5.0)
    outPhoto = inPhoto.copy()
    outPhoto = ImageEnhance.Brightness(outPhoto).enhance(value)
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)

def func_embos() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.filter(ImageFilter.EMBOSS)
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)
    
def func_blur() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.filter(ImageFilter.BLUR)
    outX = outPhoto.width
    outY = outPhoto.heightx
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)

def func_sketch() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.filter(ImageFilter.CONTOUR)
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)

def func_contour() :
    global root, canvas, inPhoto, outPhoto, inX, inY
    outPhoto = inPhoto.copy()
    outPhoto = outPhoto.filter(ImageFilter.FIND_EDGES)
    outX = outPhoto.width
    outY = outPhoto.height
    inPhoto = outPhoto
    displayPhoto(outPhoto, outX, outY)

## 전역 변수 선언 부분 ##
root, canvas = None, None
inPhoto, outPhoto = None, None
tmp = None
inX, inY = 0, 0


## 메인 코드 부분 ##
root = Tk()
root.geometry("500x500")
root.title("포토 에디터")

mainMenu = Menu(root)
root.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
imgMenu1 = Menu(mainMenu)
imgMenu2 = Menu(mainMenu)

mainMenu.add_cascade(label = "파일", menu = fileMenu)
mainMenu.add_cascade(label = "이미지 처리(1)", menu = imgMenu1)
mainMenu.add_cascade(label = "이미지 처리(2)", menu = imgMenu2)


fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_command(label = "파일 저장", command = func_save)
fileMenu.add_command(label = "프로그램 종료", command = func_exit)
fileMenu.add_separator()

imgMenu1.add_command(label = "확대", command = func_zoomin)
imgMenu1.add_command(label = "축소", command = func_zoomout)
imgMenu1.add_command(label = "상하 반전", command = func_mirror1)
imgMenu1.add_command(label = "좌우 반전", command = func_mirror2)
imgMenu1.add_command(label = "확대", command = func_rotate)
imgMenu1.add_separator()

imgMenu2.add_command(label = "밝게/어둡게", command = func_bright)
imgMenu2.add_command(label = "엠보싱", command = func_embos)
imgMenu2.add_command(label = "블러링", command = func_blur)
imgMenu2.add_command(label = "연필스케치", command = func_sketch)
imgMenu2.add_command(label = "경계선추출", command = func_contour)
imgMenu2.add_separator()

#실습1
#상단 메뉴 생성하기

root.mainloop()
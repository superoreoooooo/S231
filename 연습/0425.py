"""

f = open("C:/Users/user/Documents/python/pytest/연습/kia.txt", "r", encoding="UTF-8")
ff = open("C:/Users/user/Documents/python/pytest/연습/write.txt", "w", encoding="UTF-8")

fList = list()
f2 = f.readlines()

for i in f2 :
    if (i.count("\n") >= 1) :
        fList.append(i.split("\n")[0])
    else :
        fList.append(i)

for i in range(0, len(fList), 1) :
    ff.writelines(fList[i] + "ㅋㅋ\n")
    print(f"{i + 1}: {fList[i]}")

ff.writelines("END")

f.close()
ff.close()

"""

def copy(fn1, fn2) :
    f = open(fn1, "r", encoding="UTF-8")
    ff = open(fn2, "w", encoding="UTF-8")

    fList = list()
    f2 = f.readlines()

    for i in f2 :
        if (i.count("\n") >= 1) :
            fList.append(i.split("\n")[0])
        else :
            fList.append(i)

    for i in range(0, len(fList), 1) :
        ff.writelines(fList[i] + "\n")

    ff.writelines("\n=END=")

    f.close()
    ff.close()
    
    print("복제 완료~!")
    
copy("C:/Users/user/Documents/python/pytest/연습/kia.txt", "C:/Users/user/Documents/python/pytest/연습/write.txt")

f = open("C:/Users/user/Documents/python/pytest/연습/keyboard.txt", "w", encoding="UTF-8")

while True :
    i = input(": ")
    
    if (i == "") :
        break
    
    f.writelines(i + "\n")

f.close()
print(f.name.split("/")[len(f.name.split("/")) - 1] + " 파일이 저장되었습니다.")
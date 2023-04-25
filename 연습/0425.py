f = open("C:/Users/user/Documents/python/pytest/연습/kia.txt", "r", encoding="UTF-8")

fList = list()
f2 = f.readlines()

for i in f2 :
    if (i.count("\n") >= 1) :
        fList.append(i.split("\n")[0])
    else :
        fList.append(i)

for i in range(0, len(fList), 1) :
    print(f"{i + 1}: {fList[i]}")

f.close()
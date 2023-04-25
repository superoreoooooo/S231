f = open("C:/Users/user/Documents/python/pytest/연습/test.txt", "r", encoding="UTF-8")

fList = list()
f2 = f.readlines()

for i in f2 :
    if (i.count("\n") >= 1) :
        fList.append(i.split("\n")[0])
    else :
        fList.append(i)

print(fList)

f.close()
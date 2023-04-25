import os

f = open("C:/Users/user/Documents/python/pytest/취미생활/test.py", "r", encoding = "UTF-8")

print(f"\n\n{f.read()}\n\n")

for i in range(0, 10, 1) :
    fList = list()
    f2 = open("C:/Users/user/Documents/python/pytest/취미생활/test/test" + str(i) + ".py", "w", encoding = "UTF-8")

    for i in f.readlines() :
        if (i.count("\n") >= 1) :
            fList.append(i.split("\n")[0])
        else :
            fList.append(i)

    for i in range(0, len(fList), 1) :
        f2.writelines(fList[i] + "\n")
    f2.close()

f.close()
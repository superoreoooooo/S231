from a1 import Ms
import random

l = [Ms(x, random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for x in range(10)]


def save(_file, _list) :
    f = open("연습/" + _file + ".txt", "w", encoding="UTF-8")
    for x in _list:
        if (str(type(x)) == "<class 'a1.Ms'>") :
            f.write(x.getStr() + "\n")
        elif (type(x) == int) :
            f.write(str(x) + "\n")
        else :
            f.write(x + "\n")
        
save("log", l)
save("aaa", [x for x in range(10)])
save("bbb", ["a" for _ in range(10)])
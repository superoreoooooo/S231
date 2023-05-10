from a1 import Ms
import random

l = [Ms(x, random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for x in range(10)]


def save(_file, _list) :
    f = open("연습/" + _file + ".txt", "w", encoding="UTF-8")
    for x in _list:
        f.write(x.getStr() + "\n")
        
save("log", l)
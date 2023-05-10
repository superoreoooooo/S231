from a1 import Ms
import random

l = [Ms(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]


def save(_file, _list) :
    f = open("연습/" + _file + ".txt", "w", encoding="UTF-8")
    cnt = 0
    for x in _list:
        print(int(x.avg))
        cnt += 1
        f.write(str(cnt) + " : " + str(int(x.avg)) + "\n")
        
save("log", l)
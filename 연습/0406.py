import random

numbers = list(range(1, 46, 1))
lotto = []

def getNum(l) :
    while (True) :
        n = random.choice(numbers)
        if (n in lotto) :
            getNum(l)
        else :
            return n
        
for i in range(0, 5, 1) :
    lotto.append(getNum(numbers))

lotto.sort()

print("로또번호 => ", end = "")
for i in lotto :
    print(i, end = " ")
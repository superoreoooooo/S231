import random

numbers = list(range(1, 46, 1))
lotto = []

def getNum(l) :
    n = 0
    while (True) :
        n = random.choice(numbers)
        if (n not in lotto) :
            return n
            break
        
for i in range(0, 5, 1) :
    lotto.append(getNum(numbers))

lotto.sort()

print("로또번호 => ", end = "")
for i in lotto :
    print(i, end = " ")
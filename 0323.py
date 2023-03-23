"""

*중첩for문 구구단*

for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        print(i, "X", j, "=", i*j)

"""

"""

sum = 0

n1, n2 = 0, 0

while True :
    n1 = int(input("n1 : "))
    if n1 == 0 :
        break
    n2 = int(input("n2 : "))
    
    sum = n1 + n2
    print(num)
    
print("clear")

"""

"""

import random

cnt = 0

while True :
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    
    cnt += 1
    
    print("cnt :", cnt, "dice :", d1, d2, d3)
    
    if d1 == d2 and d2 == d3 :
        break
        
print(cnt)
"""

import random

cn = random.randint(1, 5)

for i in range (1, 11, 1) :
    c = int(input("num : "))
    
    if c == cn :
        print("t")
        break
    else :
        print("n")
        continue
    
print("over")
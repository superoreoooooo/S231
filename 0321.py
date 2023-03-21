import random
import math
import numpy as np

"""

age = int(input("age : "))

if (age >= 18) :
    print("pass")
else :
    print("fail")
print("hello")
"""

"""
status = ""

pick = input("my input : ")
pc = random.choice(["rock", "paper", "scissors"])

if (pick == pc) :
    status = "draw"
else :
    if (pick == "rock") :
        if (pc == "paper") :
            status = "win"
        else : 
            status = "lose"
    elif (pick == "paper") :
        if (pc == "rock") :
            status = "win"
        else :
            status = "lose"
    elif (pick == "scissors") :
        if (pc == "paper") :
            status = "win"
        else :
            status = "lose"
    else :
        status = "error"

print("pc input :", pc)
print(status)
"""


"""
hap = 0
s = ""

for i in range (1, 11, 1) :
    hap += i
    if (i == 10) :
        print(i, end = " = ")
    else :
        print(i, end = " + ")
print(hap)

"""

"""
fac = 1

for i in range (1, 6, 1) :
    fac *= i

print(fac)
print(math.factorial(5))
"""

"""
sum = 0

for i in range (1001, 2001, 2) :
    sum += i

print(sum)
"""

list = [10, 50, 100, 50, 200]
a = np.shape(list)
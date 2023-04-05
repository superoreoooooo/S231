import turtle
import random

"""

*실전예제 -> 모험을 떠나는 거북이*

turtle.shape('turtle')
turtle.penup()

while True :
    x = int(input("X : "))
    y = int(input("Y : "))
    text = input("String : ")
    
    turtle.goto(x, y)
    turtle.write(text, font=("Arial", 30))
    
turtle.done()
"""

"""

*자유롭게? 모험을 떠나는 거북이*

turtle.shape('turtle')
turtle.penup()

strlist = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"]

for i in range(30) :
    text = strlist[random.randint(0, len(strlist) - 1)]
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    turtle.write(text, font=("Arial", 30))
turtle.done()
"""

"""

*if / elif / else*

score = int(input("score : "))

if score >= 90 :
    print("A", end='')
elif score >= 80 :
    print("B", end='')
elif score >= 70 :
    print("C", end='')
elif score >= 60 :
    print("D", end='')
else :
    print("F", end='')
print("학점입니다.")
"""
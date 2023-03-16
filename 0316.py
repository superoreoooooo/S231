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

turtle.shape('turtle')
turtle.penup()

strlist = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"]

for i in range(30) :
    text = strlist[random.randint(0, len(strlist) - 1)]
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
    turtle.write(text, font=("Arial", 30))
turtle.done()
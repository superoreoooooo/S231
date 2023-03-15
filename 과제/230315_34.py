import turtle

#실습1

print("#실습1")

n1 = int(input("숫자1 ==> "))
n2 = int(input("숫자2 ==> "))

print(n1, "+", n2, "=", n1 + n2)
print(n1, "-", n2, "=", n1 - n2)
print(n1, "*", n2, "=", n1 * n2)
print(n1, "/", n2, "=", n1 / n2)
print(n1, "%", n2, "=", "%.5f" % (n1 % n2))
print(n1, "**", n2, "=", n1 ** n2)



#실습2

print("#실습2")

turtle.shape('turtle')
turtle.speed(1000)
cnt = 0

while(True) :
    turtle.forward(1)
    turtle.right(0.5)
    cnt += 1
    if (cnt == 720) :
        break



#실습3

print("#실습3")

str = "*"

for i in range(50) :
    print(str)
    str = str + "*"
import turtle

#과제1

print("#실습1")

n1 = int(input("숫자1 ==> "))
n2 = int(input("숫자2 ==> "))

print(n1, "+", n2, "=", n1 + n2)
print(n1, "-", n2, "=", n1 - n2)
print(n1, "*", n2, "=", n1 * n2)
print(n1, "/", n2, "=", n1 / n2)
print(n1, "%", n2, "=", "%.5f" % (n1 % n2))
print(n1, "**", n2, "=", n1 ** n2)



#과제2

turtle.shape('turtle')
turtle.speed(1000)

while(True) :
    turtle.forward(1)
    turtle.right(0.5)
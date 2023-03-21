import turtle


#과제1


num = input("학번을 입력하세요: ")
name = input("이름을 입력하세요: ")
hobby = input("취미를 입력하세요: ")
bar = ""

for i in range (42):
    bar = bar + "-"

print(bar)
print("      순천향대학교 메타버스&게임학과")
print(bar)


print("1. 학번:", num)
print("2. 이름:", name)
print("3. 취미:", hobby)


#과제2


pi = 3.1415926535

print("%0.0f"%pi)
print("%0.1f"%pi)
print("%0.2f"%pi)
print("%0.3f"%pi)
print("%0.4f"%pi)
print("%0.5f"%pi)
    
    
#과제3


print("## 택배를 보내기 위한 정보를 입력하세요. ##")
person = input("받는 사람 : ")
addr = input("주소 : ")
weight = int(input("무게 : "))

print("** 받는 사람 ==>", person)
print("** 주소 ==>", addr)
print("** 배송비 ==>", weight * 5)

      
#과제4


turtle.shape('turtle')

def building(x, y, gap):
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x * 2)
    turtle.right(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(gap)

turtle.setpos(-370, -300)
turtle.clear()

building(10, 70, 20)
building(15, 90, 20)
building(30, 150, 20)
building(20, 70, 20)
building(10, 90, 20)
building(50, 200, 20)
building(10, 70, 20)

turtle.left(90)
turtle.forward(200)
turtle.left(45)
turtle.forward(20)
turtle.right(75)
turtle.forward(60)
turtle.right(120)
turtle.forward(60)
turtle.right(75)
turtle.forward(20)
turtle.left(45)
turtle.forward(200)
turtle.left(90)
turtle.forward(20)

building(30, 150, 20)
building(50, 200, 20)
building(15, 90, 20)
building(10, 70, 20)

turtle.up()
turtle.setpos(0, 0)
turtle.down()

turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
turtle.left(60)
turtle.forward(60)
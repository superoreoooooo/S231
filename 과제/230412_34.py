"""

*제출X*

"""

#1

a = 100
b = 200

print(a + b)

#2

a = '순천향'
b = '대학교'

print(a + b)

#3

name = input("이름 : ")
age = input("나이 : ")

print(name, f'({age})')

#4


name = input("이름 : ")
age = input("나이 : ")

if (int(age) >= 20) : 
    print(name, f'({age})', "성인")
else :
    print(name, f'({age})', "미성년자")

#5

l = list(v for v in range(1, 100, 2))

for i in l :
    if (i >= 55 and i < 64) :
        print(i, end = " ")

print("")

#6

for i in l :
    if (i < 3 or i >= 94) :
        print(i, end = " ")

print("")

#7

score = int(input("점수 => "))

print(score >= 70)

#8

print("abc" == "가나다")

#9

score = int(input("점수 => "))

if (score >= 90) :
    print("A")
elif (score >= 80) :
    print("B")
else :
    print("C")

#10

for i in range(0, 10, 1) :
    for j in range(0, i + 1, 1) :
        print("*", end = "")
    print("")
    
#11

sum = 0

for i in range(101, 200, 2) :
    sum += i

print(sum)

#12

for i in range(2, 10, 1) :
    for j in range(2, 10, 1) :
        print(i, "*", j, "=", i*j)

#13

for i in range(1, 101, 1) :
    if (i % 6 == 1 or i % 5 == 2) :
        print(i, end = " ")

print("")

#14

cnt = 0

while(True) :
    cnt += 1
    if (cnt >= 100) :
        break
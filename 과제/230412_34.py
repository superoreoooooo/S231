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
    print(f'({age})', "성인")
else :
    print(f'({age})', "미성년자")

#5

l = list(range(1, 100, 2))

for i in l :
    if (i >= 55 and i <= 64) :
        print(i, end = " ")

print("")

#6

for i in l :
    if (i < 3 or i >= 94) :
        print(i, end = " ")

print("")

#7


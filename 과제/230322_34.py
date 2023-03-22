import random
"""
#실습1

c = int(input("출력할 단수 입력 : "))

for i in range (1, 10, 1) :
    print(c, "X", i, "=", c * i)

#실습2

score = int(input("점수 입력(0~100) : "))
grade = ""

if (score >= 90) :
    grade = "A"
elif (score >= 80) :
    grade = "B"
elif (score >= 70) :
    grade = "C"
elif (score >= 60) :
    grade = "D"
else :
    grade = "F"

print(grade)

#실습3

sum = 0

target = int(input("숫자 입력 : "))

for i in range (1, target + 1, 1) :
    sum += i

print(sum)

#실습4

num = int(input("input number : "))
w = int(input("배수 입력 : "))

for i in range(w, num + 1, w) :
    print(i, end = ', ')
    
print("\n")

"""
#실습5 쉬운버전
"""
numbers = list(range(1, 46, 1))

for i in range (0, 10, 1) :
    lotto = random.sample(numbers, 5)
    print(lotto)
"""
#실습5 어려운버전

def check(num) :
    return num + 1

numbers = list(range(1, 46, 1))

for i in range (0, 10, 1) :
    print(check(i))
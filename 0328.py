import random
"""

*오늘의명언*

wiseSay = [
"삶이 있는 한 희망은 있다",
"언제나 현재에 집중할 수 있다면 행복할 것이다",
"신은 용기있는 자를 결코 버리지 않는다",
"피할 수 없으면 즐겨라",
"행복한 삶을 살기위해 필요한 것은 거의 없다",
"내일은 내일의 태양이 뜬다",
"계단을 밟아야 계단 위에 올라설 수 있다",
"행복은 습관이다, 그것을 몸에 지니라",
"1퍼센트의 가능성, 그것이 나의 길이다",
"작은 기회로 부터 종종 위대한 업적이 시작된다"]

print(wiseSay[random.randint(0, len(wiseSay) - 1)])

"""

l = list(range(0, 10))
print("1 :",l)

l[1] = 100
print("2 :", l)

sum = 0
for i in range(0, len(l)) :
    sum += l[i]

print("3 :", sum)

l[2] = 'not number'
print("4 :", l)


for i in range(10, 21) :
    l.append(i)
    
print("5 :", l)
print("6 :", len(l))

l2 = l.copy()
l3 = l.copy()
l4 = l.copy()

for i in range(0, 9) :
    del(l2[0])
    
print("7 :", l2)

for i in range(3, len(l3)) :
    del(l3[3])

print("8 :", l3)
    
for i in range(0, len(l4)) :
    if (type(l4[i]) is str) :
        l4[i] = i
        
print("9 :", l4)

l5 = l4.copy()
l6 = []

for i in range(0, len(l5), 1) :
    if (l5[i] < 10) :
        l6.append(l5[i])
        
print("10 :", l6)
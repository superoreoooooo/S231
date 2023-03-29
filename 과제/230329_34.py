#베낄거면 깃헙 스타라도 눌러주세요

import random as r

l = list(range(1, 31))

print("1:", l)

l[0] = 1000

print("2:", l)

l[len(l) - 1] = 3000

print("3:", l)

for i in range(len(l) + 1, 41, 1) :
    l.append(i)

print("4:", l)

for i in range(0, len(l), 1) :
    if (l[i] >= 100) :
        l[i] = i + 1
        
print("5:", l)

print("6:", l[0:5+1])

print("7:", l[5:10+1])

l[9] = [0, 0, 0]

print("8:", l)

for i in range(0, len(l), 1) :
    if (type(l[i]) is not int) :
        l[i] = i + 1
        
print("9:", l)

l2 = l.copy()
l2.reverse()

print("10:", l2)

for i in range(0, len(l), 1) :
    if (l[i] % 2 == 0) :
        l[i] *= 10
        
print("11:", l)

numMat = [[0 for c in range(10)] for r in range(4)]

cnt = 0

for i in range(0, 4, 1) :
    c = cnt
    for j in range(0, 10, 1) :
        numMat[i][j] = l[c]
        c += 1
    cnt += 4

print("12:", numMat)

l3 = [0 for k in range(10)]

for i in range(0, 10, 1) :
    l3[i] = numMat[0][i]

print("13:", l3)

sum = 0

for i in range(0, len(l3) + 1, 1) :
    if (i == len(l3)) :
        l3[i - 1] = sum
    else :
        sum += l3[i]

print("14:", l3)

sum = 0

while(len(l3) != 1) :
    sum += l3.pop()

print("15: 총합(" + str(sum) + "),", "남은 리스트:(" + str(l3) + ")")

score = [r.randint(0, 100) for k in range(100)]

print("16", score)

max = 0
min = 100
avg = 0

for i in range(0, len(score), 1) :
    if (score[i] > max) :
        max = score[i]
    if (score[i] < min) : 
        min = score[i]
    avg += score[i]

print("최고:", str(max) + "점", "최하:", str(min) + "점,", "평균:", avg / len(score))
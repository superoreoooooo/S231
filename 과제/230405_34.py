import random

items = ["색소폰", "바이올린", "피아노", "트럼펫", "일렉기타", "베이스기타", "통기타", "리코더", "우쿨렐레", "플루트"]
counts = [80, 74, 92, 52, 21, 94, 48, 64, 20, 89]

dicts = {}

print("#1")
for i in range (0, len(items), 1) :
    dicts[items[i]] = counts[i]

print(dicts)

print("#2")
dicts["색소폰"] = 1000

print(dicts)

print("#3")
del(dicts["트럼펫"])

print(dicts)

print("#4")

sum = 0
for i in dicts :
    sum += dicts[i]

print("총합:", sum)

print("#5")

min = 1000
name = ""

for i in dicts :
    if (dicts[i] < min) :
        min = dicts[i]
        name = i

print("가장 적은 악기:", name + ",", "개수:", min)

print("#6")

max = 0
name = ""

for i in dicts :
    if (dicts[i] > max) :
        max = dicts[i]
        name = i

print("가장 많은 악기:", name + ",", "개수:", max)

print("#7")

for i in dicts :
    cnt = dicts[i]
    ndict = [0, 0]
    ndict[0] = cnt
    ndict[1] = random.randint(10000, 99999)
    
    dicts[i] = ndict

print(dicts)

print("#8")

n_max = ""
max = 0

for i in dicts :
    if (dicts[i][0] * dicts[i][1] > max) :
        max = dicts[i][0] * dicts[i][1]
        n_max = i

print("개수 * 가격이 가장 높은 악기명:", n_max)

print("#9")

l_n = []
l_c = []
l_p = []

for i in dicts :
    l_n.append(i)
    l_c.append(dicts[i][0])
    l_p.append(dicts[i][1])
    
print("악기명 리스트:", l_n)
print("개수 리스트:", l_c)
print("가격 리스트:", l_p)

x = int(input("x : "))
y = int(input("y : "))

l_final = list(range(y))

for dy in range(0, y, 1) :
    lx = []
    for dx in range(dy, x + dy, 1) :
        if (dx + 1 > x) :
            lx.append(dx + 1 - x)
        else :
            lx.append(dx + 1)
    l_final[dy] = lx

for dy in range(0, y, 1) :
    for dx in range(0, x, 1) :
        print(l_final[dy][dx], end = " ")
    print("")
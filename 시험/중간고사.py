l1 = [x for x in range(1, 20, 2)]

print(l1)

for i in l1 :
    print(i, end = " ")
    
sum = 0

for i in l1 :
    sum += i

print("\n", sum)
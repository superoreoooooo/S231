x = int(input("x : "))
y = int(input("y : "))

lx = list(range(x))

for dx in range(0, x, 1) :
    ly = []
    for dy in range(dx, y + dx, 1) :
        if (dy + 1 > y) :
            ly.append(dy + 1 - y)
        else :
            ly.append(dy + 1)
    lx[dx] = ly

for i in range(0, y, 1) :
    for j in range(0, x, -1) :
        print(lx[j][i], end=" ")
    print("")
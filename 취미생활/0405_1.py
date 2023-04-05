x = int(input("x : "))
y = int(input("y : "))

for dy in range(0, y, 1) :
    for dx in range(dy, x + dy, 1) :
        if (dx + 1 > x) :
            print(dx + 1 - x, end = " ")
        else :
            print(dx + 1,  end = " ")
    print("")
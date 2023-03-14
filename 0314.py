import os

py = 3
mo = 2
ex = 1

B = 3.5
A0 = 4
A = 4.5

avg = (py * B + mo * A0 + ex * A) / (py + mo + ex)

print("%.2f" % avg)

os.system("pause")
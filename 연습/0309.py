"""

def getkg(lb):
    return lb * 0.453592

def getlb(kg):
    return kg * 2.204623


lb = int(input("input lb : "))
print(lb, "lb is", "%0.5f"%getkg(lb), "kg")


kg = int(input("input kg : "))
print(lb, "kg is", "%0.5f"%getlb(kg), "lb")

"""

"""

total = 0

for i in range (10) :
    total -= 900

for i in range (2) :
    total += 1800

for i in range (5) :
    total -= 3500

for i in range (4) :
    total += 4000

for i in range (1) :
    total += 1500
    
for i in range (4) :
    total += 2000
    
for i in range (5) :
    total += 1800
    
print(total)

"""


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


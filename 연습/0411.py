"""

from datetime import datetime, timedelta

def getCurrent() :
    curDate = datetime.now()
    return curDate

def getAfter(now, day) :
    afterDate = now + timedelta(days = day)
    return afterDate

curDate, afterDate = None, None
curDate = getCurrent()

afterDate = getAfter(curDate, 100)

print("현재 날짜와 시간 =>", curDate, "\n100일 후 날짜와 시간 =>", afterDate)

"""

"""

def isTrue() :
    pwd = input("input password : ")
    if (pwd.isalnum()) :
        return True
    else :
        return False
    
while (True) :
    if (isTrue()) :
        print("비밀번호가 올바르게 생성되었어요.")
    else :
        print("오류! 비밀번호가 규칙에 맞지 않습니다.")

"""

print("#1")

let = "letters"

print(let[0], let[2])



print("#2")

wrd = "12가3450"
print(wrd[3:])



print("#3")

tList = ['배트맨', '슈퍼맨', '아이언맨']

for i in range(0, len(tList) + 1, 1) :
    if (tList[i] == "슈퍼맨" and tList[i + 1] == "아이언맨") :
        tList[i + 1] = "헐크"
        tList.append("아이언맨")
        
print(tList)



print("#4")

tList.remove("헐크")

print(tList)



print("#5")

l1 = [1, 2, 3]
l2 = [4, 5, 6]

ls = l1 + l2

print(ls)



print("#6")

tList = list(range(0, 11))

print("MAX :", max(tList), "/ MIN :", min(tList))



print("#7")

tList = list(range(1, 100, 2))

sum = 0

for i in tList :
    sum += i

print("Length :", len(tList), "/ sum :", sum)



print("#8")

tup = (1, 2, 3, 4, 5)
tList = list()

for i in tup :
    tList.append(i)

print(tList)
del(tup)



print("#9")

tup = tuple(tList)

print(tup)



print("#10")

tList = [c / 10 for c in range(1, 101, 1)]
    
print("List :", tList, "\n Length :", len(tList))



print("#11")

for i in range(0, len(tList), 1) :
    tList[i] = int(tList[i] * 10)

print(tList)
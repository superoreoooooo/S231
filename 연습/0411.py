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
def isTrue(pwd) :
    return pwd.isalnum()

while (True) :
    pwd = input("input password : ")
    if (isTrue(pwd)) :
        print("비밀번호가 올바르게 생성되었어요.")
        break
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

print(tList)
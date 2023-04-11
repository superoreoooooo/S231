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


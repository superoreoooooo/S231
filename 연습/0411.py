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
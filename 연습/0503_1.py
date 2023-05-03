class depart:
    c1 = ""
    c2 = ""
    
    def __init__(self, _s1 = "컴퓨터게임과기술", _s2 = "파이썬프로그래밍실습") :
        self.c1 = _s1
        self.c2 = _s2
    
    def printAll(self) :
        print(self.c1)
        print(self.c2)
    
student = depart("메타버스개론", "파이썬프로그래밍")

student.printAll()
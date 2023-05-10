class Ms:
    kor = 0
    eng = 0
    math = 0
    avg = 0
    
    def __init__(self, kor = 0, eng = 0, math = 0) :
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def getAvg(self) :
        self.avg = (self.kor + self.eng + self.math) / 3
    
s1 = Ms(50, 60 ,70)
s1.getAvg()

print(s1.avg)
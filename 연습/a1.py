class Ms:
    kor = 0
    eng = 0
    math = 0
    avg = 0
    
    def __init__(self, kor = 0, eng = 0, math = 0) :
        self.kor = kor
        self.eng = eng
        self.math = math
        self.getAvg()
    
    def getAvg(self) :
        self.avg = (self.kor + self.eng + self.math) / 3
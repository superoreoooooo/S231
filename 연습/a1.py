class Ms:
    id = 0
    kor = 0
    eng = 0
    math = 0
    avg = 0
    
    def __init__(self, id = 0, kor = 0, eng = 0, math = 0) :
        self.id = id
        self.kor = kor
        self.eng = eng
        self.math = math
        self.getAvg()
    
    def getAvg(self) :
        self.avg = (self.kor + self.eng + self.math) / 3
        
    def getStr(self) :
        return f"{self.id} : {int(self.avg)}"
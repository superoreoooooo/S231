class Ms:
    kor = 0
    eng = 0
    math = 0
    avg = 0
    
    def __init__(self, kor, eng, math) :
        self.avg = (kor + eng + math) / 3
    
s1 = Ms(50, 60 ,70)

print(s1.avg)
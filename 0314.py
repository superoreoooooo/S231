import os
import turtle

"""
*기말 평균학점 구하기*

py = 3
mo = 2
ex = 1

B = 3.5
A0 = 4
A = 4.5

avg = (py * B + mo * A0 + ex * A) / (py + mo + ex)

print("avg : %.2f" % avg)
"""
#################################################################################
"""
*while() 연습 문제*

cnt = 1
roop = True

while roop :
    print("SCV가", cnt, "번째 미네랄을 채취 했습니다.")
    cnt += 1
    
"""
#################################################################################
"""
*무한 거북이*

turtle.shape('turtle')
turtle.size(5)
turtle.color("blue")

while(True) :
    deg = int(input("deg : "))
    dis = int(input("dist : "))
    
    turtle.right(deg)
    turtle.forward(dis)
"""
#################################################################################



os.system("pause")
data = {}

print("**** 물품과 재고량 입력 ****")

while True:
    k = input("입력 물품 : ")
    
    if (k == "") :
        break
    
    data[k] = int(input("재고량 : "))

print("**** 물품과 재고량 확인 ****")

while True:
    k = input("찾을 물품 : ")
    
    if (k == "") :
        break
    elif (k in data.keys()) :
        print(str(data[k]) + "개 남았어요.")
    else :
        print("그 물품은 없어요.")
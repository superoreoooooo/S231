# 파이썬프로그래밍 실습 중간고사 유의사항
"""
	1. 시험 시작 이후 인터넷 사용 금지
	2. 파일 제출시에만 시험관에게 요청 후 인터넷 사용, 제출 후 즉시 퇴실
	3. 늦게 제출할 경우 감점
	4. 인터넷이 안되는 경우, 파이썬 설치에 문제가 있는 경우 등은 
	   예외사항으로 간주하고, 지체된 시간 만큼 추가 시간 부여
	5. 미리 준비한 pdf, 책, 노트 등은 활용 가능
	6. 문제의 오류가 있는 경우 시험관에게 바로 문의
	7. 문제당 5점, 4번 문제만 10점
"""


# 1-1
"""
- 1~20 사이의 홀수로 구성된 리스트 변수 생성해 출력
- 리스트 변수 선언시 직접 숫자 입력시 오답 처리
- 오답의 예: a = [1, 3, ..., 17, 19]

# 정답
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""
print("# 1-1번 문제")

l1 = [x for x in range(1, 20, 2)]
print(l1)


# 1-2
"""
- 1-1번에서 생성한 리스트 변수의 값을 한줄에 한 칸씩 띄어서 출력
- print문에 직접 정답 값을 입력할 경우 오답 처리

# 정답
1 3 5 7 9 11 13 15 17 19 
"""
print("\n# 1-2번 문제")

for i in l1 :
    print(i, end = " ")


# 1-3
"""
- 1-1번에서 생성한 리스트 변수의 총합을 출력
- print문에 직접 정답 값을 입력할 경우 오답 처리
- 오답의 예: print(100)

# 정답
100
"""
print("\n\n# 1-3번 문제")

sum = 0

for i in l1 :
    sum += i

print(sum)

# 1-4
"""
- 1-1번에서 생성한 리스트 변수의 길이를 출력
- print문에 직접 정답 값을 입력할 경우 오답 처리

# 정답
10
"""
print("\n# 1-4번 문제")

print(len(l1))


# 1-5
"""
- 1-1번에서 생성한 리스트 변수의 값을 역순으로 한줄에 한 칸씩 띄어서 출력
- print문에 직접 정답 값을 입력할 경우 오답 처리

# 정답
19 17 15 13 11 9 7 5 3 1 
"""
print("\n# 1-5번 문제")

l2 = l1.copy()
l2.reverse()

for i in l2 :
  print(i, end = " ")


# 1-6
"""
- 1-1번에서 생성한 리스트 변수를 3으로 나눈 나머지를 한줄에 한 칸씩 띄어서 출력
- print문에 직접 정답 값을 입력할 경우 오답 처리

# 정답
1 0 2 1 0 2 1 0 2 1 
"""
print("\n\n# 1-6번 문제")

for i in l1 :
  print(i % 3, end = " ")


# 2-1 
"""
- [40, 39, ..., 2, 1] 구성된 리스트 변수를 생성해 출력
- 리스트 변수 선언시 직접 숫자 입력시 오답 처리
- 오답의 예: a = [40, 39, ..., 2, 1] 와 같이 직접 선언

# 정답
[40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""
print("\n\n# 2-1번 문제")

l3 = [40 - x for x in range(0, 40, 1)]

print(l3)


# 2-2
"""
- 2-1의 리스트 변수에서 3 미만이거나 35 이상에 해당하는 값을 한줄에 한 칸씩 띄어서 출력
- print문에 직접 정답 값을 입력할 경우 오답 처리

# 정답
40 39 38 37 36 35 2 1 
"""
print("\n# 2-2번 문제")

for i in l3 :
  if (i < 3 or i >= 35) :
    print(i, end = " ")


# 2-3
"""
- 2-1의 리스트 변수에서 4의 배수이면서 5의 배수인 것을 한줄에 한 칸씩 띄어서 출력
- print문에 직접 정답 값을 입력할 경우 오답 처리

# 정답
40 20
"""
print("\n\n# 2-3번 문제")

for i in l3 :
  if (i % 4 == 0 and i % 5 == 0) :
    print(i, end = " ")


# 2-4
"""
- 2-1의 리스트 변수의 값 중 4의 배수와 5의 배수에 해당되는 값을 
  딕셔너리 변수로 선언해 각각 키가 '4배수', '5배수'에 해당되는
  값을 리스트 형태로 저장 후 출력
- 딕셔너리 변수에 직접 숫자를 입력해 선언하면 오답 처리      
- 4의 배수이면 5의 배수인 값은 중복으로 가지고 있음
- 오답의 예: a = {"4의 배수":[4, 8, ..., 40], ...}
- 정답 출력은 print(딕셔너리변수) 형태로

# 정답
{'4배수': [40, 36, 32, 28, 24, 20, 16, 12, 8, 4], 
'5배수': [40, 35, 30, 25, 20, 15, 10, 5]}
"""
print("\n\n# 2-4번 문제")

d1 = {}
l4, l5 = list(), list()

for i in l3 :
  if (i % 4 == 0) :
    l4.append(i)
  if (i % 5 == 0) :
    l5.append(i)

d1['4의 배수'] = l4
d1['5의 배수'] = l5

print(d1)


# 2-5
"""
- 2-4의 딕셔너리 변수의 모든 값을 하나의 리스트로 선언하고,
  오름차순 정렬 후 출력
- 중복되는 값이 있을 경우, 중복되는 값은 하나만 리스트 변수에 저장함
- print문에 직접 정답 값을 입력할 경우 오답 처리
- 힌트: 5 in [5, 10, 15]  =>  True

# 정답
[4, 5, 8, 10, 12, 15, 16, 20, 24, 25, 28, 30, 32, 35, 36, 40]
"""
print("\n# 2-5번 문제")

l6 = list()

for i in d1 :
  for j in d1[i] :
    l6.append(j)

l6.sort()

print(l6)


# 3-1
"""
- 영어, 수학, 국어의 각각 최소, 최고, 평균 점수를 출력
- 40명의 학생 번호 순서대로 선언된 eng, kor, math 사용
- print문에 직접 정답 값을 입력할 경우 오답 처리

# 정답
국어 최고점: 100, 최소점: 1, 평균점: 59.15
영어 최고점: 100, 최소점: 6, 평균점: 51.975
수학 최고점: 98, 최소점: 3, 평균점: 48.575
"""
print("\n# 3-1번 문제")
kor = [60, 10, 24, 77, 78, 62, 97, 84, 6, 67, 1, 59, 81, 81, 22, 41, 23, 97, 92, 88, 60, 10, 100, 71, 37, 99, 9, 51, 67, 75, 79, 27, 21, 72, 51, 62, 72, 91, 81, 81]
eng = [54, 91, 56, 85, 77, 44, 57, 38, 48, 34, 17, 98, 6, 100, 88, 9, 54, 43, 15, 75, 47, 40, 82, 73, 49, 90, 32, 53, 25, 53, 54, 77, 84, 48, 9, 62, 20, 17, 55, 20]
math = [46, 39, 17, 14, 69, 94, 27, 8, 33, 13, 51, 37, 35, 34, 76, 91, 90, 12, 53, 90, 36, 28, 27, 82, 59, 84, 77, 45, 25, 20, 98, 41, 62, 64, 75, 41, 14, 74, 3, 59]

k = 0
e = 0
m = 0

for i in kor :
  k += i

for i in eng :
  e += i

for i in math :
  m += i
  
k = k / len(kor)
e = e / len(eng)
m = m / len(math)


print("국어 최고점:", max(kor), "최소점:", min(kor), "평균점:", k)
print("영어 최고점:", max(eng), "최소점:", min(eng), "평균점:", e)
print("수학 최고점:", max(math), "최소점:", min(math), "평균점:", m)


# 3-2
"""
- "3-1의 리스트 3개를 입력받아 키가 학생 번호이고 값이 [국어점수, 영어점수, 수학점수]인 
  딕셔너리 변수를 생성 후 리턴" 하는 함수를 선언하고, 
  함수 호출 후 딕셔너리 변수를 리턴 받아 출력
- 각 학생의 번호는 2-1의 각 리스트의 (인덱스 + 1) 임, 첫번째 학생의 번호 1, 마지막 학생의 번호 40
- 함수를 사용하지 않는 경우 혹은 함수의 리턴 값이 없는 경우 감점
- 출력은 print(딕셔너리변수) 형태로

# 정답
{1: [60, 54, 46], 2: [10, 91, 39], 3: [24, 56, 17], 4: [77, 85, 14], 5: [78, 77, 69], 6: [62, 44, 94], 7: [97, 57, 27], 8: [84, 38, 8], 9: [6, 48, 33], 10: [67, 34, 13],
11: [1, 17, 51], 12: [59, 98, 37], 13: [81, 6, 35], 14: [81, 100, 34], 15: [22, 88, 76], 16: [41, 9, 91], 17: [23, 54, 90], 18: [97, 43, 12], 19: [92, 15, 53], 20: [88, 75, 90], 
21: [60, 47, 36], 22: [10, 40, 28], 23: [100, 82, 27], 24: [71, 73, 82], 25: [37, 49, 59], 26: [99, 90, 84], 27: [9, 32, 77], 28: [51, 53, 45], 29: [67, 25, 25], 30: [75, 53, 20], 
31: [79, 54, 98], 32: [27, 77, 41], 33: [21, 84, 62], 34: [72, 48, 64], 35: [51, 9, 75], 36: [62, 62, 41], 37: [72, 20, 14], 38: [91, 17, 74], 39: [81, 55, 3], 40: [81, 20, 59]}

"""
print("\n# 3-2번 문제")

def getDict(k, e, m) :
  d2 = {}
  for i in range(0, len(k), 1) :
    d2[i + 1] = [k[i], e[i], m[i]]
  return d2

d3 = getDict(kor, eng, math)

print(d3)

# 3-3
"""
- 3-2의 딕셔너리 변수의 값을 [국어점수, 영어점수, 수학점수, 3과목 평균]와 같이 
  수정 후 딕셔너리 변수를 출력
- 평균점수는 소수점을 버리고 저장하기 (반올림 혹은 소수점을 버린 경우 모두 정답 처리)
- 출력은 print(딕셔너리변수) 형태로

# 정답
{1: [60, 54, 46, 53], 2: [10, 91, 39, 46], 3: [24, 56, 17, 32], 4: [77, 85, 14, 58], 5: [78, 77, 69, 74], 6: [62, 44, 94, 66], 7: [97, 57, 27, 60], 8: [84, 38, 8, 43], 9: [6, 48, 33, 29], 10: [67, 34, 13, 38], 
11: [1, 17, 51, 23], 12: [59, 98, 37, 64], 13: [81, 6, 35, 40], 14: [81, 100, 34, 71], 15: [22, 88, 76, 62], 16: [41, 9, 91, 47], 17: [23, 54, 90, 55], 18: [97, 43, 12, 50], 19: [92, 15, 53, 53], 20: [88, 75, 90, 84], 
21: [60, 47, 36, 47], 22: [10, 40, 28, 26], 23: [100, 82, 27, 69], 24: [71, 73, 82, 75], 25: [37, 49, 59, 48], 26: [99, 90, 84, 91], 27: [9, 32, 77, 39], 28: [51, 53, 45, 49], 29: [67, 25, 25, 39], 30: [75, 53, 20, 49], 
31: [79, 54, 98, 77], 32: [27, 77, 41, 48], 33: [21, 84, 62, 55], 34: [72, 48, 64, 61], 35: [51, 9, 75, 45], 36: [62, 62, 41, 55], 37: [72, 20, 14, 35], 38: [91, 17, 74, 60], 39: [81, 55, 3, 46], 40: [81, 20, 59, 53]}
"""
print("\n# 3-3번 문제")

for i in range(0, len(d3), 1) :
  l = d3[i + 1]
  l.append(int((d3[i + 1][0] + d3[i + 1][1] + d3[i + 1][2]) / 3))

print(d3)

# 3-4
"""
- 3-3의 딕셔너리 변수를 입력받아 1등의 번호와 1등의 3과목 평균점을 
  리턴하는 함수를 선언 후 함수를 호출해 결과를 출력
- 1등은 3과목 평균점이 가장 높은 학생
- print문에 직접 정답 값을 입력할 경우 오답 처리
- 함수를 사용하지 않는 경우나 함수의 리턴 값이 없는 경우 감점

# 정답
1등 번호: 26, 평균: 91점
"""
print("\n# 3-4번 문제")

def getHighest(dt) :
  maximum = 0
  highNum = 0
  
  for i in range(1, len(dt) + 1, 1) :
    if (dt[i][3] > maximum) :
      maximum = dt[i][3]
      highNum = i
  
  return highNum, maximum

h, m = getHighest(d3)

print(f"1등 번호: {h}, 평균: {m}점")

# 3-5
"""
- 딕셔너리 변수를 입력받아 석차 리스트를 리턴하는 함수를 선언 후
  함수 호출 후 리턴값을 출력
- 석차 리스트는 1등부터 순서대로 학생의 번호로 구성
- 리스트 변수에 직접 숫자를 입력해 선언하면 오답 처리
- 오답의 예: tList = [3, 6, ..., 39]
- 함수를 사용하지 않는 경우나 함수의 리턴값이 없는 경우 감점
- 힌트: 내림차순 정렬 알고리즘
1) 리스트를 전체 탐색해 최대 값을 찾는다.
2) 최대값과 인덱스 첫번째 값을 교환한다.
3) 교환을 완료한 첫번째 인덱스를 제외하고, 1)~2)를 반복한다.
- 출력은 print(리스트변수) 형태로

# 정답
[26, 20, 31, 24, 5, 14, 23, 6, 12, 15, 34, 7, 38, 4, 17, 33, 36, 19, 1, 40, 18, 
28, 30, 25, 32, 21, 16, 39, 2, 35, 8, 13, 27, 29, 10, 37, 3, 9, 22, 11]
"""
print("\n# 3-5번 문제")

#틀림

# 4.
"""
- 369 게임 만들기 (배점 10점)
- 3, 6, 9, 13, 16, 19, ..., 30, 31, 32와 같이 3, 6, 9가 들어간 턴에 "짝"을 입력
  나머지 경우는 턴의 숫자를 입력
- 컴퓨터와 유저가가 번갈아 가면서 숫자 혹은 '짝'을 입력
- 컴퓨터부터 부터 시작
- 컴퓨터는 10%의 확률로 패배할 수 있음. 패배시 369게임 규칙에 따라 
  다른 숫자 혹은 '짝'을 출력하고 패배

# 정답의 예 1)
#369 게임을 시작합니다.
> 컴퓨터:  1
> 유저: 2
> 컴퓨터:  짝
> 유저: 4
> 컴퓨터:  5
> 유저: 6
* 사용자가 게임에서 패배했습니다. => 정답: 짝

# 정답의 예 2)
#369 게임을 시작합니다.
> 컴퓨터:  1
> 유저: 2
> 컴퓨터:  2
* 컴퓨터가 게임에서 패배했습니다. => 정답: 짝

#정답의 예 3)
#369 게임을 시작합니다.
> 컴퓨터:  1
> 유저: 2
> 컴퓨터:  짝
> 유저: 4
> 컴퓨터:  5
> 유저: 짝
> 컴퓨터:  7
> 유저: 8
> 컴퓨터:  짝
> 유저: 10
> 컴퓨터:  11
> 유저: 12
> 컴퓨터:  짝
> 유저: 14
> 컴퓨터:  15
> 유저: 짝
> 컴퓨터:  17
> 유저: 18
> 컴퓨터:  20
* 컴퓨터가 게임에서 패배했습니다. => 정답: 짝
"""
print("\n# 4번 문제")

import random

cnt = 0
whoWin = ""
loseCause = ""

while True :
  cnt += 1
  p = random.randint(1, 10)
  if (str(cnt).count("3") >= 1 or str(cnt).count("6") >= 1 or str(cnt).count("9") >= 1) : #369 포함일때
    if (p != 5) : #정답
      print("컴퓨터:", "짝")
    else : #오답
      print("컴퓨터:", str(cnt))
      whoWin = "Player"
      loseCause = str(cnt)
      break
  else : #일반 숫자일때
    if (p == 5) : #오답
      print("컴퓨터:", "짝")
      whoWin = "Player"
      loseCause = "짝"
      break
    else : #정답
      print("컴퓨터:", str(cnt))
  cnt += 1
  s = input("유저: ")
  if (str(cnt).count("3") >= 1 or str(cnt).count("6") >= 1 or str(cnt).count("9") >= 1) : #369 포함일때
    if (str(s) != "짝") : #오답
      whoWin = "Computer"
      loseCause = "짝"
      break
    else : #정답
      pass
  else : #일반 숫자일때
    if (s == str(cnt)) : #정답
      pass
    else : #오답
      whoWin = "Computer"
      loseCause = str(cnt)
      break
    
if (whoWin == "Player") :
  print("컴퓨터가 게임에서 패배했습니다. => 정답: ", loseCause)
else :
  print("유저가 게임에서 패배했습니다. => 정답: ", loseCause)
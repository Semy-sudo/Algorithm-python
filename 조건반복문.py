
##<조건문>
x = 15

if x>= 10:
  print("x>=10")
if x>= 0:
  print("x>=0")
if x>=30:
  print("x>=30")

#들여쓰기 블록예시
score = 85

if score>=70:
  print("성적이 70점 이상입니다.")
  if score >= 90:
    print("성적이 90이상입니다.")
else:
  print('성적이 70점 미만입니다.')
  print('조금 더 분발하세요')

print('프로그램을 종료합니다.')

#성적 구간에 따른 학점 출력 예제
score = 75

if score >= 90:
  print("학점A")
elif score >= 80:
  print("학점B")
elif score >= 70:
  print("학점C")
else:
  print("학점F")

if True or False:
  print("print!")

##<반복문>
i = 1
result = 0

#i가 9보다 작거나 같을때 반복적으로 실행
while i<=9:
  result += i
  i+=1

print(result)

#for문
array = [9,8,7,6,5]

for x in array:
  print(x)

#1~9연속적으로 순회
result = 0;
for i in range(1,10):
  result +=i
print(result)

##<break문>
# 5까지만 출력
i = 1
while True:
  print("i의 값:",i)
  if i == 5:
    break
  i += 1
    
#합격 여부 판별
scores = [90,85,77,65,96]

#80점 이상일때 합격시킴
for i in range(5):
  if scores[i] >= 80:
    print(i+1,"합격입니다.")

#특정 학생은 제외
cheating_student_list = {2,4}

for i in range(5):
  if i+1 in cheating_student_list:
    continue
  if scores[i]>=80:
    print(i+1,"번 학생은 합격입니다.")

#중첩 반복문 사용해서 2단 ~9단 구구단 출력
for i in range(2,10):
  for j in range(1,10):
    print(i,"x",j,"=",i*j)
  print()

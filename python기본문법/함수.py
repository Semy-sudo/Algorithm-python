#더하기 함수 예시 1)
def add(a,b):
  return a+b

print(add(3,4))

#더하기 함수 예시2)
def add(a,b):
  print(a+b)
add(3,4)

#global 변수
#변수 a 0에서 10으로 만들기
a = 0

def func():
  global a
  a+=1

for i in range(10):
  func()
print(a)

#함수 반환값 여러개
#패킹
def operator(a,b):
  add_var = a+b
  subtract_var = a-b
  multiply_var = a*b
  divide_var = a/b
  return add_var, subtract_var,multiply_var,divide_var

#언패킹
a,b,c,d = operator(7,3)
print(a,b,c,d)

##<람다표현식>

#람다 표현식으로 구현한메서드
print((lambda a, b: a+b)(3,7))

#각각의 위치에 맞는 원소끼리 더함
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b :a+b,list1,list2)
print(list(result))
##<문자열 자료형>

data = 'Hello World'
print(data)

#큰따옴표로 작성되어 있는 경우 내부적으로 작은 따옴표
data = "Dont you know \"python\"?"
print(data)

#문자열 연산
a = "Hello"
b = "World"
#덧셈
print(a+""+b)

##<튜플 자료형>
a = (1,2,3,4,5,6,7,8,9)
print("네 번째 원소만 출력", a[3])

##<사전 자료형>
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

#키 데이터만 담은 리스트
key_list = data.keys()
#값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])

##<집합 자료형>

#집합 자료형 초기화 방법1
data = set([1,2,3,4,5,5,5,5])
print(data)

#집합 자료형 초기화 방법2
data = {1,1,2,3,4,4,5} 
print(data)

data = set([1,2,3])
print(data)

#새로운 원소 추가
data.add(4)
print(data)

#새로운 원소 여러개 추가
data.update([5,6])
print(data)

#특정 값 갖는 원소 삭제
data.remove(3)
print(data)
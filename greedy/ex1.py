#0~9로 이루어진 문자열S가 주어졌을때, 외쪽부터 오른쪽 으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램 작성

#연산은 왼쪽에서부터 순서대로 이루어짐

#1.문자를 숫자로 
data = input()

result = int(data[0])

#1이나 0일때, 덧셈이 큰수 만듬

for i in range(1,len(data)):
  num = int(data[i])
  if num<=1:
    result += num
  else:
    result *= num

print(result)
#11399
#리스트 원소의 개수와 리스트 원소를 입력받고
#달달이 합 구하기
num = int(input())
array = list(map(int,input().split()))
array.sort()
sum = 0

for i in range(num):
  for j in range(i+1):
    sum += array[i]
print(sum)
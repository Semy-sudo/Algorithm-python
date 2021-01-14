#n개의 로프
n = int(input())#로프의 개수
lis = []#각로프의 중량 정보
for i in range(n):
  lis.append(int(input()))

lis.sort(reverse=True)
array = []
for i in range(n):
  array.append(lis[i]*(i+1)) 
print(max(array))
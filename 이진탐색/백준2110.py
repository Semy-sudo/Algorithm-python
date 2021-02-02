n,c = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))
arr.sort()
#가장 인접한 두 공유기 사이의 거리 최대
# 1 2 4 8 9


result = 0
start = 1#이거 아님arr[1]-arr[0]
end = arr[-1]-arr[0]

while start<=end:
  mid = (start+end)//2
  count = arr[0]
  num = 1
  for i in range(1,n):
    if mid<=arr[i]-count:
      num +=1
      count = arr[i]
  
  if num>=c:
    result = mid
    start = mid+1
  else:
    end = mid-1

    
print(result)
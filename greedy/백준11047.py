#백준11047
#k원 만드는데 필요한 동전 개수 최솟값

n,k = map(int,input().split())
m = []
num = 0

for i in range(n):
  m.append(int(input()))
for i in range(n-1,0,-1):
  if k == 0:
    break
  if m[i]>k:
    continue
  num += k//m[i]
  k %= m[i] 
print(num)


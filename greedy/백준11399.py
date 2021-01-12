n = int(input())
p = list(map(int,input().split()))
p.sort()
sum = 0
for i in reversed(range(1,n+1)):
  sum += p[0]*i
  del p[0]
print(sum)





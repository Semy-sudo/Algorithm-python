#1931

#회의 개수
n = int(input())
m = []
for i in range(n):
  a,b = map(int,input().split())
  m.append([a,b])
m = sorted(m,key= lambda x:x[0])
m = sorted(m,key=lambda x:x[1])


print(m)
last = 0
cnt = 0
for i,j in m:
  if i>=last:
    cnt +=1
    last = j
print(cnt)    

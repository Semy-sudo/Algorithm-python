
def dfs():
  stack = []
  check = []
  stack.append(1)
  while stack:
    p = stack.pop()
    if p not in check:
      check.append(p)
      stack += reversed(lis[p])
  return len(check)-1

n = int(input())
m = int(input())
lis = {i:[] for i in range(1,n+1)}
for i in range(m):
  a,b = map(int,input().split())
  lis[a].append(b)
  lis[b].append(a)

for i in range(1,n+1):
  lis[i].sort()

print(dfs()) 


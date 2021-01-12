import sys
sys.setrecursionlimit(10000)#최대 제귀한도

def dfs(v):
  visited[v] = True
  for e in lis[v]:
    if not visited[e]:
      dfs(e)

n,m = map(int,input().split())
lis = {i:[] for i in range(1,n+1)}
for i in range(m):
  u,v = map(int,input().split())
  lis[u].append(v)
  lis[v].append(u)
#초기화
visited = [False]*(n+1)
count = 0
for i in range(1,n+1):
  if not visited[i]:
    dfs(i)
    count +=1
  
print(count)
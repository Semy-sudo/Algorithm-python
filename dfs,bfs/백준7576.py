from collections import deque

def bfs(lis,m,n):
  #map = {i : []for _ in range(n)}
  #토마토가 1인것 찾기
  queue= deque()
  dy = [0,0,1,-1]
  dx = [1,-1,0,0]
  for i in range(m):
    for j in range(n):
      if lis[j][i]==1:
        queue.append([i,j])
  while queue:
    a,b = queue.popleft()
    for i in range(4):
      x = a+ dx[i]
      y = b+ dy[i]
      if 0<=x<m and 0<=y<n and lis[y][x]==0:
         lis[y][x] = lis[b][a]+1
         queue.append([x,y])
  

m,n = map(int,input().split())
lis = []
for i in range(n):
  lis.append(list(map(int,input().split())))

bfs(lis,m,n)

isTrue = False
result = -2
#
for i in range(n):
  for j in range(m):
    if lis[i][j]==0:
      isTrue = True
    result = max(result,lis[i][j])
if (isTrue == True):
  print(-1)
elif result == 1:
  print(0)
else:
  print(result-1)





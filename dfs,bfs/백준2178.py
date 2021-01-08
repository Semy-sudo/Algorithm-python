# #2178
import sys

def dfs(lis,n,m):
  stack = []
  visited = [[0]*m for _ in range(n)]
  visited[0][0] = 1
  stack.append([0,0])
  dx = [0,0,1,-1]
  dy = [1,-1,0,0]
  while stack:
    a,b = stack.pop()
    for i in range(4):
      x = a+dx[i]
      y = b+dy[i]
      if x==n-1 and y==m-1:
        print(visited[n-1][m-1])
        sys.exit()
      if 0<=x<n and 0<=y<m and visited[x][y] == 0 and int(lis[x][y]==1):
        visited[x][y] = visited[a][b] +1
        stack.append([x,y])
    



n,m = map(int,input().split())
lis = []
for i in range(n):
  tmp = list(input())[:m]
  lis.append(tmp)

dfs(lis,n,m)


#deque안에는 literable 만??




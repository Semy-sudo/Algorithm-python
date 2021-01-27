from collections import deque

def bfs(I,start,end):
  dx = [2,2,-2,-2,1,1,-1,-1]
  dy = [1,-1,1,-1,2,-2,2,-2]
  visited = [[0]*(I+1) for i in range(I+1)]
  q = deque()
  q.append(start)
  visited[start[1]][start[0]] = 1
  
  while q:
    a,b = q.popleft()
    for i in range(8):
      x = a+ dx[i]
      y = b+ dy[i]
      if 0<=x<I and 0<=y<I and visited[y][x] ==0:
        visited[y][x] = 1
        q.append([x,y])
        count[y][x] = count[b][a] +1
  return count

n = int(input())
for i in range(n):
  I = int(input()) #체스판의 길이
  start = list(map(int,input().split())) #[0,0]
  end = list(map(int,input().split())) #[7,0]
  count = [[0]*(I+1) for i in range(I+1)]


  bfs(I,start,end)
  print(count[end[1]][end[0]])
import sys
sys.setrecursionlimit(100000)

def dfs(i,j):
  stack = []
  stack.append([i,j])
  dx = [1,-1,0,0,1,1,-1,-1]
  dy = [0,0,1,-1,1,-1,1,-1] 
  while stack:
    a,b = stack.pop() #0,0
    for i in range(8):
      y = a+dx[i]
      x = b+dy[i]
      if 0<=x<w and 0<=y<h and lis[y][x]==1:
        stack.append([y,x])
        lis[y][x] = 0

while True:

  w,h = map(int,input().split())
  if w<=0 or w>50 or h<=0 or h>50:#이거 처리 안해주면 런타임 에러 발생!!
    break
  lis = []
  for i in range(h):
    lis.append(list(map(int,input().split())))

  count = 0
  for i in range(h):
    for j in range(w):
      if lis[i][j]==1:
        lis[i][j]=0
        dfs(i,j)
        count +=1
  
  print(count)
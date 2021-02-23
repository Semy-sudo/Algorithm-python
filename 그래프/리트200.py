grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
stack = []
#섬의 개수?
def dfs(i,j):
  stack.append([j,i])
  #대각선도 고려해주기
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  while stack:
    x,y = stack.pop()
    for k in range(4):
      a = x +dx[k]
      b = y +dy[k]
      if 0<=a<len(grid[0]) and 0<=b<len(grid) and grid[b][a]=="1":
        stack.append([a,b])
        grid[b][a] = "0"
    
count = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == "1":#육지일때만 탐색진행
      dfs(i,j) 
      count+=1

print(count)
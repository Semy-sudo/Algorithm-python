n = int(input())
origin = []
origin_n = [[0]*100 for _ in range(100)]
for i in range(n):
  origin.append(list(map(str,input())))
  for j in range(len(origin[i])):
    if origin[i][j] == 'R':
      origin_n[i][j] = 'G'
    else:
      origin_n[i][j] = origin[i][j]

# print(origin_n)

#origin 배열의 구역수 
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(origin,color):
  count = 0
  stack = []
  for i in range(n):
    for j in range(n):
      if origin[i][j] == color:
        stack.append([j,i])
        origin[i][j] = 'N'
        while stack:
          a,b = stack.pop()
          for u in range(4):
            x = a+dx[u]
            y = b+dy[u]
            if 0<=x<n and 0<=y<n and origin[y][x]==color:
              stack.append([x,y])
              origin[y][x] = 'N'
        count +=1      
  
  return count
  

print(dfs(origin,'R')+dfs(origin,'G')+dfs(origin,'B'),
dfs(origin_n,'B')+dfs(origin_n,'G'))
#색깔을 주면 해당 색깔의 영역 개수 리턴


